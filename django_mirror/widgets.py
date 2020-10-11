import json
import logging

from django import forms

from django_mirror.config import Config
from django_mirror.media import (
    get_addon_media, get_mode_media, get_theme_media
)


logger = logging.getLogger(__name__)


class MirrorArea(forms.Textarea):
    """
    Form widget that renders as a standard <textarea> but also includes the
    relevant static files that convert it into a CodeMirror editor.
    """

    def __init__(self, attrs=None, addons=[], **kwargs):
        """
        Set the config options for the CodeMirror editor.
        """
        self.config = Config()
        self.config.update(**kwargs)

        if addons:
            self.config.set_addons(addons)

        if not attrs:
            attrs = {}
        attrs['data-mirror'] = json.dumps(self.config.options)

        super().__init__(attrs)

    @property
    def media(self):
        """
        Dynamically define the css and js assets needed by the widget.
        """
        media = forms.Media(
            css={
                'all': ['django-mirror/codemirror/lib/codemirror.css']
            },
            js=['django-mirror/codemirror/lib/codemirror.js']
        )

        if 'mode' in self.config.options:
            try:
                media += get_mode_media(self.config.options['mode'])
            except ValueError as error:
                logger.error(str(error))

        if 'theme' in self.config.options:
            try:
                media += get_theme_media(self.config.options['theme'])
            except ValueError as error:
                logger.error(str(error))

        for addon in self.config.addons:
            try:
                media += get_addon_media(addon)
            except ValueError as error:
                logger.error(str(error))

        media += forms.Media(js=['django-mirror/init.js'])

        return media
