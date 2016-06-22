from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from anved.views import add, start, catalog, soft_toys, games, cart, toy, account_logout, home, account_profile, paypal_pay, paypal_success
import social.apps.django_app.urls
import paypal.standard.ipn.urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include(social.apps.django_app.urls, namespace='social')),
    url(r'^add-to-cart/$', add, name='add'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', start),
    url(r'^(?P<number>[0-9]+)/', toy),
    url(r'^catalog/', catalog),
    url(r'^soft_toys/', soft_toys),
    url(r'^games/', games),
    url(r'^cart/', cart),
    url(r'^accounts/logout/$', account_logout, name='logout'),
    url(r'^accounts/login/$', home, name='login'),
    url(r'^accounts/profile/$', account_profile, name='profile'),
    url(r'^payment/cart/$', paypal_pay, name='cart'),
    url(r'^payment/success/$', paypal_success, name='success'),
    url(r'^paypal/', include(paypal.standard.ipn.urls)),
]
