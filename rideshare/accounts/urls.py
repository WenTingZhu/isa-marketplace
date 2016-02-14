from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    # url(r'^login/$', views.login, name='login'),
    url(r'^user/$', views.create_user, name='create_user'),
    url(r'^user/(\d+)/$', views.user, name='user'),



]
