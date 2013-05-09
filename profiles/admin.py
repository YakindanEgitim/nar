from django.contrib import admin

from .models import Artist, Profile, MusicGroup

admin.site.register(Artist)
admin.site.register(Profile)
admin.site.register(MusicGroup)
