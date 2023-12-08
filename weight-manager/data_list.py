# coding: utf-8


class DataList:
    def __init__(self, data_list):
        self.__data_list = data_list

    @property
    def data_list(self):
        return self.__data_list

    @classmethod
    def create_instance(cls, notion, date_list):
        data_list = []
        for date in date_list:
            response = notion.read_data(date)
            json_data = response.json()
            data_list.extend(json_data.get('results'))

        return DataList(data_list)
