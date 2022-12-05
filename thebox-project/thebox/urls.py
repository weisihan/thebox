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
from django.contrib import admin
from theboxapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # REAL HOME
    path('', views.home),
    # AUTH
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.userlogin, name='userlogin'), 
    # STUDENT
    path('studentlogin/', views.studentlogin),
    path('studenthome/', views.studenthome,name='studenthome'),
    path('studenthome/checkmealplan/', views.checkmealplan, name='studentcheckmealplan'),
    path('studenthome/donatemealplan/', views.donatemealplan, name='studentdonatemealplan'),
    path('studenthome/registermealplan/', views.registermealplan, name='studentregistermealplan'),
    #student register the box below
    path('studenthome/studentthebox/', views.stuentthebox,name='studentthebox'),
    path('studenthome/studentcancelthebox/',views.studentcancelthebox,name='studentcancelthebox'),
    path('studenthome/studentfeedback/', views.studentfeedback, name='studentfeedback'),
    # STAFF
    path('stafflogin/', views.stafflogin, name='stafflogin'),
    path('staffhome/', views.staffhome, name='staffhome'),
    path('staffhome/staffupdatebox/', views.staffupdatebox, name='staffupdatebox'),
    path('staffhome/staffdisplaydonate/', views.staffdisplaydonate, name='staffdisplaydonate'),
    path('staffhome/staffdisplayfeedback/', views.staffdisplayfeedback,
         name='staffdisplayfeedback'),

]
