from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout

# Create your views here.


def home(requestion):
    return HttpResponse('HOME HOME')


def homepage(request):
    return render(request, 'theboxapp/home.html')


def signupuser(request):
    if request.method == "GET":
        return render(request, 'theboxapp/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # create a new user
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('homepagestudent')
            except IntegrityError:
                return render(request, 'theboxapp/signupuser.html', {'form': UserCreationForm(), 'error': 'Username has already been taken'})
        else:
            # tell the user that 2 passwords don't match
            return render(request, 'theboxapp/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords do not match'})


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect()


def homepagestudent(request):
    return render(request, 'theboxapp/homepagestudent.html')


def loginuser(request):
    return HttpResponse('placeholder')


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


def staffUpdateBox(request):
    return render(request, 'theboxapp/staffUpdateBox.html')


def staffDisplayDonate(request):
    return render(request, 'theboxapp/staffDisplayDonate.html')


def staffDisplayFeedback(request):
    return render(request, 'theboxapp/staffDisplayFeedback.html')


def studentFeedback(request):
    return render(request, 'theboxapp/studentFeedback.html')
