from django.conf.urls import patterns, include, url
from blogapp.views import hello, current

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^current/$', current),
    url(r'^polls/', include('polls.urls')),

)
