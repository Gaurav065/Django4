from audioop import reverse
from attr import fields
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.urls import reverse_lazy
from .models import hitter



class HitterLoginView(LoginView):
    template_name= 'core/Hitter_DiveIn.html'
    fields = '__all__'
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('Hitlist')


class HitterRegister(FormView):
    template_name='core/register.html'
    fields="__all__"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url= reverse_lazy('Hitlist')
    




class Hitlist(LoginRequiredMixin,ListView):
    model = hitter 
    context_object_name= 'Hits'
    ordering=['date_created']
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context 
    
class HitDetails(LoginRequiredMixin,DetailView):
    model = hitter
    context_object_name= 'h'
    template_name= 'core/hits.html'


class HitCreate(LoginRequiredMixin,CreateView):
    model = hitter
    template_name='core/hit_init.html'

    fields= '__all__'
    success_url=reverse_lazy('Hitlist')

class HitUpdate(LoginRequiredMixin,UpdateView):
    model = hitter
    template_name='core/hit_updation.html'

    fields = '__all__'
    success_url= reverse_lazy('Hitlist')

class HitTerminate(LoginRequiredMixin,DeleteView):
    model = hitter
    template_name='core/hit_terminate.html'

    context_object_name='h'
    success_url= reverse_lazy('Hitlist')
    