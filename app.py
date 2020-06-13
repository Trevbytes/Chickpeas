import os
import json
import re
from flask import Flask, render_template, redirect, request, url_for,\
    session, flash
from bson.objectid import ObjectId
from bson import json_util
from flask_pymongo import PyMongo
import bcrypt
from os import path
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

guest = 'mongodb+srv://guest_user:vD2B9MF8A4JBu5Gx@myfirstclusterci-904s1.mongodb.net/chickpeas?retryWrites=false'

if os.path.exists("env.py"):
    import env

    app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_NAME')
    app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
else:
    app.config["MONGO_DBNAME"] = 'chickpeas'
    app.config["MONGO_URI"] = guest
    app.config['SECRET_KEY'] = 'secretguest'


mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('landing_page.html')


@app.route('/recipes')
def recipes():
    all_recipes = mongo.db.recipes.find({"meal_type": "Breakfast"})
    all_recipes2 = mongo.db.recipes.find({"meal_type": "Lunch"})
    all_recipes3 = mongo.db.recipes.find({"meal_type": "Dinner"})
    all_recipes4 = mongo.db.recipes.find({"meal_type": "Dessert"})
    return render_template('recipes.html',
                           recipes=all_recipes, recipes2=all_recipes2,
                           recipes3=all_recipes3, recipes4=all_recipes4,
                           )


@app.route('/ingredients')
def ingredients():
    ingredients = mongo.db.ingredients
    return render_template('ingredients.html',
                           ingredients=ingredients.find(),
                           ingredientstest=ingredients.find().sort("name"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        user_login = users.find_one({'username': request.form.get('username')})

        if user_login:
            if check_password_hash(user_login['user_password'],
                                   request.form.get('user_password')):
                session['username'] = request.form.get('username')
                flash('Welcome back ' + session['username'])
                return redirect(url_for('dashboard'))
            flash('Invalid username or password.')
    return render_template('login.html', is_index=True)


@app.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one(
            {'username': request.form.get('username')})

        if not existing_user:
            hashpw = generate_password_hash(request.form.get('user_password'))
            users.insert_one({'username': request.form.get('username'),
                              'user_password': hashpw})
            session['username'] = request.form.get('username')
            flash('Thanks for registering! You are now logged in as ' +
                  session['username'])
            return redirect(url_for('dashboard'))
        flash('That username already exists, please try again')

    return render_template('register.html', is_index=True)


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('home'))


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    def saved_search(recipe, username):
        if 'saved_by_'+username in recipe:
            return True
        return False
    my_recipes = mongo.db.recipes.find().sort("_id", -1)
    return render_template('dashboard.html', my_recipes=my_recipes,
                           saved_search=saved_search)


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    ingredients = mongo.db.ingredients.find().sort("name")
    return render_template('add_recipe.html',
                           recipes=mongo.db.recipes.find(),
                           ingredients=ingredients)


@app.route('/add_to_cookbook/<recipe_id>/<username>', methods=['GET', 'POST'])
def add_to_cookbook(recipe_id, username):
    recipes = mongo.db.recipes
    recipes.find_one_and_update({'_id': ObjectId(recipe_id)},
                                {"$set":
                                 {'saved_by_' + username: 'saved'}},
                                upsert=True)

    return redirect(url_for('dashboard'))


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    new_recipe_id = recipes.insert_one(request.form.to_dict()).inserted_id
    return redirect(url_for('view_recipe', recipe_id=new_recipe_id))


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients_selected = mongo.db.recipes.find_one({"_id":
                                                      ObjectId(recipe_id)})

    def ingredient_search(ingredient):
        if re.search('recipe_ingredient_id_.+', ingredient):
            recID = ingredient
            return recID
        return 'blank'
    return render_template('view_recipe.html', recipe=the_recipe,
                           ingredients_selected=ingredients_selected,
                           ingredient_search=ingredient_search,
                           recipe_id=recipe_id)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    the_recipe2 = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = mongo.db.ingredients.find().sort("name")
    ingredients_selected = mongo.db.recipes.find_one({"_id":
                                                      ObjectId(recipe_id)})
    all_recipes = mongo.db.recipes.find()

    def ingredient_search(ingredient):
        if re.search('recipe_ingredient_id_.+', ingredient):
            recID = ingredient
            return recID
        return 'blank'
    return render_template('edit_recipe.html', recipe=the_recipe,
                           recipe2=the_recipe2,
                           recipes=all_recipes,
                           ingredients=ingredients,
                           ingredients_selected=ingredients_selected,
                           ingredient_search=ingredient_search)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.find_one_and_update({'_id': ObjectId(recipe_id)},
                                {"$set":
                                 (request.form.to_dict())},
                                upsert=True)
    return redirect(url_for('view_recipe', recipe_id=recipe_id))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    print(recipe_id)
    return redirect(url_for('dashboard'))


@app.route('/view_ingredient/<ingredient_id>')
def view_ingredient(ingredient_id):
    the_ingredient = mongo.db.ingredients.find_one({"id": ingredient_id})
    return render_template('ingredients.html', ingredient=the_ingredient,
                           ingredientstest=mongo.db.ingredients.find().sort("name"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
