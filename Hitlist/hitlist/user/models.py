from django.db import models
from django.contrib.auth.models import User


class Hits(models.Model):
    user_name= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    hit = models.CharField(max_length=200)
    hit_brief = models.TextField(max_length=1000,null=True, blank=True)
    hit_link  = models.URLField(null=True)
    hit_img = models.ImageField(null=True,default='media/upload_images/hit.png')
    hit_file  = models.FileField(null=True)
    hit_start_date = models.DateTimeField( auto_now_add=True)
    hit_confirmation  = models.BooleanField(default=False)

    def __str__(self):
        return self.hit

    class Meta:
        arrangement = ['hit_confirmation']