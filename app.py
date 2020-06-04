import os
from flask import Flask, render_template, redirect, request, url_for, session
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import bcrypt
from os import path

app = Flask(__name__)

try:
    MONGO_URI
except NameError:
    MONGO_URI = None
    MONGODB_NAME = None


if path.exists("env.py"):
    import env

    app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_NAME')
    app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
elif MONGO_URI is None:
    app.config["MONGO_DBNAME"] = "chickpeas"
    app.config["MONGO_URI"] = "mongodb+srv://guest_user:vD2B9MF8A4JBu5Gx@myfirstclusterci-904s1.mongodb.net/chickpeas?retryWrites=true&w=majority"
else:
    app.config["MONGO_DBNAME"] = MONGO_URI
    app.config["MONGO_URI"] = MONGODB_NAME


mongo = PyMongo(app)


@app.route('/')
def home():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('landing_page.html', users=mongo.db.users.find())


@app.route('/recipes')
def recipes():
    return render_template('recipes.html', users=mongo.db.users.find())


@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html', users=mongo.db.users.find())


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home'))

    return 'Invalid username or password'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
