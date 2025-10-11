#!/usr/bin/env python3
# coding: utf-8


import argparse
import configparser
import datetime

from .const import Const
from .mode_year_months import ModeYearMonths
from .notion import Notion
from .slack import Slack
from .google_api import GoogleApi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('date')
    args = parser.parse_args()

    config_ini = configparser.ConfigParser()
    config_ini.read(Const.Path.CONFIG, encoding='utf-8')

    mode_year_months = ModeYearMonths(args.date)

    google_api = GoogleApi(config_ini)
    new_file_key = google_api.copy_template_file(mode_year_months)

    exit()


    notion = Notion(config_ini['Notion']['database_id'], config_ini['Notion']['token'])

    data_list = []
    for month in mode_year_months.months:
        response = notion.read_monthly_data(mode_year_months.year, month)
        json_data = response.json()
        data_list.extend(json_data.get('results'))

    data_dict = {}
    for data in data_list:
        date = datetime.datetime.strptime(data['properties'][Const.DB.CULUMN_DATE]['date']['start'], '%Y-%m-%d')
        weight = data['properties'][Const.DB.CULUMN_WEIGHT]['number']
        data_dict[date] = weight
    data_dict_sorted = dict(sorted(data_dict.items()))


if __name__ == '__main__':
    main()
