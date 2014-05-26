from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import strangers_to_fiction.views as stf
import webcomic_cms.views as cms

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'strangers_to_fiction.views.home', name='home'),
    url(r'^$', stf.home),
    url(r'^about/', stf.about),
    url(r'^archive/', stf.archive),
    url(r'^comic/([0-9]+)/$', stf.comic),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
