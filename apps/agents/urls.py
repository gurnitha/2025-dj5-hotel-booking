# app/agents/urls.py

# Django modules
from django.urls import path

# Local
from agents import views

app_name = 'agents'

urlpatterns = [
    path('agents/', views.agents, name='agents'),
]
