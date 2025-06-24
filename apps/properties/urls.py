# app/properties/urls.py

# Django modules
from django.urls import path

# Local
from properties import views

app_name = 'properties'

urlpatterns = [
    path('properties/', views.properties, name='properties'),
]
