from django import forms


class MirrorArea(forms.Textarea):

    def __init__(self, attrs=None, mode='markdown', addons=[]):
        default_attrs = {'data-mirror': mode}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

        self.mode = mode
        self.addons = addons

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
            'django-mirror/codemirror/mode/{m}/{m}.js'.format(m=self.mode),
            *[
                'django-mirror/codemirror/addon/{}.js'.format(addon)
                for addon in self.addons
            ],
            'django-mirror/django.js',
        )
        return forms.Media(css=css, js=js)
