# coding: utf-8


from datetime import datetime
import os
import re
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
    def __init__(self, config_ini, mode_year_months):
        self.__template_file_key = \
            config_ini['Google']['template_month_file_key'] if mode_year_months.mode == Const.Mode.MONTH \
            else config_ini['Google']['template_year_file_key']
        self.__destination_folder_id = config_ini['Google']['destination_folder_id']

        credentials = self._create_credentials()

        self.__drive_service = build(Const.GoogleApi.SERVICE_NAME, Const.GoogleApi.VERSION, credentials=credentials)
        self.__gspread_client = gspread.authorize(credentials)

    def _create_credentials(self):
        '''Google 認証のための credencials を作成する'''
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

    def copy_template_file(self, mode_year_months):
        '''テンプレートファイルをコピーし、そのファイルのキーを返す'''
        new_file_body = {
            'name': self._get_filename_to_create(mode_year_months),
            'parents': [self.__destination_folder_id]
        }

        try:
            new_file = self.__drive_service.files().copy(fileId=self.__template_file_key, body=new_file_body).execute()
            time.sleep(1)
        except HttpError:
            raise

        return new_file['id']

    def _get_filename_to_create(self, mode_year_months):
        '''モードに合ったファイル名を取得する'''
        if mode_year_months.mode == Const.Mode.MONTH:
            return f'{mode_year_months.year}{mode_year_months.months[0]}'

        if mode_year_months.mode == Const.Mode.YEAR:
            return f'{mode_year_months.year}'

        raise InvalidModeError

    def write_data(self, file_key, data):
        '''ファイルのデータを書き込む'''
        try:
            spreadsheet = self.__gspread_client.open_by_key(file_key)
        except APIError:
            raise

        try:
            worksheet = spreadsheet.worksheet('Data')
        except WorksheetNotFound:
            raise

        weight_start_cell_address = self._get_cell_address_next_door(Const.GoogleApi.TEMPLATE_FILE_DATE_START_CELL_ADDRESS)
        weight_column_letter, _ = self._parse_cell_address(weight_start_cell_address)

        start_row_index, _ = gspread.utils.a1_to_rowcol(Const.GoogleApi.TEMPLATE_FILE_DATE_START_CELL_ADDRESS)
        end_row_index = start_row_index + len(data) - 1

        worksheet.update(f'{Const.GoogleApi.TEMPLATE_FILE_DATE_START_CELL_ADDRESS}:{weight_column_letter}{end_row_index}', [[key, value] for key, value in data.items()], value_input_option='USER_ENTERED')
        time.sleep(1)

        worksheet.delete_rows(end_row_index + 1, 400)
        time.sleep(1)

    def _get_cell_address_next_door(self, cell_address):
        '''渡されたセルアドレスの隣のセルアドレスを返す'''
        row_index, column_index = gspread.utils.a1_to_rowcol(cell_address)
        column_index_next_door = column_index + 1
        return gspread.utils.rowcol_to_a1(row_index, column_index_next_door)

    def _parse_cell_address(self, cell_address):
        '''セルアドレスを列部分と行部分に分ける'''
        re_cell = re.fullmatch(r'([A-Z]+)(\d+)', cell_address)
        return re_cell.group(1), re_cell.group(2)
