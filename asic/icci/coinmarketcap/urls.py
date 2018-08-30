from django.urls import path
from .views import coinmarketcap , coinmarketcap_editdb

urlpatterns = [
    path('', coinmarketcap, name='coinmarketcap'),
    path('coinmarketcap_editdb/', coinmarketcap_editdb, name='coinmarketcap_editdb'),
] 