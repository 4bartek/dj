from django.forms import ModelForm
from .models import Movie, GetMovies

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'author', 'icci_cat', 'icci_sub_cat',]

class AllMoviesForm(ModelForm):
    class Meta:
        model = GetMovies
        fields = ['kod']
