# coding: utf-8


import re
import sys

from .exceptions import *


class ExecDate:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    def is_valid_date(self):
        try:
            if re.fullmatch(r'\d{4}/(0[1-9]|1[0-2])', self.date) or re.fullmatch(r'\d{4}', self.date):
                return True
            else:
                raise InvalidDate(f'入力された日付（{self.date}）が無効です。')
        except InvalidDate as e:
            print('Error:', e)
            sys.exit(1)
