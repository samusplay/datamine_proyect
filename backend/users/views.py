from django.shortcuts import render,redirect
from .forms import customuserCreationFrom

def register(request):
    if request.method=='Post':
       form=customuserCreationFrom(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login')# redirigir al login despues de registrar
    else:
        form=customuserCreationFrom()
        return render (request,'users/register.html',{'form':form})   


# Create your views here.
