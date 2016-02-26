from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'frontend.views.index', name="index"),
    url(r'^login/', 'frontend.views.login', name="login"),
]
