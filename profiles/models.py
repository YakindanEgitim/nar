# profiles/models.py
import os

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models import AbstractTimeStampedModel
from nar.settings.base import MEDIA_ROOT


def get_default_avatar_path():
    return 'avatars/default.jpg'


def get_upload_path(instance, filename):
    """Finds where to save avatar and overrides if exists
       TODO: Better handling is needed for different storages
    """
    rel_path = "avatars/{0}".format(instance.username)
    abs_path = os.path.join(MEDIA_ROOT, rel_path)
    if os.path.exists(abs_path):
        os.remove(abs_path)
    return rel_path


class Profile(AbstractUser, AbstractTimeStampedModel):
    avatar = models.ImageField(upload_to=get_upload_path, blank=True)

    def is_artist(self):
        try:
            return self.artist
        except ObjectDoesNotExist:
            return None


class Artist(AbstractTimeStampedModel):
    profile = models.OneToOneField(Profile, primary_key=True)
    bio = models.TextField(default=_(""))
    genres = models.ManyToManyField('music.Genre')
    following = models.ManyToManyField('self')


class MusicGroup(AbstractTimeStampedModel):
    members = models.ManyToManyField(Artist)
    genres = models.ManyToManyField('music.Genre')
