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