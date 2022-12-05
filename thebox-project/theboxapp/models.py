from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(
        User, related_name='account', on_delete=models.CASCADE)
    password = models.CharField(max_length=200, default='none')
    who = models.CharField(
        max_length=7,
        # ('actual value', 'human readable value')
        choices=[('none', 'N/A'), ('staff', 'staff'), ('student', 'student')],
        default='none'
    )
    mealSwipNum = models.IntegerField()

    def __str__(self):
        return self.user.username


class DonatedMealSwipe(models.Model):
    # will automatically be set to creation time
    donatedTime = models.DateTimeField(auto_now_add=True)
    receivedTime = models.DateTimeField(null=True, blank=True)
    # availability of the donated meal swipe
    availability = models.BooleanField(default=True)
    donateUser = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='donateUser')
    receiveUser = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='receiveUser')

    def __str__(self):
        return "Mealswipe donated"  # + self.donateUser.username


class TheBox(models.Model):
    nutritionFacts = models.TextField(blank=True)  # nutrition facts of the box
    # will automatically be set to creation time
    creationTime = models.DateTimeField(auto_now_add=True)
    receivedTime = models.DateTimeField(null=True, blank=True)
    # availability of the donated meal swipe
    availability = models.BooleanField(default=True)
    receiveUser = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nutritionFacts
