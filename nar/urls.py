from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('social_auth.urls')),
    url(r'^', include('core.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^', include('aas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
