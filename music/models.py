# music/models.py
from django.db import models
from django.contrib.auth import get_user_model

from core.models import AbstractTimeStampedModel


class Genre(AbstractTimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField()


class Album(AbstractTimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    genres = models.ManyToManyField(Genre)
    artist = models.ForeignKey('profiles.Artist')
    groups = models.ForeignKey('profiles.MusicGroup')


class Song(AbstractTimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    lyrics = models.TextField()
    genres = models.ManyToManyField(Genre)
    album = models.ForeignKey(Album)
