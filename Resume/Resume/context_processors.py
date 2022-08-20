from django.contrib.auth.models import User
from django.shortcuts import render


def project_context(request):
    
    context={ 
        
        'me':User.objects.first(),
    }

    return context