from django.db import models
import datetime
from django import forms
from django.forms import ModelForm


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


# pr_ln = (
#     ("1", "Python"),
#     ("2", "Java"),
#     ("3", "C"),
#     ("4", "C++"),
#     ("5", "C#"),
#     ("6", "Rust"),
#     ("7", "GoLang"),
#     ("8", "SQL"),
#     ("9", "PHP"),
#     ("10", "Scala"),
#     ("11", "Swift"),
#     ("12", "Matlab"),
#     ("13", "Kotlin"),
#     ("14", "Node.js"),
#     ("15", "React.js"),
#     ("16", "CSS"),
#     ("17", "HTML"),
#     ("18", "TypeScript"),
#     ("19", "Ruby"),
# )

# type_j = (
#     ("1", "Internship"),
#     ("2", "Full time"),
#     ("3", "Part Time"),
#     ("4", "Freelancing"),
# )


# db = (
#     ("1", "MongoDB"),
#     ("2", "Postgres"),
#     ("3", "MySQL"),
# )


class education(models.Model):
    
    university = models.CharField(default="Lovely Professional University", max_length=100)
    course = models.CharField(default='B.Tech CSE with specialization In ML and AI', max_length=100)
    gpa = models.FloatField(default=7.54, max_length=10.0)

    date_start = models.DateField(("Date"), default=datetime.date.today)
    date_end = models.DateField(("Date"), default=datetime.date.today)

    location = models.CharField(default='Phagwara, Punjab, India, 144411', max_length=150)

    

class experiance(models.Model):

    job= models.CharField(default='None', max_length=200,choices=jobs)
    company_name = models.CharField(default='Client_Based', max_length=100)

    job_type = models.CharField(default='None',max_length=200, choices=type_j)

    description = models.TextField(default=job, max_length=300)
    location = models.CharField(default='India', max_length=50)
    end_date = models.DateField(('Date'), default=datetime.date.today)
    start_date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.job


class skill(models.Model):
    skill_type = (
        ("P","Programming Language"),
        ("M","Modules/Libraries"),
        ("T","Tools"),
        ("D","Databases"),
    )
    
    typeof = models.CharField(default="P",max_length=20,choices=skill_type)
    name = models.CharField(default="Python", max_length=25)

    # modules_libraries = models.CharField(default='python libraries', max_length=400)
    # tools = models.CharField(default='VS code, Github, pyqt designer, unreal engine, adobe, etc', max_length=200)
    # databases = models.CharField(default='SQL',choices=db,max_length=100)
    # programming_languages=models.CharField(default='Python',choices=pr_ln,max_length=100)



class certificates(models.Model):
    name = models.CharField(default="best programmer", max_length=100)
    url = models.URLField()
    certi = models.ImageField(default='img/Screenshot 2022-08-21 054646.png', upload_to='img/')
