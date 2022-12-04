from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Account
from .backends import AccountBackend
from django.db import IntegrityError
from django.contrib.auth import login, logout
from django.contrib.auth import forms  
from django.contrib import messages  

# Create your views here.


def home(request):
    # rmb to create a real home page
    return render(request, 'theboxapp/generalhome.html')


def homepage(request):
    return render(request, 'theboxapp/home.html')


def signupuser(request):
    return render(request, 'theboxapp/signupuser.html')


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


def userlogin(request):
    if request.method == 'GET':
        return render(request, 'theboxapp/userlogin.html', {'form':AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = AccountBackend.authenticate(username, password)
        if user is None:
            return render(request, 'theboxapp/userlogin.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user[0], backend='theboxapp.backends.AccountBackend')
            if user[1] == 'staff':
                return redirect('staffhome')
            elif user[1] == 'student':
                return redirect('studenthome')    


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
