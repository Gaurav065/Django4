from audioop import reverse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView,LogoutView

from django.urls import reverse_lazy
from .models import hitter



class HitterLoginView(LoginView):
    template_name= 'core/Hitter_DiveIn.html'
    fields = '__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('Hitlist')

class HitterLogoutView(LogoutView):
    template_name='core/Hitter_DiveOut.html'
    fields = '__all__'
    re

class Hitlist(ListView):
    model = hitter 
    context_object_name= 'Hits'
    ordering=['date_created']
    
class HitDetails(DetailView):
    model = hitter
    context_object_name= 'h'
    template_name= 'core/hits.html'


class HitCreate(CreateView):
    model = hitter
    template_name='core/hit_init.html'

    fields= '__all__'
    success_url=reverse_lazy('Hitlist')

class HitUpdate(UpdateView):
    model = hitter
    template_name='core/hit_updation.html'

    fields = '__all__'
    success_url= reverse_lazy('Hitlist')

class HitTerminate(DeleteView):
    model = hitter
    template_name='core/hit_terminate.html'

    context_object_name='h'
    success_url= reverse_lazy('Hitlist')
    