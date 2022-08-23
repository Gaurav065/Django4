from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('resume/',views.resume, name="Resume"),
    path('<int:pk>/',views.experiance, name='experiance'),
    path('experiance/', views.experiance_det, name='exp')
]
