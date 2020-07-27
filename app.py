import os
import re
from flask import Flask, render_template, redirect, request, url_for,\
    session, flash
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

if os.path.exists("env.py"):
    import env

app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_NAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)


# Landing Page
@app.route('/')
def home():
    return render_template('landing_page.html')


# Recipes page - Recipes sorted and returned by course
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


# Ingredients page returns full ingredient list and a selected ingredient.
@app.route('/ingredients')
def ingredients():
    ingredients = mongo.db.ingredients
    return render_template('ingredients.html',
                           ingredients=ingredients.find(),
                           selectedIngredient=ingredients.find().sort("name"))


# Login page - When a login request is sent this checks that username and
# password are correct. Otherwise a flashed message is sent.
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


# Registration page- This handels a request for a new user.
# It checks that the username is unique and sends a flashed
# message to notify the user if they successfully registered.
# A newly registered user is sent to their dashboard.
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
                from an existing recipe to get started!')
            return redirect(url_for('dashboard', username=session['username']))
        flash('That username already exists, please try again')

    return render_template('register.html', is_index=True)


# Logout route - When logout is requested the session is
# cleared and the user is sent to home/landing page.
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('home'))


# Dashboard page- Returns the full ingredient list to be used in
# modals, sorted by name. Returns recipes that were added or edited
# by the user to display on their dashboard, sorted by added/edited
# most recently.
@app.route('/dashboard/<username>', methods=['GET', 'POST'])
def dashboard(username):
    ingredients = mongo.db.ingredients.find().sort("name")
    my_recipes = mongo.db.recipes.find({"$or": [{"added_by": username},
                                                {"edited_by": username}
                                                ]}).sort("_id", -1)

    return render_template('dashboard.html', my_recipes=my_recipes,
                           ingredients=ingredients)


# Add Recipe modal- returns full ingredient list, sorted
# by name.
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    ingredients = mongo.db.ingredients.find().sort("name")
    return render_template('add_recipe.html',
                           ingredients=ingredients)


# Submit Ingredient modal - returns full ingredient list, sorted
# by name.
@app.route('/submit_ingredient', methods=['GET', 'POST'])
def submit_ingredient():
    ingredients = mongo.db.ingredients.find().sort("name")
    return render_template('submit_ingredient.html',
                           ingredients=ingredients)


# Insert recipe route - This adds the submitted recipe
# to the database and returns the new id in order to view
# the newly created recipe.
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    new_recipe_id = recipes.insert_one(request.form.to_dict()).inserted_id
    return redirect(url_for('view_recipe', recipe_id=new_recipe_id))


# Insert ingredient route - This adds the submitted ingredient
# to the database and returns the new id in order to view
# the newly added ingredient.
@app.route('/insert_ingredient', methods=['POST'])
def insert_ingredient():
    ingredients = mongo.db.ingredients
    new_ingredient_id = ingredients.insert_one(
        request.form.to_dict()).inserted_id
    flash('Ingredient Added!')
    return redirect(url_for('view_ingredient',
                            ingredient_id=new_ingredient_id))


# View Recipe page - Receives the recipe ID to show the recipe.
# Returns the recipe, the recipe again to use to extract
# ingredients, the ingredient search function and the recipe ID.
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients_selected = mongo.db.recipes.find_one({"_id":
                                                      ObjectId(recipe_id)})
    return render_template('view_recipe.html', recipe=the_recipe,
                           ingredients_selected=ingredients_selected,
                           ingredient_search=ingredient_search,
                           recipe_id=recipe_id)


# Edit Recipe modal - Receives the recipe ID to show the recipe.
# Returns the recipe, the recipe again to use to extract
# ingredients and the full list of ingredients.
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients_selected = mongo.db.recipes.find_one({"_id":
                                                      ObjectId(recipe_id)})
    ingredients = mongo.db.ingredients.find().sort("name")
    return render_template('edit_recipe.html', recipe=the_recipe,
                           ingredients=ingredients,
                           ingredients_selected=ingredients_selected,
                           ingredient_search=ingredient_search)


# Edit Ingredient modal - Receives the ingredient ID to show the ingredient.
# Returns the ingredient, the ingredient search function
# and the full list of ingredients.
@app.route('/edit_ingredient/<ingredient_id>', methods=['GET', 'POST'])
def edit_ingredient(ingredient_id):
    ingredients = mongo.db.ingredients
    the_ingredient = ingredients.find_one({"_id": ObjectId(ingredient_id)})
    ingredients = mongo.db.ingredients.find().sort("name")
    return render_template('edit_ingredient.html', ingredient=the_ingredient,
                           ingredients=ingredients,
                           sub_ingredient_search=sub_ingredient_search)


# Update Recipe route- This deletes the recived recipe ID and
# adds a new recipe with the form information. Only the creator
# of the recipe has access to this route. Delete and Add New
# are used instead of update to update the ingredients in the
# recipe properly.
# Returns the new recipe ID.
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.delete_one({'_id': ObjectId(recipe_id)})
    recipe_id = recipes.insert_one(request.form.to_dict()).inserted_id
    return redirect(url_for('view_recipe', recipe_id=recipe_id))


