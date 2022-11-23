from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DonatedMealSwipe(models.Model):
    donatedBy = models.CharField(max_length = 10) # netid of the student
    receivedBy = models.TextField(blank=True) # netid of the student
    donatedTime = models.DateTimeField(auto_now_add=True) # will automatically be set to creation time
    receivedTime = models.DateTimeField(null=True, blank=True)
    availability = models.BooleanField(default=True) # availability of the donated meal swipe
    donateUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        str = "Mealswipe donated by " + self.donatedBy
        return str