from django.contrib import admin
from django_mirror.admin import MirrorAdmin

from echoes.models import Echo, Utterance


@admin.register(Utterance)
class UtteranceAdmin(MirrorAdmin, admin.ModelAdmin):
    mirror_fields = (
        ('words', {
            'mode': 'rst',
            'line_wrapping': True,
        }),
    )

    class EchoAdmin(MirrorAdmin, admin.StackedInline):
        model = Echo
        extra = 0
        mirror_fields = (
            ('words', {
                'mode': 'markdown',
                'line_wrapping': True
            }),
        )

    inlines = (EchoAdmin,)
