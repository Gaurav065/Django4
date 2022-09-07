from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('resume/',views.resume, name="Resume"),
    

]
