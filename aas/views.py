from django.http import HttpResponse
from django.shortcuts import render_to_response
from aas.models import Artist, Album, Song


def index(request):
    return render_to_response('index.html')


def list_artists(request):
    artists = Artist.objects.all()
    return render_to_response('list_artists.html', {'artists': artists})


def add_artist(request):
    pass


def show_artist(request, artist_id):
    pass


def list_albums(request, artist_id):
    albums = Album.objects.filter(artist_id=artist_id)
    return render_to_response('list_albums.html', {'albums': albums})


def add_album(request, artist_id):
    pass


def show_album(request, artist_id, album_id):
    pass


def list_songs(request, artist_id, album_id):
    songs = Song.objects.filter(album_id=album_id)
    return render_to_response('list_songs.html', {'songs': songs})


def add_song(request, artist_id, album_id):
    pass


def show_song(request, artist_id, album_id, song_id):
    pass
