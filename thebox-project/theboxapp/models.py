from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DonatedMealSwipe(models.Model):
    donatedTime = models.DateTimeField(auto_now_add=True) # will automatically be set to creation time
    receivedTime = models.DateTimeField(null=True, blank=True)
    availability = models.BooleanField(default=True) # availability of the donated meal swipe
    donateUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donateUser')
    receiveUser = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='receiveUser')

    def __str__(self):
        return "Mealswipe donated by " + self.donateUser.username

class TheBox(models.Model):
    nutritionFacts = models.TextField(blank=True) # nutrition facts of the box
    creationTime = models.DateTimeField(auto_now_add=True) # will automatically be set to creation time
    receivedTime = models.DateTimeField(null=True, blank=True)
    availability = models.BooleanField(default=True) # availability of the donated meal swipe
    receiveUser = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.nutritionFacts