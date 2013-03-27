from django.conf.urls import patterns, url

urlpatterns = patterns('aas.views',
    url(r'^$', 'index', name='index'),
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