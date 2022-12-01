from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout
from django.contrib.auth import forms  
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm  
from .forms import CustomUserCreationForm  

# Create your views here.


def home(request):
    # rmb to create a real home page
    return render(request, 'theboxapp/generalhome.html')


def homepage(request):
    return render(request, 'theboxapp/home.html')


def signupuser(request):  
    if request.POST == 'POST':  
        form = CustomUserCreationForm()  
        if form.is_valid():  
            form.save()  
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'theboxapp/signupuser.html', context) 


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect()


def homepagestudent(request):
    return render(request, 'theboxapp/homepagestudent.html')


# below are for students:
def checkmealplan(request):
    return render(request, 'theboxapp/checkmealplan.html')


def donatemealplan(request):
    return render(request, 'theboxapp/donatemealplan.html')


def registermealplan(request):
    return render(request, 'theboxapp/registermealplan.html')


def studentlogin(request):
    return render(request, 'theboxapp/studentlogin.html')


def stuentthebox(request):
    return render(request, 'theboxapp/studentthebox.html')


def studenthome(request):
    return render(request, 'theboxapp/studenthome.html')


def stafflogin(request):
    return render(request, 'theboxapp/stafflogin.html')


def staffhome(request):
    return render(request, 'theboxapp/staffhome.html')


def staffupdatebox(request):
    return render(request, 'theboxapp/staffupdatebox.html')


def staffdisplaydonate(request):
    return render(request, 'theboxapp/staffdisplaydonate.html')


def staffdisplayfeedback(request):
    return render(request, 'theboxapp/staffdisplayfeedback.html')


def studentfeedback(request):
    return render(request, 'theboxapp/studentfeedback.html')
