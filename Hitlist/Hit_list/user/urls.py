from django.urls import path, include
from . import views

urlpatterns = [
    path('register/',views.reg,name='Register'),
    path('login/',views.log_in,name='Login')
]

