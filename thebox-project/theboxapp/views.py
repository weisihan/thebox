from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'theboxapp/home.html')


def login(request):
    return HttpResponse("You have logged in")

#below are for students: 
def checkmealplan(request):
    return render(request, 'theboxapp/checkmealplan.html')

def donatemealplan(request):
    return render(request, 'theboxapp/donatemealplan.html')

def registermealplan(request):
     return render(request, 'theboxapp/registermealplan.html')

def studentlogin(request):
    return render(request,'theboxapp/studentlogin.html')

def stuentthebox(request):
    return render(request,'theboxapp/studentthebox.html')

def studenthome(request):
    return render(request,'theboxapp/studenthome.html')