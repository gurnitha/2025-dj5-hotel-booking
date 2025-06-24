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
