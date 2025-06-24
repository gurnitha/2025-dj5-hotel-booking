# app/home/urls.py

# Django modules
from django.urls import path

# Local
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]
