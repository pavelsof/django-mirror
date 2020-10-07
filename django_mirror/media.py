import json
import os.path

from django.forms.widgets import Media


MEDIA_PATHS = {}

with open(os.path.join(os.path.dirname(__file__), 'media.json')) as f:
    MEDIA_PATHS = json.load(f)


def _follow(path):
    """
    Recursively gather the list of paths required by the given path.
    """
    reqs = []
    if path in MEDIA_PATHS:
        for another in MEDIA_PATHS[path]:
            reqs += _follow(another)
    return reqs + [path]


def _make(path):
    """
    Init a media instance for the given path.
    """
    css, js = [], []

    for req in _follow(path):
        req = os.path.join('django-mirror/codemirror', req)

        if req.endswith('.css'):
            css.append(req)
        elif req.endswith('.js'):
            js.append(req)

    return Media(css={'all': css}, js=js)


def get_mode_media(mode):
    """
    Return a media instance pointing to the css and js files required by the
    given mode.
    """
    path = 'mode/{}/{}.js'.format(mode, mode)
    return _make(path)


def get_addon_media(addon):
    """
    Return a media instance pointing to the css and js files required by the
    given addon.
    """
    path = 'addon/{}'.format(addon if addon.endswith('.js') else addon+'.js')
    return _make(path)
