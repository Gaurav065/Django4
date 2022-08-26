from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('resume/',views.resume, name="Resume"),
    path('<int:pk>/',views.experience, name='experience'),
    path('experience/', views.experience_det, name='exp')
]
