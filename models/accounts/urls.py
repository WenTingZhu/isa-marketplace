from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    # url(r'^login/$', views.login, name='login'),
    url(r'^user/(\d+)/$', views.user, name='user'),
    url(r'^user/authenticate/$',
        views.authenticate_user, name='authenticate_user'),
    url(r'^user/$', views.create_user, name='create_user'),
    url(r'^user/delete/(\d+)/$', views.delete_user, name='delete_user'),
    url(r'^user/(\d+)/rides/$', views.user_rides, name='user_rides'),


]
