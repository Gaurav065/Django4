from django.shortcuts import render
from django.urls import path, include
from .models import education,experiance, certificates

def resume(request,pk):
    
    X=education.objects.all(pk=pk)
    
    y=experiance.objects.all(pk=pk)
    
    z=certificates.objects.all(pk=pk)
    
    
