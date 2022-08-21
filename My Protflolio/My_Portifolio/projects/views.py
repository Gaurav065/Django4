from django.shortcuts import render


# Create your views here.
def project(request):
    # X=project.objects.get(id=1)
    # context={'me':X}
    return render(request,'projects.html')#context)