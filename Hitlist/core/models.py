
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class hitter(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank=True)
    hit_title = models.CharField(max_length = 300, null=True, blank=True)
    hit_brief = models.CharField(max_length  = 200, null= True, blank=True)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hit_title

    class Meta:
        ordering = ['status']