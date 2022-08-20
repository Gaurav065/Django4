from secrets import choice
from socket import fromshare
from sys import maxsize
from django.db import models
import datetime
from django import forms


jobs =(
    ("1", "Frontend dev"),
    ("2", "Backend dev"),
    ("3", "Full Stack"),
    ("4", "Software developer"),
    ("5", "Data Scientist"),
    ("6", "Data Engineer"),
    ("7", "Database Administrator"),
    ("8", "Machine Learning Engineer"),
    ("9", "Software Architect"),
    ("10", "Dev Ops Engineer"),
    ("11", "Cloud Engineer"),
    ("12", "IT project Manager"),
    ("13", "Enterprise Architect"),
)


type_j = (
    ("1", "Internship"),
    ("2", "Full time"),
    ("3", "Part Time"),
    ("4", "Freelancing"),
)

class education(models.Model):
    
    university = models.CharField(default="Lovely Professional University", max_length=100)
    course = models.CharField(default='B.Tech CSE with specialization In ML and AI', max_length=100)
    gpa = models.FloatField(default=7.54, max_length=10.0)

    date_start = models.DateField(("Date"), default=datetime.date.today)
    date_end = models.DateField(("Date"), default=datetime.date.today)

    location = models.CharField(default='Phagwara, Punjab, India, 144411', max_length=150)

    def uni_name(self):
        return self.university
    
    def crs(self):
        return self.course

    def cgpa(self):
        return self.gpa
    
    def dt(self):
        return self.date_start +"-"+ self.date_end

    def loc(self):
        return self.loc




class experiance(models.Model):

    job= forms.ChoiceField(choices=jobs)
    company_name = models.CharField(default='Client_Based', max_length=100)

    job_type = forms.ChoiceField(choices=type_j)

    description = models.TextField(default=job, max_length=300)
    location = models.CharField(default='India', max_length=50)
    end_date = models.DateField(('Date'), default=datetime.date.today)
    start_date = models.DateField(("Date"), default=datetime.date.today)

    def edt(self):
        return   self.location+'|' + self.start_date + '-' + self.end_date

class skill(models.Model):
    pass