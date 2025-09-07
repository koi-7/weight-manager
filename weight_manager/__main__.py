#!/usr/bin/env python3
# coding: utf-8


import argparse
import configparser
import datetime

from .mode_year_months import *
from .notion import *
from .slack import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('date')
    args = parser.parse_args()

    mode_year_months = ModeYearMonths(args.date)

    config_ini = configparser.ConfigParser()
    config_ini.read(Const.PATH_CONFIG, encoding='utf-8')

    notion = Notion(config_ini['Notion']['database_id'], config_ini['Notion']['token'])

    data_list = []
    for month in mode_year_months.months:
        response = notion.read_monthly_data(mode_year_months.year, month)
        json_data = response.json()
        data_list.extend(json_data.get('results'))

    data_dict = {}
    for data in data_list:
        date = datetime.datetime.strptime(data['properties']['Date']['date']['start'], '%Y-%m-%d')
        weight = data['properties']['Weight']['number']
        data_dict[date] = weight
    data_dict_sorted = dict(sorted(data_dict.items()))


if __name__ == '__main__':
    main()
