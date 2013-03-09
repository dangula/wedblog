from django.conf.urls import patterns, include, url
from registration.views import register

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'finalsite.views.home', name='home'),
    # url(r'^finalsite/', include('finalsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('wedblog.urls')),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'blog/login.html'},
        name="login"),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name="logout"),
    url(r'^register/$',
        register,
        {'backend': 'registration.backends.simple.SimpleBackend', 'success_url':'/'},
        name='registration_register'),
    url(r'', include('registration.auth_urls')),
)
