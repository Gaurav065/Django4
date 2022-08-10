from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Soul Shift Horizon Home Page')

def wallpaper_gallery(request):
    return HttpResponse('Wallpaper Gallery')