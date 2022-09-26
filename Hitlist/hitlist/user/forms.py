
from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Hitter_profile

# class HitterForm(ModelForm):
#     class Meta:
#         model= Hitter_profile
#         fields = '__all__'



# class create_user(UserCreationForm):
#     class Meta:
#         model = User
#         fields=['username', 'email', 'password1', 'password2','email']