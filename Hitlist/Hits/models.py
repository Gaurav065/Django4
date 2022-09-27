from django.db import models
from django.contrib.auth.models import User




class Hitter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.CharField(max_length=150, null=True, blank= True)
    hit_brief = models.CharField(max_length=300, null=True, blank=True)
    hit_status = models.BooleanField(default=False)
    hit_history = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.hit