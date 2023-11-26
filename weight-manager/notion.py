# coding: utf-8


class Notion:
    def __init__(self, database_id, token):
        self.__database_id = database_id
        self.__token = token

    @property
    def database_id(self):
        return self.__database_id

    @property
    def token(self):
        return self.__token
