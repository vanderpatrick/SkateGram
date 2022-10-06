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

![landing page image](/static/images/navbar.png)

- Footer
    - The footer is responsible for giving information about the development of the application and contact info about the development team.
    

![info content image](/static/images/navbar.png)

- Home section
    - Simple homepage for registered users to access the blog content which consists of a list of the most recent blog posts
    - The user cannot access the content of the blog without being registered, defensive code was applied to all content pages.
    - After the user becomes registered he is allowed to log in and see the contents of the application.
    - Pagination system that allows users to navigate to older posts.

![feedback info image](/static/images/navbar.png)


- Post Creation
    - The user is allowed after becoming registered to create a post that consists of a unique title, a post image, and the contents of the post.
    - After submitting, the user is redirected to the home page with his post as the first one.

![Footer image](/static/images/navbar.png)

- Post detail
    - From the home page the user can click on a post of his choice.
    - There the user can read the content of the post, like the post unlike the post, and or comment on the post.
    - If the user is the owner of the post he is allowed to choose between deleting and editing the post 
![Footer image](/static/images/navbar.png)

- Post Deletion
    - The user is allowed if authenticated to delete his post
![Footer image](/static/images/navbar.png)
- Log in 
    - The user after registration can fill in a form to login into the blog
![Footer image](/static/images/navbar.png)   
- registration
    - The user fills in a registration form that automatically creates a profile for such a user
![Footer image](/static/images/navbar.png)
- Profile
    - user can check and edit his profile info
![Footer image](/static/images/navbar.png) 
# Future Features :
 - User profile visiting
    
 - Upvoting comments
    
 - Deleting and adding comments

# Testing :

This is a Full stack Framework project using Django

 - The testing in this project was made by manually testing every single functionality 

 - It was hard to fix the Js bugs in all HTML pages. But in the end, it passed all tests.


- registration
    - Before
    -![Footer image](/assets/images/quiz_result.png)
    -After
    ![Footer image](/assets/images/quiz_result.png)

-  log in
    - Before
    -![Footer image](/assets/images/quiz_result.png)
    - After
    -![Footer image](/assets/images/quiz_result.png)

- Post creation
    - before
    -![Footer image](/assets/images/quiz_result.png)
    - after
    -![Footer image](/assets/images/quiz_result.png)

- Post Editing
    -before
    ![Footer image](/assets/images/quiz_result.png)
    - after
    -![Footer image](/assets/images/quiz_result.png)
    
- Post Editing
    -Before
    -![Footer image](/assets/images/quiz_result.png)
    -after
    -![Footer image](/assets/images/quiz_result.png)
    
- Post deleting
    - Before
    -![Footer image](/assets/images/quiz_result.png)
    - after
    -![Footer image](/assets/images/quiz_result.png)

- Profile editing
    -before
    ![Footer image](/assets/images/quiz_result.png)
    -after
    -![Footer image](/assets/images/quiz_result.png)


 # Test Validators :

## Since this is a Full stack framework project The HTML validation comes with a couple of errors, that occur because of the inputs that Django gives us such inputs are not considered HTML syntax 
 
 ## [HTML Validator - Base]([https://validator.w3.org/nu/?doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Findex.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fskategram.herokuapp.com%2Fhome%2F))
 -Besides id duplication, the Home page didn't get any relevant HTML errors
 ## [HTML Validator - landing](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fquiz_box.html#textarea)
 ## [HTML Validator - post](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fhelp.html#textarea)
 ## [HTML Validator - tutorial](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html)
 ## [HTML Validator - profile](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)
 ## [HTML Validator - login](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)
 ## [HTML Validator - logout](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)
 ## [HTML Validator - base](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)
 ## [HTML Validator - create post](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)
 ## [HTML Validator - post detail](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)
 ## [HTML Validator - post update](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)
 ## [HTML Validator - post delete](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)
 ## [HTML Validator - register](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)
 ## [HTML Validator - tutorial detail](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)

All Html pages have been tested and passed with no relevant errors

 ## [Jigsaw CSS Validator]([https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fskategram.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en))
 - For responsiveness, this project was tested at the desktop level, laptops, tablets(iPad), and telephones, all screen sizes have shown responsiveness

The CSS file has been tested and passed with success.

## Bugs
- The application had a lot of path bugs regarding the detail pages that were fixed using the post id as an integer 
- Custom CSS was a major problem in this application because the classes just didn't want to work, it was fixed by the use of ID instead of regular classes which gave an unfortunate duplication of id's for the application

## lighthouse
- The rating of the application was acceptable with a good performance rating

![JavaScript Validator](/assets/images/light_house.png)


# Deployment :
 ## Remote Deployment :
  - In the GitHub repository go to settings.
  ![image of the settings location](assets/images/settings.png)

  - In the settings tab click the page button.
  ![Image of the page's location](assets/images/pages.png)

  - Change the none button to the main.
  ![image of the "main" button location](/assets/images/branch.png)
  
  - Click save and then check your link URL.
  ![image of the project URL link](/assets/images/result.png)

## How to fork :
  - In the repository, you want to fork, go to the upper right corner and click fork.
  ![image of location from fork](/assets/images/how_to_fork.png)
  - After "forking" wait while GitHub copies the repository into your profile.
  
## Desktop Deployment :
  - In the repository click on code.
  ![image of location from fork](/assets/images/desktop_deploy.png)
  - Click on a download zip file.
  ![image of location from fork](/assets/images/desktop_deploy_part_1.png)
  - When that is done, open with your chosen code program. 

  # External Features :
  ### In the links below, you will find all the icons and fonts used in the project. 

- [Google Fonts](https://fonts.google.com/)
  - Was used to select the font combination for this project.
- [Font Awesome](https://fontawesome.com/)
  - Was used to select the icons used in this project. 

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
