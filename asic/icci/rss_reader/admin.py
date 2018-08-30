from django.contrib import admin
from .models import Feeds

# Register your models here.

@admin.register(Feeds)
class Ico(admin.ModelAdmin):
    # fields = ('name', 'description', 'year')
    list_per_page = 400
    list_display = ('rss_feed_title', 'rss_feed_source', 'rss_feed_published' )
    list_filter = ('rss_feed_title','rss_feed_description', 'rss_feed_source' )
    search_fields = ('rss_feed_title', 'rss_feed_description', 'rss_feed_source')
