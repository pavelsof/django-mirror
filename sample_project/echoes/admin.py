from django.contrib import admin
from django_mirror.admin import MirrorAdmin

from echoes.models import Echo


@admin.register(Echo)
class EchoAdmin(MirrorAdmin, admin.ModelAdmin):
    mirror_fields = (
        ('words', {
            'mode': 'markdown',
            'line_wrapping': True,
        }),
    )
