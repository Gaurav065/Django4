from multiprocessing import context
from django.shortcuts import render
from django.urls import path, include
from .models import education,experience, certificates

def resume(request):
    
    education_details=education.objects.get(id=1)
    
    return render(request, 'resume.html',{'education_details':education_details})
def experience_det(request):
    experience_detail=experience.objects.all()
    
    context={
        'experience_details':experience_detail,
    }

    return render(request,'experience.html',context)
