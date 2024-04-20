# coding: utf-8


import re
import sys

from .consts import *
from .exceptions import *

class ModeYearMonths:
    def __init__(self, date):
        re_year = re.fullmatch(r'\d{4}', date)
        re_year_month = re.fullmatch(r'(\d{4})/(0[1-9]|1[0-2])', date)
        try:
            # date のパターンによって区別
            if re_year_month:
                    self.__mode = Consts.MODE_MONTH
                    self.__year = re_year_month.group(1)
                    self.__months = [re_year_month.group(2)]
                    return
            if re_year:
                    self.__mode = Consts.MODE_YEAR
                    self.__year = re_year.group(0)
                    self.__months = [str(m).zfill(2) for m in range(1, 13)]
                    return
            raise InvalidDateError(f'InvalidDateError: 日付（{date}）が無効です。')
        except InvalidDateError as e:
            print(e)
            sys.exit(1)

    @property
    def mode(self):
          return self.__mode

    @property
    def year(self):
         return self.__year


    @property
    def months(self):
         return self.__months
