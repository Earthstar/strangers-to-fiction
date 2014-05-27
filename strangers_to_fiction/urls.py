from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
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
    # Comic api: can index number, or go to first or last comic
    url(r'^comic/([0-9]+)/$', stf.comic),
    url(r'^comic/first/$', stf.first_comic),
    url(r'^comic/last/$', stf.last_comic),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
