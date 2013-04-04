from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('aas.views',
    url(r'^$', 'index_view', name='index'),

    url(r'^aas/(?P<artist_name>.*?)/$', 'profile', name='profile'),
    url(r'^settings/$', 'settings', name='settings'),

    url(r'^accounts/$', 'accounts_view', name='accounts'),
    url(r'^login/$', 'login_view', name='login'),
    url(r'^login-error/$', 'login_error_view', name='login_error'),
    url(r'^register/$', 'register_view', name='register'),
    url(r'^logout/$', 'logout_view', name='logout'),

    url(r'^artists/$', 'list_artists', name="list_artists"),
    url(r'^artists/add/$', 'add_artist', name="add_artist"),
    url(r'^artists/(?P<artist_id>\d+)/$', 'show_artist', name="show_artist"),
    url(r'^artists/(?P<artist_id>\d+)/albums/$', 'list_albums', name="list_albums"),
    url(r'^artists/(?P<artist_id>\d+)/albums/add/$', 'add_album', name="add_album"),
    url(r'^artists/(?P<artist_id>\d+)/albums/(?P<album_id>\d+)/$', 'show_album', name="show_album"),
    url(r'^artists/(?P<artist_id>\d+)/albums/(?P<album_id>\d+)/songs/$', \
      'list_songs', name="list_songs"),
    url(r'^artists/(?P<artist_id>\d+)/albums/(?P<album_id>\d+)/songs/add/$', \
      'add_song', name="add_song"),
    url(r'^artists/(?P<artist_id>\d+)/albums/(?P<album_id>\d+)/songs/(?P<song_id>\d+)/$', \
      'show_song', name="show_song"),
)

urlpatterns += staticfiles_urlpatterns()
