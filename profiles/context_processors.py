from .models import get_default_avatar_path


def default_avatar(request):
    return {'DEFAULT_AVATAR': get_default_avatar_path()}
