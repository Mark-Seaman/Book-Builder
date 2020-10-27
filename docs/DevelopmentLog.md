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
* Known Problems
* Update Data Models (Author, Book, Chapter)
* Rename bookbuilder/ to config/


### Setup Dev Context
* Define a script that sets up the dev environment and tools
* [start development script](../start)


### Rename app settings folder
* mv bookbuilder config
* Edit files (manage, asgi, wsgi, settings)
* dj test
* dj runserver


### Deploy & test code

Test locally (auto, manual)

* dj test
* Basic user tests

Commit and push

    co "Rename app settings folder to config"
    

Pull and bounce server

    Login to Python Anywhere console
        
        cd /home/markseaman/Book-Builder
        
        git pull
        
    Migrate the database
    
        python manage.py makemigrations
        
        python manage.py migrate
        
    Browse to WebApp config
    
    Edit the WSGI.py
        
        # +++++++++++ DJANGO +++++++++++
        # To use your own django app use code like this:
        import os
        import sys

        ## assuming your django settings file is at '/home/markseaman/Book-Builder/bookbuilder/config/settings.py'
        ## and your manage.py is is at '/home/markseaman/Book-Builder/bookbuilder/manage.py'
        path = '/home/markseaman/Book-Builder/bookbuilder'
        if path not in sys.path:
            sys.path.append(path)

        os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()


    Reload server
    
    Browse to http://markseaman.pythonanywhere.com


Test remotely

    dj test
    
    Basic user tests
    
    
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

