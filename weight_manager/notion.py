# coding: utf-8


import calendar
import time

import requests


class Notion:
    def __init__(self, database_id, token):
        self.__database_id = database_id
        self.__token = token

    def read_monthly_data(self, year, month):
        date_after = f'{year}-{month}-01'
        date_before = f'{year}-{month}-{calendar.monthrange(int(year), int(month))[1]}'

        url = 'https://api.notion.com/v1/databases/' + self.__database_id + '/query'
        headers = {'Authorization': 'Bearer ' + self.__token,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Notion-Version': '2022-06-28'}
        json = {
            'filter': {
                'and': [
                    {
                        'property': 'Date',
                        'date': {
                            'on_or_after': date_after
                        }
                    },
                    {
                        'property': 'Date',
                        'date': {
                            'on_or_before': date_before
                        }
                    }
                ]
            }
        }

        time.sleep(1)

        return requests.post(url=url, headers=headers, json=json)
