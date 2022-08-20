from django.shortcuts import render
from django.urls import path, include

def resume(request):
    return render(request, 'resume.html')
