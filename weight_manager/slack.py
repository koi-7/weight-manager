# coding: utf-8


import time

import requests

from .const import Const


class Slack:
    def __init__(self, config_ini):
        self.__channel_id = config_ini['Slack']['channel_id']
        self.__token = config_ini['Slack']['token']

    def notify(self, mode_year_months, spread_sheet_file_key):
        '''Slack での通知を行う'''
        url = Const.Slack.API_URL
        headers = {'Authorization': f'Bearer {self.__token}'}
        message = \
            Const.Slack.MONTHLY_MESSAGE_BASE.format(year=mode_year_months.year, month=mode_year_months.months[0]) if mode_year_months.mode == Const.Mode.MONTH \
            else Const.Slack.YEARLY_MESSAGE_BASE.format(year=mode_year_months.year)
        file_url = Const.Slack.SPREAD_SHEET_URL_BASE.format(file_key=spread_sheet_file_key)
        text = f'{message}\n{file_url}'
        data = {'channel': self.__channel_id, 'text': text}

        requests.post(url=url, headers=headers, data=data)
        time.sleep(1)
