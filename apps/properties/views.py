# app/properties/views.py

# Django modules
from django.shortcuts import render

# Local
from django.http import HttpResponse

# Create your views here.

def properties(request):
    return render(request, 'properties/properties.html')