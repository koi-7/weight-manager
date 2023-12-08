# coding: utf-8


import time

import requests


class Slack:
    def __init__(self, channel_id, token):
        self.__channel_id = channel_id
        self.__token = token

    def notify(self, sio):
        url = 'https://slack.com/api/files.upload'
        headers = {'Authorization': 'Bearer ' + self.__token}
        params = {'channels': self.__channel_id}
        files = {'file': sio.getvalue()}

        requests.post(url=url, headers=headers, params=params, files=files)

        time.sleep(1)
