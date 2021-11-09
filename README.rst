=============
django-mirror
=============

This package marries `Django`_ with `CodeMirror`_. It provides (1) a customisable form widget, and (2) a shorthand way to use this widget in the admin. In both cases the relevant static files (including mode/theme/addon files) are automatically included as form assets.


installation
============

This is a Python 3 package with no other dependencies apart from Django and it is offered at the `Cheese Shop`_:

.. code:: sh

    # usually inside a virtual environment
    pip install django-mirror

The CodeMirror files (version `5.63.3`_) are included in the package. The supported Django versions are **2.2**, **3.0**, **3.1**, and **3.2**.


settings
========

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
======

Bascially this package provides a form widget called ``MirrorArea`` that extends Django's ``Textarea`` widget.

.. code:: python

    from django import forms
    from django_mirror.widgets import MirrorArea

    class CommentForm(forms.Form):
        text = forms.CharField(
            widget=MirrorArea(
                attrs={'rows': 20},  # the parent class' attrs still works
                mode='markdown',  # the other kwargs are forwarded to CodeMirror
            )
        )

The ``MirrorArea`` widget can be initialised with the following arguments:

- Any of CodeMirror's `config options`_. These can be specified in either camelCase or snake_case (e.g. both ``tabSize`` and ``tab_size`` would work). The css/js files associated with the ``mode``, if provided, are included as form assets.
- ``addons``, a list of CodeMirror `addons`_, e.g. ``dialog/dialog``. The css/js files associated with the addons are recursively included as form assets.
- ``attrs``, just as Django's form widgets.

The addons and config options are merged with and override ``DJANGO_MIRROR_DEFAULTS`` if the setting has been defined.


admin
=====

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
                'line_wrapping': True,
            }),
        )

The mixin also includes a bit of css to make CodeMirror look more like regular admin textarea fields.


similar projects
================

There are several other packages that provide customisable CodeMirror widgets:

* `django-codemirror`_
* `django-codemirror2`_
* `django-codemirror-widget`_
* `django-codemirror-widget-2`_


licence
=======

`GNU LGPLv3`_. Please refer to ``COPYING`` for the base GPLv3 licence and to ``COPYING.LESSER`` for the additional permissions on top that constitute LGPLv3.


.. _`5.63.3`: https://github.com/codemirror/CodeMirror/releases/tag/5.63.3
.. _`addons`: https://codemirror.net/doc/manual.html#addons
.. _`Cheese Shop`: https://pypi.python.org/pypi/django-mirror
.. _`CodeMirror`: https://codemirror.net/
.. _`config options`: https://codemirror.net/doc/manual.html#config
.. _`Django`: https://www.djangoproject.com/
.. _`django-codemirror`: https://pypi.org/project/django-codemirror/
.. _`django-codemirror2`: https://pypi.org/project/django-codemirror2/
.. _`django-codemirror-widget`: https://pypi.org/project/django-codemirror-widget/
.. _`django-codemirror-widget-2`: https://pypi.org/project/django-codemirror-widget-2/
.. _`GNU LGPLv3`: https://www.gnu.org/licenses/lgpl-3.0.html
