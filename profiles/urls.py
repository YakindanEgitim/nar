# profiles/urls.py
from django.conf.urls import patterns, url

from .views import ProfileDetailView, ProfileListView, ProfileUpdateView

urlpatterns = patterns('',
    url(r'^edit/$', ProfileUpdateView.as_view(), name='profile_edit'),
    url(r'^search/$', ProfileListView.as_view(), name='profile_search'),
    url(r'^(?P<username>[-_\.\w]+)/$', ProfileDetailView.as_view(), name='profile_detail'),
    url(r'^$', ProfileDetailView.as_view(), name='profile_detail'),
)
