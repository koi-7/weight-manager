# coding: utf-8


import io

import matplotlib.pyplot as plt

from .consts import *
from .mode import *


class Graph:
    def __init__(self, sio):
        self.__sio = sio

    @property
    def sio(self):
        return self.__sio

    @classmethod
    def create_instance(self, mode, title, data_dict):
        date_list = list(data_dict.keys())
        weight_list = list(data_dict.values())

        width = Consts.GRAPH_WIDTH_MONTHLY if mode == Consts.MODE_MONTH else Consts.GRAPH_WIDTH_ANNUAL
        plt.figure(figsize=(width, 4.8))
        plt.title(title)
        plt.xticks([])  # 目盛り非表示
        plt.ylim(min(weight_list) - 5, max(weight_list) + 5)
        plt.grid(axis='y', color='gray', alpha=0.3)
        plt.plot(date_list, weight_list)

        sio = io.BytesIO()
        plt.savefig(sio, format='png')

        return Graph(sio)
