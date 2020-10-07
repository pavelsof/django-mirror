import json

from django import forms

from django_mirror.config import Config
from django_mirror.media import get_addon_media, get_mode_media


class MirrorArea(forms.Textarea):

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
            media += get_mode_media(self.config.options['mode'])

        for addon in self.config.addons:
            media += get_addon_media(addon)

        media += forms.Media(
            css={
                'all': ['django-mirror/django.css']
            },
            js=['django-mirror/django.js']
        )

        return media
