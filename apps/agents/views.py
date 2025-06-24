# app/agents/views.py

# Django modules
from django.shortcuts import render

# Local
from django.http import HttpResponse

# Create your views here.

def agents(request):
    return render(request, 'agents/agents.html')
