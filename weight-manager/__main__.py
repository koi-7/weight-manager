#!/usr/bin/env python3
# coding: utf-8


import argparse
import configparser
import os
import re
import time
import urllib

from .exec_date import *
from .figure import *
from .notion import *
from .records import *
from .slack import *


MAIN_DIR = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(MAIN_DIR, '../config/config.ini')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('date')
    args = parser.parse_args()

    exec_date = ExecDate(args.date)

    exec_date.is_valid_date()

    config_ini = configparser.ConfigParser()
    config_ini.read(CONFIG_PATH, encoding='utf-8')

    notion_database_url = config_ini['Notion']['database_url']
    notion_database_id = os.path.basename(urllib.parse.urlparse(notion_database_url).path)
    notion_token = config_ini['Notion']['token']
    notion = Notion(notion_database_id, notion_token)

    records = Records()
    if re.fullmatch(r'\d{4}/(0[1-9]|1[0-2])', exec_date.date):
        response = notion.read_data(exec_date.date)
        records.make_list(response)
    elif re.fullmatch(r'\d{4}', exec_date.date):
        for i in range(1, 13):
            date = exec_date.date + '/' + str(i).zfill(2)
            response = notion.read_data(date)
            records.make_list(response)
            time.sleep(1)

    records.make_dict()
    records.dict_sort()

    figure = Figure(exec_date.date)
    figure.savefig_to_memory(records.dict)

    slack_channel_url = config_ini['Slack']['channel_url']
    slack_channel_id = os.path.basename(urllib.parse.urlparse(slack_channel_url).path)
    slack_token = config_ini['Slack']['token']
    slack = Slack(slack_channel_id, slack_token)

    slack.notify(figure.sio)


if __name__ == '__main__':
    main()
