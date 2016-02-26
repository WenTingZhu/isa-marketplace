from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'experience.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^connector/', include('connector.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
