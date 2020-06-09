from django_mirror.widgets import MirrorArea


class MirrorAdmin:
    mirror_fields = tuple()

    def get_mirror_fields(self, request, obj=None):
        """
        Hook for specifying custom mirror fields.
        """
        return self.mirror_fields

    def get_form(self, request, obj=None, **kwargs):
        """
        Overwrite ModelAdmin's get_form method in order to provide the widgets
        argument to the modelform_factory.
        """
        mirror_fields = self.get_mirror_fields(request, obj)
        mirror_widgets = {}

        for field in mirror_fields:
            if isinstance(field, (list, tuple)):
                field_name = field[0]
                widget_args = field[1]
            else:
                field_name = str(field)
                widget_args = {}

            mirror_widgets[field_name] = MirrorArea(**widget_args)

        if mirror_widgets:
            if 'widgets' in kwargs and kwargs['widgets'] is not None:
                kwargs['widgets'].update(mirror_widgets)
            else:
                kwargs['widgets'] = mirror_widgets

        return super().get_form(request, obj, **kwargs)
