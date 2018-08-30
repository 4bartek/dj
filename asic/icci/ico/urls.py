from django.urls import path
from .views import ico, ico_editdb


urlpatterns = [
    path('', ico, name='ico'),
    path('ico_editdb/', ico_editdb, name='ico_editdb'),
] 