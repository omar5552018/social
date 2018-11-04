from django.conf.urls import url
from . import views
from .views import UploadView

urlpatterns = [









    url(r'upload/$', UploadView.as_view(), name='post_page'),
    url(r'^(?P<username>.+)/$', views.user_Page, name='user_page')
]
