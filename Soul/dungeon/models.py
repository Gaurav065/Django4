from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Party(models.Model):
    
    party_id= models.CharField(default='Duo Party',max_length= 100)
    
    party_members= models.CharField(max_length=100)
    member_level= models.IntegerField(default=0)

    member_role= models.CharField(max_length=75)
    
    notes = models.TextField(max_length=300, default='No notes')

    def __str__(self):
        return self.party_member, self.name, str(self.member_level), str(self.member_role), str(self.notes)

class party_member_info(models.Model):
    level= models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    skills= models.CharField(default='basic survival',max_length=500)

    skill_level= models.IntegerField(default=1,validators=[MaxValueValidator(20)])

    blessings= models.TextField(default='natural Hp and Mana regin')

    rank=models.CharField(default='G', max_length=1)

    def __str__(self):
        return self.rank.upper()


class Party_Info(models.Model):
    # party_name = models.ForeignKey(Party, on_delete=models.CASCADE, default=Party.party_id)
    party_level = models.IntegerField(default=1,validators=[MaxValueValidator(100)])
    party_size = models.IntegerField(default=2,validators=[MaxValueValidator(10)])
    party_rank = models.CharField(default='G',max_length=1)

    def __str__(self):
        return self.party_name

class quest(models.Model):
    quest_party= models.CharField(default='Herb collection', max_length=300)
    quest_rank = models.CharField(default='F', max_length=1)
    quest_time  = models.DateField(('Date'), default=datetime.date.today)

    def __str__(self):
        return self.quest_rank

class Reward(models.Model):
    quest_reward = models.CharField(default='10 coppers', max_length= 50)

    def __str__(self):
        return self.quest_reward

# class reg_party(models.Model):
#     party_id = models.ForeignKey(Party.party_id, on_delete=models.SET_NULL )
#     party_size = models.ForeignKey(Party_Info.party_size, on_delete= models.SET_NULL)
#     party_cap = models.CharField(max_length=50)