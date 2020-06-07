import os
from flask import Flask, render_template, redirect, request, url_for, session
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import bcrypt
from os import path


app = Flask(__name__)


if path.exists("env.py"):
    import env

    app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_NAME')
    app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
else:
    app.config["MONGO_DBNAME"] = 'chickpeas'
    app.config["MONGO_URI"] = 'mongodb+srv://guest_user:vD2B9MF8A4JBu5Gx@myfirstclusterci-904s1.mongodb.net/chickpeas?retryWrites=true&w=majority'


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
                           recipes=all_recipes,recipes2=all_recipes2,recipes3=all_recipes3,recipes4=all_recipes4)


@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html', users=mongo.db.users.find())


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    return render_template('add_recipe.html',
                           recipes=mongo.db.recipes.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('view_recipe'))


@app.route('/view_recipe')
def view_recipe():
    all_recipes = mongo.db.recipes.find()
    return render_template('view_recipe.html', recipes=all_recipes)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
