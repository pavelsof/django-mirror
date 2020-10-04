#!/usr/bin/env python
import json
import os
import re
import sys


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CODEMIRROR_DIR = os.path.join(
    PROJECT_DIR, 'django_mirror/static', 'django-mirror/codemirror'
)
ADDONS_DIR = os.path.join(CODEMIRROR_DIR, 'addon')
MODES_DIR = os.path.join(CODEMIRROR_DIR, 'mode')


regex_mod = re.compile(
    r"""
    (mod\(
        (?: require\(.+\)[,\s]* )+
        .*
    \))
    """,
    re.VERBOSE
)
regex_require = re.compile(
    r"""
    require\(
        \s*['"]
        ([\w/.]+)
        ['"]\s*
    \)
    """,
    re.VERBOSE
)


def extract_from_file(file_path):
    """
    Return the list of paths of the dependencies which the specified js module
    requires. The paths are relative to the codemirror repo dir.

    For example, given the abs path to rst.js, this func should return:

        ['mode/python/python.js', 'mode/stex/stex.js', 'addon/mode/overlay.js']

    Note that lib/codemirror.js is always included by the widget, so it is not
    needed to be listed as a dependency here. On the other hand, if there is a
    css file with the same name in the dir, it is considered a dependency.
    """
    harvest = []

    css_file_name = os.path.splitext(os.path.basename(file_path))[0] + '.css'
    css_file_path = os.path.join(os.path.dirname(file_path), css_file_name)
    if os.path.exists(css_file_path):
        harvest.append(os.path.relpath(css_file_path, start=CODEMIRROR_DIR))

    with open(file_path) as f:
        match = regex_mod.search(f.read())
        if not match:
            print('{}: no mod(...) call.'.format(file_path), file=sys.stderr)
            return harvest

    for item in regex_require.findall(match[1]):
        abs_path = os.path.join(os.path.dirname(file_path), item) + '.js'
        if not os.path.exists(abs_path):
            print('{} does not exist.'.format(abs_path), file=sys.stderr)
            continue

        rel_path = os.path.relpath(abs_path, start=CODEMIRROR_DIR)
        if rel_path != 'lib/codemirror.js':
            harvest.append(rel_path)

    return harvest


def extract_from_dir(start_dir_path):
    """
    Return a dict mapping the js modules in the given dir to their respective
    dependencies (css and js). Both keys and values are paths relative to the
    codemirror repo dir.

    Assume that the js modules are nested one level deep from start_dir_path.
    """
    harvest = {}

    for dir_path, dir_names, file_names in os.walk(start_dir_path):
        if dir_names:
            continue

        for file_name in file_names:
            try:
                assert file_name.endswith('.js')
                assert not file_name.endswith('test.js')
            except AssertionError:
                continue

            file_path = os.path.join(dir_path, file_name)
            rel_path = os.path.relpath(file_path, start=CODEMIRROR_DIR)

            harvest[rel_path] = extract_from_file(file_path)

    return harvest


if __name__ == '__main__':
    harvest = {}
    harvest.update(**extract_from_dir(MODES_DIR))
    harvest.update(**extract_from_dir(ADDONS_DIR))
    print(json.dumps(harvest, indent=2, sort_keys=True))
