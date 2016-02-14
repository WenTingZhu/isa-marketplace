from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'rideshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'accounts.views.home', name='home'),
    url(r'^api/v1/accounts/', include('accounts.urls', namespace='accounts'), name='accounts'),
    url(r'^api/v1/rides/', include('ride.urls', namespace='rides'), name='rides'),
]
