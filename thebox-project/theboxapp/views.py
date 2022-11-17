from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'theboxapp/home.html')

def login(request):
    return HttpResponse("You have logged in")