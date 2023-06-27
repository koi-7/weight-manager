#!/usr/bin/env python3
# coding: utf-8


import datetime
import os

from .functions import *


MAIN_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(MAIN_DIR, '../data/')
DB_URL_PATH = os.path.join(DATA_DIR, 'db_url')
NOTION_TOKEN_PATH = os.path.join(DATA_DIR, 'notion_token')
SLACK_TOKEN_PATH = os.path.join(DATA_DIR, 'slack_token')
SLACK_CHANNEL = '03_weight-manager-with-notion'


def main():
    db_id = Functions.get_dbid(DB_URL_PATH)
    notion_token = Functions.get_token(NOTION_TOKEN_PATH)

    yesterday = str(datetime.datetime.today().date() - datetime.timedelta(1)).replace('-', '/')
    previous_month = yesterday[:-3]
    record_dict = Functions.read_records(db_id, notion_token, previous_month)

    sio = Functions.savefig_to_memory(record_dict)

    slack_token = Functions.get_token(SLACK_TOKEN_PATH)
    Functions.send_notify(sio, slack_token, SLACK_CHANNEL)


if __name__ == '__main__':
    main()
