from django.shortcuts import render
from .models import Project

# Create your views here.
def project(request):
    projects=Project.objects.all()
    
    context={'project':projects}
    return render(request,'projects.html', context)#context)