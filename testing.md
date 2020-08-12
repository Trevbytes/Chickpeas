
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

Most errors throughout the project have been simple syntax errors that took very little time to locate and correct. Some of the larger issues/bugs can be found below.

##### Resolved
 - Grid view not displaying rows correctly.
    - Jinja python logic is used to create rows depending on the amount of recipes. This creates rows of no more than 2 recipes and closes the last row if there is an uneven amount of recipes.
 - Ingredients removed in a recipe or ingredient are not removed in the database.
    - A hidden list is created when removing ingredients. This list is submitted when the recipe/ingredient is updated. All ingredients in this list are then removed from the database. 
 - The nav bar design is inconsistent on differnt pages.
    - Two design frameworks were being used, Bootstrap and Materialize. Both and been removed and only MDB is being used as the framework.
 - Long recipe descriptions are distorting recipe cards.
    - A max character of 200 has been implemented to keep descriptions short. Text is shown informing the user.
 - Pressing return when a modal is open attempts to submit the form.
    - Code has been added to prevent form submission when pressing return.
 - When removing an ingredient from a list in the modals the first click of the button appears to do nothing.
    - The first click was creating the event listener for the button but not executing the code. The event listeners for existing ingredients are now created at runtime so that the first click is responsive. Script is added to each new user added ingredient to allow removal of those ingredients.
 - Modals are unable to be reopened on some pages.
    - jQuery was being linked multiple times. Cleaning the code and ensuring only one link for jQuery exists fixed this issue.
 - Multiple ajax modals appear to be opened when clicking on an ingredient from the view recipe page.
    - Opening and closing modals did not always fully close the modal. All possible modals are now closed when closing a modal. All possbile modals are also closed when opening a new modal, before the new modal content is loaded. This allows a user to open new modals from within a modal. 
 - The filter input does not clear after submitting an ingredient.
    - Issues were happening with the cache of a modal to test if new code worked. After applying "Disable cache (while DevTools is open)" I was able to test my code and confirm that filter input now clears correctly. 

##### Unresolved
 - Removing an ingredient from the database does not remove the ingredient from recipes containing it. This results in a error when trying to view the ingredient info from a recipe.
    - This error is handled with a Error modal to help inform the user of the issue and get back to the site.
 - The filter input does not work on iOS devices. A user can still select an ingredient. However, the user must scroll through the entire ingredient database to find an ingredient.
    - A redesign of the filter code would be my ideal solution. This bug has been left due to time constraints.
 - Whitespace after an ingredient name causes an internal error when selecting that ingredient from the view recipe page.
    - This error is handled with a Error modal to help inform the user of the issue and get back to the site.
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
- Check that all links in navbar, both when logged in and when logged out, work.
    - No errors
- Check that images and nav bar display properly on all screen sizes. 
    - No errors

