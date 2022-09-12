from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('base.urls')),
    path('forums/', include('forums.urls')),
    path('events/', include('events.urls')),
    path('matches/', include('matches.urls')),
    path('rankings/', include('rankings.urls')),
    path('stats/', include('stats.urls')),

    path('players/', include('players.urls')),
    path('teams/', include('teams.urls')),

    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)