# coding: utf-8


import os


class Const:
    class Path:
        _MAIN_DIR = os.path.dirname(__file__)
        LOG = os.path.join(_MAIN_DIR, '../logs/weight_manager.log')
        CONFIG = os.path.join(_MAIN_DIR, '../config/config.ini')
        CLIENT_SECRET = os.path.join(_MAIN_DIR, '../data/client_secret.json')
        TOKEN = os.path.join(_MAIN_DIR, '../data/token.json')

    class GoogleApi:
        SERVICE_NAME = 'drive'
        VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']

    class Mode:
        MONTH = 'month'
        YEAR = 'year'

    class DB:
        CULUMN_DATE = 'Date'
        CULUMN_WEIGHT = 'Weight'
