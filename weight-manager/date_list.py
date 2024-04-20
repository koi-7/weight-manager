# coding: utf-8


from .consts import *


class DateList:
    # def __init__(self, date_list):
    #     self.__date_list = date_list

    def __init__(self, mode_date):
        if mode_date.mode == Consts.MODE_MONTH:
            self.__date_list = [mode_date.date]
            return

        if mode_date.mode == Consts.MODE_YEAR:
            year = mode_date.date
            date_list = []
            for i in range(1, 13):
                year_month = f'{year}/{str(i).zfill(2)}'
                date_list.append(year_month)
            self.__date_list = date_list
            return

    @property
    def date_list(self):
        return self.__date_list

    # @classmethod
    # def create_instance(cls, mode, date):
    #     if mode == Consts.MODE_MONTH:
    #         return DateList([date])

    #     if mode == Consts.MODE_YEAR:
    #         date_list = []
    #         for i in range(1, 13):
    #             year_month = date + '/' + str(i).zfill(2)
    #             date_list.append(year_month)
    #         return DateList(date_list)

