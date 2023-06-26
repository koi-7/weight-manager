#!/usr/bin/env python3
# coding: utf-8


from argparse import ArgumentParser
import datetime
import os
import sys



from .functions import *


MAIN_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(MAIN_DIR, '../data/')
DB_URL_PATH = os.path.join(DATA_DIR, 'db_url')
NOTION_TOKEN_PATH = os.path.join(DATA_DIR, 'notion_token')
SLACK_TOKEN_PATH = os.path.join(DATA_DIR, 'slack_token')
SLACK_CHANNEL = '03_weight-manager-with-notion'


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

def main():
    db_id = Functions.get_dbid(DB_URL_PATH)
    notion_token = Functions.get_token()

    if str(datetime.datetime.today().date())[-2:] == '01':
        yesterday = str(datetime.datetime.today().date() - datetime.timedelta(1))
        previous_month = yesterday[:-3]
        records = Functions.read_records(db_id, notion_token, previous_month)

        date_list = list(records.keys())
        weight_list = list(records.values())

        sio = Functions.save_fig_to_memory(date_list, weight_list)

        slack_token = Functions.get_slack_token(SLACK_TOKEN_PATH)
        Functions.send_notify(slack_token, sio)





if __name__ == '__main__':
    main()
