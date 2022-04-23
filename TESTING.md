# Sweets 'N' Treats - Testing document

[README.md file](/README.md)

## Table of contents

1. [Validation Testing](#validation-testing)
2. [Lighthouse Testing](#lighthouse-testing)
   * [Mobile Phone](#mobile-phone)
   * [Desktop](#desktop)
3. [Manual Testing](#manual-testing)
   * [All Pages](#all-pages)
   * [Forms](#forms)
4. [User Story Testing](#user-story-testing)
5. [Bugs](#bugs)

## Validation Testing

* [html testing with W3C Markup Validation Service](https://validator.w3.org/)
All errors and warnings listed

* [index](docs/testing/html-validation/index.png)
  * removed 'type=text/javascript' from script tags
* [product](docs/testing/html-validation/products.png)
  * removed strag </i> tag from html code where it appeared
  * removed 'type=text/javascript' from script tags
* [product detail](docs/testing/html-validation/product-detail.png)
  * removed strag </div> tag which was before the 'endif' statement and should have been after
  * removed 'type=text/javascrpt' from script tags
* [basket](docs/testing/html-validation/basket.png)
  * removed 'type=text/javascript' from script tags
* [checkout](docs/testing/html-validation/checkout.png)
  * removed 'type=text/javascript' from script tags
* [add-product](docs/testing/html-validation/add-product.png)
  * removed 'type=text/javascript' from script tags
* [edit-product](docs/testing/html-validation/edit-product.png)
  * removed 'type=text/javascript' from script tags
* [edit-review](docs/testing/html-validation/edit-review.png)
  * removed 'type=text/javascript' from script tags

* [css testing using W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
All CSS code was put through the W3C Validation Service. The following message was shown: -
![css testing results](docs/testing/css.png)

* [JsQuery testing using jshint.com](https://jshint.com/).
  At the time of writing this Testing document I have not had chance to check the jquery/javascript through jshint.

* [Pep8 Testing](http://pep8online.com/)
pep8 tests were done on all html and py files. All html pages had similar warnings about whitespace and identation. Where possible this was changed to remove warning. However, removing some warnings by adding/deleting whitespace or changing identation broke the code and some code wouldn't work as expected. This was especially true of the following example - £{{ item.product.price | calc_subtotal:item.quantity }}

On the settings.py in the sweetsntreats folder the only errors were lines too lone. I was unable to change this and still get the page to site to work correctly. Changing back to the longer line worked fine.

Not all pages that were tested are included in the images attached.

* [index](docs/testing/pep8/index.txt)
* [products](docs/testing/pep8/products.txt)
* [product detail](docs/testing/pep8/product-detail.txt)
* [basket](docs/testing/pep8/basket.txt)
* [checkout](docs/testing/pep8/checkout.txt)
* [Example of settings.py](docs/testing/pep8/sweetsntreats-settingspy.txt) other py files were checked and no errors found

All unused variables appeared to be called when required and code was seen to be functioning as intended.

[Back to content](#table-of-contents)

## Lighthouse Testing

### Mobile phone

ALL USERS

* [index](docs/testing/lighthouse-mobile/index.html.png)
* [products](docs/testing/lighthouse-mobile/products.png)
* [product detail](docs/testing/lighthouse-mobile/product-detail.png)
* [basket](docs/testing/lighthouse-mobile/basket.png)
* [checkout](docs/testing/lighthouse-mobile/checkout.png)

LOGGED ON USER & SUPERUSER

* [edit a review](docs/testing/lighthouse-mobile/edit-review.png)

LOGGED IN SUPERUSER

* [add a new product](ddocs/testing/lighthouse-mobile/add-product.png)
* [edit a product](docs/testing/lighthouse-mobile/edit-product.png)

I also noticed that running more than one lighthouse test on this page delivered a different set of results.
The registration/login pages produced similar results

* FINDINGS
The main issue on the lighthouse test was assessability scores which on most pages was below 90%. This was mainly due to the contrast of colours chosen and the lack of tags on some buttons for screen readers. To fix this I would change the contrast and add the relevant text where required. Please see the WAVE testing for more details.

The other issue I found was the performance on Mobiles was less than 90% which I'm not very happy about. If I get time I will reduce the size of the images which is the biggest issue affecting performance here.

### Desktop

ALL USERS

* [index](docs/testing/lighthouse-desktop/index.png)
* [products](docs/testing/lighthouse-desktop/products.png)
* [product detail](docs/testing/lighthouse-desktop/product-detail.png)
* [basket](docs/testing/lighthouse-desktop/basket.png)
* [checkout](docs/testing/lighthouse-desktop/checkout.png)

LOGGED ON USER & SUPERUSER

* [edit a review](docs/testing/lighthouse-desktop/edit-review.png)

LOGGED IN SUPERUSER
  
* [add a new product](ddocs/testing/lighthouse-desktop/add-product.png)
* [edit a product](docs/testing/lighthouse-desktop/edit-product.png)

* FINDINGS
All the above have very good scores for all pages apart from the assessability scores which I need to address. I have used WAVE to highlight the changes needed - see later. I may not get the time to implement these changes as I desire.

[Back to content](#table-of-contents)

## Assessability Testing

Used Wave.

## Manual Testing  

The layout of the website is as follows: -
[layout](docs/readme/navigation.png)

An unregistered user can use the following pages: -

* index
* products
* product-detail
* basket
* checkout

A registered and logged in user will also be able to do the following: -

* add a review
* edit a review they created (not edit a review by a different user)
* delete a review they created (not delete a review by a different user)
* add an item as a favourite
* remove an item as a favourite
* add a purchase to their profile and see past purchases
* see their profile and make changes to delivery information

A superuser can do the above and the following: -

* add a product to the store
* edit a product in the store
* delete a product from the store

[Back to content](#table-of-contents)

### Header and Navigation

Search Bar

* Expectation: - A user can type in a name or part of a name of a product they hope to find. i.e searching for 'candy' will bring up a search result for any product with the word candy in it
* Test: - Searched for a product called candy
* Result: - Displayed 2 products with the name candy within the product name
* Verdict: - Working as intended

Hero Text on Navigation bar

* Expectation: - The site name hero text should take a user back to the home (index.html) page
* Test: - I clicked the text on every page
* Result: -  I then directed me back to the home (home.html) page, i.e - clicking the site name text on the basket page  (basket.html) directed me back to the Home (index.html) page
* Verdict: - Working as intended

My Account

* Expectation: - A user can register for an acocunt or login into an existing account
* Test: - Register a new user into the account and click on the new users profile. Log out and then log back in with new user
* Result: - A new user was created, profile checked and new user details used to log in
* Verdict: - Working as intended

Profile - (Logged in user or superuser only)

* Expectation: - A logged in user should be able to see link to their profile
* Test: - Log on with the following user details: -
   username - JohnnyMillard
   password - BS2208df
* Result: - Profile information for this user was visable when clicking the profile link in the My Account 
* Verdict: - Working as intended

Product Management - Only available for a superuser

TEST 1 - Product Management Link - (SUPERUSER ONLY)

* Expectation: - A superuser has a 'Product Mangement' link in the My Account' section on the nav bar
* Test: - using the following superuser log in details: -
   username - michaelgreenberry
   password - BS2208df
This should now allow a menu option to access the Product Management which will add a product
* Result - Product Management tab is available and superuser is able to add a new product
* Verdict - Working as intended

TEST 2 - Add a product (SUPERUSER ONLY)

* Expectation: - Superuser is able to add a product to the store
* Test: - A test product can be added to the store (please use the following picture and details): -
   category - fizzy sweets
   SKU - FIZZCOLA
   Name - Fizza Cola Bottles
   Description - Fizzy cola flavoured sweets in the shape of a bottle
   Price - 1.49
   Rating - 4
   Image URL - leave blank
   Select Image - [picture]()

Log out

* Expectation: - logged in user can log out of their account
* Test: - Click log out from the 'My Account' button on the nav bar to log out
* Result: - Logged out from account
* Verdict - Working as intended

Basket

* Expectation: - clicking the basket link with products added to it will take the user to thier basket. If no products have been added then clicking the basket link will display a message to the user and provide them a link to the products page.
* Test: - Without adding a product click basket and see message to state empty basket. Add a product and click basket link. 
* Result: - Clicked basket without adding a product and saw the empty basket message with link to products. Added a product to the basket and clicked the basket to see items added
* Verdict: - Working as intended

[Back to content](#table-of-contents)

### index.html

* Expectation: - Clicking on the 'Shop Now' button will take user to all the products
* Test: - Click on 'Shop Now' button to take user to all products
* Result: - Clicking on the 'Shop Now' button took me to the all products page
* Verdict: - Working as intended

### products

TEST 1 - Visiting product detail page (User not logged in)

* Expectation: - Clicking on any product will take user to the product detail page
* Test: - Click on a product to display individual products
* Result: - Clicked the first item on the products page and was taken to the individual product details page
* Verdict: - Working as intended

TEST 2 - Marking item as favourite (User logged in (please use the log on details for JohnnyMillard))

* Expectation: - Clicking on the empty heart icon will add product as a favourite for logged on user. Heart will then go solid.
* Test: - Click on empty heart icon to add product as a favourite
* Result: - Clicking on empty heart added an item as a favourite - this was seen by the heart going solid and the admin site showing the item linked to the user (use superuser log in details in the admin site)
* Verdict: - Working as intended

### product detail

TEST 1 - Add product to basket (User not logged on)

* Expectation: - An item can be added to the basket
* Test: - Click on 'Add to Basket' to add item to basket
* Result: - Clicked on 'Add to Basket' and added items to basket. This is shown in the navigation bar with the basket icon
* Verdict: - Working as intended

TEST 2 - Add extra items to the product (User not logged in)

* Expectation: - An individual product quantity can be increased and added to basket
* Test: - Increase the quantity of a product and add items to basket
* Result: - Increased a product to 5 and added to basket. Basket icon showed new subtotal
* Verdict: - Working as intended

TEST 3 - Keep Shopping button (User not logged in)

* Expectation: - Clicking the 'Keep Shopping' button will take user back to the all product page
* Test: - Click the 'Keep Shopping' button to return to the all products page
* Result: - Clickign the 'Keep Shopping' button returned user to page displaying all the products
* Verdict: - Working as intended

TEST 4 - Add a review to a product (User logged in)

* Expectation: - On the Individual Product page click the Review Title and Review body and fill in a review
* Test: - Add a review to a product by entering a Review Title and Body to an individual product
* Result: - Added a review to the product by entering a review title and body and clicking the 'Add Review' button
* Verdict: - Working as intended

TEST 5 - Edit a review (Same user logged in)

* Expectation: - Clicking on 'Edit Review' allows logged in user to edit review written by them
* Test: - Click on 'Edit Review' button and change review details
* Result: - Clicked on 'Edit Review' button and changed the review
* Verdict: - Working as intended

TEST 6 - Edit a review (Different user logged in)

* Expectation: - User should not be able to edit a review they haven't created
* Test: - Try to change review
* Result: - There should be no option for a different user to the review user to change review
* Verdict: - Working as intended

TEST 7 - Edit Product (SUPERUSER LOGIN ONLY!!)

* Expectation: - Superuser should be able to edit an existing product by clicking on 'Edit Review' button
* Test: - Edit the test product added earlier and submit
* Result: - Test product was edited correctly
* Verdict: - Working as intended

TEST 8 - Delete Product (SUPERUSER LOGIN ONLY!!)

* Expectation: - Superuser can delete an existing product. A modal should prevent accidental deletion (Use TEST PRODUCT Created)
* Test: - Click the 'Delete Product' button. On modal choose 'Delete Product' confirmation
* Result: - Modal warning message displayed and confirm delete, deleted product
* Verdict: - Working as intended

[Back to content](#table-of-contents)

### Basket

TEST 1 - 





[Back to content](#table-of-contents)

#### Forms

There are multiple forms within the website: -

1. Register containing username and password
2. Log In containing username and password
3. Add Food Item allowing the user to enter food into their current stock list
4. Edit Food Item allowing the user to edit the food item if error made
5. Add Shopping Food Item allowing the user to add an item to their shopping list
6. Edit Shopping Food Item allowing the user to edit the item in their shopping list if error made

**Registration Form**

1. User Name (required) - Text entered - michael
2. Password (required) - Text entered - michael01
   * Expectation: - Entering text in the right format in all fields and then pressing 'Submit' button allows the form to be submitted
   * Test: - Created an account using the username - michael and password michael01
   * Result: - I was directed to the 'profile' page once registered
   * Result: - A message was displayed on the profile page
   * Verdict: - Working as intended

**Registration Form - Incorrect/Duplicate Entry**

1. User name (required) - Entered the same username - michael
2. Password (required) - Entered the same password - michael01
   * Expectation: - Error message displayed informing user that username and/or password has already been taken
   * Test: - Filled in the same username and password as the previous registration
   * Result: - A warning message displayed informing me that username and/or password was already taken
   * Verdict: - Working as intended

**Log In Form**

1. User Name - Text entered - michael
2. Password - Text entered - michael01
   * Expectation: - Directed to my current Food/Stock List
   * Test: - Filled in form using my previously registered username and password
   * Result: - A welcome message appears on my Food/Stock List
   * Verdict: - Working as intended

**Log In Form - Incorrect Entry**

1. User Name - Text entered - mickey
2. Password - Text entered - michael01
   * Expectation: - Error message telling user that the username and/or password is incorrect. A second messge displayed asking user to register
   * Test: - Logged in with incorrect username
   * Result: - An error message displayed telling user that name and/or password incorrect and asking user to register
   * Verdict: - Working as intended

**Add Food Item**

1. Food Name (required) - Milk entered (not entering data doens't allow submission of form)
2. Quantity (required) - 1 entered (not entering data doens't allow submission of form)
3. Price (required) - 0.99 entered (not entering data doens't allow submission of form)
4. Barcode/ID No. - 12345 entered as test
5. Purchase Date - 07/11/21 entered (current date)
6. Use by Date (required) - 10/11/21 entered (not entering data doens't allow submission of form)
   * Expectation: - Submitting form adds a food item to current stock/food list
   * Test: - Submitted the above information into the form
   * Result: - Food Item displayed on the Food/Stock List (groceries.html)
   * Verdict: - Working as intended

**Edit Food Item**

1. Food Name (required) - Milk entered
2. Quantity (required) - 5 entered (changed the quantity)
3. Price (required) - 0.99 entered
4. Barcode/ID No. - 12345 entered as test
5. Purchase Date - 07/11/21 entered (current date)
6. Use by Date (required) - 10/11/21 entered
   * Expectation: - Submitting form edits the food item selected in the current stock/food list
   * Test: - Submitted the above information into the form
   * Result: - Food Item displayed on the Food/Stock List (groceries.html) with changes made
   * Verdict: - Working as intended

**Add Shopping Food Item**

1. Food Name (required) - Bread entered (not entering data doens't allow submission of form)
2. Quantity (required) - 2 entered (not entering data doens't allow submission of form)
3. Price (required) - 1.09 entered (not entering data doens't allow submission of form)
   * Expectation: - Submitting form adds a Shopping item to current Shopping List
   * Test: - Submitted the above information into the form
   * Result: - Shopping Item displayed on the Shopping List (shopping-list.html)
   * Verdict: - Working as intended

**Edit Shopping Food Item**

1. Food Name (required) - Eggs entered - Changed from Bread entered earlier
2. Quantity (required) - 2 entered (not entering data doens't allow submission of form)
3. Price (required) - 1.09 entered (not entering data doens't allow submission of form)
   * Expectation: - Submitting form edits a Shopping item in the current Shopping List
   * Test: - Submitted the above information into the form
   * Result: - Shopping Item displayed on the Shopping List (shopping-list.html) with amendments made
   * Verdict: - Working as intended

[Back to content](#table-of-contents)

## User Story Testing

The following are the User Stories from the README.md page and the resulting Test and Result

### User Stories

As a user visiting the site for the first time:

1. I would like to be able to register for the website so I can have my personal grocery list
   * Test: - I registered for an account using username - michael, and password - michael01
   * Result: - I was directed to the profile page on the site
   * Verdict: - Success
2. I would like to easily log in once an account has been created and see my personal grocery list
   * Test: - I logged into the site from the home page with username - michael, and password - michael01
   * Result: - I was directed to the Food List page (current stock list)
   * Verdict: - Success
3. I would like to see my existing food stock displayed in an easy to understand format
   * Test: - I added a list of food items to my stock list
   * Result: - The food items were displayed in 'use by date' order
   * Verdict: - Success
4. I would like to be able to add new items to this stock list
   * Test: - I added a list of food items to my stock list
   * Result: - The food items was added to my existing stock/food list in use-by-date order
   * Verdict: - Success
5. I would like to be able to edit any items added to add/amend information created in error
   * Test: - I clicked the 'edit' button and editing an existing food item
   * Result: - The food items was sucessefully changed with the new information
   * Verdict: - Success
6. I would like to be able to delete food items no longer needed
   * Test: - I clicked the 'delete' button and a warning message was displayed to confirm deletion
   * Result: - The food items was sucessefully deleted from the food/stock list
   * Verdict: - Success
7. I would like to be able to add an item that has been eaten to my shopping list if desired. If not the item is deleted
   * Test: - I clicked the 'eaten' button and a message was displayed to confirm adding item to shopping list
   * Result: - The food item was sucessefully added to the shopping list
   * Verdict: - Success
8. I would like to be able to see what food I have wasted
   * Test: - I clicked the 'thrown away' button on a food item
   * Result: - The food item was sucessefully added to the wasted food list
   * Verdict: - Success
9. I would like to be able to see a shopping list of items I need to buy again that have been eaten
   * Test: - Click the 'shopping list' text in the navigation bar/hamburger menu
   * Result: - The shopping list displayed items I had in my shopping list in alphabetical order
   * Verdict: - Success
10. I would like to be able to add items to this shopping list that were not on the original grocery/food list

* Test: - I added a food item to my shopping list
* Result: - The food items was added to my existing shopping list in alphabetical order
* Verdict: - Success

11. I would like to be able to edit/delete items from the shopping list once ordered or no longer needed

* Test: - I clicked the 'edit' button and editing an existing shopping item. I clicked the 'delete' button and the item was deleted after a warning message was displayed
* Result: - The shopping item was sucessefully changed with the new information or deleted as required
* Verdict: - Success

12. I would like to be able to see a list of food that has been wasted

* Test: - Click the 'wasted food list' text in the navigation bar/hamburger menu
* Result: - The wasted food list displayed items I had thrown away from my stock/food list in alphabetical order
* Verdict: - Success

13. I would like to be able to delete food items from the wasted food list

* Test: - I clicked the 'delete' button
* Result: - The wasted food item was sucessefully deleted from the wasted food list
* Verdict: - Success

14. I want to able to learn and easily understand what the website is about

* Test: - I clicked the 'waste not want not' text. I also clicked the instructions menu within the profile page
* Result: - Once logged in the home page displays an 'about' section. There is also more informaition in the profile page
* Verdict: - Success

15. I want to easily understand what each section of the app does

* Test: - To make sure that all headers, paragraphs and other content was clear and readable
* Result: - I created the website using Materalize and the "row" and "col" tags to make the site responsive to all devices, but especially mobile
* Verdict: - Success

16. I want to click on navigation links to be taken to the correct page/section and to be able to return to the home page or another page without using the brower forward/backward buttons

* Test: - Each link was tested for each page, i.e. the 'shopping list' text directs me to the 'shopping list' section
* Result: - Each link directed to the correct page
* Verdict: - Success

17. I want these navigation links to include user friendly menus which are easy to uderstand and use

* Test: - I tested the navigation links on a Samsung Fold 3, an iPad Pro and a MacBook Pro 2021 model
* Result: - The navigation links worked on all devices
* Verdict: - Success

18. I want the content to be easy to read and have a predictable layout so that each page can be navigated easily

* Test: - I tested the website on a Samsung Fold 3, an iPad Pro and a MacBook Pro 2021 model
* Result: - The website worked on all devices and was responsive so that all content was easily readable
* Verdict: - Success

For the above, when designing the website I did the following to resolve the User Story desires:-

1. Created a registration section which directs new users to their profile which contains instructions, contact details and log out
2. Created a 'Log In' section on the very first page of the website so existing users do not have to find log in page
3. Created an existing food list in 'use by date' order allowing user to quickly see which items need using first
4. Created a page and a button which allows the user to add extra items to their existing food/grocery stock list
5. Created a page and a button which allows the user to be able to edit any items added to add/amend information created in error
6. Created a button which would allow the user to be able to delete food items no longer needed
7. Created a button which allows the user to add an item that has been eaten to my shopping list if desired
8. Created a html page which displays a page that shows the user the food items wasted
9. Created a html page which displays a page that shows the user a shopping list of items that the user may need to buy again
10. Created a page and a button which allows the user to add items to this shopping list that were not on the original grocery/food list
11. Created a button which will delete items from the shopping list once ordered or no longer needed
12. Created a page which displays a page that shows a list of food that has been wasted
13. Created a button that allows the user to delete food items from the wasted food list
14. Designed a home page with an 'about' section
15. Designed navigation tabs which clearly display each section link
16. Designed and impliment a navigation bar which contains links to different pages and sections in the website
17. Designed and label the navigation bar with clear and understandable text to direct users to the correct page  
18. Designed the website to have good readability throughout

[Back to content](#table-of-contents)

## Bugs

* add-food.html

Some bugs with food not being added or page not displaying on mobile devices very well

Edited page with additional css/html to render page on mobile device.

* add-shopping.html

There was a bug with the url_for function for adding food items as this wasn't allowing me to link up the username at first. Most of this is shown below in the app.py section

* base.html

Creating the jinga templates and app.py for base.html was amended from the task mini project

* edit-food.html

```
Message sent to tutor support October 16th 2021:-

I am trying to display a form which is already filled out from a database. This form will then be edited by the user.
I am following along the mini-project for tasks on the course but adapting for my own needs.
I have created a 'add_food.html' which is working as intended but my 'edit_food.html is not working at present.
So far I am not getting pre-filled in fields in my 'edit_food.html table in my preview.
My app.py seems to be calling the correct _id number related to the item that was added but is not displaying the name, date, etc in the form that it has found.
```

> To solve the issue I needed to 'inject' the properties of the food into the respective fields - e.g. ```<p>{{ food.description }}</p>```

* edit-shopping.html

See app.py for issues relating to editing the shopping - Issues 3

* groceries.html

No issues

* home.html

No issues

* profile.html

Username wasn't displaying once user logged in but this was amended

* register.html

No issues

* shopping.html

Major issues moving items from the Food/Stock List to the Shopping List - see app.py - Issue 1
Issue seeing items moved into Shopping List when clicking the navigation link -  see app.py Issue 2

* waste.html

No issues

* app.py
  1. Error on moving item from the Stock/Food List to the Shopping List

```
@app.route("/shopping")
def shopping():
mongo.db.food.pop("food_name")
mongo.db.shopping.insert_one("food_name")
flash("You have added an item to your shopping list")
```

> I was trying to move an item from one list in my Mongdo.db collection to another collection. For example. I wanted the user to be able to click on a button which will move a food item from the food list and put it on a shopping list.
Both the food list and shopping list appear on my mongo.db database.
I tried a pop method and searched slack and asked other students too. I also tried reading and understanding the documentation in mongo website

> I tried the following: - <https://www.w3schools.com/python/python_mongodb_delete.asp>

```
I then tried the following code in my app.py: -

@app.route("/add_food", methods=["GET", "POST"])
def add_food():
if request.method == "POST":
short_date = "on" if request.form.get("short_date") else "off"
food = {
"location": request.form.get("location"),
"food_name": request.form.get("food_name"),
"barcode": request.form.get("barcode"),
"purchase_date": request.form.get("purchase_date"),
"use_by_date": request.form.get("use_by_date"),
"short_date": short_date,
"created_by": session["user"]
}
mongo.db.food.insert_one(food)
flash("Food added succesfully")
return redirect(url_for("modifies"))
foods = mongo.db.food.find().sort("food_name", 1)
return render_template("add_food.html", foods=foods)
```

> Tutor support helped me to rewrite this to: -

```
<a href="/add_to_list/{{ item_id }}"
@app.route('/add_to_list/<item_id>/)
def add_to_list(item_id):
# get the item by id from the first collection
# copy the item as a dictionary
# delete the id from the copy
# delete the item from the first list
# insert the copy into the second list
```

```
I then created new code to move the food item to the shopping list: -

@app.route("/shopping/<food_name>", methods=['GET', 'POST'])
def shopping(food_name):
# get the item by id from the first collection
print(food_name)
food = mongo.db.food.find_one(
{"food_name": "food_name"})
print(food)
return render_template("modifies.html")
```

> I then had some issues with testing that meant that I would get the following [error message](docs/testing-images/move-error.jpg)

```
The final working code with help from my mentor was: -

@app.route("/shopping/<food_name>", methods=['GET', 'POST'])
def shopping(food_name):
    """
    Moves selected food item from the food list collection to the shopping list
    Displays success message to user
    """
    food = mongo.db.food.find_one({"food_name": food_name})
    if food:
        new_shopping_item = {
            "food_name": food.get('food_name'),
            "quantity": food.get('quantity'),
            "price": food.get('price'),
            "created_by": session['user']
        }
        print(food.get("created_by"))
        mongo.db.shopping.insert_one(new_shopping_item)
        mongo.db.food.remove({"food_name": food_name})
        flash("Food Item added to Shopping List")

    items = mongo.db.shopping.find().sort('food_name', 1)
    return render_template("shopping.html", items=items)
```

[Back to content](#table-of-contents)

  2. Error on listing items in Shopping List after user had moved them or added them

```
Message sent to tutor support

So my base.html has a nav link which is this: -
{{ url_for('shopping', username=session['user']) }}
However, I keep getting errors on the username part. I want the page to display for the current user so copied the code from one of the nav links above.
```

> The main issue was that I was getting a jinga message telling me that 'user' could not be found. A secondary issue was that I had a function which added an itme to the Shopping List from the original stock/food list which was working.

```
In the groceries.html there is a button 'Eaten'.
Clicking the "eaten' button then adds this item to the shopping list and deletes from the food list.
I am hoping to then be able to show the shopping list to the user from the nav link when they are logged in.
At the moment, I can delete an item from the food item list, it then does display a html page showing a shopping list but I can't access this page from the nav bar.
```

> I was trying to add a navigation and a function at the same time. With tutor support I created a separate function for the navigation. The navigation bar now links to the following function ![function](docs/testing-images/nav-function.png)

[Back to content](#table-of-contents)

  3. Clicking the edit shopping item on the shopping.html brings up the edit_shopping.html page and also shows the data to be edited.
However, changing any of the items has no effect on the database when submitting the form.

 ```
edit_shopping.html 

<form class="col s12" method="POST" action="{{ url_for('edit_shopping', food_name=shopping._id) }}">
```

```
app.py

@app.route("/edit_shopping/<food_name>", methods=["GET", "POST"])
def edit_shopping(food_name):
# Allows user to change food details if error in list
if request.method == "POST":
submit = {
"food_name": request.form.get("food_name"),
"created_by": session["user"]
}
mongo.db.shopping.update({"_id": ObjectId(food_name)}, submit)
flash("Shopping List Item Updated Succesfully")
return redirect(url_for("shopping"))
food = mongo.db.shopping.find_one({"_id": ObjectId(food_name)})
foods = mongo.db.shopping.find().sort("food_name", 1)
return render_template("edit_shopping.html", food=food, foods=foods)
```

However I seemed to get errors with each fix.
[Image 1](docs/testing-images/shopping-error.png)
[Image 2](docs/testing-images/shopping-error-2.png)
[Image 3](docs/testing-images/shopping-food-name-error.png)

> This was finally fixed by using the following code with help from tutors

```
@app.route("/edit_shopping/<food_name>", methods=["GET", "POST"])
def edit_shopping(food_name):
    """
    Allows user to change shopping list item details if error in list
    Displays message to user
    """
    if request.method == "POST":
        submit = {
            "food_name": request.form.get("food_name"),
            "quantity": request.form.get("quantity"),
            "price": request.form.get("price"),
            "created_by": session["user"]
        }
        mongo.db.shopping.update({"_id": ObjectId(food_name)}, submit)
        flash("Shopping List Item Updated Succesfully")
        return redirect(url_for("shopping_list"))

    shopping = mongo.db.shopping.find_one({"_id": ObjectId(food_name)})
    return render_template("edit-shopping.html", shopping=shopping)
```

* other

All other issues were minor bugs such as mistyped words, missing '{}' around template code and passing the wrong variable within the app.py or url_for jinga links

[Back to content](#table-of-contents)
