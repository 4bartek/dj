from django.urls import path
from .views import wszystkie_filmy, editdb

from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)


urlpatterns = [
    path('', wszystkie_filmy, name='wszystkie_filmy'),
    path('editdb/', editdb, name='editdb'),
    url(r'^', include(router.urls)),
] 