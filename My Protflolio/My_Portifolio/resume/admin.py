from django.contrib import admin
from .models import education, experience,certificates, skill

admin.site.register(education)
admin.site.register(experience)
admin.site.register(skill)
admin.site.register(certificates)
# Register your models here.
