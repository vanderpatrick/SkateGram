# SkateGram

## By Patrick Alexander Lucas Van Der Flier

### [Check SkateGram](https://skategram.herokuapp.com/)

![Responsive image from the project](/assets/images/responsive.png)

# SkateGram :

### SkateGram was developed as my fourth project for CodeInstitute

# Reason :
As a skateboarder, I have always been part of the skate community. Being part of a skate community means supporting and sharing, we always help each other by teaching tricks giving tips, etc... One of the main things that I saw was the dependence on social media platforms for this (Support/Sharing) experience, but it gets overwhelming with the number of different subjects in such platforms hence the birth of skategram. a skate social media blog where people can share their thoughts about the skate universe as well as follow tutorials regarding skateboarding.

# The User Experience (UX)

##  Audience : 

- People who want to engage more in skateboarding.
- Skaters that want to discuss major skate topics.
- skaters who wish to share their thoughts about skating on different topics.

## User Report : 

- first experience

    1. As a user I would like easy navigation across the web application.
    2. As a user I would like access to skateboarding social media.
    3. As a user I would like to share my thoughts with other users in a dynamic way.

- Second experience

    1. I would want to check my post for likes and comments.
    2. I would want to edit posts and profiles.
    3. I would want to check for new subjects to discuss.

- As a developer    
    
    1. I want to make it interactive.
    2. I want the site to be easy to fulfill basic forms such as registration, post, and log in. 
    3. I want to give a focused blog about skateboarding so skaters feel more comfortable with their kind.


# Features :

The Features were designed to distinguish each area with ease so the user can explore the site instinctively.

- Navigation bar
    - The navigation bar is featured on all HTML pages using the extend method from Django.
    - It consists of intuitive links that tell you precisely what you can do in the application. 
    - as it shrinks the navigations become the brand title and a burger menu.

 ![navigation bar image](/static/images/navbar.png)

- Landing page
    - The homepage consists of a welcome message with options of register/login for new and old users.
    - it is easy to look at and intuitive to choose what to do.

![landing page image](/static/images/landing.png)

- Footer
    - The footer is responsible for giving information about the development of the application and contact info about the development team.
 

![info content image](/static/images/footer.png)

- Home section
    - Simple homepage for registered users to access the blog content which consists of a list of the most recent blog posts
    - The user cannot access the content of the blog without being registered, defensive code was applied to all content pages.
    - After the user becomes registered he is allowed to log in and see the contents of the application.
    - Pagination system that allows users to navigate to older posts.

![feedback info image](/static/images/navbar.png)


- Post Creation
    - The user is allowed after becoming registered to create a post that consists of a unique title, a post image, and the contents of the post.
    - After submitting, the user is redirected to the home page with his post as the first one.

![Footer image](/static/images/post-creation.png)

- Post detail
    - From the home page the user can click on a post of his choice.
    - There the user can read the content of the post, like the post unlike the post, and or comment on the post.
    - If the user is the owner of the post he is allowed to choose between deleting and editing the post 
 
![Footer image](/static/images/post-detail.png)

- Post Deletion
    - The user is allowed if authenticated to delete his post
    
![Footer image](/static/images/deleting.png)

- Log in 
    - The user after registration can fill in a form to login into the blog
    
![Footer image](/static/images/login.png)   

- registration
    - The user fills in a registration form that automatically creates a profile for such a user
 
![Footer image](/static/images/register.png)

- Profile
    - user can check and edit his profile info
    - The profile comes with a default picture and description

![Footer image](/static/images/profile.png)
 
 - pagination
    - user can check older posts through pagination
   
![Footer image](/static/images/pagination.png)
# Future Features :
 - User profile visiting
    
 - Upvoting comments
    
 - Deleting and adding comments

# Testing :

Testing in this application was made manually, defensive code was also added so that only authenticated users are allowed to edit/delete his/her posts

