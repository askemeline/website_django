from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^accounts/logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/edit_profile/$', views.edit_profile, name='edit_profile'),
]
