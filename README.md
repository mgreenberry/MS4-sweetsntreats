![image]()

# Sweets 'N' Treats
> ## Online Sweet and Treat Shop

[View the website here]()

## Author Note

With more time I would like to tidy up the html pages so that they are more modular. I would also work on the colours of the website and some of the css using classes to target differing elements.

I would also use something like [blueprint]() to tidy and make my app.py file more modular

## About



This is my MS4 Milstone Project website created as part of a Full Stack Software Development in Code Institute by [Michael Greenberry](https://www.linkedin.com/in/michael-greenberry-637299108/).

![Mockup]()

## Table of contents
1. [UX - User Experience](#ux-user-experience)
   * [User Goals](#user-goals)
   * [User Stories](#user-stories)
   * [Design Choices](#design-choices)
     1. [Typography](#typography)
     2. [Colours](#colours)
     3. [Imagery](#imagery)
     4. [Icons](#icons)
     5. [Layout](#layout)
   * [Structure](#structure)
   * [Wireframes](#wireframes)
2. [Features](#features)
   * [All Pages](#all-pages)
   * [Food List](#food-list)
   * [Shopping List](#shopping-list)
   * [Wasted Food List](#wasted-food-list)
   * [Error Pages](#error-pages)
3. [Structure](#structure)
   * [Users](#users)
   * [Food List](#food)
   * [Shopping List](#shopping)
   * [Wasted Food List](#wasted-food)
4. [Technologies Used](#technologies-used)
   * [Languages](#languages)
   * [Framework Library](#framework-library)
   * [Tools](#tools)
   * [Testing Tools](#testing-tools)
5. [Testing](TESTING.md)
6. [Deployment](#deployment)
   * [Project creation](#project-creation)
   * [Linking Site to MongoDB](#linking-site-to-mongodb)
   * [Deployment on Heroku](#deploying-on-heroku)
   * [Forking](#forking)
   * [Cloning and Implementing Locally](#cloning-and-implementing-locally)
7. [Credits](#credits)
   * [Content](#content)
   * [Media](#media)
   * [Icons](#icons)
   * [Code](#code)
8. [Acknowledgements](#acknowledgements)
9. [Author Information](#author-information)

## UX (User Experience)

### User Goals


[Back to content](#table-of-contents)

The site owner has done the following:-
1. 

TO BE IMPLEMENTED!
As a new user or user returning to the site:
1. 

[Back to content](#table-of-contents)
### Design Choices

#### Typography

For fonts, I used [Google Fonts](https://fonts.google.com) for my website. 

I have chosen the font-family: [Open Sans]() for the information displayed within the lists, and [Lato](); for the Headings and Menu sections of the website as it is easy to read and has a nice cursive font which matches the style of the website. I also felt this fitted in well with the design of the website.

#### Colours

For this website I chose colours that would match food waste - greens and browns and kept buttons blue and red as this is expected convention for website forms, etc. 

To style apart from materalize, Coloors was used to add colours to all elements that were needed that materalize wasn't used

From: - (https://materializecss.com/color.html)

Additonal colours from:- (https://coolors.co/8fb339-f7fff7-d62828-7494ea-4c934c)

![]()

#### Imagery

* Favicom: 
  *  [Hero Image]()
  
* All pages
  * Background Image: [Background Image]()

#### Icons

All icons from [Font Awesome](https://fontawesome.com/)

#### Layout

This website is designed with access from the home page to all other pages from the navigation bar. 

[Proposed Layout]() 

This blueprint was then used to design the navigation and call-out buttons featured in the website.

[Back to content](#table-of-contents)

### Structure 

I have used [Materialize](https://materializecss.com/) to create the overall structure for my website. 
Materialize is similar to Bootstrap in that it provides templates for items such as navigation, buttons, and structure
The reason I choose Materiaize was mainly due to the various features they offer like a datepicker for the forms and card/modal elements

## Wireframes
I used Balsamiq to create my wireframes. I chose to do a mobile version first with the pages I wanted and then create a desktop version after. I did this as this was going to be the way I designed my website, mobile first.

**Mobile**
* [Mobile]()

**Tablet**
* [Tablet]()

**Desktop**
* [Desktop Computer]()

[Back to content](#table-of-contents)
## Features

### Existing Features

#### All Pages
```
ON USER REGISTRATION OR LOG IN
```
Every page contains the following features at the top of the website as standard: -
* Text as a header reading "Waste Not Want Not" which also acts as a clickable event to take to the home page
* A responsive navigation bar, which reduces into a 'hamburger' navigation bar on mobiles. Allows all users to click on the page they want and access said page easily. Each navigation bar has the following links: -
  1. MOBILE ONLY - Home Page - Displays 'Log In' section if user not logged in. Displays an 'about' section
  2. Food List - displays food stock list in the order of use-by-date
  3. Shopping List - displays food items added to shopping list in alphabetical order
  4. Wasted Food List - displays food wasted from stock list in alphabetical order
  5. Profile Page - Instructions, contact details and log out function

  Every page contains the following features in the footer: -
* Site header and strapline
* Contact details (fake)
* Website creator with link to LinkedIn page

#### Food List
  1. Food List - displays food stock list in the order of use-by-date
  2. Add Food - allows users to add food to a food stock list
  3. Allows user to edit items on their food list
  4. Allows user to add item from food list to a shopping list
  5. Allows user to delete food item from their food list
  6. Allows user to add food item to a food wasted list if food is thrown out

#### Shopping List
  1. Shopping List - displays food stock list in alphabetical order
  2. Add Food - allows users to add food to a shopping list
  3. Allows user to edit items on their shopping list
  4. Allows user to delete food item from their food list

#### Wasted Food List
  1. A list of items that a user has had to waste taken from food used up/wasted or added by user  
  2. A button which allows user to delete waste food items

#### Profile Page
  1. A log out button which removes user from current session
  2. A set of instructions on how to use the site
  3. Contact detail information 

#### Error Pages
* These pages are not linked to any other page in the website
* These pages are only accessed if the user encounters an error within the navigation process
* The error page displays a message to the user to notify them of the error
* There is 1 call-out button in this section. This allows the user to return to the home page of the main website - [Home Page]()

## Structure
[]() was used to create the database. This allows the following functionality: -
* Registration
* Log In/Sign Out
* Add multiple food items to users collection
* CRUD:-
  * Create: Create a new user. Create a new food item in grocery/shopping or wasted food list
  * Read: Collects information held within the database
  * Update: Allows editing of items in database, such as food items in the grocery and shopping list
  * Delete: Allows deleting of items in database, such as food items in the grocery, shopping and wasted list
  
The MongoDB database holds the following information: -

### Users

Key      | Value
---------|-----------
_id      | ObjectId
username | String
password | String

### Food

Key             | Value
----------------|-----------
_id             | ObjectId
food_name       | String
quantity        | String
price.          | String
purchase_date   | String
use_by_date     | String
created_by      | String

### Shopping

Key      | Value
---------|-----------
_id      | ObjectId
food_name| String
quantity | String
price    | String

### Wasted Food

Key      | Value
---------|-----------
_id      | ObjectId
food_name| String
quantity | String
price    | String

[Back to content](#table-of-contents)
## Technologies Used
### Languages
* [HTML](https://en.wikipedia.org/wiki/HTML5) Used as the main markup language of the website content
* [CSS](https://en.wikipedia.org/wiki/CSS) Used to style the content of the website
* [JavaScript](https://www.javascript.com/) Used with Bootstrap for the Navigation menu at the top and bottom of the website and for all interactive parts of the website
* [JQuery](https://jquery.com/) Used for temperal literals in some javascript code.
* [Python](https://www.python.org/) 
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)

### Framework Library
* [Materalize](https://materializecss.com/) Used for a mobile first responsive website, display properties such as grid layout, preset css such as for containers, forms, etc
* [JQuery](https://jquery.com/) Used for temperal literals in some javascript code.

### Tools
* [Wireframes with Balsamiq](https://balsamiq.com/) To create mockups of the website to aid creation
* [Github](https://github.com/) To store and host source code
* [Gitpod](https://gitpod.io/) To write the code 
* [Google Fonts](https://fonts.google.com) for the fonts used in the website
* [Coolors](https://coolors.co/) to source the main colours for the website
* [Favicons](https://www.favicon.cc) to create a favicon for the tab and website title
* [Heroku](https://id.heroku.com/login) to host the finished project

### Testing Tools
* [hmtl validation](https://validator.w3.org) to check the html code had no errors
* [css validation](https://jigsaw.w3.org/css-validator/) to check the css code had no errors
* [JAVASCRIPT](https://jshint.com/) to check for warnings/errors
* [pep8 Online](http://pep8online.com/) to test Python code
* [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) an online validation tool that helps to improve performance and quality of the webpage with helpful tips to improve as each html page is scored.

[Back to content](#table-of-contents)
## Testing
Testing information can be found [here](TESTING.md)

[Back to content](#table-of-contents)
## Deployment

### Project creation
* The website project was created by going to [Github](https://github.com/), a code hosting platform, using the following steps: -
  1. Create an account using an email address and password or a google account
  2. Log in to account and create a new repository!
  3. Give this new repository a creative name. Then click the green Gitpod button which will take you to [Gitpod](https://gitpod.io/workspaces). Gitpod is an open source platform for code development
  4. Then open this platform and start coding
  5. To save the work I had to do the following: - Click 'File', click 'auto save'
  6. To save the work to github I needed to do the following: -
    * git add (either the name of the file, i.e. home.html or '-A', or '.' which adds everything that has been worked on that day)
    * git commit (either the name of the file, i.e. index.html or '-m' and then add a comment in parenthesis "" and enter)
    * It is recommended to commit daily. To complete the necessary steps to upload to github I needed to use the command - git push. This then 'pushed' all the saved work back to Github

### Linking site to mongoDB

To clone the project: 
1. From the repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:
    ```
    git clone https://github.com/mgreenberry/Waste-Not-Want-Not.git
    ```
2. Access the folder in your terminal window and install the application's [required modules](https://github.com/mgreenberry/Waste-Not-Want-Not/blob/main/requirements.txt) using the following command:
    ```
    pip3 install -r requirements.txt
    ```
3. Sign-in or sign-up to [MongoDB](https://www.mongodb.com/) and create a new cluster
  * Within the Sandbox, click the collections button and after click Create Database
  * Set up the following collections: users, food, shopping, waste
  * In the user collection set up the following: -

        Key             | Value     | Information
        ----------------|-----------|-------------
        _id             | ObjectId  |       This will be automatically generated by MongoDB
        username        | String    |       creates a username
        password        | String    |       will store a password

    * The food, shopping and waste collections will automatically be created when using entering in your own form entries.

  * Under the Security Menu on the left, select Database Access.
  * Add a new database user, and keep the credentials secure
  * Within the Network Access option, add IP Address 0.0.0.0
4. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ["IP"] = "0.0.0.0"
    os.environ["PORT"] = "5000"
    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"
    os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
    os.environ["MONGO_DBNAME"]= "DATABASE_NAME" 
    ```
    Please note that you will need to update the **SECRET_KEY** with your own secret key, as well as the **MONGO_URI** and **MONGO_DBNAME** variables with those provided by MongoDB.

    To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. 
    Don't forget to update the necessary fields like password and database name. 

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.
5. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 app.py. 
    ```
### Deploying on Heroku: 

1. Register for your free Heroku account and create a new app. Choose your region. 
2. Name the app something unique and choose what region you are in then click 'Create app'.
3. Go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.
4. Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository. For example: -
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile: echo web: python app.py > Procfile
    ```
3. The Procfile should contain the following line:
    ```
    web: python app.py
    ```    
4. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
5. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
6. Scroll back up and click "settings". 
    Scroll down and click "Reveal config vars". 
    Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME):
    Do not set the DEBUG variable here. This should be set to False before deployment.
    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = YOUR_SECRET_KEY
    MONGO_URI = YOUR_MONGODB_URI
    MONGO_DBNAME = DATABASE_NAME
    ```
7. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
8. Just beneath, click "Deploy branch". Heroku will now start building the app. 
    When the build is complete, click "view app" to open it.
9. In order to commit your changes to the branch, use git push within gitpod to push your changes. 

### Forking  
* If you wish to use this repository as a starting point for your own design, or to contribute to this project, you can fork it. Follow the steps below.
  1. Navigate to the repository in [github](https://github.com/). 
  2. Choose the correct repository. In this case it is [waste not want not](https://github.com/mgreenberry/Waste-Not-Want-Not)
  2. Click 'Fork' in the top-right corner.
  4. This will then create a copy (make sure you have already created your own github account) in your repository
  5. Now follow the steps outlined in [project creation](#project-creation) 
  6. Click 'Pull Requests' and seclect 'New Pull Request' button

### Cloning and Implementing Locally
* To clone the website please use the following steps: -
  1. Navigate to the repository in [github](https://github.com/). 
  2. Choose the correct repository. In this case it is [](https://github.com/mgreenberry/Waste-Not-Want-Not)
  3. Click the 'Code' button
  4. You will now be given options to make a clone of the website, to download it or to open with GitHub Desktop. You can choose to clone the 'HTTPS', the 'SSH' or 'GitHub CLI'
  5. Open Git Bash or similar
  6. Navigate to your desired directory for the cloned project.
  7. Type 'git clone' followed by the URL copied in step 3.
  8. Press 'Enter' to create your local clone.

[Back to content](#table-of-contents)

## Credits

Coding is credited where necessary within code. Most of the python code was amended from the task mini project from Code Institute with additional help from tutors and mentor. 

### Content
The text content was provided by the creator

### Media
* Favicom created by designer
* background image - [Artist and zabiyaka](https://pixabay.com/users/victoria_borodinova-6314823/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6620951)
    from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6620951)

### Icons
All icons used were sourced form [Font Awesome](https://fontawesome.com/)

### Code

#### HTML
HTML pages adapted from the Task mini project from Code Institute with additonal coding by myself. 
add-food.html
add-shopping.html
base.html
edit-food.html
edit-shopping.html
profile.html
register.html

groceries.html adapted from catergories.html with lots of amendments and additional code required for functionality

home.html - created by myself apart from log in section
shopping & waste.html pages adapted from catergories.html with lots of amendments and additional code required.

#### CSS
CSS code was written by the creator Michael Greenberry unless stated

#### JavaScript/JQuery
JQuery code was taken from Materalize or task mini project apart from navbar collapse and datepicker which was adapted

#### Python
Python, Flask and Jinga code adapted from the task mini project with extra code written by Michael Greenberry
Help from Code Institute for moving an item from one list to another. Other help mentioned in TESTING.md
Help also received on tidying code and clean code from mentor

[Back to content](#table-of-contents)
## Acknowledgements
Many thanks to the following people for their help with this project: -

Scott, Sean and Jo and other tutors from Code Institute

Mentor: narender_mentor

Code Institute Slack Students for their feedback and help with my questions

[Back to content](#table-of-contents)
## Author information
Michael Greenberry is the creator and owner of this website. This is a MS3 Milstone Project website created as part of a Full Stack Software Development in Code Institute by [Michael Greenberry](https://www.linkedin.com/in/michael-greenberry-637299108/).

[Back to content](#table-of-contents)