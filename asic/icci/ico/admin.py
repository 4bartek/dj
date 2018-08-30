from django.contrib import admin
from .models import IcoEvent

# Register your models here.

@admin.register(IcoEvent)
class Ico(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_per_page = 400
    list_display = ('ico_title', 'ico_typ', 'ico_source', 'ico_start_time', 'ico_end_time' )
    list_filter = ('ico_title', 'ico_typ' ,'ico_source', 'ico_start_time', 'ico_end_time' )
    search_fields = ('ico_title', 'ico_description', 'ico_source')
