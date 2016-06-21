from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from anved.views import add, start, catalog, soft_toys, games, cart, toy1, toy2, toy3, toy4, toy5, toy6, toy7, toy8, toy9, toy10, toy11, toy12, account_logout, home, account_profile
import social.apps.django_app.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include(social.apps.django_app.urls, namespace='social')),
    url(r'^add-to-cart/$', add, name='add'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', start),
    url(r'^1/', toy1),
    url(r'^2/', toy2),
    url(r'^3/', toy3),
    url(r'^4/', toy4),
    url(r'^5/', toy5),
    url(r'^6/', toy6),
    url(r'^7/', toy7),
    url(r'^8/', toy8),
    url(r'^9/', toy9),
    url(r'^10/', toy10),
    url(r'^11/', toy11),
    url(r'^12/', toy12),
    url(r'^catalog/', catalog),
    url(r'^soft_toys/', soft_toys),
    url(r'^games/', games),
    url(r'^cart/', cart),
    url(r'^accounts/logout/$', account_logout, name='logout'),
    url(r'^accounts/login/$', home, name='login'),
    url(r'^accounts/profile/$', account_profile, name='profile'),
]
