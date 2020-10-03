from django.test import TestCase, override_settings
from django.utils.html import format_html

from django_mirror.widgets import MirrorArea


class MirrorAreaTestCase(TestCase):

    def assert_data_mirror(self, widget, json):
        """
        Assert that the widget renders a textarea with a data-mirror attribute
        containing the given JSON.
        """
        template = (
            '<textarea name="name" cols="40" rows="10" data-mirror="{}">'
            'value'
            '</textarea>'
        )
        self.assertHTMLEqual(
            widget.render('name', 'value'),
            format_html(template, json)
        )

    def test_no_config(self):
        """
        The widget should render an empty data-mirror object if there is no
        config provided.
        """
        widget = MirrorArea()
        self.assert_data_mirror(widget, '{}')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'tabSize': 8})
    def test_default_config(self):
        """
        The widget should render a data-mirror object containing the default
        config if there are no init kwargs provided.
        """
        widget = MirrorArea()
        self.assert_data_mirror(widget, '{"tabSize": 8}')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'tab_size': 8})
    def test_default_config_snake_case(self):
        """
        The widget should render a data-mirror object with the default config
        in camelCase even if it is given in snake_case.
        """
        widget = MirrorArea()
        self.assert_data_mirror(widget, '{"tabSize": 8}')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'tabSize': 8})
    def test_override_default_config(self):
        """
        The widget should render a data-mirror object with the config provided
        as init kwargs when these override the default config.
        """
        widget = MirrorArea(tabSize=4)
        self.assert_data_mirror(widget, '{"tabSize": 4}')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'tabSize': 8})
    def test_override_default_config_snake_case(self):
        """
        The widget should render a data-mirror object with the config provided
        as init kwargs even if these are given in snake_case.
        """
        widget = MirrorArea(tab_size=4)
        self.assert_data_mirror(widget, '{"tabSize": 4}')
