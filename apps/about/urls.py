# app/about/urls.py

# Django modules
from django.urls import path

# Local
from about import views

app_name = 'about'

urlpatterns = [
    path('about/', views.about, name='about'),
]
