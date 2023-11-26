# coding: utf-8


import io

import matplotlib.pyplot as plt


class Functions:
    def __init__(self):
        pass

    @classmethod
    def savefig_to_memory(self, record_dict):
        date_list = list(record_dict.keys())
        weight_list = list(record_dict.values())

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.grid(which = "major", axis = "y", color = "gray",
                alpha = 0.3, linestyle = "-", linewidth = 1)
        ax.axes.xaxis.set_visible(False)
        plt.title(date_list[0].strftime('%Y/%m'))
        plt.ylim(min(weight_list) - 5, max(weight_list) + 5)
        plt.plot(date_list, weight_list)
        sio = io.BytesIO()
        plt.savefig(sio, format='png')
        plt.close(fig)

        return sio
