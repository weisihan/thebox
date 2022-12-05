from django.forms import ModelForm
from theboxapp.models import TheBox

class UpdateboxForm(ModelForm):
    class Meta:
        model = TheBox
        fields = ['receiveUser','receivedTime']
        # fields = '__all__'