**Browse Public Recipes Page**
- Check that images display properly on all screen sizes. 
    - No errors
    - *Note:* When viewing recipes in grid view, the larger image on a row of recipes sets sets the size of both recipes. This, unintentionally, can poorly crop some images. Ideally, I would like to implement [Cloudinary's](https://cloudinary.com/) API to automaticlly resize images that users upload.
- Check that Grid View and List View work on all screen sizes.
    - No errors
- Check that tabs work correctly.
    - No errors
- Check that Edit, Copy and Delete buttons work on all tabs.
    - No errors
- Check that Edit and Delete are only shown for the owner of a recipe.
    - No errors
- Check that the Copy button is shown when logged in and viewing another's public recipe.
    - No errors
- Check that all modals open and close correctly.
    - No errors

**Ingredients Page**
- Check that the search button works on all screen sizes.
    - No errors
    - *Note:* After opening the search dropdown, closing the search bar without entering an ingredient can be difficult on smaller screens. The only way to close the dropdown is to either choose an ingredient or click on the search button again.
- Check many differnt ingredients for broken links.
    - No errors
    - *Note:* All 1000 ingredients have not been reviewed. When clicking on broken likes the user is redirected to an error page.
- Check that logged in users can add new ingredients.
    - No errors
- Check that all modals open and close correctly.
    - Error 500 happens when a ingredient link is clicked if the ingredient no longer exists in the database or if the ingredient name contains whitespace before or after the name. A modal appears for the user explaining the possible issues.
- Check that a user can remove an ingredient added by the user.
    - No errors

**Submit Ingredient Modal**
- Check that a name and description must be added to submit an ingredient.
    - If whitespace is added after an ingredient name, the ingredient cannot currently be viewed in modal form.
- Check that a non-admin user can add a substitute ingredient to any ingredient. A non-admin should not be able to edit or delete any other part of an ingredient.
    - No errors
- Check that the an ingredient is added to the database and that user feedback is given.
    - No errors

**Update Ingredient Modal**
- Check that an admin can fully edit or remove any ingredient.
    - No errors
- Check that a user can fully edit and remove an ingredient added by the user.
    - No errors
- Check that when submitted, the ingredient updates correctly in the database. Ensure that removed substitutes are removed from the database. 
    - No errors

**Dashboard Page**
- Check that images display properly on all screen sizes. 
    - No errors
    - *Note:* When viewing recipes in grid view, the larger image on a row of recipes sets sets the size of both recipes. This, unintentionally, can poorly crop some images. Ideally, I would like to implement [Cloudinary's](https://cloudinary.com/) API to automaticlly resize images that users upload.
- Check that only a users recipes or recipes copied by the user are displayed.
    - No errors
- Check that the grid view works with an odd number of recipes.
    - No errors
- Check that all modals (update recipe, create recipe) open and close.
    - No errors

**Create Recipe Modal**
- Check that the modal resizes to all screen sizes.
    - No errors
- Check that the ingredient filter works when adding a recipe.
    - Does not work on iOS and Safari. All ingredients are shown but none are filtered. Further research into why the current code does not work is required. 
- Check that ingredients can be added to a recipe.
    - No errors
- Check that all required inputs must be filled in order to submit.
    - A recipe filled with whitespaces can be submitted. A check to see that there is text in the input should be created.

**Update Recipe/Copy Recipe Modal**
- Check that the correct information stored in the database is used to fill the form. 
    - No errors
- Check that information is updated when submitted to the database.
    - No errors
- Check that the data in the form is sent via the correct route depending on if the form information is creating a copy of the recipe or updating the recipe.
    - No errors

**View Recipe Page**
- Check that the recipe image displays properly on all screen sizes. 
    - No errors
- Check that all buttons work as intended (Back, Cookbook, Update, Delete, Copy).
    - No errors
    - *Note:* The back button can send users to their filled in form from creating recipe. This situation could be handled better but has been left as it does not break the app and would reqiure more time to implement a better solution.
    - *Note:* After a recipe is updated a new ID is given to the recipe. If a user clicks on the back button after updating a recipe the user is sent to a recipe that no longer exists. The user is redirected to their dashboad when this happens. 
- Check that all modals (update recipe, create recipe, ingredient info) open and close.
    - Error 500 happens when a ingredient link is clicked if the ingredient no longer exists in the database or if the ingredient name contains whitespace before or after the name. A modal appears for the user explaining the possible issues.
    - *Resolved:* ~~When opening a ingredient info modal it seems that multiple instances of the modal are created. All are closed when the close button is clicked. However, when scrolling through the modal on smaller screens the underlying modal can sometimes be seen.~~
- Check that a confirmation window appears when attempting to delete a recipe.
    - No errors
- Check that no broken links to images are displayed. When a link does not work, a default image is displayed.
    - No errors

**View Ingredient Modal**
- Check that links displayed in the modal work. A new modal is opened and the current is closed when clicking on an ingredient link. When cliking on an external link a new window is created.
    - Error 500 happens when a ingredient link is clicked if the ingredient no longer exists in the database or if the ingredient name contains whitespace before or after the name. A modal appears for the user explaining the possible issues.
- Check that both close buttons work.
    - No errors
    - *Resolved:* ~~After opening an closing multiple modals on the same page loading time is increased. The buttons for closing the modal can therefore be unresponsive for a few seconds after opening a modal.~~ 

**Delete Recipe or Ingredient**
- Check that a confirm window appears when removing a recipe or ingredient. 
    - No errors
- Check the database to confirm that the recipe/ingredient is removed.
    - No errors

**Login/Logout**
- Ensure login and logout works.
    - No errors
- Ensure users are provided feedback on login, logout and signup.
    - No errors
- Ensure proper feedback is given when incorrect input is given. (Wrong username, wrong password, password mismatch when confirming a password, username already exists)
    - No errors