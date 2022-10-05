# SkateGram

## By Patrick Alexander Lucas Van Der Flier

### [Check SkateGram](https://vanderpatrick.github.io/The-Amazing-Quizaru/)

![Responsive image from the project](/assets/images/responsive.png)

# SkateGram :

### SkateGram was developed as my fourth project for CodeInstitute

# Reason :
As a skateboarder i always been part of the skate comunity. Beeing part of a skate community means support and sharing, we always help eachother teaching tricks giving tips etc... One of the main things that i saw was the dependenci of social media platforms for this (Support/Sharing) experience, but it gets overwelming with the amount of different subjects in such platforms hence the birth of skategram. an skate social media blog where people can share their thoughts about the skate universe as well as following tutorials regarding skateboarding.

# The user Experience (UX)

##  Audience : 

- People who want to engage more into skateboarding.
- Skaters that want to discuss about major skate topics.
- skaters who wish to share their thoughts about skating in different topics.

## User Report : 

- first experience

    1. As a user I would like easy navigation across the web application.
    2. As a user I would like access to an skate social media.
    3. As a user I would like to share my thoughts with other users in an dinamic way.

- Second experience

    1. I would want to check my post for likes and comments.
    2. I would want to edit posts and profile.
    3. I would want to check for new subjects to discuss about.

- As a developer    
    
    1. I want to make it interactive.
    2. I want the site to be easy to fulfill basic forms such registration, post, login. 
    3. I want to give a focused blog about skateboarding so skaters fell more confortable with their own kind.


# Features :

The Features were designed to distinguish each area with ease so the user can explore the site instinctively.

- Navigation bar
    - The navigation bar is featured on all HTML pages using the extend method from django.
    - It consists of intuitive links that tells you precisesly what you can do in the application. 
    - as it shrinks the navigations becomes the brand title and an burger menu.

 ![navigation bar image](/assets/images/nav_bar.png)

- Landing page
    - The homepage consists of an welcome message with options of register/login for new and old users.
    - it is easy to look at and intuitive to chose what to do.

![landing page image](/assets/images/home_screen.png)

- Footer
    - The footer is responsible for giving information about the developing of the application and contact info about the develeopemnt team.
    

![info content image](/assets/images/footer.png)

- Home section
    - Simple homepage for registrated users to access the blog content witch consists of a list of the most recent blog posts
    - The user cannot access teh content of the blog whitout beeing registrated, defensive code was applied in all content pages.
    - After the user becomes registrated he is allowd to log in and see the contents of the application.
    - Pagination system that allows users to navigate to older posts.

![feedback info image](/assets/images/quiz_options.png)
![Quiz when wrong question is clicked](/assets/images/quiz_options.png)

- Post Creation
    - The user is allowd after becoming registered to create a post that consist of an unique title, a post image and the contents of the post.
    - After submiting the users is redirected to the home page with his post as the first one.

![Footer image](/assets/images/quiz_result.png)

- Post detail
    - From the home page the user is able to click on a post of his choice.
    - There the user can read the content of the post, like the post unlike the post and or comment the post.
    - If the user is the owner of the post he is allowed to choose between deleting and editign the post 

- Post Deletion
    - The user is allowed if authenticated to delete his own post
    
- Log in 
    - The user after registration is ablle to Fill in a form to login in the blog
   
- registration
    - The user fills in a registration form that authomaticly creates a profile for such user

- Profile
    - user can check and edit his profile info

# Testing :

This is an HTML CSS and JS website, my main concern in the project was the logic applied to the quiz.

 - The project was built with a desktop approach Because it was easier for me to create the content on the page.

 - It was hard to fix the Js bugs in all HTML pages. But in the end it passed all tests.

 # Test Validators :

## Here you have access to all HTML validators from all 5 pages:
 
 ## [HTML Validator - Index](https://validator.w3.org/nu/?doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Findex.html)
 ## [HTML Validator - Quiz_box](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fquiz_box.html#textarea)
 ## [HTML Validator - Help](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fhelp.html#textarea)
 ## [HTML Validator - Credits](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html)
 ## [HTML Validator - Result](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2Fcredits.html#textarea)

All Html pages have been tested and passed with success with irrelevant warnings.

 ## [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvanderpatrick.github.io%2FThe-Amazing-Quizaru%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
 - For responsiveness, this project was tested in the desktop level, laptops, tablets(iPad), telephones, all screen sizes have shown responsiveness

The CSS file has been tested and passed with success.

## JavaScript Validator :
- The code was tested numerous times and didn't show any major bugs in the final code.
- The undefinable variables are objects from an array.
- Since the game is in an different HTML the function "runGame" cannot be called.
![JavaScript Validator](/assets/images/js_validator.png)

## Bugs
- The main bug that I had at the super frustrating beginning was calling the function, somehow even when the function was done it wasn't called, by simply calling the function at the end of the script fixed my problem.
- Since the game is in a different HTML the function "runGame" cannot be called in any other HTML file besides the game.

## LigthHouse
- Unfortunately, I saw it too late that existed the light house function at dev tools, which would have helped me choose a better combination of colors.

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
  - In the repository that you want to fork, go to the right upper corner and click fork.
  ![image of location from fork](/assets/images/how_to_fork.png)
  - After "forking" wait while GitHub copies the repository into your profile.
  
## Desktop Deployment :
  - In the repository click on code.
  ![image of location from fork](/assets/images/desktop_deploy.png)
  - Click at download zip file.
  ![image of location from fork](/assets/images/desktop_deploy_part_1.png)
  - When that is done, open with your chosen code program. 

  # External Features :
  ### In the links below, you will find all the icons and fonts used in the project. 

- [Google Fonts](https://fonts.google.com/)
  - Was used to select the font combination for this project.
- [Font Awesome](https://fontawesome.com/)
  - Was used to select the icons used in this project. 

  # Credits :
 1. [Web Dev Simplified](https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw)
  - For helping me again with my nav bar.

 2. [CodingNepal](https://www.youtube.com/c/CodingNepal/featured)
  - CodingNepal was my stepping stone to make this quiz project.
  
 3.  [Code Institute](https://codeinstitute.net/)
  - Code Institute for all the suporte and care with me and my projects.

  ## Special thanks 
  I would like to thank everyone who helped me with this project.

- My mentor.
- Jean my good French friend for all the support and advice.
- Code Institute for giving the best support to develop this project.
