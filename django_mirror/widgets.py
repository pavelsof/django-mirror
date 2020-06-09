from django import forms


class MirrorArea(forms.Textarea):

    def __init__(self, attrs=None, mode='markdown'):
        default_attrs = {'class': 'django-mirror-area'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
        self.mode = mode

    @property
    def media(self):
        css = {
            'all': (
                'django-mirror/codemirror/lib/codemirror.css',
                'django-mirror/django.css',
            )
        }
        js = (
            'django-mirror/codemirror/lib/codemirror.js',
            'django-mirror/codemirror/mode/markdown/markdown.js',
            'django-mirror/django.js',
        )
        return forms.Media(css=css, js=js)
