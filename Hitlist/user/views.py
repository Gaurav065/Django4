from django.shortcuts import render

def user_log(request):
    return render(request, 'user_login.html')

def home(request):
    return render(request,'home.html')
# Create your views here.
