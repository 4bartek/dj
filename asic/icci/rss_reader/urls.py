from django.urls import path
from .views import feeds, editdb


urlpatterns = [
    path('', feeds, name='feeds'),
    path('rss_editdb/', editdb, name='rss_editdb'),    
] 