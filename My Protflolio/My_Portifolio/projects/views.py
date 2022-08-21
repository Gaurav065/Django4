from django.shortcuts import render
from .models import Project

# Create your views here.
def project(request):
    X=Project.objects.all()
    
    context={'me':X}
    return render(request,'projects.html', context)#context)