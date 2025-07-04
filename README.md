# Building A Bookin Hotel App Using Django 5


## 1. Creating virtual environment

#### 1.1. Checking python and pip version

        E:\2025-workspace\django\Udemy\Mahmoud Ahmed\hotel-booking\haus\the-project(master)
        λ python --version
        Python 3.12.1

        λ pip --version
        pip 25.0.1

#### 1.2. Creating virtual environment venv3151

        λ python -m venv venv3151
        λ ls
        venv3151/

#### 1.3. Installing Django version 5.1

        λ venv3151\Scripts\activate.bat
        (venv3151) λ pip install django==5.1
        Collecting django==5.1
          ...
        Using cached Django-5.1-py3-none-any.whl (8.2 MB)
        Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
        Using cached sqlparse-0.5.3-py3-none-any.whl (44 kB)
        Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
        Installing collected packages: tzdata, sqlparse, asgiref, django
        Successfully installed asgiref-3.8.1 django-5.1 sqlparse-0.5.3 tzdata-2025.2

        [notice] A new release of pip is available: 23.2.1 -> 25.1.1
        [notice] To update, run: python.exe -m pip install --upgrade pip

        (venv3151) λ django-admin --version
        5.1

#### 1.4. Upgrade pip

        (venv3151) λ python.exe -m pip install --upgrade pip
        ...
        Successfully installed pip-25.1.1


## 2. Creating remote repository

#### 2.1. Creating remote repository on Github

        Creating an account
        Login
        Creating a new repository
        https://github.com/gurnitha/2025-dj5-hotel-booking

#### 2.2. Pushing remote repository on Github

        git remote add origin git@github.com:gurnitha/2025-dj5-hotel-booking.git
        git branch -M main
        git push -u origin main


## 3. Creating Project

#### 3.1. Creating Django project

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

        (venv3151) λ tree /f
        Folder PATH listing for volume Local Disk
        Volume serial number is 42EB-BBDC
        E:.
        │   .gitignore
        │   manage.py
        │   README.md
        │
        └───config
                asgi.py
                settings.py
                urls.py
                wsgi.py
                __init__.py

#### 3.2. Python manage.py sub commands

        (venv3151) λ python manage.py

        Type 'manage.py help <subcommand>' for help on a specific subcommand.

        Available subcommands:

        [auth]
            changepassword
            createsuperuser

        [contenttypes]
            remove_stale_contenttypes

        [django]
            check
            compilemessages
            createcachetable
            dbshell
            diffsettings
            dumpdata
            flush
            inspectdb
            loaddata
            makemessages
            makemigrations
            migrate
            optimizemigration
            sendtestemail
            shell
            showmigrations
            sqlflush
            sqlmigrate
            sqlsequencereset
            squashmigrations
            startapp # <---
            startproject # <---
            test
            testserver

        [sessions]
            clearsessions

        [staticfiles]
            collectstatic
            findstatic
            runserver # <---

#### 3.2. Running Django's development server

        (venv3151) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        June 25, 2025 - 05:02:31
        Django version 5.1.5, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.


## 4. Creating Apps

#### 4.1. Creating 'home' app

        modified:   README.md
        new file:   home/__init__.py
        new file:   home/admin.py
        new file:   home/apps.py
        new file:   home/migrations/__init__.py
        new file:   home/models.py
        new file:   home/tests.py
        new file:   home/views.py

        (venv3151) λ tree /f
        Folder PATH listing for volume Local Disk
        Volume serial number is 42EB-BBDC
        E:.
        │   .gitignore
        │   db.sqlite3
        │   manage.py
        │   README.md
        │
        ├───config
        │   │   asgi.py
        │   │   settings.py
        │   │   urls.py
        │   │   wsgi.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           settings.cpython-312.pyc
        │           urls.cpython-312.pyc
        │           wsgi.cpython-312.pyc
        │           __init__.cpython-312.pyc
        │
        └───home
            │   admin.py
            │   apps.py
            │   models.py
            │   tests.py
            │   views.py
            │   __init__.py
            │
            └───migrations
                    __init__.py

#### 4.2. Creating 'properties' app

        modified:   README.md
        new file:   properties/__init__.py
        new file:   properties/admin.py
        new file:   properties/apps.py
        new file:   properties/migrations/__init__.py
        new file:   properties/models.py
        new file:   properties/tests.py
        new file:   properties/views.py

#### 4.3. Creating 'agents' app

        modified:   README.md
        new file:   agents/__init__.py
        new file:   agents/admin.py
        new file:   agents/apps.py
        new file:   agents/migrations/__init__.py
        new file:   agents/models.py
        new file:   agents/tests.py
        new file:   agents/views.py

#### 4.4. Creating 'about' app

        modified:   README.md
        new file:   about/__init__.py
        new file:   about/admin.py
        new file:   about/apps.py
        new file:   about/migrations/__init__.py
        new file:   about/models.py
        new file:   about/tests.py
        new file:   about/views.py

#### 4.5. Creating 'contact' app

        modified:   README.md
        new file:   contact/__init__.py
        new file:   contact/admin.py
        new file:   contact/apps.py
        new file:   contact/migrations/__init__.py
        new file:   contact/models.py
        new file:   contact/tests.py
        new file:   contact/views.py

