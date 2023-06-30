import io

import matplotlib.pyplot as plt
import requests


class Functions:
    def __init__(self):
        pass

    @classmethod
    def get_dbid(self, path):
        with open(path, 'r') as f:
            url =  f.readline().rstrip('\n')
        l = url.split('/')
        return l[4].split('?')[0]

    @classmethod
    def get_token(self, path):
        with open(path, 'r') as f:
            return f.readline().rstrip('\n')

    @classmethod
    def read_records(self, db_id, notion_token, year_month):
        url = 'https://api.notion.com/v1/databases/' + db_id + '/query'
        headers = {'Authorization': 'Bearer ' + notion_token,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Notion-Version': '2022-06-28'}

        response = requests.post(url=url, headers=headers)
        json_data = response.json()
        results = json_data.get('results')

        data_dict = {}
        for result in results:
            date = result['properties']['Date']['title'][0]['text']['content']
            weight = result['properties']['Weight']['number']

            if date[:-3] == year_month:
                data_dict[date] = weight

        return dict(sorted(data_dict.items()))

    @classmethod
    def savefig_to_memory(self, record_dict):
        date_list = list(record_dict.keys())
        weight_list = list(record_dict.values())

        fig = plt.figure()
        plt.subplots_adjust(bottom=0.2)
        ax = fig.add_subplot(1, 1, 1)
        ax.grid(which = "major", axis = "y", color = "gray",
                alpha = 0.3, linestyle = "-", linewidth = 1)
        plt.ylim(85, 95)
        plt.plot(date_list, weight_list)
        plt.xticks(rotation=90)
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
