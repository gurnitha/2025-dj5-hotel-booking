# app/contact/views.py

# Django modules
from django.shortcuts import render

# Local
from django.http import HttpResponse

# Create your views here.

def contact(request):
    return render(request, 'contact/contact.html')