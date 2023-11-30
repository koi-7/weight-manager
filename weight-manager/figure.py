# coding: utf-8


import io

import matplotlib.pyplot as plt


class Figure:
    def __init__(self, title):
        self.__title = title
        self.__sio = io.BytesIO()

    @property
    def sio(self):
        return self.__sio

    @sio.setter
    def date(self, sio):
        self.__sio = sio

    @property
    def title(self):
        return self.__title

    def savefig_to_memory(self, record_dict):
        date_list = list(record_dict.keys())
        weight_list = list(record_dict.values())

        plt.figure(figsize=(12, 4.8))
        plt.title(self.title)
        plt.xticks([])  # 目盛り非表示
        plt.ylim(min(weight_list) - 5, max(weight_list) + 5)
        plt.grid(axis='y', color='gray', alpha=0.3)
        plt.plot(date_list, weight_list)
        plt.savefig(self.sio, format='png')
