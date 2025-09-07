# coding: utf-8


import io

import matplotlib.pyplot as plt

from .consts import *


class Graph:
    def __init__(self, mode_year_months, data_dict):
        date_list = list(data_dict.keys())
        weight_list = list(data_dict.values())

        width = Consts.GRAPH_WIDTH_MONTHLY if mode_year_months.mode == Consts.MODE_MONTH else Consts.GRAPH_WIDTH_ANNUAL
        title = f'{mode_year_months.year}/{mode_year_months.months[0]}' if mode_year_months.mode == Consts.MODE_MONTH else str(mode_year_months.year)

        plt.figure(figsize=(width, 4.8))
        plt.title(title)
        plt.xticks([])  # 目盛り非表示
        plt.ylim(min(weight_list) - 5, max(weight_list) + 5)
        plt.grid(axis='y', color='gray', alpha=0.3)
        plt.plot(date_list, weight_list)

        sio = io.BytesIO()
        plt.savefig(sio, format='png')

        self.__sio = sio

    @property
    def sio(self):
        return self.__sio
