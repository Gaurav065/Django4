from email.policy import default
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Party(models.Model):
    
    
    party_member= models.CharField(max_length=100)
    member_level= models.IntegerField(default=0)

    member_role= models.CharField(max_length=75)
    
    notes = models.TextField(max_length=300, default='No notes')

    def __str__(self):
        return self.party_member, str(self.member_level), str(self.member_role), str(self.notes)

class party_member_info(models.Model):
    level= models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    skills= models.CharField(default='basic survival',max_length=500)

    skill_level= models.IntegerField(default=1,validators=[MaxValueValidator(20)])

    blessings= models.TextField(default='natural Hp and Mana regin')

    rank=models.CharField(default='G', max_length=1)

    def __str__(self):
        return self.rank.upper()


class Party_Info(models.Model):
    party_name = models.CharField(max_length=125)
    party_level = models.IntegerField(default=1,validators=[MaxValueValidator(100)])
    party_size = models.IntegerField(default=2,validators=[MaxValueValidator(10)])
    party_rank = models.CharField(default='G',max_length=1)

    def __str__(self):
        return self.party_name