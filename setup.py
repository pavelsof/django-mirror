import os.path

from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(BASE_DIR, 'README.rst')) as f:
    README = f.read()


with open(os.path.join(BASE_DIR, 'django_mirror/__version__.py')) as f:
    exec(f.read())


setup(
    name='django-mirror',
    version=VERSION,

    description='This package marries Django with CodeMirror',
    long_description=README,
    long_description_content_type='text/x-rst',

    url='https://github.com/pavelsof/django-mirror',
    author='Pavel Sofroniev',
    author_email='mail@pavelsof.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords='django codemirror',
    project_urls={
        'Source': 'https://github.com/pavelsof/django-mirror',
        'Tracker': 'https://github.com/pavelsof/django-mirror/issues',
    },

    packages=find_packages(exclude=['tests']),

    install_requires=['django>=1.11'],
    python_requires='>=3',

    package_data={
        'django_mirror': [
            'media.json',
            'static/django-mirror/*.css',
            'static/django-mirror/*.js',
            'static/django-mirror/codemirror/addon/*/*.css',
            'static/django-mirror/codemirror/addon/*/*.js',
            'static/django-mirror/codemirror/lib/*.css',
            'static/django-mirror/codemirror/lib/*.js',
            'static/django-mirror/codemirror/mode/*/*.js',
            'static/django-mirror/codemirror/theme/*.css',
        ]
    },
)
