from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.redirectToHome),
    url(r'^home/', include('home.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^people/', include('people.urls')),
    url(r'^friend/', include('friend.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    