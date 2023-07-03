#!/usr/bin/env python3
# coding: utf-8


import configparser
import datetime
import os
import re

from .functions import *


MAIN_DIR = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(MAIN_DIR, '../config/config.ini')


def main():
    config_ini = configparser.ConfigParser()
    config_ini.read(CONFIG_PATH, encoding='utf-8')

    notion_database_url = config_ini['Notion']['database_url']
    notion_database_id = re.split('[/?]', notion_database_url)[-2]

    notion_token = config_ini['Notion']['token']

    month = str(datetime.datetime.today().date()).replace('-', '/')[:-3]
    record_dict = Functions.read_records(notion_database_id, notion_token, month)

    sio = Functions.savefig_to_memory(record_dict)

    slack_token = config_ini['Slack']['token']

    slack_channel_url = config_ini['Slack']['channel_url']
    slack_channel_id = slack_channel_url.split('/')[-1]

    Functions.send_notify(sio, slack_token, slack_channel_id)


if __name__ == '__main__':
    main()
