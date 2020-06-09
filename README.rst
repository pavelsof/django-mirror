=============
django mirror
=============

This package marries `Django`_ with `CodeMirror`_.


rationale
=========

- You can enable vim mode :)


usage
=====

installation
------------

This is a standard Python 3 package without dependencies (apart from Django itself) offered at the `Cheese Shop`_::

    # usually inside a virtual environment
    pip install django-mirror

And then you have to add ``django_mirror`` to the ``INSTALLED_APPS`` setting of your Django project.


widget
------

To django-mirror textarea is provided as a form widget::

    from django import forms
    from django_mirror.widgets import MirrorTextarea

    class CommentForm(forms.Form):
        text = forms.CharField(widget=MirrorTextarea(mode='markdown'))


admin
-----

To use the django-mirror textarea widget in the admin panel you can subclass the respective model form. But you can also use the admin mixin provided by the library::

    from django.contrib import admin
    from django_mirror.admin import MirrorAdmin

    from weblog.models import Comment


    @admin.register(Comment)
    class CommentAdmin(MirrorAdmin, admin.ModelAdmin):
        mirror_fields = ('comment',)  # default options
        mirror_fields = (  # with custom options
            ('comment', {
                'mode': 'markdown',
            })
        )


uploads
-------




licence
=======

GPL. You can do what you want with this code as long as you let others do the same.


.. _`Django`: https://www.djangoproject.com/
.. _`Cheese Shop`: https://pypi.python.org/pypi/django-mirror
.. _`CodeMirror`: https://codemirror.net/