- Registration
    - The registration form allows the user to create an account if filled correctly
    - Before

 ![registration image](/static/images/test-registration.png)
  
  - After
  - The registration works as expected registering the user in the database and creating a profile automatically

 ![registration image](/static/images/test-registration-pass.png)
 
 - Log in
    - After filling in the user credentials he is allowed to see the application content
    - Before
    - The navbar confirms that the user is logged in and has access to the contents of the website

 ![Login image](/static/images/test-login.png
  - After
  - the username followed by the profile confirms that the user is logged in giving access to the rest of the content to the user 

 ![Login image](/static/images/test-login-pass.png)


- Profile
    - The profile is immediately created with the account registration. Pretty neat if you ask me he also comes with two default values one for the profile image and another for the description
    - Before

 ![Profile image](/static/images/test-profile.png)
  
  - After
  - The profile in the admin panel proves that the creation of the profile works fine

 ![Profiler image](/static/images/test-profile-pass.png)
 
 - Logout
    - Clicking on the logout button the user logout from his account 
    - Before

 ![LogOut image](/static/images/test-logut.png)
  
  - After
  - This confirms that the user is no longer allowed to see the contents of the page 

 ![LogOut image](/static/images/test-logout-pass.png)
 
 - Liking
    - The user is allowed to like posts when liked shows the number of likes on the page the like button becomes an unlike button reflecting directly to the database
    - Before

 ![liking system image](/static/images/test-like.png)
  
  - After
  - The admin panel highlights users that have liked a determined post as well as in the front end (see image below)

 ![liking system image](/static/images/test-like-pass.png)
  - Unliking
    - The user is also allowed to unlike the posts reflecting directly to the database
    - Before

 ![Unlikig image](/static/images/test-unlike.png)
  
  - After
  - The admin panel highlights users that have liked a determined post as well as in the front end 

 ![Unlikig image](/static/images/test-unlike-pass.png)
 
 - Edit
    - If the user is not happy with his post he is allowed to edit it
    - Before

 ![Editing image](/static/images/test-edit.png)
  
  - After
  - This confirms that the user has edited his post

 ![Editing image](/static/images/test-edit-pass.png)
 
 - Create
    - When logged in the user can create his posts
    - Before

 ![Creation image](/static/images/test-post-creation.png)
  
  - After 
  - This confirms that the creation functionality is working fine

 ![Creation image](/static/images/test-post-creation-pass.png)
 
 - Delete
    - the user is also allowed to delete his posts in a dynamic way where all tables related to that post are also deleted(likes/comments)
    - Before

 ![Deleting image](/static/images/deleting.png)
  
  - After
  - In the admin panel we can see that the data over that post no longer exists which means the delete functionality works
  

 ![Deleting image](/static/images/test-delete-pass.png)
 
 
 # User stories:
 ## For the user's stories GitHuh and Miro were used, Github as a Kambam Board and miro as a Flow Chart
  - The order of the issues was kind of random, I tried to do it with a flow of work but circumstances made me redo the project a couple of times 
  - GitHub kambarm board

 ![Kambam Board image](/static/images/kambam-board.png)
 
 - The Flow Chart was used to set the general direction that the code needed to go
  - Miro Flow Chart

 ![Miro Flow Chart image](/static/images/flowchart.png)
 
 
 # Test Validators :

## Since this is a Full stack framework project The HTML validation comes with a couple of errors, that occur because of the inputs that Django gives us such inputs are not considered HTML syntax besides that all Html pages pass with only stray div error and Django register form error
 - AN Ul error is being displayed but unfortunately this is out of my hands because is a Django form which I don't have access
 - And a stray div error that occurs because of the {% if user.is_authenticated %} tag if I move the tag it brakes the code, so unfortunately we have this div issue
 
 ## [HTML Validator - landing](https://validator.w3.org/nu/?doc=https%3A%2F%2Fskategram.herokuapp.com%2F)
 ## [HTML Validator - post](https://validator.w3.org/nu/?doc=https%3A%2F%2Fskategram.herokuapp.com%2Fpost%2F21%2F)
 ## [HTML Validator - Team](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fskategram.herokuapp.com%2Fteam%2F#l59c22)
 ## [HTML Validator - profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Fskategram.herokuapp.com%2Fprofile%2F)
 ## [HTML Validator - login](https://validator.w3.org/nu/?doc=https%3A%2F%2Fskategram.herokuapp.com%2Flogin%2F)
 ## [HTML Validator - logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fskategram.herokuapp.com%2Flogout%2F)
 ## [HTML Validator - create post](https://validator.w3.org/nu/?doc=https%3A%2F%2Fskategram.herokuapp.com%2Fpost%2Fnew%2F)
 ## [HTML Validator - register](https://validator.w3.org/nu/?doc=https%3A%2F%2Fskategram.herokuapp.com%2Fregister%2F)
 ## [HTML Validator - Team detail](https://validator.w3.org/nu/?doc=https%3A%2F%2Fskategram.herokuapp.com%2Ftutorial%2F5%2F)

All Html pages have been tested and passed with no relevant errors

 ## [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fskategram.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
 - For responsiveness, this project was tested at the desktop level, laptops, tablets(iPad), and telephones, all screen sizes have shown responsiveness

The CSS file has been tested and passed with success.

## Bugs
- The application had a lot of path bugs regarding the detail pages that were fixed using the post id as an integer 
- Custom CSS was a major problem in this application because the classes just didn't want to work, it was fixed by the use of ID instead of regular classes which gave an unfortunate duplication of id's for the application

## lighthouse
- The rating of the application was acceptable with a good performance rating

![Light House image](/static/images/light-house.png)


# Deployment :
 ## Remote Deployment (Heroku) :
 

  - Connect to your GitHub repository by searching the chosen repository and clicking connect
  ![Heroku deployment registry search](/static/images/heroku-deployment-github.png)

  - Chose the proper branch in the manual deployment and click deploy branch
  ![Heroku manual deployment](/static/images/heroku-deployment-deploy-branch.png)
  
  - Wait for the application to load and then click view 
  ![Heroku deployment loading](/static/images/heroku-deployment-view.png)
  
   - After clicking view your site will be loaded 
  ![image of the project page](/static/images/heroku-deployment-done.png)
## How to fork :
  - In the repository, you want to fork, go to the upper right corner and click fork, then click in create  fork (random project image to show how to fork)
  ![image of location from fork](/static/images/forking.png)
  - After "forking" wait while GitHub copies the repository into your profile.
  
## Desktop Deployment :
  - In the repository click on code.
  ![Code button from GitHub repository](/static/images/git-code.png)
  - Click on a download zip file.
  - When that is done, open with your chosen code program and download the requirements.txt with the commend.
  - pip install -r requirements.txt. 

  # External Features :
  ### In the links below, you will find all the icons and fonts used in the project. 

- [Google Fonts](https://fonts.google.com/)
  - Was used to select the font combination for this project.
- [Font Awesome](https://fontawesome.com/)
  - Was used to select the icons used in this project. 
- [Bootstrap](https://getbootstrap.com/)
  - Bootstrap was used as the CSS framework for this project 
  # Credits :
 1. [MDBoostrap](https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw)
  - For providing the footer code

 2. [Codemy](https://www.youtube.com/c/CodingNepal/featured)
  - For providing insight into the creation of the profile and comment section
  
 3.  [Code Institute](https://codeinstitute.net/)
  - Code Institute for all the support and care for me and my projects.

  ## Special thanks 
  I would like to thank everyone who helped me with this project.

- My mentor.
- Code Institute for giving the best support to develop this project.
- And all friends involved with helping this project 
