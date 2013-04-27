# music/urls.py
from django.conf.urls import patterns, url

from .views import ArtistDetailView, ArtistUpdateView
from .views import AlbumDetailView, AlbumUpdateView
from .views import SongDetailView, SongUpdateView

urlpatterns = patterns('',
    url(r'^(?P<username>[-_\.\w]+)/$',
        ArtistDetailView.as_view(), name="artist_detail"),
    url(r'^(?P<username>[-_\.\w]+)/edit/$',
        ArtistUpdateView.as_view(), name="artist_edit"),
    url(r'^(?P<username>[-_\.\w]+)/(?P<album>[-_\w]+)/$',
        AlbumDetailView.as_view(), name="album_detail"),
    url(r'^(?P<username>[-_\.\w]+)/(?P<album>[-_\w]+)/edit$',
        AlbumUpdateView.as_view(), name="album_edit"),
    url(r'^(?P<username>[-_\.\w]+)/(?P<album>[-_\w]+)/(?P<song>[-_\w]+)/$',
        SongDetailView.as_view(), name="song_detail"),
    url(r'^(?P<username>[-_\.\w]+)/(?P<album>[-_\w]+)/(?P<song>[-_\w]+)/edit$',
        SongUpdateView.as_view(), name="song_edit"),
)
