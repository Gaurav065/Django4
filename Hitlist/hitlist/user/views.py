from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


# from .models import *
# from .forms import HitterForm


def register(request):
    
    
    context = {}
    return render(request, 'register.html',context)

def login(request):
    

    context  ={}
    return render(request, 'login.html', context)
    
