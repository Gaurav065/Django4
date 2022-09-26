from django.shortcuts import render,redirect

def hits(request):
    context={}
    return render(request, 'hits.html',context)

# Create your views here.
