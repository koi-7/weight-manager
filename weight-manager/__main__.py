#!/usr/bin/env python3
# coding: utf-8


import argparse
import configparser

from .consts import *
from .data_dict import *
from .data_list import *
from .date import *
from .date_list import *
from .graph import *
from .mode import *
from .notion import *
from .slack import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('date')
    args = parser.parse_args()

    designated_date = Date(args.date)
    designated_mode = Mode.create_instance(designated_date.date)
    date_list = DateList.create_instance(designated_mode.mode, designated_date.date)

    config_ini = configparser.ConfigParser()
    config_ini.read(Consts.PATH_CONFIG, encoding='utf-8')

    notion = Notion(config_ini['Notion']['database_id'], config_ini['Notion']['token'])

    data = DataList.create_instance(notion, date_list.date_list)
    data = DataDict.create_instance(data.data_list)
    data = data.sort()

    graph = Graph.create_instance(designated_mode.mode, designated_date.date, data.data_dict)

    slack = Slack(config_ini['Slack']['channel_id'], config_ini['Slack']['token'])
    slack.notify(graph.sio)


if __name__ == '__main__':
    main()
