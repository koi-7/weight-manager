# coding: utf-8


import re
import sys

from .consts import *
from .exceptions import *


class Mode:
    def __init__(self, mode):
        self.__mode = mode

    @property
    def mode(self):
          return self.__mode

    @classmethod
    def create_instance(cls, date):
        try:
            # date のパターンによって区別
            if re.fullmatch(r'\d{4}/(0[1-9]|1[0-2])', date):
                    return Mode(Consts.MODE_MONTH)
            if re.fullmatch(r'\d{4}', date):
                    return Mode(Consts.MODE_YEAR)
            raise InvalidDateError(f'InvalidDateError: 日付（{date}）が無効です。')
        except InvalidDateError as e:
            print(e)
            sys.exit(1)

