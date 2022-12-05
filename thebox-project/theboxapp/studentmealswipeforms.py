from django.forms import ModelForm
from .models import Account, DonatedMealSwipe


class StudentMealSwipeForm(ModelForm):
    class Meta:
        model = DonatedMealSwipe
        fields = ['availability']
        #fields = ['mealSwipNum']
