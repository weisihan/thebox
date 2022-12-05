from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Account
from .backends import AccountBackend
from django.db import IntegrityError
from django.contrib.auth import login, logout
from django.contrib.auth import forms
from django.contrib import messages
from .models import *
from theboxapp.staffboxforms import BoxForm
from theboxapp.studentboxforms import UpdateboxForm
from django.http import HttpResponseRedirect
from datetime import datetime
from datetime import date
from .studentmealswipeforms import StudentMealSwipeForm

# Create your views here.


def home(request):
    # rmb to create a real home page
    print("realhome")
    # request.session.setdefault('username', 'none')
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
    context = {'user': request.user}
    return render(request, 'theboxapp/checkmealplan.html', context)


def donatemealplan(request):
    print(request.user.account.mealSwipNum)
    if request.method == 'POST':
        form = StudentMealSwipeForm(request.POST)
        if form.is_valid():
            form.save()
            acc = request.user.account
            meal = acc.mealSwipNum
            setattr(acc, 'mealSwipNum', meal-1)
            acc.save()
            print(request.user.account.mealSwipNum)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        context = {'form': form}
        return render(request, 'theboxapp/donatemealplan.html', context)
    else:
        form = StudentMealSwipeForm(request.POST)
        context = {'form': form}
        return render(request, 'theboxapp/donatemealplan.html', context)


def registermealplan(request):
    print(request.user.account.mealSwipNum)
    if request.method == 'POST':
        acc = request.user.account
        meal = acc.mealSwipNum
        setattr(acc, 'mealSwipNum', meal+1)
        acc.save()
        print(request.user.account.mealSwipNum)
        allDonated = DonatedMealSwipe.objects.all()
        print(len(allDonated))
        delete = DonatedMealSwipe.objects.all()[:1]
        for one in delete:
            one.delete()
        print(len(DonatedMealSwipe.objects.all()))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return render(request, 'theboxapp/registermealplan.html')
    else:
        return render(request, 'theboxapp/registermealplan.html')


def userlogin(request):

    if request.method == 'GET':
        return render(request, 'theboxapp/userlogin.html', {'form': AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = AccountBackend.authenticate(username, password)
        # realuse = user[0]
        if user is None:
            return render(request, 'theboxapp/userlogin.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user[0],
                  backend='theboxapp.backends.AccountBackend')
            # print(user[0])
            # request.session['username']=realuse
            if user[1] == 'staff':
                return redirect('staffhome')
            elif user[1] == 'student':
                return redirect('studenthome')


def studentlogin(request):
    return render(request, 'theboxapp/studentlogin.html')


def stuentthebox(request):
    # form1 = BoxForm()
    today = datetime.today()
    daynow = today.day
    monthnow = today.month
    yearnow = today.year
    boxcurr = "none"
    form1 = "none"
    # print("daynow",daynow)
    boxes = TheBox.objects.all()
    currUser = request.user
    flag = 0
    for item in boxes:
         if item.creationTime.year == yearnow:
            if item.creationTime.month == monthnow:
                if item.creationTime.day == daynow:
                    if item.receiveUser == currUser:
                        flag = 1
    for item in boxes:
        if item.creationTime.year == yearnow:
            if item.creationTime.month == monthnow:
                if item.creationTime.day == daynow:
                    if item.receiveUser == None:
                        if item.receiveUser != currUser:
                            # print("YAY",item.creationTime.day)
                            # boxcurr = TheBox.objects.get(item.id)
                            boxcurr = item
                            form1 = BoxForm(instance=boxcurr)
                            # box = TheBox.objects.get(creationTime=item.creationTime)
                            # box.receiveUser = "sw4293"
    # form = BoxForm(instance=boxcurr)

    # box = TheBox.objects.get(creationTime="2022-11-23 22:21:27.312086+00:00")
    # form = BoxForm(instance=box)

    print(currUser)
    if request.method == "POST" and flag == 0:
        if boxcurr != "none":
            # boxcurr.update(receivedTime=today)
            # boxcurr.update(receiveUser=currUser)
            boxcurr.receivedTime = today
            boxcurr.receiveUser = currUser
            boxcurr.save()
            # form = BoxForm(request.POST,instance=boxcurr)
            # if form.is_valid():
            #     form.save()
            #     return redirect('/')
    if form1 != "none" and flag == 0:
        context = {'form': form1}
        return render(request, 'theboxapp/studentthebox.html', context)
    else:
        return render(request, 'theboxapp/studentthebox.html')


def studentcancelthebox(request):
    boxes = TheBox.objects.all()
    currUser = request.user
    for eachbox in boxes:
        if eachbox.receiveUser == currUser:
            eachbox.receiveUser = None
            eachbox.save()
    return render(request, 'theboxapp/studentcancelthebox.html')


def studenthome(request):
    return render(request, 'theboxapp/studenthome.html')


def stafflogin(request):
    return render(request, 'theboxapp/stafflogin.html')


def staffhome(request):
    return render(request, 'theboxapp/staffhome.html')


def staffupdatebox(request):
    form = BoxForm()
    if request.method == 'POST':
        # print("printing post", request.POST)
        form = BoxForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {'form': form}
    return render(request, 'theboxapp/staffupdatebox.html', context)


def staffdisplaydonate(request):
    return render(request, 'theboxapp/staffdisplaydonate.html')


def staffdisplayfeedback(request):
    return render(request, 'theboxapp/staffdisplayfeedback.html')


def studentfeedback(request):
    return render(request, 'theboxapp/studentfeedback.html')
