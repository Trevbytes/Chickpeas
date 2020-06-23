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

if os.path.exists("env.py"):
    import env

app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_NAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('landing_page.html')


@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    breakfast_recipes = mongo.db.recipes.find({"meal_type": "Breakfast",
                                               "public": "on"})
    lunch_recipes = mongo.db.recipes.find({"meal_type": "Lunch",
                                           "public": "on"})
    dinner_recipes = mongo.db.recipes.find({"meal_type": "Dinner",
                                            "public": "on"})
    dessert_recipes = mongo.db.recipes.find({"meal_type": "Dessert",
                                             "public": "on"})
    return render_template('recipes.html',
                           breakfast=breakfast_recipes, lunch=lunch_recipes,
                           dinner=dinner_recipes, dessert=dessert_recipes,
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
                return redirect(url_for('dashboard',
                                        username=session['username']))
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
            flash(
                'Thanks for registering! Create a recipe or go make a copy \
                from an existing recipe to get started')
            return redirect(url_for('dashboard', username=session['username']))
        flash('That username already exists, please try again')

    return render_template('register.html', is_index=True)


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('home'))


@app.route('/dashboard/<username>', methods=['GET', 'POST'])
def dashboard(username):
    ingredients = mongo.db.ingredients.find().sort("name")
    my_recipes = mongo.db.recipes.find({"$or": [{"added_by": username},
                                                {"edited_by": username}
                                                ]}).sort("_id", -1)

    return render_template('dashboard.html', my_recipes=my_recipes,
                           ingredients=ingredients)


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    ingredients = mongo.db.ingredients.find().sort("name")
    return render_template('add_recipe.html',
                           recipes=mongo.db.recipes.find(),
                           ingredients=ingredients)


@app.route('/submit_ingredient', methods=['GET', 'POST'])
def submit_ingredient():
    ingredients = mongo.db.ingredients.find().sort("name")
    return render_template('submit_ingredient.html',
                           recipes=mongo.db.recipes.find(),
                           ingredients=ingredients)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    new_recipe_id = recipes.insert_one(request.form.to_dict()).inserted_id
    return redirect(url_for('view_recipe', recipe_id=new_recipe_id))


@app.route('/insert_ingredient', methods=['POST'])
def insert_ingredient():
    ingredients = mongo.db.ingredients
    new_ingredient_id = ingredients.insert_one(request.form.to_dict()).inserted_id
    new_ingredient = ingredients.find_one({"_id": ObjectId(new_ingredient_id)})
    print(new_ingredient)
    return redirect(url_for('view_ingredient2',
                            ingredient_name=new_ingredient['name']))


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients_selected = mongo.db.recipes.find_one({"_id":
                                                      ObjectId(recipe_id)})

    def ingredient_search(ingredient):
        if re.match('recipe_ingredient_id_.+', ingredient):
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
    ingredients = mongo.db.ingredients.find().sort("name")
    ingredients_selected = mongo.db.recipes.find_one({"_id":
                                                      ObjectId(recipe_id)})
    all_recipes = mongo.db.recipes.find()

    def ingredient_search(ingredient):
        if re.match('recipe_ingredient_id_.+', ingredient):
            recID = ingredient
            return recID
        return 'blank'
    return render_template('edit_recipe.html', recipe=the_recipe,
                           recipes=all_recipes,
                           ingredients=ingredients,
                           ingredients_selected=ingredients_selected,
                           ingredient_search=ingredient_search)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.delete_one({'_id': ObjectId(recipe_id)})
    recipe_id = recipes.insert_one(request.form.to_dict()).inserted_id
    return redirect(url_for('view_recipe', recipe_id=recipe_id))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('dashboard', username=session['username']))


@app.route('/view_ingredient/<ingredient_id>')
def view_ingredient(ingredient_id):
    ingredients = mongo.db.ingredients
    the_ingredient = ingredients.find_one({"_id": ObjectId(ingredient_id)})
    return render_template('ingredients.html', ingredient=the_ingredient,
                           ingredientstest=ingredients.find().sort("name"))


@app.route('/view_ingredient2/<ingredient_name>', methods=['GET', 'POST'])
def view_ingredient2(ingredient_name):
    ingredients = mongo.db.ingredients
    if isinstance(ingredient_name, dict):
        the_ingredient = ingredient_name
    else:
        the_ingredient = ingredients.find_one({"name": ingredient_name})
    return render_template('view_ingredient.html', ingredient=the_ingredient)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
