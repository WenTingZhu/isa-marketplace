from django.conf.urls import include, url
from django.contrib import admin
import connector

urlpatterns = [
    # Examples:
    # url(r'^$', 'experience.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/$', 'connector.views.home', name='home'),
    url(r'^authenticate_user/$',
        'connector.views.authenticate_user', name='authenticate_user'),
    url(r'^user_rides/(\d+)/$',
        'connector.views.user_rides', name='user_rides'),
    url(r'^all_rides/$',
        'connector.views.all_rides', name='all_rides'),
    url(r'^get_ride/(\d+)/$', 'connector.views.get_ride', name='get_ride'),
    url(r'^create_ride/$', 'connector.views.create_ride', name='create_ride'),
    url(r'^create_account/$',
        'connector.views.create_account', name='create_account'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user_detail/(\d+)/$', 'connector.views.user_detail', name='user_detail'),
]
