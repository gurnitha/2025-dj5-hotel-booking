# app/about/views.py

# Django modules
from django.shortcuts import render

# Local
from django.http import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'about/about.html')