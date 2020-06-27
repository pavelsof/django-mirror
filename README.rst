=============
django mirror
=============

This package marries `Django`_ with `CodeMirror`_.


usage
=====

installation
------------

This is a Python 3 package with no other dependencies apart from Django and it is offered at the `Cheese Shop`_:

.. code:: sh

    # usually inside a virtual environment
    pip install django-mirror


settings
--------

.. code:: python

    # add 'django_mirror' to your INSTALLED_APPS if you want the package to be
    # handled by Django's collectstatic command
    INSTALLED_APPS += ['django_mirror']

    # use DJANGO_MIRROR_DEFAULTS to specify default options for your widgets
    # see the next section for more info about the options
    DJANGO_MIRROR_DEFAULTS = {
        'mode': 'rst',
        'addons': ['mode/overlay'],
        'line_wrapping': True,
    }


widget
------

Bascially this package provides a form widget called ``MirrorArea`` that extends ``forms.Textarea``.

.. code:: python

    from django import forms
    from django_mirror.widgets import MirrorTextarea

    class CommentForm(forms.Form):
        text = forms.CharField(
            widget=MirrorArea(
                attrs={'rows': 20},  # the parent class' attrs still works
                mode='markdown',  # the other kwargs are forwarded to CodeMirror
            )
        )

The ``MirrorArea`` widget can be initialised with the following arguments:

- ``attrs``, as the other Django form widgets.
- ``addons``, a list of CodeMirror `addons`_ to include as form assets.
- Any of CodeMirror's `config options`_, in both camelCase and snake_case.

The addons and config options are merged with ``DJANGO_MIRROR_DEFAULTS`` if the setting has been defined.


admin
-----

If you want to use the widget in the admin panel, you can subclass the ``MirrorAdmin`` mixin, which provides the ``mirror_fields`` model admin option:

.. code:: python

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


similar projects
================

There are at least two other packages that would offer alternative takes on adding CodeMirror to Django:

* `django-codemirror`_
* `django-codemirror2`_


licence
=======

GPL. You can do what you want with this code as long as you let others do the same.


.. _`addons`: https://codemirror.net/doc/manual.html#addons
.. _`Cheese Shop`: https://pypi.python.org/pypi/django-mirror
.. _`CodeMirror`: https://codemirror.net/
.. _`config options`: https://codemirror.net/doc/manual.html#config
.. _`Django`: https://www.djangoproject.com/
.. _`django-codemirror`: https://pypi.org/project/django-codemirror/
.. _`django-codemirror2`: https://pypi.org/project/django-codemirror2/
