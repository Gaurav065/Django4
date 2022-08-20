from django.contrib import admin
from django.urls import path, include

from E_commerce_website.settings import MEDIA_ROOT, MEDIA_URL
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns+= static(MEDIA_URL, document_settings=MEDIA_ROOT)