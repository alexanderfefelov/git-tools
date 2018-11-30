#!/usr/bin/env python2

import json
import os
import sys
import urllib2


GITHUB_API_MAX_PAGE_SIZE = 100


def encode_string(string):
    if string is None:
        return
    try:
        return string.encode('utf-8')
    except UnicodeEncodeError:
        return string.encode('latin-1')


def print_repository_info(repository):
    print('-' * 42)
    print(repository['name'])
    print('-' * 42)
    print(repository['html_url'])
    print(encode_string(repository['description']))
    print('Created at: {0}'.format(repository['created_at']))
    print('Updated at: {0}'.format(repository['updated_at']))
    print('Language: {0}'.format(repository['language']))
    print('Stars: {0}'.format(repository['stargazers_count']))
    print('Forks: {0}'.format(repository['forks_count']))
    print('Open issues: {0}'.format(repository['open_issues_count']))


def cmd_list_repos(username):
    url = 'https://api.github.com/users/{0}/repos?per_page={1}'.format(username, GITHUB_API_MAX_PAGE_SIZE)
    repositories = json.loads(urllib2.urlopen(url).read())
    for repository in repositories:
        print_repository_info(repository)


def cmd_list_stars(username):
    url = 'https://api.github.com/users/{0}/starred?per_page={1}'.format(username, GITHUB_API_MAX_PAGE_SIZE)
    repositories = json.loads(urllib2.urlopen(url).read())
    for repository in repositories:
        print_repository_info(repository)


def cmd_clone(username):
    url = 'https://api.github.com/users/{0}/repos?per_page={1}'.format(username, GITHUB_API_MAX_PAGE_SIZE)
    repositories = json.loads(urllib2.urlopen(url).read())
    for repository in repositories:
        print('-' * 42)
        print(repository['name'])
        print('-' * 42)
        os.system('git clone {0}'.format(repository['clone_url']))


commands = {
    'list_repos': (cmd_list_repos, 'Lists all user\'s public repositories'),
    'list_stars': (cmd_list_stars, 'Lists user\'s stars'),
    'clone': (cmd_clone, 'Clones all user\'s public repositories')
}


def print_usage():
    script_path = sys.argv[0]
    script_name = os.path.basename(script_path)
    program_name = os.path.splitext(script_name)[0]
    usage = ('{0} does something with GitHub user\n\n'
             'Usage:\n'
             '\tpython {1} GITHUB_USERNAME COMMAND\n').format(program_name, script_path)
    print(usage)
    print('Available commands:')
    for (k, v) in sorted(commands.iteritems()) :
        print('\t{0}\t{1}'.format(k, v[1]))


def main():
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)
    username = sys.argv[1]
    command = sys.argv[2]
    if command in commands:
        commands[command][0](username)
    else:
        print_usage()
        sys.exit(1)


if __name__ == '__main__':
    main()
