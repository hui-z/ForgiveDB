# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import sys

# codecov.io project token
codecov_token = '' or os.environ.get('FORGIVE_DB_CODECOV_TOKEN')

base_dir = os.path.dirname(__file__)

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


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    sub_command = sys.argv[1]
    if sub_command not in sub_commands:
        usage()
    func = sub_commands[sub_command]
    func()
