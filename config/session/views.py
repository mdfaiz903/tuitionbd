from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def loginuser(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid username or password')
    else:
        form =AuthenticationForm()
    return render(request,'session/login.html',{'form':form})


def logoutuser(request):
    logout(request)
    messages.success(request,'Successfully logout')
    return redirect('home')

from.forms import registationForm

def registation(request):
    if request.method=='POST':
        form = registationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = registationForm()
    return render(request,'session/registation.html',{'form':form})