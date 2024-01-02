# from django.conf.urls import patterns, include, url # old django
from django.urls import include, re_path, path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from relevation import settings

admin.autodiscover()

# Examples:
# url(r'^$', 'relevation.views.home', name='home'),
# url(r'^relevation/', include('relevation.foo.urls')),

# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Uncomment the next line to enable the admin:

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^%s' % settings.URL_PREFIX, include('judgementapp.urls')),
]
