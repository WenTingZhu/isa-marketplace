from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^ride/(\d+)/$', views.ride, name='ride'),
    url(r'^ride/$', views.create_ride, name='create_ride'),
    url(r'^ride/delete/(\d+)/$', views.delete_ride, name='delete_ride'),
    url(r'^ride/rides/$', views.all_rides, name='all_rides'),
    #url(r'^ride/searchrides/$', views.search_rides, name='search_rides'),
    url(r'^rideRequest/(\d+)/$', views.ride_request, name='ride_request'),
    url(r'^rideRequest/$', views.create_ride_request,
        name='create_ride_request'),
]
