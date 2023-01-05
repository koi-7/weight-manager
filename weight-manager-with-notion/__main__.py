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


class Manager:
    def __init__(self):
        self.__dbid = None
        self.__token = None
        self.__data = None

    @property
    def dbid(self):
        return self.__dbid

    @property
    def token(self):
        return self.__token

    @property
    def data(self):
        return self.__data

    def fetch_dbid(self):
        with open(DB_URL_PATH, 'r') as f:
            url =  f.readline().rstrip('\n')
        l = url.split('/')
        self.__dbid = l[4].split('?')[0]

    def fetch_token(self):
        with open(TOKEN_PATH, 'r') as f:
            self.__token = f.readline().rstrip('\n')

    def fetch_data(self):
        req_url = 'https://api.notion.com/v1/databases/' + self.dbid + '/query'
        headers = {'Authorization': 'Bearer ' + self.token,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Notion-Version': '2022-06-28'}

        try:
            response = requests.post(url=req_url, headers=headers)
            response.raise_for_status()
        except Exception:
            print('Error: DB URL or token is invalid.')
            sys.exit(1)

        json_data = response.json()
        results = json_data.get('results')

        try:
            date_list = [r['properties']['Date']['title'][0]['text']['content'] for r in results]
            weight_list = [r['properties']['Weight']['number'] for r in results]
        except Exception:
            print('Error: Name or type of column is wrong.')
            sys.exit(1)

        dic = dict(zip(date_list, weight_list))

        self.__data = dict(sorted(dic.items()))


def arg_check():
    if len(sys.argv) == 1:
        try:
            raise Exception
        except Exception:
            print('Error: Lack of argument. See usage with -h or --help option.')
            sys.exit(1)

def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('--graph', action='store_true', help='show graph')
    argparser.add_argument('--list', type=int, help='show recent N records')
    argparser.add_argument('--set', action='store_true', help='set db_url and token')

    return argparser.parse_args()

def check_files():
    if (not os.path.exists(DB_URL_PATH)) or (not os.path.exists(TOKEN_PATH)):
        try:
            raise Exception
        except Exception:
            print("Error: Conf files don't exist. Use --set option to set DB and token info.")
            sys.exit(1)

def make_files():
    if not os.path.isdir(CONF_DIR):
        os.mkdir(CONF_DIR)

    db_url = input('Input DB URL: ')
    token = input('Input Token: ')

    with open(DB_URL_PATH, 'w') as f:
        f.write(db_url)
    with open(TOKEN_PATH, 'w') as f:
        f.write(token)

    print('Info: Setting completed.')

def show_graph(data):
    date_list = list(data.keys())
    weight_list = list(data.values())

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.grid(which = "major", axis = "y", color = "gray",
            alpha = 0.3, linestyle = "-", linewidth = 1)
    plt.plot(date_list, weight_list)
    plt.xticks(rotation=90)
    plt.show()

def show_list(data, num_of_record):
    date_list = list(data.keys())[-num_of_record:]
    weight_list = list(data.values())[-num_of_record:]

    for i in range(len(date_list)):
        print('   ' + date_list[i] + ': ' + str(weight_list[i]) + ' kg')


def main():
    arg_check()

    args = get_option()

    check_files()

    manager = Manager()
    manager.fetch_dbid()
    manager.fetch_token()
    manager.fetch_data()

    data = manager.data

    if args.graph:
        show_graph(data)

    if args.list:
        show_list(data, args.list)


if __name__ == '__main__':
    main()
