# app/contact/urls.py

# Django modules
from django.urls import path

# Local
from contact import views

app_name = 'contact'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
