from django.forms import ModelForm
from theboxapp.models import Feedback

class feedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['content']