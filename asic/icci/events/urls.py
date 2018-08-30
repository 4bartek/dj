from django.urls import path
from .views import events, events_editdb

urlpatterns = [
    path('', events, name='events'),
    path('events_editdb/', events_editdb, name='events_editdb'),
] 