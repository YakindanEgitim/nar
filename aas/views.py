from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.forms.util import ErrorList
from aas.models import Artist, Album, Song
from aas.forms import LoginForm, RegistrationForm


def index_view(request):
    if request.user.is_authenticated():
        return render_to_response('home.html', {}, RequestContext(request))
    else:
        return render_to_response('tour.html')


def accounts_view(request, login_form=LoginForm(), registration_form=RegistrationForm()):
    context = {'login_form': login_form, 'registration_form': registration_form}
    return render_to_response('accounts.html', context, RequestContext(request))


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    # User isn't active
                    pass
            else:
                form._errors["password"] = ErrorList([u"Username and password don't match"])
                return accounts_view(request, login_form=form)
        else:
            return accounts_view(request, login_form=form)
    else:
        return accounts_view(request)


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], password=cd['password'], first_name=cd['first_name'], last_name=cd['last_name'], email=cd['email'])
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponseRedirect(reverse('index'), RequestContext(request))
        else:
            return accounts_view(request, registration_form=form)
    else:
        return accounts_view(request)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'), RequestContext(request))


def login_error_view(request):
    pass

def profile(request, artist_name):
    return render_to_response('profile.html', {}, RequestContext(request))

def settings(request):
    pass

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
