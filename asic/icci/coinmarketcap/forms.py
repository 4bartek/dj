from django.forms import ModelForm
from .models import EditCoinmarketcap

class EditCoinmarketcap(ModelForm):
    class Meta:
        model = EditCoinmarketcap
        fields = ['kod']