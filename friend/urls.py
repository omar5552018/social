from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^commit/(?P<operation>.+)/(?P<pk>\d+)/$', views.add_or_remove_friend, name='add_or_remove_friend'),
]