#### 4.6. Creating 'users' app

        modified:   README.md
        new file:   users/__init__.py
        new file:   users/admin.py
        new file:   users/apps.py
        new file:   users/migrations/__init__.py
        new file:   users/models.py
        new file:   users/tests.py
        new file:   users/views.py

#### 4.7. Registering the apps to the project

        (venv3151) λ python manage.py check
        modified:   README.md
        modified:   config/settings.py

#### 4.8. The project's strunctures

        (venv3151) λ tree /f
        Folder PATH listing for volume Local Disk
        Volume serial number is 42EB-BBDC
        E:.
        │   .gitignore
        │   db.sqlite3
        │   manage.py
        │   README.md
        │
        ├───about
        │   │   admin.py
        │   │   apps.py
        │   │   models.py
        │   │   tests.py
        │   │   views.py
        │   │   __init__.py
        │   │
        │   ├───migrations
        │   │   │   __init__.py
        │
        ├───agents
        │   │   admin.py
        │   │   apps.py
        │   │   models.py
        │   │   tests.py
        │   │   views.py
        │   │   __init__.py
        │   │
        │   ├───migrations
        │   │   │   __init__.py
        │
        ├───config
        │   │   asgi.py
        │   │   settings.py
        │   │   urls.py
        │   │   wsgi.py
        │   │   __init__.py
        │
        ├───contact
        │   │   admin.py
        │   │   apps.py
        │   │   models.py
        │   │   tests.py
        │   │   views.py
        │   │   __init__.py
        │   │
        │   ├───migrations
        │
        ├───home
        │   │   admin.py
        │   │   apps.py
        │   │   models.py
        │   │   tests.py
        │   │   views.py
        │   │   __init__.py
        │   │
        │   ├───migrations
        │
        ├───properties
        │   │   admin.py
        │   │   apps.py
        │   │   models.py
        │   │   tests.py
        │   │   views.py
        │   │   __init__.py
        │   │
        │   ├───migrations
        │   │   │   __init__.py
        │
        └───users
            │   admin.py
            │   apps.py
            │   models.py
            │   tests.py
            │   views.py
            │   __init__.py
            │
            ├───migrations
            │   │   __init__.py

#### 4.9.Restruncturing the project

        tree -L 2
        .
        ├── README.md
        ├── apps
        │   ├── about
        │   ├── agents
        │   ├── contact
        │   ├── home
        │   ├── properties
        │   └── users
        ├── config
        │   ├── __init__.py
        │   ├── __pycache__
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3
        └── manage.py


## 5. Hello, World

#### 5.1. Displaying 'Hello, World'

        modified:   README.md
        new file:   apps/home/urls.py
        modified:   apps/home/views.py
        modified:   config/urls.py


## 6. Django's Views, Urls, and Template

#### 6.1. 'Hello, World from template'

        modified:   README.md
        modified:   apps/home/views.py
        modified:   config/settings.py
        new file:   templates/home/index.html

#### 6.2. Adding html code to the template

        modified:   README.md
        modified:   templates/home/index.html

#### 6.3. Adding static assets

        modified:   .gitignore
        modified:   README.md

        Note: for copyright reasons, assets by designed, are ignored in git commit

#### 6.4. Loading static assets to home page

        modified:   README.md
        modified:   config/settings.py
        modified:   templates/home/index.html

#### 6.5. Creating base template

        modified:   README.md
        modified:   apps/home/views.py
        new file:   templates/base.html

#### 6.6. Extending base template to the home page

        modified:   README.md
        modified:   apps/home/views.py
        modified:   templates/base.html
        modified:   templates/home/index.html

#### 6.7. Adding properties page

        new file:   apps/properties/urls.py
        modified:   apps/properties/views.py
        modified:   config/urls.py
        new file:   templates/properties/properties.html

#### 6.8. Adding agents page

        modified:   README.md
        new file:   apps/agents/urls.py
        modified:   apps/agents/views.py
        modified:   config/urls.py
        new file:   templates/agents/agents.html

#### 6.9. Adding about page

        modified:   README.md
        new file:   apps/about/urls.py
        modified:   apps/about/views.py
        modified:   config/urls.py
        new file:   templates/about/about.html

#### 6.10. Adding contact page

        modified:   README.md
        new file:   apps/contact/urls.py
        modified:   apps/contact/views.py
        modified:   config/urls.py
        new file:   templates/contact/contact.html


## 7. Templates inheritance

#### 7.1. Creating partials template

        modified:   README.md
        new file:   templates/_partials/explore-our-neighborhoods.html
        new file:   templates/_partials/featured-listing.html
        new file:   templates/_partials/our-agents.html
        new file:   templates/_partials/why-choose-us.html
        modified:   templates/about/about.html
        modified:   templates/agents/agents.html
        modified:   templates/contact/contact.html
        modified:   templates/home/index.html
        modified:   templates/properties/properties.html


## 8. Page title

#### 8.1. Adding page title using block super

        modified:   README.md
        modified:   templates/about/about.html
        modified:   templates/agents/agents.html
        modified:   templates/base.html
        modified:   templates/contact/contact.html
        modified:   templates/home/index.html
        modified:   templates/properties/properties.html


## 9. Navigations

#### 9.1. Linking the pages

        modified:   README.md
        modified:   templates/base.html

#### 9.2. Adding active state to the navigation

        modified:   README.md
        modified:   templates/base.html