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

* Setup Dev Context
* Rename app settings folder
* Deploy & test code
* Use View Inheritance
* Known Problems


### Setup Dev Context
* Define a script that sets up the dev environment and tools
* [start development script](../start)


### Rename app settings folder
* mv bookbuilder config
* Edit files (manage, asgi, wsgi, settings)
* dj test
* dj runserver


### Deploy & test code

* Test locally (auto, manual)
* Commit and push
* Pull and bounce server 
* Test remotely
* [Update Server](UpdateServer.md)

    
### Use View Inheritance

Create a series of templates
    
    book_theme.html
    _header.html
    _footer.html
    _navbar.html
    _user.html
    
[View Templates](ViewInheritance.md)


### Improve Appearance
* Use logic from Shrinking World website
    * Header with globe banner art
    * CSS stylesheet (static/shrinking-world.css)
    * Body background (static/paper.png)
    * Set text color to dark
    

---

## Remaining Tasks

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


### Fix Chapter edit
* TBD


### Fix Book edit
* TBD


### Add Book Description
* TBD


### Fix favicon
* TBD
