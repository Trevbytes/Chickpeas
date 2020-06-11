import os
import json
import re
from flask import Flask, render_template, redirect, request, url_for, session
from bson.objectid import ObjectId
from bson import json_util
from flask_pymongo import PyMongo
import bcrypt
from os import path


app = Flask(__name__)

guest = 'mongodb+srv://guest_user:vD2B9MF8A4JBu5Gx@myfirstclusterci-904s1.mongodb.net/chickpeas?retryWrites=false'

if os.path.exists("env.py"):
    import env

    app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_NAME')
    app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
else:
    app.config["MONGO_DBNAME"] = 'chickpeas'
    app.config["MONGO_URI"] = guest


mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('landing_page.html', users=mongo.db.users.find())


@app.route('/recipes')
def recipes():
    all_recipes = mongo.db.recipes.find()
    all_recipes2 = mongo.db.recipes.find()
    all_recipes3 = mongo.db.recipes.find()
    all_recipes4 = mongo.db.recipes.find()
    return render_template('recipes.html', users=mongo.db.users.find(),
                           recipes=all_recipes, recipes2=all_recipes2,
                           recipes3=all_recipes3, recipes4=all_recipes4)


@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html',
                           ingredients=mongo.db.ingredients.find(),
                           ingredientstest=mongo.db.ingredients.find())


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    my_recipes = mongo.db.recipes.find().sort("_id", -1)
    return render_template('dashboard.html', my_recipes=my_recipes)


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    ingredients = mongo.db.ingredients.find().sort("name")
    return render_template('add_recipe.html',
                           recipes=mongo.db.recipes.find(),
                           ingredients=ingredients)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    new_recipe_id = recipes.insert_one(request.form.to_dict()).inserted_id
    return redirect(url_for('view_recipe', recipe_id=new_recipe_id))


@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe=the_recipe)


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
    recipes.delete_one({'_id': ObjectId(recipe_id)})
    recipe_id = recipes.insert_one(request.form.to_dict()).inserted_id
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
