# profiles/pipelines.py
import os
from urllib import urlretrieve

from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.twitter import TwitterBackend

from nar.settings.base import MEDIA_ROOT
from .models import get_upload_path


def get_user_avatar(backend, details, response, social_user, uid,
                    user, *args, **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
    elif backend.__class__ == TwitterBackend:
        url = response.get('profile_image_url', '').replace('_normal', '')

    if url:
        filepath = get_upload_path(user, None)
        urlretrieve(url, os.path.join(MEDIA_ROOT, filepath))
        user.avatar = filepath
        user.save()
