# profiles/views.py
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, DetailView, ListView
from django.utils.translation import ugettext as _

from braces.views import LoginRequiredMixin

from core.mixins import ActionMixin, SearchMixin
from .models import Profile
from .forms import ProfileUpdateForm


class ProfileUpdateView(LoginRequiredMixin, ActionMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profiles/profile_edit.html'  # better naming than profile_form
    action = _("Profile is successfully updated")

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profile_detail')


class ProfileDetailView(DetailView):
    model = Profile

    def get_object(self, queryset=None):
        """There are two ways to be called `profile/` or `profile/{username}`"""
        if "username" in self.kwargs:
            try:
                return Profile.objects.get(username=self.kwargs["username"])
            except:
                pass
        else:
            if hasattr(self.request, "user"):
                return self.request.user
            else:
                """Anonymous user must be handled
                   May be redirected to `accounts/`
                """
                pass

    def is_request_user(self):
        try:
            return self.object == self.request.user
        except:
            return False

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        # context['default_avatar'] = get_default_avatar_path() # done via context processors
        context['editable'] = self.is_request_user()
        return context


class ProfileListView(SearchMixin, ListView):
    model = Profile
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        context['t'] = self.request.GET.get('t')
        return context
