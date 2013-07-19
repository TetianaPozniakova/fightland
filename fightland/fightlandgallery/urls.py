from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'fightlandgallery.views.gallery'),
    url(r'^album/(?P<album_id>\d+)/$', 'fightlandgallery.views.album_list'),
)
