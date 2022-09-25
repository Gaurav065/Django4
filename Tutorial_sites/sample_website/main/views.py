from django.shortcuts import render
from django.urls import path, include

def home(request):
    return render(request,'home.html')
# Create your views here.
