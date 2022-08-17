from pyexpat import version_info
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('start/', views.home, name='start'),
]
