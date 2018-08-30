from django.contrib import admin
from .models import Movie



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_per_page = 400
    list_display = ('title', 'author', 'icci_cat', 'icci_sub_cat')
    list_filter = ('author','title', )
    search_fields = ('title', 'description', 'tags')

