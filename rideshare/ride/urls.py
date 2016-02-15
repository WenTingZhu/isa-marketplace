from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^ride/$', views.create_ride, name='create_ride'),
    url(r'^ride/(\d+)/$', views.ride, name='ride'),
]
