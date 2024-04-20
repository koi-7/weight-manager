# coding: utf-8


import os


class Consts:
    PATH_MAIN_DIR = os.path.dirname(__file__)
    PATH_LOG = os.path.join(PATH_MAIN_DIR, '../logs/weight_manager.log')
    PATH_CONFIG = os.path.join(PATH_MAIN_DIR, '../config/config.ini')

    MODE_MONTH = 'month'
    MODE_YEAR = 'year'

    GRAPH_WIDTH_MONTHLY = 6.4  # デフォルト値
    GRAPH_WIDTH_ANNUAL = 12
