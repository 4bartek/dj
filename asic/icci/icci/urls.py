from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('video/', include('video.urls')),
    path('rss_reader/', include('rss_reader.urls')),
    path('ico/', include('ico.urls')),
    path('events/', include('events.urls')),
]
