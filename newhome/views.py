from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import logout , authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import forms

from newhome.forms import SignUpForm

# Create your views here.

def  index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check if authorized
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def signup(request):
    form={}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
        for f in form:
            print(f)
    return render(request, 'signup.html', {'form': form})     
