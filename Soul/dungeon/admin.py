from django.contrib import admin
from .models import Party, party_member_info


admin.site.register(Party)
admin.site.register(party_member_info)

# Register your models her