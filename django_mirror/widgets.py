from django import forms

from django_mirror.config import Config


class MirrorArea(forms.Textarea):

    def __init__(self, attrs=None, addons=[], **kwargs):
        """
        Set the config options for the CodeMirror editor.
        """
        config = Config()
        config.update(kwargs)

        self.addons = addons
        self.mode = config.data.get('mode', 'markdown')

        html_attrs = {'data-mirror': config.to_json()}
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
