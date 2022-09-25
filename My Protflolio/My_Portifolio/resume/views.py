from multiprocessing import context
from django.shortcuts import render
from django.urls import path, include
from .models import education, experience, certificates, skill
import mimetypes
from django.shortcuts import HttpResponse

def resume(request):

    education_details = education.objects.get(id=1)

    experience_detail = experience.objects.all()

    skill_details = skill.objects.all()

    ctf = certificates.objects.all()

    context = {
        'experience_detail': experience_detail,
        'education_details': education_details,
        'sk_d': skill_details,
        'ct': ctf,
    }

    return render(request, 'resume.html', context)


# def download_file(request):
#     fl_path = 'C:\Users\dell\Desktop\learn_django\My Protflolio\My_Portifolio\media\img\Screenshot 2022-08-21 054646.png'
#     filename = 'resume.pdf'

#     fl = open(fl_path, 'r')
#     mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     return response