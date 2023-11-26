# coding: utf-8


from .records import *


class Notion:
    def __init__(self, database_id, token):
        self.__database_id = database_id
        self.__token = token

    @property
    def database_id(self):
        return self.__database_id

    @property
    def token(self):
        return self.__token

    def read_data(self, date):
        url = 'https://api.notion.com/v1/databases/' + self.database_id + '/query'
        headers = {'Authorization': 'Bearer ' + self.token,
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

        return requests.post(url=url, headers=headers, json=json)
