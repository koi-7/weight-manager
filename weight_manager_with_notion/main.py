#!/usr/bin/env python3
# coding: utf-8


from argparse import ArgumentParser
import os
import sys


MAIN_DIR = os.path.dirname(__file__)
CONF_DIR = os.path.join(MAIN_DIR, '../conf/')
DB_URL_PATH = os.path.join(CONF_DIR, 'db_url')
TOKEN_PATH = os.path.join(CONF_DIR, 'token')


def make_files(db_url, token):
    if not os.path.isdir(CONF_DIR):
        os.mkdir(CONF_DIR)

    with open(DB_URL_PATH, 'w') as f:
        f.write(db_url)
    with open(TOKEN_PATH, 'w') as f:
        f.write(token)

def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('--set', action='store_true', help='set db_url nad token')

    return argparser.parse_args()

def main():
    if len(sys.argv) == 1:
        print('See usage with -h, --help option.')
        sys.exit(0)

    args = get_option()

    if args.set:
        db_url = input('Input DB URL: ')
        token = input('Input Token: ')
        make_files(db_url, token)
        print('Setting completed.')


if __name__ == '__main__':
    main()
