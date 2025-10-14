# coding: utf-8


from datetime import datetime
import os
import time

import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from gspread.exceptions import APIError, WorksheetNotFound

from .const import Const
from .exceptions import *


class GoogleApi:
    def __init__(self, config_ini):
        self.__template_file_key = config_ini['Google']['template_file_key']
        self.__destination_folder_id = config_ini['Google']['destination_folder_id']

        credentials = self._create_credentials()

        self.__drive_service = build(Const.GoogleApi.SERVICE_NAME, Const.GoogleApi.VERSION, credentials=credentials)
        self.__gspread_client = gspread.authorize(credentials)

    def _create_credentials(self):
        credentials = None

        if os.path.exists(Const.Path.TOKEN):
            credentials = Credentials.from_authorized_user_file(Const.Path.TOKEN, Const.GoogleApi.SCOPES)

        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(Const.Path.CLIENT_SECRET, Const.GoogleApi.SCOPES)
                credentials = flow.run_local_server(open_browser=False)

            with open(Const.Path.TOKEN, 'w') as token:
                token.write(credentials.to_json())

        return credentials

    def copy_template_file(self, mode_year_month):
        '''テンプレートファイルをコピーし、そのファイルのキーを返す'''
        new_file_body = {
            'name': self._get_filename_to_create(mode_year_month),
            'parents': [self.__destination_folder_id]
        }

        try:
            new_file = self.__drive_service.files().copy(fileId=self.__template_file_key, body=new_file_body).execute()
            time.sleep(1)
        except HttpError:
            raise

        return new_file['id']

    def _get_filename_to_create(self, mode_year_month):
        if mode_year_month.mode == Const.Mode.MONTH:
            return f'{mode_year_month.year}{mode_year_month.months[0]}'

        if mode_year_month.mode == Const.Mode.YEAR:
            return f'{mode_year_month.year}'

        raise InvalidModeError

    def write_data(self, file_key, data):
        try:
            spreadsheet = self.__gspread_client.open_by_key(file_key)
        except APIError:
            raise

        try:
            worksheet = spreadsheet.worksheet('Data')
        except WorksheetNotFound:
            raise

        start_row = 3
        goal_row = start_row + len(data) - 1

        worksheet.update(f'B{start_row}:C{goal_row}', [[key, value] for key, value in data.items()], value_input_option='USER_ENTERED')
        time.sleep(1)
