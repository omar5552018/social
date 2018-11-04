from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'account/loginPage.html'}, name='loginPage'),
    url(r'^logout/$', logout, {'template_name': 'account/logoutPage.html'}, name='logoutPage'),
    url(r'^register/$', views.register, name='registerPage'),
    url(r'^profile/$', views.view_profile, name='userProfilePage'),
    url(r'^change_password/$', views.change_password, name='changePasswordPage'),
    url(r'^update_info/$', views.update_info, name='updateInfoPage'),
]
