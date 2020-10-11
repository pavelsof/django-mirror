from django.test import TestCase, override_settings
from django_mirror.widgets import MirrorArea

from tests.mixins import WidgetAssertions


class MirrorAreaTestCase(WidgetAssertions, TestCase):

    def test_no_config(self):
        """
        The widget should render an empty data-mirror object if there is no
        config provided.
        """
        widget = MirrorArea()
        self.assert_textarea(widget, '{}')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'tabSize': 8})
    def test_default_config(self):
        """
        The widget should render a data-mirror object containing the default
        config if there are no init kwargs provided.
        """
        widget = MirrorArea()
        self.assert_textarea(widget, '{"tabSize": 8}')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'tab_size': 8})
    def test_default_config_snake_case(self):
        """
        The widget should render a data-mirror object with the default config
        in camelCase even if it is given in snake_case.
        """
        widget = MirrorArea()
        self.assert_textarea(widget, '{"tabSize": 8}')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'tabSize': 8})
    def test_override_default_config(self):
        """
        The widget should render a data-mirror object with the config provided
        as init kwargs when these override the default config.
        """
        widget = MirrorArea(tabSize=4)
        self.assert_textarea(widget, '{"tabSize": 4}')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'tabSize': 8})
    def test_override_default_config_snake_case(self):
        """
        The widget should render a data-mirror object with the config provided
        as init kwargs even if these are given in snake_case.
        """
        widget = MirrorArea(tab_size=4)
        self.assert_textarea(widget, '{"tabSize": 4}')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'mode': 'python'})
    def test_default_mode(self):
        """
        The widget should include the media files of the mode specified in the
        default config.
        """
        widget = MirrorArea()
        self.assert_css(widget, 'codemirror/lib/codemirror.css')
        self.assert_js(widget, 'codemirror/lib/codemirror.js')
        self.assert_js(widget, 'codemirror/mode/python/python.js')
        self.assert_js(widget, 'django.js')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'mode': 'python'})
    def test_override_mode(self):
        """
        The widget should include the media files of the mode provided as an
        init kwarg when this overrides the default config.
        """
        widget = MirrorArea(mode='erlang')
        self.assertTrue('python' not in str(widget.media))
        self.assert_css(widget, 'codemirror/lib/codemirror.css')
        self.assert_js(widget, 'codemirror/lib/codemirror.js')
        self.assert_js(widget, 'codemirror/mode/erlang/erlang.js')
        self.assert_js(widget, 'django.js')

    def test_mode_addons(self):
        """
        The widget should include the media files of the addons (and further
        modes) required by the given mode.
        """
        widget = MirrorArea(mode='rst')
        self.assert_css(widget, 'codemirror/lib/codemirror.css')
        self.assert_js(widget, 'codemirror/lib/codemirror.js')
        self.assert_js(widget, 'codemirror/mode/rst/rst.js')
        self.assert_js(widget, 'codemirror/mode/python/python.js')
        self.assert_js(widget, 'codemirror/mode/stex/stex.js')
        self.assert_js(widget, 'codemirror/addon/mode/overlay.js')
        self.assert_js(widget, 'django.js')

    def test_unknown_mode(self):
        """
        The widget should not include non-existing media files when inited with
        an unrecognised mode.
        """
        widget = MirrorArea(mode='mumbo-jumbo')
        with self.assertLogs(level='ERROR'):
            self.assertTrue('mumbo-jumbo' not in str(widget.media))
            self.assert_css(widget, 'codemirror/lib/codemirror.css')
            self.assert_js(widget, 'codemirror/lib/codemirror.js')
            self.assert_js(widget, 'django.js')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'addons': ['dialog/dialog']})
    def test_default_addons(self):
        """
        The widget should include the media files of the addons specified in
        the default config.
        """
        widget = MirrorArea()
        self.assert_css(widget, 'codemirror/lib/codemirror.css')
        self.assert_css(widget, 'codemirror/addon/dialog/dialog.css')
        self.assert_js(widget, 'codemirror/lib/codemirror.js')
        self.assert_js(widget, 'codemirror/addon/dialog/dialog.js')
        self.assert_js(widget, 'django.js')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'addons': ['dialog/dialog']})
    def test_override_addons(self):
        """
        The widget should include the media files of the addons provided in the
        init kwargs when these override the default config.
        """
        widget = MirrorArea(addons=['wrap/hardwrap'])
        self.assertTrue('dialog.css' not in str(widget.media))
        self.assertTrue('dialog.js' not in str(widget.media))
        self.assert_css(widget, 'codemirror/lib/codemirror.css')
        self.assert_js(widget, 'codemirror/lib/codemirror.js')
        self.assert_js(widget, 'codemirror/addon/wrap/hardwrap.js')
        self.assert_js(widget, 'django.js')

    def test_addon_modes(self):
        """
        The widget should include the media files of the modes (and other
        addons) required by the given addons.
        """
        widget = MirrorArea(addons=['hint/sql-hint'])
        self.assert_css(widget, 'codemirror/lib/codemirror.css')
        self.assert_js(widget, 'codemirror/lib/codemirror.js')
        self.assert_js(widget, 'codemirror/addon/hint/sql-hint.js')
        self.assert_js(widget, 'codemirror/mode/sql/sql.js')
        self.assert_js(widget, 'django.js')

    def test_unknown_addon(self):
        """
        The widget should not include non-existing media files when inited with
        an unrecognised addon.
        """
        widget = MirrorArea(addons=['mumbo-jumbo'])
        with self.assertLogs(level='ERROR'):
            self.assertTrue('mumbo-jumbo' not in str(widget.media))
            self.assert_css(widget, 'codemirror/lib/codemirror.css')
            self.assert_js(widget, 'codemirror/lib/codemirror.js')
            self.assert_js(widget, 'django.js')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'theme': 'yeti'})
    def test_default_theme(self):
        """
        The widget should include the css file of the theme specified in the
        default config.
        """
        widget = MirrorArea()
        self.assert_css(widget, 'codemirror/lib/codemirror.css')
        self.assert_css(widget, 'codemirror/theme/yeti.css')
        self.assert_js(widget, 'codemirror/lib/codemirror.js')
        self.assert_js(widget, 'django.js')

    @override_settings(DJANGO_MIRROR_DEFAULTS={'theme': 'yeti.css'})
    def test_override_theme(self):
        """
        The widget should include the css file of the theme specified as an
        init kwarg when this overrides the default config.
        """
        widget = MirrorArea(theme='nord')
        self.assertTrue('yeti' not in str(widget.media))
        self.assert_css(widget, 'codemirror/lib/codemirror.css')
        self.assert_css(widget, 'codemirror/theme/nord.css')
        self.assert_js(widget, 'codemirror/lib/codemirror.js')
        self.assert_js(widget, 'django.js')

    def test_unknown_theme(self):
        """
        The widget should not include non-existing media files when inited with
        an unrecognised theme.
        """
        widget = MirrorArea(theme='mumbo-jumbo')
        with self.assertLogs(level='ERROR'):
            self.assertTrue('mumbo-jumbo' not in str(widget.media))
            self.assert_css(widget, 'codemirror/lib/codemirror.css')
            self.assert_js(widget, 'codemirror/lib/codemirror.js')
            self.assert_js(widget, 'django.js')
