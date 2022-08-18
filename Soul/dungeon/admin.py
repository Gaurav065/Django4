from django.contrib import admin
from .models import Party, party_member_info, Party_Info, quests


admin.site.register(Party)
admin.site.register(party_member_info)
admin.site.register(Party_Info)
admin.site.register(quests)
# Register your models her