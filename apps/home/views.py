# app/home/views.py

# Django modules
from django.shortcuts import render

# Local
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base.html')
    # return render(request, 'home/index.html')