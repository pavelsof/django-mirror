import json
import os.path

from django.forms.widgets import Media


PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
CODEMIRROR_DIR = os.path.join(PACKAGE_DIR, 'static/django-mirror/codemirror')


MEDIA_PATHS = {}
with open(os.path.join(PACKAGE_DIR, 'media.json')) as f:
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
    given mode. Raise an error if the mode cannot be recognised.
    """
    path = 'mode/{}/{}.js'.format(mode, mode)

    if path not in MEDIA_PATHS:
        raise ValueError('Unknown mode: {!s}'.format(mode))

    return _make(path)


def get_addon_media(addon):
    """
    Return a media instance pointing to the css and js files required by the
    given addon. Raise an error if the mode cannot be recognised.
    """
    path = 'addon/{}'.format(addon if addon.endswith('.js') else addon+'.js')

    if path not in MEDIA_PATHS:
        raise ValueError('Unknown addon: {!s}'.format(addon))

    return _make(path)


def get_theme_media(theme):
    """
    Return a media instance pointing to the css file of the requested theme.
    Raise an error if the theme cannot be recognised.
    """
    path = 'theme/{}.css'.format(theme)

    if not os.path.exists(os.path.join(CODEMIRROR_DIR, path)):
        raise ValueError('Unknown theme: {!s}'.format(theme))

    path = os.path.join('django-mirror/codemirror', path)

    return Media(css={'all': [path]})
