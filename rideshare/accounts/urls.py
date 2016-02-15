from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    # url(r'^login/$', views.login, name='login'),
    url(r'^user/$', views.create_user, name='create_user'),
    url(r'^user/(\d+)/$', views.user, name='user'),
<<<<<<< HEAD
    url(r'^user/(\d+)/ride/$', views.create_ride, name='create_ride'),

=======
>>>>>>> 092b3854ab1fda2aa4ee5b41dbb2796c1f32fcb4
]
