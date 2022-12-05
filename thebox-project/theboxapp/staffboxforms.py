from django.forms import ModelForm
from theboxapp.models import TheBox

class BoxForm(ModelForm):
    class Meta:
        model = TheBox
        fields = ['nutritionFacts']
        # fields = '__all__'