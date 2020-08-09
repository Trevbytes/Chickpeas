# Chickpeas

<img src="/static/images/readme/intro_image.jpg">

Chickpeas is my third milestone project while studying at [The Code Institute](https://codeinstitute.net/).
The purpose of the milestone project is to utilize a database in a website built with a Python Flask project using Python, HTML, CSS and Javascript.

Chickpeas is a cookbook with a focus on individual ingredients used in cooking.

[Live Link to Site](https://chickpeas-creative-cooking.herokuapp.com/)

## Table of Contents

- [**UX**](#UX)
  - [User Stories](#User-Stories)
- [**Features**](#Features)
    - [Existing Features](#Existing-Features)
    - [Features Left to Implement](#Features-Left-to-Implement)
- [**Technologies Used**](#Technologies-Used)
- [**Database Schema**](#Database-Schema)
- [**Testing**](#Testing)
- [**Deployment**](#Deployment)
    - [GitHub](#GitHub)
    - [Local Deployment](#Local-Deployment)
    - [Remote Deployment](#Remote-Deployment)
- [**Credits**](#Credits)

## UX

These [wireframes](https://github.com/Trevbytes/Chickpeas/blob/master/wireframes/chickpeas_wireframes.pdf) show the original idea for the site.

The original idea of the project was to create a site with recipes with the focus of the site on the ingredients inside a recipe. A user should be able to see if there are substitutes for ingredients in a recipe. This has great value for users with cooking for people with allergies and/or food restrictions.

This project has been created using the AGILE Software development model. Design changes and additions to the original wireframe ideas have been made throughout the development of the project to improve the user experience. Some of the major changes include: A grid view for viewing recipes. A dashboard for users to gather their recipes. New pages for ingredients, login, registration and search. Modals have been added for adding and editing recipes/ingredients and even viewing ingredients.

Chickpeas has been designed with two main features/goals in mind.

 - A custom cookbook, where the user can create their own recipes and create copies of other recipes that have been shared. All user recipes and publicly shared recipes are editable by the user.

 - An ingredient database, where all ingredients contain information about the ingredient. Each ingredient can contain references to common substitutes. This feature is ideally shown when viewing a recipe and clicking on a specific ingredient.

The vibrate colors and gradients of the website were chosen to inspire creativity while cooking. As foods can be in all shades of color, the site is designed to highlight the “fresh & vibrant” color that food can be. 

I used MDB (Material Design for Bootstrap) framework in building the design of this site. Icons are provided by the framework and Font Awesome. The fonts used are Amarante and Roboto, provided by Google Fonts.

### User Stories

As a User I would like to:
- Use the site on all devices from mobile to desktop.
- Be able to register to create my own recipes or ingredients.
- Be able to browse recipes or ingredients easily.
- Be able to view information about ingredients.
- Be able to search for recipes.
- Browse recipes by course.
- Submit my own recipes and ingredients.
- Be able to view substitutes for ingredients.
- Copy public recipes to my collection.
- Register or log in to the site simply. 
- Edit and delete recipes or ingredients I have submitted.
- Be able to choose to share a recipe or keep it private.
- Get visual feedback when adding/editing recipes/ingredients and logging in/out.
- View a collection of all my recipes.
- Get error messages in case of unexpected issues.

With admin access I would like to do everything above as well as:
- Be able to access, edit and delete all ingredients.

## Features

### Existing Features

- **Navagation Bar** - All pages contain the nav bar. It is simple and provides access to the whole site as well as a built in search bar. When a user is logged in the user has access to their personal cookbook and the ability to log out.
- **Search Recipes** - This feature is designed to take a user's search request and find public recipes and user's personal recipes that contain the search request.
- **Landing Page** - The first page a new user sees. It is also a page to send users to on logout. Here a user can read about the basic idea of the site.
- **Browse Public Recipes** - This page allows a user to view all public recipes. It is sorted into 4 catagories for easier navigation. A logged in user can edit or delete their submitted recipes or create-and-edit a copy of another's recipe to add to their personal cookbook.
- **Ingredients** - This page allows a user to search through all ingredients in the database. When an ingredient is selected the user can learn more about that ingredient and see common subsitutes, if any have been added.
    - A logged in user can add new ingredients to the database. The user can also fully edit or delete an ingredient created by the user. A user can partially edit ANY ingredient by adding a common subsitute to the selected ingredient.
- **Login/Register** - These two pages are used to handle the simple login and registration process.
- **Dashboard** - The users personal cookbook. Here a user can create a new recipe and view all recipes created by the user, including copied recipes.
- **Create Recipe or Ingredient** - These modals are used to provide the user a form to submit new a recipe or ingredient to the database.  
- **Edit/Copy Recipes** - This modal allows a user to edit their recipes or create and edit a copy of another users recipe. 
- **Delete Recipe/Ingredient** - A user can delete their own recipe or ingredient but not others.  
- **Edit Ingredient** - This modal allows users to edit an ingredient. As mentioned earlier, all ingredients can be edited by users. However, full editing access is granted only to the creator (or admin) of the ingredient.
- **Loading Page** - A simple loading page shown when the site is loading.
- **Error Pages** - In case of unforseen errors these pages will help the user return to the site.
- **Extensive Ingredient Options** - The site currently has over 950 ingredients to choose from in recipes.

### Features Left to Implement

- Implement [Cloudinary](https://cloudinary.com/). Users should be able to upload their own images and the urls should be stored in the database with the recipe.
- Rework the search filter/search when adding ingrdients in modals. A filter similar to the search ingredients dropdown (located on the ingredients page) list would be ideal.   
- Redesign the browse recipes page so that more courses can be added. Currently there are only four options of courses to choose from. Ideally I would create a fixed side navigation bar to easily access the diffrent meal types from anywhere on the page. 
- Add pictures to ingredients. An icon next to an ingredient's name would be another great addition.
- Implement the seaching of ingredients in the navigation search bar. Power the search by using Google.
- Add a Rich Text editor, possibly [CKEditor 4 or 5](https://ckeditor.com/), to enable users to format their input text.
- Add "characters remaining" info under the input of recipe descriptions.
- Add a page to email me (or an admin) about site issuses or suggestions.
- Add video tutorials for the features of the site.
- Add metrics to the site. Such as: Total user recipes added and "Liking" of recipes.
- Add the ability to create a copy of your own recipe.
- Add more information to recipes. Such as but not limited to: Prep Time, Cook Time, Serving Amount, Date Added, Creator of Recipe, Kitchen Tools Needed.
- **User settings** - Add the ability to change their username, personalize their cookbook or delete their account and all their recipes.
- Add the ability to sign in using a third party such as Google or Facebook.
- Add the ability to reset a forgotten password.
- Pagination for pages where many recipes are shown.
- Redesign the landing page so that featured recipes are displayed and selectable.

## Technologies Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML5)

  - The project uses **HTML 5** to construct the website.

- [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

  - The project uses **CSS 3** to style the HTML elements.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

  - The project uses **Javascipt** as a source of interactivity in the website. It manipulates both the HTML and CSS elements of the site.

- [Python 3.8.2](https://www.python.org/)

  - The project uses **Python** as the base program which runs the website. It works with the database to execute CRUD functions.

- [Mongo DB](https://www.mongodb.com/)

  - The project uses **MongoDB** for managing the database. 

- [Material Design for Bootstrap](https://mdbootstrap.com/)

  - The project uses **MDB** to create the layout of the site as well as style most of the elements thorughout the site.

- [JQuery](https://jquery.com)

  - The project uses **JQuery** to simplify DOM manipulation in javascript files.

- [Google Fonts](https://fonts.google.com/)

  - The project uses **Google Fonts** for fonts used in the website.

- [Font Awesome](https://fontawesome.com/icons?d=gallery)

  - The project uses **Font Awesome** for icons in the website.

- [Favicon.io](https://favicon.io/)

  - The project uses **Favicon.io** to create favicon icons for the website.

- [CSS Gradient](https://cssgradient.io/)

  - The project used **CSS Gradient** to create gradient colors for active keys.

- [Balsamiq Wireframes](https://balsamiq.com/)

  - The project used **Balsamiq Wireframs** to create the initial wireframes.

- [Git](https://git-scm.com/)

  - The project uses **Git** for tracking changes in code during development.

- [GitPod](https://www.gitpod.io/)

  - The project used **GitPod** as the online IDE/workspace during development .

- [GitHub](https://github)

  - The project uses **GitHub** for hosting the webpage and the repository.
  - In this project I learned how create new branches of a repository for development of the project. The landing page of this project was developed in a seperate branch and then merged with the main branch when finished. A development branch was then created to work out remaining bugs and add the final polish to the project before being submitted for assesment.

- [Heroku](https://www.heroku.com/platform)

  - The project uses **Heroku** for hosting the python app/webpage.

- [Cloudinary](https://cloudinary.com/)

  - The project uses **Cloudinary** for storing media outside of app and database. No API is currently implemented. Recipe pictures and the majority of the apps picture are stored on the Cloudinary platform.  

- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)

  - The project uses **Chrome Developer Tools** for debugging the webpage during development.

- [W3C Markup Validation Service](https://validator.w3.org)

  - The project uses **W3C Markup Validation** for validating code during development.

- [JShint](https://jshint.com/)

  - The project uses **JShint** for validating and improving JS code during development.

- [Am I Responsive](http://ami.responsivedesign.is/)
  - The ReadME used **Am I Responsive** for creating an image of the website on multiple displays to show responsiveness.

## Database Schema

- The application uses `MongoDB Atlas` for data storage.  

The data stored in the database are the following:
- Object ID
- String

The Database has three collections: 

**Recipes**

| Title | Field in db | Form validation type | Data type |
--- | --- | --- | --- 
Recipe ID | _id | None | ObjectId 
Recipe Name | recipe_name | text | string
Meal Type | meal_type | text | string
Recipe Description | recipe_description | text | string
Recipe Picture | recipe_pic_url | text | string
Recipe Ingredient and Info | recipe_ingredient_id_* | none | string
Recipe Ingredient Name | name_recipe_ingredient_id_* | none | string
Recipe Instructions | recipe_insturctions | text | string
Added By | added_by | none | string
Edited By | edited_by | none | string
Public Recipe | public | checkbox | string

- Each ingredient added to the recipe is given two unique fields in the object. One containing the name of the ingredient, measurment info and comments. The other, just the name of the ingredient.

**Ingredients**

| Title | Field in db | Form validation type | Data type | Core Ingredient Field | User Ingredient Field |
--- | --- | --- | --- | --- | ---
MongoDB Ingredient ID | _id | None | ObjectId | Yes | Yes  
Original ID | id | none | string | Yes | No
Ingredient Name | name | text | string | Yes | Yes
Ingredient Description | description | text | string | Yes | Yes
Wikipedia Article | wikipedia_id | none | string | Yes | No
Food Group | food_group | none | string | Yes | No
More Info Link | more_info_link | text | string | No | Yes
Added By | added_by | none | string | Yes | Yes
Subsitute Ingredient and Info | sub_ingredient_id_* | none | string | Yes | Yes
Subsitute Ingredient Name | name_sub_ingredient_id_* | none | string | Yes | Yes

- Each substitute ingredient added to the ingredient is given two unique fields in the object. One containing the name of the subsitute ingredient and the 'how to subsitute' comment. The other, just the name of the subsitute ingredient.
- The core ingredients were converted and uploaded from a free food database. As such, the fields of the core ingredients and the user added ingredients are slightly diffrent. When viewing a user submitted ingredient, 'User Submitted' is displayed.  

**Users**

| Title | Field in db | form validation type | Data type |
--- | --- | --- | --- 
User ID | _id | None | ObjectId 
Username | username | text | string
Hashed Password | user_password | text | string

## Testing

This project as be throughly tested throughout development. Some of the main testing of features included:

- Register/Create a new user.
- Create a recipe.
- Edit a recipe.
- Copy a recipe.
- Delete a recipe.
- Create an ingredient.
- Edit an ingredient.
- Delete an ingredient.
- Search for a recipe.

- The code has been validated by [W3C Markup Validation Service](https://validator.w3.org), [JShint](https://jshint.com/) and [PEP8online](http://pep8online.com/)

Through details on testing can be found in [Testing.md](testing.md)

## Deployment

### GitHub 

[My GitHub Repository](https://github.com/Trevbytes/Chickpeas)

After navigating to my repo you can download the project to a .zip file or open it in the online IDE Gitpod.

<img src="/static/images/readme/clone_repo.jpg">

For more infomation on how to clone or download the repository click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Local Deployment

**To run this project locally**

To run the project locally the following must be installed: 
- An IDE, such as [VS Code](https://code.visualstudio.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/), python requirements installer.
- [Python3](https://www.python.org/downloads/), chosen coding language of the app.
- [GIT](https://www.atlassian.com/git/tutorials/install-git), version control.
- [MongoDB](https://www.mongodb.com/), database.


After, download a .ZIP file of my repository ([Master Branch](https://github.com/Trevbytes/Chickpeas)) and unzip this file. In the control line interface, with GIT installed, enter the following command: 
   
    https://github.com/Trevbytes/Chickpeas.git

- Navigate to the root path using the `cd` command. 
- Create a `.env` file for environment variables. Include `MONGO_URI` and `SECRET_KEY` values.
- All requirements from requirements.txt must be installed. Use the following command:
    
        sudo -H pip3 -r requirements.txt
- Sign up for a free account on MongoDB and create a new Database for the Chickpeas app. Three collections should be created: recipes, ingredients and users. 
- You should then be able to launch your app using the following command in your terminal:

        python app.py

### Remote Deployment

This project is hosted on Heroku with the [master branch](https://github.com/Trevbytes/Chickpeas) deployed.

In order to remotely deploy this project on Heroku the following is the method I recommend.

- Ensure an updated `requirements.txt` exsists in the project. Use the terminal command `pip freeze > requirements.txt` to quickly create/update the file.
- Ensure a Procfile exists, this essientaly lets Heroku know where to start the app. Use the terminal command `echo web: python app.py > Procfile` to quickly create a Procfile. 
- Using git (`git add .`, `git commit -m "<your comment>"`) will stage any created or updated files. After, push the project to GitHub using `git push`.
- Using a browser, naviagte to [Heroku](https://dashboard.heroku.com/login). Login or create a free account.
- Select the "new" button, give the project a name & set the region. 
- After, from the Heroku dashboard of the new app, click on "Deploy" > "Deployment method" and choose GitHub.
- Review and confirm the connection of your Heroku app to your GitHub repository.
- From the Heroku dashboard for the app, select "Settings" and then "Reveal Config Vars".
- Configure the following variables:

| KEY | VALUE |
--- | --- | 
IP | 0.0.0.0|
PORT | 5000|
MONGODBNAME | <database_name>
MONGO_URI| mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority 
SECRET KEY | <secret_key>

- In the Heroku dashboard, click "Deploy".
- Congrats, if all went well, the app is now deployed.

## Credits

### README Structure

- While writing this README I have used two other READMEs (alongside my previous knowledge) for content and structural inspiration. [Sabinemm](https://github.com/sabinemm/recipe-site-ms3/blob/master/README.md) and [ClaireLally](https://github.com/ClaireLally8/StudyPal/blob/master/README.md) 

### Ingredient Content

- The core ingredients and their content found in this project were imported from a free database created by [www.foodb.ca](https://foodb.ca/). 

### Media

- Images I have used are freely useable and provided from [Unsplash](https://unsplash.com/). 

### Acknowledgements

- When stuck with coding issues, I used the following sites to help understand/solve the issues: [W3schools](https://www.w3schools.com/) and [StackOverflow](https://stackoverflow.com/)
- I'd like to thank Tutor Support from Code Institute for helping me "Rubber Duck" my way through some of the more complex areas of the project.