import os.path

from django.utils.html import format_html


class WidgetAssertions:

    def assert_textarea(self, widget, json):
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

    def assert_css(self, widget, path):
        """
        Assert that the widget renders a <link> pointing to the given path.
        """
        path = os.path.join('django-mirror', path)
        link_html = (
            '<link href="{}" type="text/css" media="all" rel="stylesheet">'
        )
        self.assertInHTML(link_html.format(path), str(widget.media))

    def assert_js(self, widget, path):
        """
        Assert that the widget renders a <script> pointing to the given path.
        """
        path = os.path.join('django-mirror', path)
        script_html = '<script src="{}"  type="text/javascript"></script>'
        self.assertInHTML(script_html.format(path), str(widget.media))
