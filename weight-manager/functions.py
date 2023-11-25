import datetime
import io

import matplotlib.pyplot as plt
import requests


class Functions:
    def __init__(self):
        pass

    @classmethod
    def read_records(self, db_id, notion_token, exec_date):
        url = 'https://api.notion.com/v1/databases/' + db_id + '/query'
        headers = {'Authorization': 'Bearer ' + notion_token,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Notion-Version': '2022-06-28'}

        response = requests.post(url=url, headers=headers)
        json_data = response.json()
        results = json_data.get('results')

        data_dict = {}
        for result in results:
            date = datetime.datetime.strptime(result['properties']['Date']['title'][0]['text']['content'], '%Y/%m/%d')
            weight = result['properties']['Weight']['number']

            if date.strftime('%Y/%m') == exec_date.strftime('%Y/%m'):
                data_dict[date] = weight

        return dict(sorted(data_dict.items()))

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

    @classmethod
    def send_notify(self, sio, slack_token, slack_channel):
        api_url = 'https://slack.com/api/files.upload'
        headers = {'Authorization': 'Bearer ' + slack_token}
        params = {'channels': slack_channel}
        files = {'file': sio.getvalue()}

        requests.post(api_url, headers=headers, params=params, files=files)
