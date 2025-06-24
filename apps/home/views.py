# app/home/views.py

# Django modules
from django.shortcuts import render

# Local
from django.http import HttpResponse

# Create your views here.

def home(request):
    # request is handled using HttpResponse object
    return HttpResponse("Hello, World")