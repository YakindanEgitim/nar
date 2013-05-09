# music/models.py
from django.db import models
from django.contrib.auth import get_user_model

from core.models import AbstractTimeStampedModel


class Genre(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name,)


class Album(AbstractTimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    genres = models.ManyToManyField(Genre, blank=True, null=True)
    artist = models.ForeignKey('profiles.Artist', blank=True, null=True)
    groups = models.ForeignKey('profiles.MusicGroup', blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name,)


class Song(AbstractTimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    lyrics = models.TextField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True, null=True)
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return u'%s' % (self.name,)
