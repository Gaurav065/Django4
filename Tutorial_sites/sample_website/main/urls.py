from nturl2path import url2pathname
from django.contrib import admin
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.home,name='home')
        
    ]
