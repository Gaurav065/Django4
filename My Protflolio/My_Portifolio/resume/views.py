from django.shortcuts import render
from django.urls import path, include
from .models import education,experiance, certificates

def resume(request):
    
    education_details=education.objects.all()
    
    experiance_details=experiance.objects.all()
    
    certi_details=certificates.objects.all()
    
    return render(request, 'resume.html',{'education_details':education_details},{'experiance_details':experiance_details},{'cerificate_detials':certi_details} )
