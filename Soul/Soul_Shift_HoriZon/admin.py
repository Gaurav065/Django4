from django.contrib import admin

# Register your models here.
from .models import Wallpaper,Skill, message

admin.site.register(Wallpaper)
admin.site.register(Skill)
admin.site.register(message)