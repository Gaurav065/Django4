from django.contrib import admin

# Register your models here.
from .models import Wallpaper,Skill, Info

admin.site.register(Wallpaper)
admin.site.register(Skill)
admin.site.register(Info)
# admin.site.register(Time_login)