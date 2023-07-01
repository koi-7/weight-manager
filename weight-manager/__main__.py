#!/usr/bin/env python3
# coding: utf-8


import datetime
import os

from .functions import *


MAIN_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(MAIN_DIR, '../data/')
NOTION_DATABASE_URL_PATH = os.path.join(DATA_DIR, 'notion_database_url')
NOTION_TOKEN_PATH = os.path.join(DATA_DIR, 'notion_token')
SLACK_CHANNEL_URL_PATH = os.path.join(DATA_DIR, 'slack_channel_url')
SLACK_TOKEN_PATH = os.path.join(DATA_DIR, 'slack_token')



def main():
    notion_database_id = Functions.get_database_id(NOTION_DATABASE_URL_PATH)
    notion_token = Functions.get_token(NOTION_TOKEN_PATH)

    yesterday = str(datetime.datetime.today().date() - datetime.timedelta(1)).replace('-', '/')
    previous_month = yesterday[:-3]
    record_dict = Functions.read_records(notion_database_id, notion_token, previous_month)

    sio = Functions.savefig_to_memory(record_dict)
    slack_channel_id = Functions.get_channel_id(SLACK_CHANNEL_URL_PATH)
    slack_token = Functions.get_token(SLACK_TOKEN_PATH)
    Functions.send_notify(sio, slack_token, slack_channel_id)


if __name__ == '__main__':
    main()
