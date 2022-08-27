from multiprocessing import context
from django.shortcuts import render
from django.urls import path, include
from .models import education,experience, certificates, skill

def resume(request):
    
    education_details=education.objects.get(id=1)

    experience_detail=experience.objects.all()

    skill_details=skill.objects.all()

    ctf=certificates.objects.all()

    
    context={
        'experience_detail':experience_detail,
        'education_details':education_details,
        'sk_d':skill_details,
        'ct':ctf,
    }
    
    return render(request, 'resume.html',context)
