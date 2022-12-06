from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .backends import AccountBackend
from django.db import IntegrityError
from django.contrib.auth import login, logout
from django.contrib.auth import forms
from django.contrib import messages
from .models import *
from theboxapp.staffboxforms import BoxForm
from theboxapp.studentboxforms import UpdateboxForm
from theboxapp.studentfeedbackforms import feedbackForm
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
    logout(request)
    request.user = None
    return redirect('/')


# below are for students:
def checkmealplan(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'staff':
            return redirect('staffhome')
    except Account.DoesNotExist:
        return redirect('/')

    return render(request, 'theboxapp/checkmealplan.html', context)


def donatemealplan(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'staff':
            return redirect('staffhome')
    except Account.DoesNotExist:
        return redirect('/')

    print(request.user.account.mealSwipNum)
    if request.method == 'POST':
        form = StudentMealSwipeForm(request.POST)
        if request.user.account.mealSwipNum <= 0:
            messages.error(
                request, 'Sorry, you do not have any mealswips left in your account.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            if form.is_valid():
                form.save()
                acc = request.user.account
                meal = acc.mealSwipNum
                setattr(acc, 'mealSwipNum', meal-1)
                acc.save()
                print(request.user.account.mealSwipNum)
                messages.success(
                    request, 'Succcessfully donated one mealswipe. Thank you!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            context = {'form': form}
            return render(request, 'theboxapp/donatemealplan.html', context)
    else:
        form = StudentMealSwipeForm(request.POST)
        context = {'form': form}
        return render(request, 'theboxapp/donatemealplan.html', context)


def registermealplan(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'staff':
            return redirect('staffhome')
    except Account.DoesNotExist:
        return redirect('/')

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
        messages.success(
            request, 'Successfully registered for one free mealswipe!')
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
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'staff':
            return redirect('staffhome')
    except Account.DoesNotExist:
        return redirect('/')

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
    if request.method == 'GET':
        if flag == 1:
            messages.error(
                request, 'You have already registered for the box today.')
            return render(request, 'theboxapp/studentthebox.html')
        elif len(TheBox.objects.all()) == 0:
            messages.info(
                request, 'There is no availbale box at this moment. Please come back later.')
            return render(request, 'theboxapp/studentthebox.html')
    if request.method == "POST":
        if len(TheBox.objects.all()) == 0:
            messages.info(
                request, 'There is no availbale box at this moment. Please come back later.')
            return render(request, 'theboxapp/studentthebox.html')
        elif flag == 0:
            if boxcurr != "none":
                boxcurr.receivedTime = today
                boxcurr.receiveUser = currUser
                boxcurr.save()
                messages.success(
                    request, 'Successfully registered for the box!')
                return render(request, 'theboxapp/studentthebox.html')
        elif flag == 1:
            messages.error(
                request, 'You have already registered for the box today.')
            return render(request, 'theboxapp/studentthebox.html')
    if form1 != "none" and flag == 0:
        context = {'form': form1}
        return render(request, 'theboxapp/studentthebox.html', context)
    else:
        return render(request, 'theboxapp/studentthebox.html')


def studentcancelthebox(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'staff':
            return redirect('staffhome')
    except Account.DoesNotExist:
        return redirect('/')
    boxes = TheBox.objects.all()
    currUser = request.user
    doIHaveABox = False
    for each in boxes:
        if each.receiveUser == currUser:
            doIHaveABox = True
    if request.method == 'GET':
        if doIHaveABox == False:
            messages.error(
                request, 'You have not registered for box yet.')
        return render(request, 'theboxapp/studentcancelthebox.html')
    if request.method == 'POST':
        for eachbox in boxes:
            if eachbox.receiveUser == currUser:
                doIHaveABox = True
                eachbox.receiveUser = None
                eachbox.save()
                messages.success(
                    request, 'You have successfully canceled your box.')
        if (doIHaveABox == False):
            messages.error(
                request, 'You have not registered for box yet.')
        return render(request, 'theboxapp/studentcancelthebox.html')


def studenthome(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'staff':
            return redirect('staffhome')
    except Account.DoesNotExist:
        return redirect('/')

    return render(request, 'theboxapp/studenthome.html', context)


def stafflogin(request):
    return render(request, 'theboxapp/stafflogin.html')


def staffhome(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'student':
            return redirect('studenthome')
    except Account.DoesNotExist:
        return redirect('/')

    return render(request, 'theboxapp/staffhome.html', context)


def staffupdatebox(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'student':
            return redirect('studenthome')
    except Account.DoesNotExist:
        return redirect('/')
    form = BoxForm()
    if request.method == 'POST':
        form = BoxForm(request.POST)
        if form.is_valid() and form.data['nutritionFacts']:
            form.save()
            messages.success(request, 'You have successfully added a new box.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(
                request, 'Please fill in nutrition facts of the box before submitting.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {'form': form}
    return render(request, 'theboxapp/staffupdatebox.html', context)


def studentfeedback(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'staff':
            return redirect('staffhome')
    except Account.DoesNotExist:
        return redirect('/')

    form = feedbackForm()
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid() and form.data['content']:
            form.save()
            messages.success(request, 'Thank you for sharing you feedback!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(
                request, 'Please fill in feedback content before submitting.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {'form': form}
    return render(request, 'theboxapp/studentfeedback.html', context)


def staffdisplaydonate(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'student':
            return redirect('studenthome')
    except Account.DoesNotExist:
        return redirect('/')

    donated = list(DonatedMealSwipe.objects.all())
    context = {"number": len(donated)}
    return render(request, 'theboxapp/staffdisplaydonate.html', context)


def staffdisplayfeedback(request):
    context = {'user': request.user}
    try:
        account = Account.objects.get(username=request.user)
        if account.who == 'student':
            return redirect('studenthome')
    except Account.DoesNotExist:
        return redirect('/')

    feedbacks = list(Feedback.objects.all())
    context = {}
    fblst = []
    for feedback in feedbacks:
        fblst.append(feedback.content)
    context["allfeedback"] = fblst
    return render(request, 'theboxapp/staffdisplayfeedback.html', context)
