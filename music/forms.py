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

# currently put default to extras but eventual values need to be defined later
ArtistAlbumFormSet = inlineformset_factory(ArtistForm, Album, extra=50)
AlbumSongFormSet = inlineformset_factory(AlbumForm, Song, extra=20)
