from re import X
from django.shortcuts import render
from django.urls import path, include
from .models import Profile


def home(request):
    X=Profile.objects.get(id=1)
    context={'me':X}
    return render(request, 'home.html',context)

def contact_me(request):
    X=Profile.objects.get(id=1)
    context={'me':X}
    return render(request,'contact.html',context)
