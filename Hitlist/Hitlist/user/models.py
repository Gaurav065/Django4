from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hitter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=13)
    about = models.TextField(default="I am a Hitter")
    avatar = models.ImageField(upload_to='user_avatars/',default='user_avatars/hitter.png')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def full_name(self):
        return (self.user.first_name +" " +self.user.last_name)


    def __str__(self):
        return self.user.username


    