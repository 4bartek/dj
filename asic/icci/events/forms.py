from django.forms import ModelForm
from .models import GetEvents

class EditEvents(ModelForm):
    class Meta:
        model = GetEvents
        fields = ['kod']