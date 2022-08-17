from django.shortcuts import render
from .models import Party

def home(request):
    party=Party.objects.all()
    return render(request,'start.html')
# Create your views here.
