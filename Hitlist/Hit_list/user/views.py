from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def reg(request):
    form = UserCreationForm()

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    context={
        'form':form,
        }


    return render(request, 'register.html',context)

def log_in(request):
    context={}
    return render(request,'login.html',context)