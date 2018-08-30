from django.forms import ModelForm
from .models import GetFeeds

class EditFeeds(ModelForm):
    class Meta:
        model = GetFeeds
        fields = ['kod']