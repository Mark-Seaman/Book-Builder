# Book Builder Development Log

There are several goals that must be met on the Book Builder project.

Here is a log of recent activity and notes for later.

---


## Goals  10-25

* Rebuild Virtual Env  (Installed Python 3.8.6)
* Add user administration
* Update Data Models (Author, Book, Chapter)
* Testing


### Rebuild Virtual Env
* [Rebuild Virtual Env](RebuildVenv.md)
    
 
### Add user administration
* [Users accounts](UserAccounts.md)
* Register
* Login/logout
* Require login
* Show login info


### Update Data Models
* Testing
    * dj test
    * Basic user tests
* Known Problems
    * Author
        * Authors are currently hard code to Author 1
        * Need to create views to add and edit new authors
        * Tie author to logged in user
    *  Book
        * Works correctly
    *  Chapter
        * Tie add chapter to a specific book

---


## Goals  10-27

* Rename app settings folder
* Deploy & test code
* Known Problems
* Update Data Models (Author, Book, Chapter)
* Rename bookbuilder/ to config/


### Rename app settings folder
* mv bookbuilder config
* Edit files (manage, asgi, wsgi, settings)
* dj test
* dj runserver


### Deploy & test code
* Test locally (auto, manual)
    * dj test
    * Basic user tests
* Commit and push
* Pull and bounce server
* Test remotely
    * dj test
    * Basic user tests
    
    
### Known Problems

* Author
    * Authors are currently hard code to Author 1
    * Need to create views to add and edit new authors
    * Tie author to logged in user
*  Book
    * Works correctly
*  Chapter
    * Tie add chapter to a specific book
* Theme
    * Favicon - Setup book icon
    * Banner - Use Shrinking World banner




### Fix Chapter edit
*
* 


### Fix Book edit
* 
* 


### Add Book Description
* 



### Rename bookbuilder/ to config/

