from django.contrib import admin
from .models import Event

# Register your models here.

@admin.register(Event)
class Events(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_per_page = 400
    list_display = ('event_title','event_date','event_feed_source')
    list_filter = ('event_title','event_date')
    search_fields = ('event_title','event_description','event_date','event_feed_source')

