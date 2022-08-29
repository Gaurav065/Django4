from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.user_log, name='Login'),
    path('home/', views.home, name='Home'),
]
