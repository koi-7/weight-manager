# coding: utf-8


import requests


class Slack:
    def __init__(self, channel_id, token):
        self.__channel_id = channel_id
        self.__token = token

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def token(self):
        return self.__token

    def notify(self, sio):
        url = 'https://slack.com/api/files.upload'
        headers = {'Authorization': 'Bearer ' + self.token}
        params = {'channels': self.channel_id}
        files = {'file': sio.getvalue()}

        requests.post(url=url, headers=headers, params=params, files=files)
