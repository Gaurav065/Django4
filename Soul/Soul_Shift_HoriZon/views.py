from django.shortcuts import render
from .models import Wallpaper


# Create your views here.
def home(request):

    wallpapers=Wallpaper.objects.all()
    return render(request,'home.html')

def wallpaper_gallery(request):
    wallpapers=Wallpaper.objects.all()
    return render(request,'wallpaper.html')

def navbar(request):
    return render(request,'navbar.html')