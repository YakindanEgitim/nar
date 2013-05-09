# music/views.py
import logging

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView
from django.utils.text import slugify
from django.utils.translation import ugettext as _

from braces.views import LoginRequiredMixin

from core.mixins import ActionMixin
from profiles.models import Artist
from .models import Album, Song
from .forms import *

logger = logging.getLogger(__name__)


class ArtistDetailView(DetailView):
    model = Artist
    template_name = "music/artist_detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Artist, profile__username=self.kwargs.get("username"))


class ArtistUpdateView(LoginRequiredMixin, ActionMixin, UpdateView):
    model = Artist
    template_name = "music/artist_edit.html"
    action = _("Artist is successfully updated")

    def get_object(self, queryset=None):
        return get_object_or_404(Artist, profile__username=self.kwargs.get("username"))

    def get_success_url(self):
        return reverse('artist_detail', kwargs=self.kwargs)


class ArtistCreateView(LoginRequiredMixin, ActionMixin, CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'music/artist_add.html'
    action = _("Artist is successfully added")

    def get_success_url(self):
        return reverse('artist_detail', kwargs={"username": self.object.profile.username})


class AlbumCreateView(LoginRequiredMixin, ActionMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'music/album_add.html'
    action = _("Album is successfully added")

    def form_valid(self, form):
        print "\nFORM VALID\n"
        context = self.get_context_data()
        albumsong_form = context['albumsong_formset']
        if albumsong_form.is_valid():
            self.object = form.save(commit=False)
            self.object.artist = Artist.objects.get(profile__username__exact=self.kwargs.get("username"))
            self.object.slug = slugify(self.object.name)
            self.object.save()
            for song_form in albumsong_form:
                song = song_form.save(commit=False)
                song.slug = slugify(song.name)
                song.album = self.object
                song.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        print "\nFORM INVALID\n"
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(AlbumCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['albumsong_formset'] = AlbumSongFormSet(self.request.POST)
        else:
            context['albumsong_formset'] = AlbumSongFormSet()
        return context

    def get_success_url(self):
        return reverse('artist_detail', kwargs=self.kwargs)


class AlbumDetailView(DetailView):
    model = Album
    template_name = "music/album_detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Album,
                                 slug=self.kwargs.get("album"),
                                 artist__profile__username=self.kwargs.get("username"))


class AlbumUpdateView(LoginRequiredMixin, ActionMixin, UpdateView):
    model = Album
    template_name = "music/album_edit.html"
    action = _("Album is successfully updated")

    def get_object(self, queryset=None):
        return get_object_or_404(Album,
                                 slug=self.kwargs.get("album"),
                                 artist__profile__username=self.kwargs.get("username"))

    def get_success_url(self):
        return reverse('album_detail', self.kwargs)


class SongCreateView(CreateView):
    model = Song
    form_class = SongForm
    template_name = 'music/song_add.html'
    action = _("Song is successfully added")


class SongDetailView(DetailView):
    model = Song
    template_name = "music/song_detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Song,
                                 slug=self.kwargs.get("song"),
                                 album__slug=self.kwargs.get("album"),
                                 album__artist__profile__username=self.kwargs.get("username"))


class SongUpdateView(LoginRequiredMixin, ActionMixin, UpdateView):
    model = Song
    template_name = "music/song_edit.html"
    action = _("Song is successfully updated")

    def get_object(self, queryset=None):
        return get_object_or_404(Song,
                                 slug=self.kwargs.get("song"),
                                 album__slug=self.kwargs.get("album"),
                                 album__artist__profile__username=self.kwargs.get("username"))

    def get_success_url(self):
        return reverse('song_detail', self.kwargs)
