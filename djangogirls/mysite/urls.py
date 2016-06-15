from django.conf.urls import include, url
from django.contrib import admin
from anved.views import start, catalog, soft_toys, cart, toy

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', start),
    url(r'^catalog/', catalog),
    url(r'^soft_toys/', soft_toys),
    url(r'^cart/', cart),
    url(r'^toy/', toy),
]
