=================
how to contribute
=================

Thank you for opening this file! :)


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
--------------

The repo includes a simple Django project to serve as a playground. Please refer to ``sample_project/README.rst`` for setup info.


conventions
===========

For file encoding, newlines, indentation: please use the ``.editorconfig`` rules (`take a look here <https://editorconfig.org/>`_ if this is new for you).

For coding style: please follow `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_.


how to...
=========

...upgrade codemirror?
----------------------

.. code:: sh

    # go to codemirror's dir
    cd django_mirror/static/django-mirror/codemirror/

    # checkout the newer version
    git pull
    git checkout 5.65.0

    # build lib/codemirror.js
    npm install
    npm test
    npm run build

    # go back to django-mirror's dir
    cd -

    # update media.json
    scripts/extract_deps.py > django_mirror/media.json

    # update the README and the CHANGELOG
    vim README.rst
    vim CHANGELOG.rst

    # commit
    git commit -am "Upgraded CodeMirror to 5.65.0."
