=================
how to contribute
=================

I am happy that you are reading this!


project setup
=============

.. code:: sh

    # clone this repo or your fork of it
    # recursively, because codemirror's repo is a submodule
    git clone --recursive github:pavelsof/django-mirror
    cd django-mirror

    # create a virtual env
    # the venv dir is git-ignored
    python3 -m venv venv
    source venv/bin/activate

    # install the dependencies
    # you can also pip install -r requirements.txt
    pip install pip-tools
    pip-sync

    # run the tests
    tox


sample project
==============

The repo includes a simple Django project to serve as a playground. Please refer to ``sample_project/README.rst`` for setup info.
