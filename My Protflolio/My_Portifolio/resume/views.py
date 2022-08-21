from django.shortcuts import render
from django.urls import path, include
from .models import education,experiance, certificates

def resume(request):
    X=education.objects.get(id=1)
    y=experiance.objects.get(id=1)
    z=certificates.objects.get(id=1)
    context={'ed':X,'ex':y,'ct':z}
    return render(request, 'resume.html',context)
