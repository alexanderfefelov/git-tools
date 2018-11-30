#!/usr/bin/env python2

import os
import sys


def print_usage():
    script_path = sys.argv[0]
    script_name = os.path.basename(script_path)
    program_name = os.path.splitext(script_name)[0]
    usage = ('{0} executes git command on all children directories\n\n'
        'Usage:\n'
        '\tpython {1} GIT_COMMAND [ARGUMENTS]').format(program_name, script_path)
    print(usage)

def process_directory(directory, command_with_args):
    os.chdir(directory)
    os.system('git {0}'.format(command_with_args))
    os.chdir('..')

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    command_with_args = ' '.join(sys.argv[1:])
    root_dir = os.getcwd()
    for directory in [x for x in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, x))]:
        print('-' * 42)
        print(directory)
        print('-' * 42)
        process_directory(directory, command_with_args)

if __name__ == '__main__':
    main()
