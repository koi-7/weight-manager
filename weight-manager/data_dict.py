# coding: utf-8


import datetime


class DataDict:
    def __init__(self, data_dict):
        self.__data_dict = data_dict

    @property
    def data_dict(self):
        return self.__data_dict

    @classmethod
    def create_instance(cls, data_list):
        data_dict = {}
        for data in data_list:
            date = datetime.datetime.strptime(data['properties']['Date']['title'][0]['text']['content'], '%Y/%m/%d')
            weight = data['properties']['Weight']['number']
            data_dict[date] = weight

        return DataDict(data_dict)

    def sort(self):
        return DataDict(dict(sorted(self.__data_dict.items())))
