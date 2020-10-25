# Book Builder Development Log

## Goals

There are several goals that must be met on the Book Builder project.

* Rebuild Virtual Env  (Installed Python 3.8.6)
* Add user administration
* Build comprehensive test suite
* Create view workshop
* Update Data Models (Author, Book, Chapter)
* Rename bookbuilder/ to config/


## Development of User Stories

### Rebuild Virtual Env

Create new env

    python3 -m venv .venv
    
    source $code/.venv/bin/activate
    
    pip install --upgrade pip
    
    pip install django pillow markdown django-crispy-forms requests
    
    pip freeze
    
        asgiref==3.2.10
        certifi==2020.6.20
        chardet==3.0.4
        Django==3.1.2
        django-crispy-forms==1.9.2
        idna==2.10
        Markdown==3.3.2
        Pillow==8.0.1
        pytz==2020.1
        requests==2.24.0
        sqlparse==0.4.1
        urllib3==1.25.11
        
    dj test
    
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        ................
        ----------------------------------------------------------------------
        Ran 16 tests in 1.917s
        
        OK

    dj runserver
    
        Watching for file changes with StatReloader
        Performing system checks...
        
        System check identified no issues (0 silenced).
        October 25, 2020 - 19:57:21
        Django version 3.1.2, using settings 'bookbuilder.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.
    
 
### Add user administration

Tasks to complete

* Use the accounts app developed in BACS 350 - Demo 26
* Hook up to Book Builder
* Require login for Edit, Add, Delete
* Test with Book Editing 


Use the accounts app developed in BACS 350 - Demo 26

    dj startapp accounts
    
    cp /Users/seaman/Github/UNC-BACS-350/demo/week10/Demo29/accounts/* accounts
    
    cp /Users/seaman/Github/UNC-BACS-350/demo/week10/Demo29/templates/registration/* templates/registration


bookbuilder/settings.py

    INSTALLED_APPS = [ ... 'accounts' ]
    STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
    
    LOGIN_REDIRECT_URL = ''
    LOGOUT_REDIRECT_URL = '' 


book/views.py

    from django.contrib.auth.mixins import LoginRequiredMixin

    class BookAdd(LoginRequiredMixin, CreateView):
    
    class BookEdit(LoginRequiredMixin, UpdateView):

dj runserver  -- test the add and edit book

fix base page "book_theme.html"


### Show login info

Create User Info Template

templates/_user.html

    {% block user %}
        {% if user.is_authenticated %}
            <li class="nav-item active">
                <span class="nav-link p-2 m-2">Welcome {{ user.username }}</span>
            </li>
            <li class="nav-item">
                <a href="{% url 'logout' %}" class=" nav-link text-light p-2 m-2">
                    <i class="fas fa-sign-out-alt"></i> Log out
                </a>
            </li>
        {% else %}
            <li class="nav-item">
                <span class="nav-link p-2 m-2">You are not logged in.</span>
            </li>
    
            <li class="nav-item active">
                <a href="{% url 'login' %}" class="nav-link text-light p-2 m-2">
                    <i class="fas fa-sign-in-alt"></i> Log In
                </a>
            </li>
        {% endif %}
    {% endblock user %}


templates/_navbar.html

    {% block navbar %}

        <nav class="navbar navbar-expand-sm navbar-light">
            <div class="container">
                <div class="collapse">
                    <a href="{% url 'home' %}" class="navbar-brand">Book Builder App</a>
                    <ul class="navbar-nav ml-auto">
                        {% include '_user.html' %}
                    </ul>
                </div>
            </div>
        </nav>
        
    {% endblock navbar %}


templates/book_theme.html

    {% block content %}

        {% block header %}
        {% endblock header %}

        {% include '_navbar.html' %}

        <main>
            <div class="container py-5">

                {% block main %}
                    <h2>NO MAIN DEFINED</h2>
                {% endblock main %}

            </div>
        </main>

    {% endblock content %}


### Update Data Models (Author, Book, Chapter)
* Setup Book Description
* Don't edit the Author


### Create view workshop

### Build comprehensive test suite
