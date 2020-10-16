from unittest.mock import Mock

from django.contrib import admin
from django.test import TestCase
from django_mirror.admin import MirrorAdmin

from tests.mixins import WidgetAssertions
from tests.models import Echo, EchoReply


class MirrorAdminTestCase(WidgetAssertions, TestCase):

    def setUp(self):
        self.admin_site = admin.AdminSite()

    def get_form_instance(self, echo_admin_class):
        """
        Init and return an instance of the form of the given EchoAdmin class.
        """
        echo_admin = echo_admin_class(Echo, self.admin_site)
        echo_form_class = echo_admin.get_form(Mock())
        return echo_form_class()

    def test_simple_list(self):
        """
        The mixin should be able to handle simple mirror_fields lists.
        """
        class EchoAdmin(MirrorAdmin, admin.ModelAdmin):
            mirror_fields = ('words',)

        form = self.get_form_instance(EchoAdmin)

        self.assert_css(form, 'codemirror/lib/codemirror.css')
        self.assert_css(form, 'admin.css')

        self.assert_js(form, 'codemirror/lib/codemirror.js')
        self.assert_js(form, 'init.js')

    def test_tuples_list_with_modes(self):
        """
        The mixin should be able to handle mirror_fields with modes.
        """
        class EchoAdmin(MirrorAdmin, admin.ModelAdmin):
            mirror_fields = (
                ('words', {'mode': 'mirc'}),
            )

        form = self.get_form_instance(EchoAdmin)

        self.assert_css(form, 'codemirror/lib/codemirror.css')
        self.assert_css(form, 'admin.css')

        self.assert_js(form, 'codemirror/lib/codemirror.js')
        self.assert_js(form, 'codemirror/mode/mirc/mirc.js')
        self.assert_js(form, 'init.js')

    def test_tuples_list_with_addons(self):
        """
        The mixin should be able to handle mirror_fields with addons.
        """
        class EchoAdmin(MirrorAdmin, admin.ModelAdmin):
            mirror_fields = (
                ('words', {'addons': ['search/search.js']}),
            )

        form = self.get_form_instance(EchoAdmin)

        self.assert_css(form, 'codemirror/lib/codemirror.css')
        self.assert_css(form, 'codemirror/addon/dialog/dialog.css')
        self.assert_css(form, 'admin.css')

        self.assert_js(form, 'codemirror/lib/codemirror.js')
        self.assert_js(form, 'codemirror/addon/search/searchcursor.js')
        self.assert_js(form, 'codemirror/addon/dialog/dialog.js')
        self.assert_js(form, 'codemirror/addon/search/search.js')
        self.assert_js(form, 'init.js')

    def test_tuples_list_with_themes(self):
        """
        The mixin should be able to handle mirror_fields with themes.
        """
        class EchoAdmin(MirrorAdmin, admin.ModelAdmin):
            mirror_fields = (
                ('words', {'theme': 'dracula'}),
            )

        form = self.get_form_instance(EchoAdmin)

        self.assert_css(form, 'codemirror/lib/codemirror.css')
        self.assert_css(form, 'codemirror/theme/dracula.css')
        self.assert_css(form, 'admin.css')

        self.assert_js(form, 'codemirror/lib/codemirror.js')
        self.assert_js(form, 'init.js')

    def test_admin_with_media(self):
        """
        The mixin should include its admin.css also when the model admin has
        its own media.
        """
        class EchoAdmin(MirrorAdmin, admin.ModelAdmin):
            mirror_fields = ('words',)

            class Media:
                css = {'all': ['another.css']}

        form = self.get_form_instance(EchoAdmin)

        self.assert_css(form, 'codemirror/lib/codemirror.css')
        self.assert_css(form, 'admin.css')

        self.assert_js(form, 'codemirror/lib/codemirror.js')
        self.assert_js(form, 'init.js')

    def test_inline_admin(self):
        """
        The mixin should work with InlineAdmin subclasses.
        """
        class EchoReplyAdmin(MirrorAdmin, admin.StackedInline):
            model = EchoReply
            mirror_fields = ('words',)

        class EchoAdmin(admin.ModelAdmin):
            inlines = [EchoReplyAdmin]

        echo_admin = EchoAdmin(Echo, self.admin_site)
        formsets_and_inlines = echo_admin._create_formsets(Mock(), None, False)
        formset = formsets_and_inlines[0][0]

        self.assert_css(formset, 'codemirror/lib/codemirror.css')
        self.assert_css(formset, 'admin.css')

        self.assert_js(formset, 'codemirror/lib/codemirror.js')
        self.assert_js(formset, 'init.js')
