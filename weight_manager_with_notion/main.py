#!/usr/bin/env python3
# coding: utf-8


from argparse import ArgumentParser
import matplotlib.pyplot as plt
import os
import requests
import sys


MAIN_DIR = os.path.dirname(__file__)
CONF_DIR = os.path.join(MAIN_DIR, '../conf/')
DB_URL_PATH = os.path.join(CONF_DIR, 'db_url')
TOKEN_PATH = os.path.join(CONF_DIR, 'token')


def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('--graph', action='store_true', help='show graph')
    argparser.add_argument('--list', type=int, help='show recent N records')
    argparser.add_argument('--set', action='store_true', help='set db_url and token')

    return argparser.parse_args()

def make_files(db_url, token):
    if not os.path.isdir(CONF_DIR):
        os.mkdir(CONF_DIR)

    with open(DB_URL_PATH, 'w') as f:
        f.write(db_url)
    with open(TOKEN_PATH, 'w') as f:
        f.write(token)

def get_dbid():
    with open(DB_URL_PATH, 'r') as f:
        url =  f.readline().rstrip('\n')
    l = url.split('/')
    dbid = l[4].split('?')[0]
    return dbid

def get_token():
    with open(TOKEN_PATH, 'r') as f:
        token = f.readline().rstrip('\n')
    return token


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
        sys.exit(0)

    dbid = get_dbid()
    token = get_token()

    req_url = 'https://api.notion.com/v1/databases/' + dbid + '/query'

    if args.graph or (args.list != None):
        headers = {'Authorization': 'Bearer ' + token,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Notion-Version': '2022-06-28'}
        response = requests.post(url=req_url, headers=headers)
        json_data = response.json()
        results = json_data.get('results')
        date_list = [r['properties']['Date']['title'][0]['text']['content'] for r in results]
        weight_list = [r['properties']['Weight']['number'] for r in results]

        dic = dict(zip(date_list, weight_list))
        dic = dict(sorted(dic.items()))

        date_list_sorted = list(dic.keys())
        weight_list_sorted = list(dic.values())

        if args.graph:
            plt.plot(date_list_sorted, weight_list_sorted)
            plt.xticks(rotation=90)
            plt.show()

        if args.list != None:
            dlist = date_list_sorted[-args.list:]
            wlist = weight_list_sorted[-args.list:]
            for i in range(len(dlist)):
                print('   ' + dlist[i] + ': ' + str(wlist[i]) + ' kg')

        sys.exit(0)


if __name__ == '__main__':
    main()
