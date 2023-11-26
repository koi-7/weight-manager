# coding: utf-8


import datetime

import requests


class Records:
    def __init__(self):
        self.__data = []
        self.__dict = {}

    @property
    def data(self):
        return self.__data

    @property
    def dict(self):
        return self.__dict

    @dict.setter
    def dict(self, dict):
        self.__dict = dict

    def make_list(self, response):
        json_data = response.json()
        self.data.extend(json_data.get('results'))

    def make_dict(self):
        for data in self.data:
            date = datetime.datetime.strptime(data['properties']['Date']['title'][0]['text']['content'], '%Y/%m/%d')
            weight = data['properties']['Weight']['number']
            self.dict[date] = weight

    def dict_sort(self):
        self.dict = dict(sorted(self.dict.items()))
