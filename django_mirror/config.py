from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def snake_to_camel(snake):
    """
    Convert a string from snake_case to camelCase.
    """
    first, *rest = snake.split('_')
    return first + ''.join(word.capitalize() for word in rest)


class Config:
    """
    A config instance represents a CodeMirror configuration [1]. Usage:

        config = Config()
        config.update(read_only=True, addons=['dialog/dialog'])
        assert config.options == {'readOnly': True}
        assert config.addons == ['dialog/dialog.js']

    [1]: https://codemirror.net/doc/manual.html#config
    """

    def __init__(self):
        """
        Init the config with the default values provided in the settings.
        """
        self.options = {}
        self.addons = []

        if hasattr(settings, 'DJANGO_MIRROR_DEFAULTS'):
            try:
                self.update(**settings.DJANGO_MIRROR_DEFAULTS)
            except TypeError:
                message = 'DJANGO_MIRROR_DEFAULTS should be a dict.'
                raise ImproperlyConfigured(message)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'addons':
                self.set_addons(value)
            else:
                self.options[snake_to_camel(key)] = value

    def set_addons(self, addons):
        self.addons = [
            addon if addon.endswith('.js') else addon + '.js'
            for addon in addons
        ]
