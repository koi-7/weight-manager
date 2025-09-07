# coding: utf-8


import os


class Const:
    class Path:
        _MAIN_DIR = os.path.dirname(__file__)
        LOG = os.path.join(_MAIN_DIR, '../logs/weight_manager.log')
        CONFIG = os.path.join(_MAIN_DIR, '../config/config.ini')

    class Mode:
        MONTH = 'month'
        YEAR = 'year'

    class DB:
        CULUMN_DATE = 'Date'
        CULUMN_WEIGHT = 'Weight'
