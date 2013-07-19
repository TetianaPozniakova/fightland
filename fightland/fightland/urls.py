from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from infoportal.views import *
admin.autodiscover()
import os

media = os.path.join(os.path.dirname(__file__), 'media')

from sitemap import SitemapForum, SitemapTopic
from forms import RegistrationFormUtfUsername
from djangobb_forum import settings as forum_settings

sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}

urlpatterns = patterns('',
    (r'^', include('infoportal.urls')),
    (r'^news/', include('easy_news.urls')),
    (r'^gallery/', include('fightlandgallery.urls')),
    (r'^video/$', video_list),

    # static content
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': media}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Sitemap
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Apps
    (r'^forum/account/', include('django_authopenid.urls')),
    (r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
)

# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('django_messages.urls')),
   )

if (settings.DEBUG):
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
