# core/views.py
from django.views.generic import FormView, ListView, TemplateView

from music.models import Album, Song
from profiles.models import Artist
from .forms import ContactForm

class AboutView(TemplateView):
    template_name = "core/about.html"


class ThanksView(TemplateView):
    template_name = "core/thanks.html"


class ContactView(FormView):
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # form.send_email()
        return super(ContactView, self).form_valid(form)


class SearchView(ListView):
    template_name = "core/search.html"
    queryset = Artist.objects.none()

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        q = self.request.GET.get('q')
        context["artist_list"] = Artist.objects.filter(profile__username__icontains=q)
        context["album_list"] = Album.objects.filter(name__icontains=q)
        context["song_list"] = Song.objects.filter(name__icontains=q)
        return context