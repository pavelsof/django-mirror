============================
django-mirror sample project
============================

A bare-bones Django 2.2 project with a single app with a single model with a single field for playing with the admin integration.


setup
=====

.. code:: sh

    # this will create a db.sqlite3 file (git-ignored)
    python manage.py migrate

    # you need a user to login into the admin with
    python manage.py createsuperuser

    # and then go to http://localhost:8000/admin/echoes/echo/add/
    python manage.py runserver
