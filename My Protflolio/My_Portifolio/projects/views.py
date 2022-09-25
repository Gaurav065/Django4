from django.shortcuts import render
from .models import Project

# Create your views here.
def project(request):
    projects=Project.objects.all()
    print(len(projects))
    context={'project':projects}
    return render(request,'projects.html', context)