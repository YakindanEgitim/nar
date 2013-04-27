# music/views.py
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.utils.translation import ugettext as _

from braces.views import LoginRequiredMixin

from core.mixins import ActionMixin
from .models import Album, Song
from .forms import AlbumForm, AlbumSongFormSet


class AlbumCreateView(LoginRequiredMixin, ActionMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'music/album_add.html'
    action = _("Album is successfully created")

    def form_valid(self, form):
        context = self.get_context_data()
        albumsong_form = context['albumsong_formset']
        if albumsong_form.is_valid():
            self.object = form.save()
            albumsong_form.instance = self.object
            albumsong_form.save()
            return HttpResponseRedirect(self.get_success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(AlbumCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['albumsong_form'] = AlbumSongFormSet(self.request.POST)
        else:
            context['albumsong_form'] = AlbumSongFormSet()
        return context

    def get_success_url(self):
        return reverse('artist_detail', self.request.user.username)


class AlbumDetailView(DetailView):
    model = Album
    template_name = "music/album_detail.html"

    def get_object(self, queryset=None):
        pass


class AlbumUpdateView(LoginRequiredMixin, ActionMixin, UpdateView):
    model = Album
    template_name = "music/album_edit.html"
    action = _("Album is successfully updated")

    def get_object(self, queryset=None):
        pass

    def get_success_url(self):
        pass


class SongDetailView(DetailView):
    model = Song
    template_name = "music/song_detail.html"

    def get_object(self, queryset=None):
        pass


class SongUpdateView(LoginRequiredMixin, ActionMixin, UpdateView):
    model = Song
    template_name = "music/song_edit.html"
    action = _("Song is successfully updated")

    def get_object(self, queryset=None):
        pass

    def get_success_url(self):
        pass
