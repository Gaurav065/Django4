from django.db import models



class Hitter_profile(models.Model):

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    avatar = models.ImageField(default='media/')
    # hit = models.ForeignKey('hits.Hits',on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.name