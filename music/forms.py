# music/forms.py
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from profiles.models import Artist
from .models import Album, Song


class ArtistForm(ModelForm):
    class Meta:
        model = Artist


class AlbumForm(ModelForm):
    class Meta:
        model = Album


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ('name', 'lyrics', 'genres',)

ArtistAlbumFormSet = inlineformset_factory(Artist, Album, form=ArtistForm, extra=1)
AlbumSongFormSet = inlineformset_factory(Album, Song, form=AlbumForm, extra=1)
