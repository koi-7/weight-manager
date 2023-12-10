# coding: utf-8


import time

import requests


class Notion:
    def __init__(self, database_id, token):
        self.__database_id = database_id
        self.__token = token

    def read_data(self, date):
        url = 'https://api.notion.com/v1/databases/' + self.__database_id + '/query'
        headers = {'Authorization': 'Bearer ' + self.__token,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Notion-Version': '2022-06-28'}
        json = {
            'filter': {
                'property': 'Date',
                'title': {
                    'contains': date
                }
            }
        }

        time.sleep(1)

        return requests.post(url=url, headers=headers, json=json)
