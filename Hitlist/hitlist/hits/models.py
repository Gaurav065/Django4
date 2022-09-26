from django.utils import timezone
from django.db import models
import datetime



# Create your models here.
class Hits(models.Model):
    user = models.ForeignKey('user.Hitter_profile', on_delete=models.CASCADE, null=False)
    hit = models.CharField(max_length=500,null=False)
    hit_brief = models.TextField(max_length=1000,null=False)
    hit_link = models.URLField(null=True)
    hit_img = models.ImageField(null=True)
    hit_file = models.FileField(null=True)
    hit_start_date = models.DateField(auto_now_add=True)
    hit_end_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user
