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
    return render_template('recipes.html', users=mongo.db.users.find())


@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html', users=mongo.db.users.find())


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