# Update Ingredient route- This updates the received ingredient. It
# uses upsert to add any new items. It then removes substitute ingredients
# that are labeled as fields that begin with 'remove' in the form.
# Returns the updated ingredient ID.
@app.route('/update_ingredient/<ingredient_id>', methods=["POST"])
def update_ingredient(ingredient_id):
    ingredients = mongo.db.ingredients
    formDataDict = request.form.to_dict()
    ingredients.find_one_and_update({'_id': ObjectId(ingredient_id)},
                                    {"$set":
                                     (formDataDict)},
                                    upsert=True)
    for field, value in formDataDict.items():
        if re.match('remove_.+', field):
            # Field that begins with 'remove_'
            # Example 'remove_sub_ingredient_1'
            deletequery = (field)
            # Original field in the database
            # Example 'sub_ingredient_1'
            deletequery2 = (field[7:])
            ingredients.update_one({'_id': ObjectId(ingredient_id)},
                                   {'$unset': {deletequery: 1}})
            ingredients.update_one({'_id': ObjectId(ingredient_id)},
                                   {'$unset': {deletequery2: 1}})
    return redirect(url_for('view_ingredient', ingredient_id=ingredient_id))


# Delete Recipe route- This removes the received recipe from the
# database and redirects the user to their dashboard. *Even when removed
# from the recipes page*
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('dashboard', username=session['username']))


# Delete Ingredient route - This removes the received ingredient from the
# database and redirects the user to the ingredients page.
@app.route('/delete_ingredient/<ingredient_id>')
def delete_ingredient(ingredient_id):
    mongo.db.ingredients.delete_one({'_id': ObjectId(ingredient_id)})
    return redirect(url_for('ingredients'))


# View Ingredient page - Receives the ingredient ID.
# Returns the ingredient, the ingredient search function to
# extract substitute ingredients and the full list of ingredients.
@app.route('/view_ingredient/<ingredient_id>')
def view_ingredient(ingredient_id):
    ingredients = mongo.db.ingredients
    the_ingredient = ingredients.find_one({"_id": ObjectId(ingredient_id)})
    return render_template('ingredients.html', ingredient=the_ingredient,
                           sub_ingredient_search=sub_ingredient_search,
                           selectedIngredient=ingredients.find().sort("name"))


# View Ingredient modal - Receives the ingredient name.
# Checks if the ingredient name is a dictonary, else finds
# the correct dictonary.
# Returns the ingredient, the ingredient search function to
# extract substitute ingredients and the full list of ingredients.
@app.route('/view_ingredient2/<ingredient_name>', methods=['GET', 'POST'])
def view_ingredient2(ingredient_name):
    ingredients = mongo.db.ingredients
    if isinstance(ingredient_name, dict):
        the_ingredient = ingredient_name
    else:
        the_ingredient = ingredients.find_one({"name": ingredient_name})

    return render_template('view_ingredient.html', ingredient=the_ingredient,
                           sub_ingredient_search=sub_ingredient_search)


# Recipe Search route - This searchs the recipe database for the query
# entered by the user. It returns public recipes or recipes created or copied
# by the user. The search is run twice to return a count tocheck if there is
# at least one recipe to return.
@ app.route('/search', methods=["GET", "POST"])
def search():
    mongo.db.recipes.create_index([('$**', 'text')])
    query = request.form.get("query")
    result = mongo.db.recipes.find(
        {"$and": [{"$text": {"$search": query}},
                  {"public": "on"}]}).sort("_id", -1)
    if 'username' in session:
        result = mongo.db.recipes.find({
            "$and": [
                {"$text": {"$search": query}},
                {"$or": [{"public": "on"}, {"added_by": session['username']}, {
                    "edited_by": session['username']}]}
            ]}).sort("_id", -1)
    result_num = mongo.db.recipes.find(
        {"$and": [{"$text": {"$search": query}},
                  {"public": "on"}]}).count()
    if 'username' in session:
        result_num = mongo.db.recipes.find({
            "$and": [
                {"$text": {"$search": query}},
                {"$or": [{"public": "on"}, {"added_by": session['username']}, {
                    "edited_by": session['username']}]}
            ]}).count()
    if result_num > 0:
        return render_template("search_results.html",
                               result=result)
    else:
        return render_template("search_results.html",
                               result=result,
                               message="No results found. Please try again")


# Function that returns the key value pair if the key
# is an ingredient.
def ingredient_search(ingredient):
    if re.match('recipe_ingredient_id_.+', ingredient):
        ingredientMatch = ingredient
        return ingredientMatch
    return 'blank'


# Function that returns the key value pair if the key
# is a substitute ingredient.
def sub_ingredient_search(ingredient):
    if re.match('sub_ingredient_id_.+', ingredient):
        ingredientMatch = ingredient
        return ingredientMatch
    return 'blank'

# Error 404
@ app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


# Error 500
@ app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


# Starts the app
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
