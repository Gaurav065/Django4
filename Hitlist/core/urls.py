from django.urls import path,include
from .views import Hitlist

urlpatterns = [
    path('', Hitlist.as_view(), name='Hitlist'),
]