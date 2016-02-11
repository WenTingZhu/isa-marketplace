from django.conf.urls import include, url
from django.contrib import admin
from accounts import views as accounts_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'rideshare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'accounts.views.home', name='home')
    url(r'^accounts/', include('accounts.urls', namespace='accounts'), name='accounts'),
]
