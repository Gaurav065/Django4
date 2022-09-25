from django.shortcuts import render
from .models import Party





def home(request):
    party=Party.objects.all()
    return render(request,'start.html')
# Create your views here.

def party(party, key):
    party = None
    for p in party:
        if p['party']==int(key):
            party = p
    context = {'party':party}