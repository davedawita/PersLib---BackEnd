# PersLib---BackEnd

**<h3>Description</h3>**

PersLib is an application that can be utilized by users who need to record their pictures, videos, documents, etc. through the years. In addition, users can transfer dissiminated files and documents in their phones, laptops, hard discs, etc. to this PerLib (Personal Library) website. They can also create their account and access their footprints easily without getting frustrated with security. PerLib app alleviates the risk of loosing important pictures and documents through unexpected events such as losing a phone, malfunctioning of hard discs, etc.

The PersLib app has two repositories:</br>
 - PersLib_Back-End: is for back-end of the app with with Python & Django.
 - PersLib_Front-End: is for front-end of the app with React & Node.js
 

Users will need to create account and login if they need to access the app.




<h2>PersLib---Back-End</h2>

**<h3>Back-end Repository</h3>**
The backend repo can be accessed through the link below:</br>
Important Note:</br>
Models are the database tables represented in Django as Python classes.</br>
Views are the HTML returned from function in views.py.</br>
Controllers are the actual functions themselves in views.py invoked from a HTTP request.</br>


**<h3>MODELS:</h3>** 
The following models are included: </br></br>
<b>perslib/users/manager.py:</b></br>

class User(Manager):</br>
   
    def create_user(self, username, password, **extra_fields):</br>
        
        if not username:</br>
            raise ValueError(_("The username must be set"))</br>
        email = self.normalize_username(username)</br>
        user = self.model(username=username, **extra_fields)</br>
        user.set_password(password)</br>
        user.save()</br>
        return user</br></br>


<b>perslib/models.py:</b></br>
class Perslib(models.Model):</br></br>
    date = models.TimeField(auto_now=False, auto_now_add=False)</br>
    description = models.CharField(max_length=20)</br></br>
    
 **<h3>ROUTES:</h3>**     
User Routes:

POST /users/register/: Register a new user</br>
POST /users/login/: Login a user</br>
GET /users/profile/: Get user profile details</br>

Index Page Route:

GET /: This lists the dates which will direct us to titles page</br>

Titles Page Routes:

POST /title/: This adds a new title</br>
GET /title/: This lists all titles</br>
PUT /title/:id/: This updates a title</br>
DELETE /title/:id/: This deletes a title</br>

Documents/Perslib Routes:

POST /perslib/: This adds a new document (picture, video, etc.)</br>
GET /perslib/: This list all documents</br>
PUT /perslib/:id/: This updates a document</br>
DELETE /perslib/:id/: This deletes a document</br>

 <h2> PersLib---Front-End </h2></br>

 **<h3>Front-end Repository</h3>**
The frontend repository can be accessed through the link below:</br>


 **<h3>Wireframes</h3>**
 
- Please see the wireframe for the Create Account page below: </br></br>
 ![image](https://github.com/davedawita/PersLib---FrontEnd/assets/155693018/20c5d680-d7da-42eb-a8a0-c9f753f609a2)
 
 - Please see the wireframe for the Login page below: </br></br> 

![image](https://github.com/davedawita/PersLib---FrontEnd/assets/155693018/988a5461-2348-420d-b65e-076d2cd9715c)

 - Please see the wireframe for the index page below: </br></br>

![image](https://github.com/davedawita/PersLib---FrontEnd/assets/155693018/15628a15-6a31-4777-a653-2e059d1dd777)

 - Please see the wireframes for the show pages page below: </br></br>
 
![image](https://github.com/davedawita/PersLib---FrontEnd/assets/155693018/bf92e803-4ae6-4a36-b833-da64aff834c6)

![image](https://github.com/davedawita/PersLib---FrontEnd/assets/155693018/47f2d682-d009-4a00-bc21-68771b7e7dd3)

**<h3>User Stories</h3>** 
User Stories
 - As a user, I want to be able to create an account with a first name, last name, new username and new password, so that I can have access to my Personal Library (PersLib). In addition, I need to be able to add profile photograph.
 - As a user, I want to be able to log in with my username and password, so that I can use the app’s features and functionalities and ensure that anything I do within the app is saved to my account.
 - As a user, I want to logout of my account so that noone can access my personal library.
 - As a user, I want to have a personal library that enables me to search for my life events and documents and access them by selecting a specific year from list of years.
 - As a user, I want to have Icons such as pictures, videos, favorite books, documents, etc. so that I can access my life events and documents easily.
 - As a user, I also need to add icons and define them I like. I also need to delete them whenever I need.
 - As a user, I want to be able to edit the details of any added life event or document description, so that I can update the information.
 - As a user, I want to be able to delete a feature (picture, video, or favourite book), so that if it is no longer necessary it will no longer appear in the list. </br> </br>
 
The folder structure includes components: Header, main & pages: Create, Edit, Index, & Show.</br>
The app resides in App.js. User log-in/createaccount code is also in App.js.</br>

<h2>Installation Instructions</h2>
 - Please use the link below to install the app. Enjoy the app!   </br>
 
 
If you are on a browser, use of Google chrome is highly recommended.    </br>
<h2>Technologies used</h2>

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
[![Visily](https://img.shields.io/badge/Visily-02066F?style=for-the-badge&logoColor=white)](https://www.visily.ai)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![MDN Web Docs](https://img.shields.io/badge/MDN_Web_Docs-black?style=for-the-badge&logo=mdnwebdocs&logoColor=white)
![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)
![NPM](https://img.shields.io/badge/NPM-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white)
![Nodemon](https://img.shields.io/badge/NODEMON-%23323330.svg?style=for-the-badge&logo=nodemon&logoColor=%BBDEAD)
![Mongoose](https://img.shields.io/badge/Mongoose-F04D35?logo=mongoosedotws&logoColor=fff&style=for-the-badge)
![.ENV Badge](https://img.shields.io/badge/.ENV-ECD53F?logo=dotenv&logoColor=000&style=for-the-badge)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Adobe Fonts](https://img.shields.io/badge/Adobe%20Fonts-000B1D.svg?style=for-the-badge&logo=Adobe%20Fonts&logoColor=white)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![SASS](https://img.shields.io/badge/SASS-hotpink.svg?style=for-the-badge&logo=SASS&logoColor=white)
![Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![React Router](https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=react-router&logoColor=white)
![Jira](https://img.shields.io/badge/jira-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=
Python (Backend programming Language), Django (Backend Framework), REACT (FrontEnd Framework), Javascript, Node.js (Server Side JavaScript runtime), HTML, tailwind CSS, Postgres (Database), Postman, and Figma(Only for wireframes without Dev Mode). We can also say that we use Python-Django stack.  </br>

<h2>MVP Goals</h2>
Full CRUD(Create, Read, Update, Delete) Functionality. </br>
Login and Logout access for users   </br>

<h2>Troubleshooting</h2>
Please click the back button of the browser to go back to previous page. Refresh the page.   </br>

<h2>Forthcoming Features</h2>
In the future, we need users to be able to give access to family members so that the documents can be viewed by others. In addition, I need to learn Angular (FrontEnd Framework) and do this same app with it.
