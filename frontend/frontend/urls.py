from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'frontend.views.index', name="index"),
    url(r'^rides/', 'frontend.views.rides', name="rides"),
    url(r'^ride_detail/(\d+)/',
        'frontend.views.ride_detail', name="ride_detail"),
    url(r'^login/', 'frontend.views.login', name="login"),
    url(r'^logout/', 'frontend.views.logout', name="logout"),
    url(r'^dashboard/', 'frontend.views.dashboard', name="dashboard"),
    url(r'^create_ride/', 'frontend.views.create_ride', name="create_ride"),
    url(r'^create_user/', 'frontend.views.create_user', name="create_user"),
    url(r'^search_results/', 'frontend.views.search_results', name='search_results'),
    url(r'^error/', 'frontend.views.error', name="error"),
]
