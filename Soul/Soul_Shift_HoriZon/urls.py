from django.contrib import admin
from django.urls import path
from django.conf  import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('wallpaper_gallery/',views.wallpaper_gallery, name='wallpaper_gallery'),
    path('navbar/',views.navbar,name='navbar'),
]
