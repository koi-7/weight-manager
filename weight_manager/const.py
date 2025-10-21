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
        TEMPLATE_FILE_DATE_START_CELL_ADDRESS = 'B3'

    class Slack:
        API_URL = 'https://slack.com/api/chat.postMessage'
        MONTHLY_MESSAGE_BASE = '{year} 年 {month} 月の集計です。'
        YEARLY_MESSAGE_BASE = '{year} 年の集計です。'
        SPREAD_SHEET_URL_BASE = 'https://docs.google.com/spreadsheets/d/{file_key}'

    class Mode:
        MONTH = 'month'
        YEAR = 'year'

    class DB:
        CULUMN_DATE = 'Date'
        CULUMN_WEIGHT = 'Weight'
