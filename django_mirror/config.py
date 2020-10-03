import json

from django.conf import settings


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
        config.update({'read_only': True})
        assert config.to_json() == '{"readOnly": true}'

    [1]: https://codemirror.net/doc/manual.html#config
    """

    def __init__(self):
        """
        Init the config with the default values provided in the settings.
        """
        self.data = {}

        if hasattr(settings, 'DJANGO_MIRROR_DEFAULTS'):
            self.update(settings.DJANGO_MIRROR_DEFAULTS)

    def update(self, more_options):
        """
        Update the config with more options.
        """
        for key, value in more_options.items():
            self.data[snake_to_camel(key)] = value

    def to_json(self):
        """
        Serialise the config so that CodeMirror can consume it.
        """
        return json.dumps(self.data)
