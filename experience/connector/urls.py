from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^authenticate_user/$', views.authenticate_user, name='authenticate_user'),
]
