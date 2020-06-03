import os
from flask import Flask, render_template, redirect, request, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('landing_page.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
