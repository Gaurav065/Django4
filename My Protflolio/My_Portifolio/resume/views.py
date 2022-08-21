from django.shortcuts import render
from django.urls import path, include
# from .models import education,experiance, certificates

def resume(request):
    # X=education.objects.get(id=1)
    # y=experiance.objects.all()
    # z=certificates.objects.all()
    # context={'ed':X,'ex':y,'ct':z}
    return render(request, 'resume.html')
