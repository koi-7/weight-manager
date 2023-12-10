# coding: utf-8


class Date:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date
