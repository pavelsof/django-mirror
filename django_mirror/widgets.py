import json

from django import forms
from django.conf import settings


class MirrorArea(forms.Textarea):

    def __init__(self, attrs=None, addons=[], **kwargs):
        """
        Set the config options for the CodeMirror editor.
        """
        options = getattr(settings, 'DJANGO_MIRROR_DEFAULTS', {})
        for key, value in kwargs.items():
            first, *rest = key.split('_')
            key = first + ''.join([x.capitalize() for x in rest])
            options[key] = value

        self.addons = addons
        self.mode = options.get('mode', 'markdown')

        html_attrs = {'data-mirror': json.dumps(options)}
        if attrs:
            html_attrs.update(attrs)

        super().__init__(html_attrs)

    @property
    def media(self):
        """
        Dynamically define the css and js assets needed by the widget.
        """
        css = {
            'all': (
                'django-mirror/codemirror/lib/codemirror.css',
                'django-mirror/django.css',
            )
        }
        js = (
            'django-mirror/codemirror/lib/codemirror.js',
            'django-mirror/codemirror/mode/{m}/{m}.js'.format(m=self.mode),
            *[
                'django-mirror/codemirror/addon/{}.js'.format(addon)
                for addon in self.addons
            ],
            'django-mirror/django.js',
        )
        return forms.Media(css=css, js=js)
