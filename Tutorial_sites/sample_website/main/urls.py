from nturl2path import url2pathname
from django.contrib import admin
from . import views
from django.urls import path, include


urlpatterns = [
    path('home/', views.home,name='home')
        
    ]
