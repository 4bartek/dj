from django.forms import ModelForm
from .models import GetIco

class EditIco(ModelForm):
    class Meta:
        model = GetIco
        fields = ['kod']