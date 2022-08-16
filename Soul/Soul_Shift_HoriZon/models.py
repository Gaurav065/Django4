from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Skill(models.Model):
    skil = models.CharField( max_length=200)

    def __str__(self):
        return self.skil



class Wallpaper(models.Model):
    
    skill= models.ForeignKey(Skill, on_delete=models.SET_NULL, null= True)
    #host
    char_name= models.CharField(max_length=100)
    role= models.TextField(null=True, blank=True)

    #fav_wallpaper

    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.char_name

class Info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    wallpaper=models.ForeignKey(Wallpaper, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50 ]