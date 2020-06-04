import os
from flask import Flask, render_template, redirect, request, url_for, session
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import bcrypt
from os import path

app = Flask(__name__)

login_manager = LoginManager()

login_manager.init_app(app)


try:
    MONGO_URI
except NameError:
    MONGO_URI = None
    MONGODB_NAME = None


if path.exists("env.py"):
    import env

    app.secret_key = SECRET
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        return redirect(url_for('dashboard'))
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            check_user = User.objects(email=form.email.data).first()
            if check_user:
                if check_password_hash(check_user['password'], form.password.data):
                    login_user(check_user)
                    return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            existing_user = User.objects(email=form.email.data).first()
            if existing_user is None:
                hashpass = generate_password_hash(
                    form.password.data, method='sha256')
                hey = User(form.email.data, hashpass).save()
                login_user(hey)
                return redirect(url_for('dashboard'))
    return render_template('register.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.email)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


class User(UserMixin, db.Document):
    meta = {'collection': '<---YOUR_COLLECTION_NAME--->'}
    email = db.StringField(max_length=30)
    password = db.StringField()


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


class RegForm(FlaskForm):
    email = StringField('email',  validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
