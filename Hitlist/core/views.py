from django.shortcuts import render
from django.views.generic.list import ListView
from .models import hitter

class Hitlist(ListView):
    model = hitter 
    