import email
from email.policy import default
from operator import getitem
from django.db import models



class Profile(models.Model):
    
    avatar = models.ImageField(default='img/default.jpeg', upload_to='img/')
    f_name= models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)

    about= models.TextField(default='About Me')
    git_link = models.URLField(default='https://github.com/Gaurav065')
    
    link_link = models.URLField(default='https://www.linkedin.com/in/gaurav-patel-a822931bb/')

    phone_number = models.CharField(default='+91-9721645391', max_length=15)
    email = models.EmailField(default='gaurav.patel.gpp@gmail.com')

    
    def full_name(self):
        return self.f_name +" "+ self.l_name