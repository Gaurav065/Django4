from multiprocessing import context
from django.shortcuts import render
from django.urls import path, include
from .models import education,experiance, certificates

def resume(request):
    
    education_details=education.objects.get(id=1)
    
    return render(request, 'resume.html',{'education_details':education_details})
def experiance_det(request):
    experiance_detail=experiance.objects.all()
    
    context={
        'experiance_details':experiance_detail
    }

    return render(request,'experiance.html',context)
