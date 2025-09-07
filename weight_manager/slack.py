# coding: utf-8


import json
import time

import requests


class Slack:
    def __init__(self, channel_id, token):
        self.__channel_id = channel_id
        self.__token = token

    def notify(self, sio):
        upload_url, file_id = self._get_upload_url_and_file_id(sio)
        self._upload_file_content(upload_url, sio)
        self._complete_upload(file_id)

        time.sleep(1)

    def _get_upload_url_and_file_id(self, sio):
        url = 'https://slack.com/api/files.getUploadURLExternal'
        headers = {'Authorization': f'Bearer {self.__token}'}
        params = {'filename': 'file.png', 'length': len(sio.getvalue())}

        response = requests.get(url, headers=headers, params=params)
        response_json = response.json()

        return response_json['upload_url'], response_json['file_id']

    def _upload_file_content(self, upload_url, sio):
        requests.post(url=upload_url, data=sio.getvalue())

    def _complete_upload(self, file_id):
        url = 'https://slack.com/api/files.completeUploadExternal'
        headers = {'Authorization': f'Bearer {self.__token}', 'Content-Type': 'application/json'}
        data = {
            'files': [{'id': file_id, 'title': 'title'}],
            'channel_id': self.__channel_id
        }

        requests.post(url, headers=headers, data=json.dumps(data))
