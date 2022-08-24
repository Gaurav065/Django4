from os import link
from django.db import models
from django.forms import ModelForm
from resume.models import skill,experiance

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    sk = models.ManyToManyField('resume.skill', related_name='sk')
    link = models.URLField(default='https://github.com/Gaurav065')
    description = models.TextField(default=project_name, max_length=300)
    client= models.ForeignKey('resume.experiance', on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

class achievement(models.Model):
    achievements = models.CharField(default='Current work', max_length=300)


