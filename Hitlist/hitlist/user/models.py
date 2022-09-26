from django.db import models
from django.utils import timezone


class Hitter_profile(models.Model):

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    avatar = models.ImageField(default='media/')
    user_hits = models.ForeignKey('Hits',on_delete=models.CASCADE)
   
    

    def __str__(self):
        return self.name

class Hits(models.Model):
    user_name= models.ForeignKey(Hitter_profile, on_delete=models.CASCADE)
    # user_avatar = models.ForeignKey(Hitter_profile.avatar, on_delete=models.CASCADE)

    hit = models.CharField(max_length=100)
    hit_brief = models.TextField(max_length=1000)
    hit_link  = models.URLField(null=True)
    hit_img = models.ImageField(null=True,default='media/upload_images/hit.png')
    hit_file  = models.FileField(null=True)
    hit_start_date = models.DateField( auto_now_add=True)
    hit_end_date = models.DateField( auto_now_add=True)

    def __str__(self):
        return self.hit