
This is an extension from the [README.MD](README.md) file.

[Live Application](https://chickpeas-creative-cooking.herokuapp.com/)


# Table of Contents

1. [**Code Testing**](#code-testing)
    - [**Validator Testing**](#validator-testing)
    - [**Compatibility Testing**](#compatibility-testing)
    - [**Known Issues**](#known-issues)
        - [**Resolved**](#resolved)
        - [**Unresolved**](#unresolved)

2. [**Functional Testing**](#functional-testing)
    - [**User Testing**](#user-tests)
    - [**Manual Testing**](#manual-testing)

---
## Code Testing
---
### Validator Testing

[W3C Markup Validation](https://validator.w3.org/)

W3C was used for HTML and CSS validation.
- One error is found on the ingredients page, stray end div tag.
- No errors were found in the CSS validation. 

[JSHint](https://jshint.com/)

JSHint was used to validate the Javascript files.
- No errors or warnings were found.

[JSesprima](https://esprima.org/demo/validate.html)

JSeprima was used to validate JS formatting.
- No errors were found.

[PEP8online](https://pypi.org/project/autopep8/)

PEP8online was used to validate formatting of python code. 
- No errors were found. 

#### Compatibility Testing

This project has been tested for display responsiveness throughout development. : 
 - Browsers
    - Chrome
    - Firefox
    - Opera
    - Microsoft Edge
    - Samsung Internet
 - Screen Sizes
    - 27-inch display
    - 17-inch display
    - 15-inch display
    - 13-inch display
    - 10-inch display
    - 6-inch display
    - 5-inch display    

#### Known Issues

##### Resolved 


##### Unresolved
 - Removing an ingredient from the database does not remove the ingredient from recipes containing it. This results in a error when trying to view the ingredient info from a recipe.
 - The filter input does not clear after submitting an ingredient.
---
## Functional Testing
---
 
#### User Tests

This project have been reviewed/tested by an experienced web developer. A mentor provided by Code Institute during my studies.

This project have been reviewed/tested by friends and family.

A single Full Usability test was done when all features were in place. This was done to identify possible bugs as well as ensure that the application is easy-to-use.
- Test Audience - A new user interested in cooking, looking to store their recipes and find new recipes.

    User Actions:
    - Arrive on landing page. Read 'About the Site' info.
    - Click LOGIN/SIGNUP from the nav bar.
    - Click Register .
    - Create account by entering a unique username and a password. Form lets the user know if the username is already taken or if their password does not match the 'Confirm Password' input.
    - Auto redirect to user dashboad/cookbook. Click 'Create a Recipe'.
    - Enter recipe info into form.
    - Add ingredients individually in the recipe. Use the filter to easily find the ingredient. Add measument and optional comment.
    - If ingredient does not exist, read tooltip. Finish recipe, add the ingredient to the database, then update the recipe with the new ingredient.  
    - On submission, redirected to the View Recipe page. Feedback from site that the recipe was added.
    - User creates more recipes. Navigation using the nav bar or the user's cookbook button on the recipe's page.
    - User sees that recipes they create are added to their cookbook.
    - User wants to add an ingredient. Click Ingredients in the nav bar.
    - Click "Submit a New Ingredient".
    - Enter ingredient info into form.
    - Add optional substitute ingredients.
    - Submit
    - Redirect to view ingredient when submitted with visual confirmation of added ingredient.  
    - User wants to update a recipe.
    - Type the recipe name or part of the recipe in the search bar located in the nav bar.
    - Click search or hit return.
    - Click on update button for chosen recipe.
    - Add and ingredient or update text.
    - On update, redirected to the View Recipe page. Feedback from site that the recipe was updated.
    - User wants to find a new recipe.
    - Click Browse Public Recipes in the nav bar.
    - Click desired tab: Breakfast, Lunch, Dinner, Dessert.
    - Click copy button.
        - Optional - Click recipe's name or picture to view the recipe
        - Click copy button located at the bottom of the recipe.
    - Add new name to the copy.
    - Make changes if desired.
    - Click Create Copy of Recipe. Redirected to view recipe. Feedback for recipe added.
    - User is using a small screen and viewing lots of recipes from Public Recipes or their cookbook.
    - Click the list view button for larger recipe cards.
    - View a recipe with an unknown ingredient.
    - Click on an ingredient while viewing a recipe.
    - Read ingredient info. If there are registered common substitutes, they are shown.
    - Click on a common substitute to view that ingredient info.
    - User wants to log out. Click on the account icon in the nav bar and click Logout. Redirected to landing page.   

**Feedback From User Test**

After this full test the following feedback was given:
- When making a recipe, using the 'return' key submits the recipe if the recipe is complete. If the recipe is not complete the keyboard focus shifts to the incomplete input field.
  - This issue has been resolved. Code has been added to prevent the 'return' key's attempt to submit the form.
- When updating a recipe the public toggle switch is reset to off.
  - This issue has been resolved. When updating a recipe created by the user, the public toggle option is set to the saved user preference.
- After adding an ingredient to a recipe (or substitute ingredient to ingredient) input fields are cleared expect for the filter.
  - This issue has NOT been resolved. It is a known issue.
- Gradient backround in lunch recipes did not conform to the other tabs style.
  - This issue has been resolved. A new gradient has been applied with a similar right to left gradient.

**Errors After User Test**

After the full test the following errors were found:
- Not all newly added ingredients were displaying (in modal form) when selected from a recipe.
  - This issue has been indentified. If an ingredient name contains whitespace after the name, a 500 error happens when calling the modal of that ingredient. The solution would be to automaticlly trim the input of the ending (and beginning) whitespace before it is submitted to the database.

#### Manual Testing

The testing and debugging of this project was done extensively in Chrome Dev Tools throughout the project. The process would typically go as follows:
- Create a function/feature.
- Test that function and try to break the function using unexpected input.
- Have friends/family test/review certain features to gain input and opinions.
- Fix the bugs and make updates.
- Create next function/feature.
- Repeat.

In order to ensure the site works as required, I manually tested all aspects of the deployed site.

**Landing Page and Nav Bar**
- Check that all links in navbar both when logged in and when logged out.
    - No errors
- Check that images display properly on all screen sizes. 
    - No errors

**Browse Public Recipes Page**
- Check that images display properly on all screen sizes. 
    - No errors

**Ingredients Page**
- Check that images display properly on all screen sizes. 
    - No errors

**Create Ingredient Modal**
- Check that images display properly on all screen sizes. 
    - No errors

**Update Ingredient Modal**
- Check that images display properly on all screen sizes. 
    - No errors

**Dashboard Page**
- Check that images display properly on all screen sizes. 
    - No errors

**Create Recipe Modal**
- Check that images display properly on all screen sizes. 
    - No errors

**Update Recipe/Copy Recipe Modal**
- Check that images display properly on all screen sizes. 
    - No errors

**View Ingredient Modal**
- Check that images display properly on all screen sizes. 
    - No errors

**Delete Recipe or Ingredient**
- Check that images display properly on all screen sizes. 
    - No errors

**Login/Logout**
- Ensure logout works
    - No errors