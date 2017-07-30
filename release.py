#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import sys

# codecov.io project token
import pypandoc

codecov_token = '' or os.environ.get('FORGIVE_DB_CODECOV_TOKEN')

base_dir = os.path.dirname(os.path.abspath(__file__))

sub_commands = {}


def run(*commands):
    os.system('cd {} && {}'.format(base_dir, ' && '.join(commands)))


def cmd(name):
    def decorator(func):
        sub_commands[name] = func

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def usage():
    print('Usage: {} <sub_command> <args...>'.format(sys.argv[0]))
    print('Sub command: [{}]'.format(', '.join(sub_commands)))
    exit(1)


@cmd('test')
def test():
    run('pytest --cov=./', 'codecov --token={}'.format(codecov_token))


@cmd('release')
def release(*setup_commands):
    markdown_file = os.path.join(base_dir, 'README.md')
    rst_file = os.path.join(base_dir, 'README.rst')
    rst_content = pypandoc.convert(markdown_file, 'rst')
    with open(rst_file, 'wb') as f:
        f.write(rst_content.encode('utf-8'))
    run('python setup.py {}'.format(' '.join(setup_commands)))
    os.unlink(rst_file)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    sub_command = sys.argv[1]
    if sub_command not in sub_commands:
        usage()
    func = sub_commands[sub_command]
    func(*sys.argv[2:])
