"""thebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from theboxapp import views

urlpatterns = [
    path('', views.home),
    path('wwlogin/', views.login),
    #below is for students page
    path('checkmealplan', views.checkmealplan),
    path('donatemealplan',views.donatemealplan),
    path('studentlogin',views.studentlogin),
    path('registermealplan',views.registermealplan),
    path('studentthebox',views.stuentthebox),
    path('studenthome',views.studenthome),
]
