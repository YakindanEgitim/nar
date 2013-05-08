from django.conf.urls import patterns, url

from .views import AboutView, ContactView, SearchView, ThanksView

urlpatterns = patterns('',
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
    url(r'^search/$', SearchView.as_view(), name='search'),
)
