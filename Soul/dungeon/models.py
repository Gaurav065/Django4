from django.db import models

# Create your models here.
class Party(models.Model):
    
    
    party_member= models.CharField(max_length=100)
    member_level= models.IntegerField(default=0)

    member_role= models.CharField(max_length=75)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.party_member


