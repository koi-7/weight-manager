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
        request_url = 'https://api.notion.com/v1/databases/' + db_id + '/query'
        headers = {'Authorization': 'Bearer ' + notion_token,
                   'Content-Type': 'application/json; charset=UTF-8',
                   'Notion-Version': '2022-06-28'}

        response = requests.post(url=request_url, headers=headers)

        json_data = response.json()
        results = json_data.get('results')

        date_list = [r['properties']['Date']['title'][0]['text']['content'] for r in results]
        weight_list = [r['properties']['Weight']['number'] for r in results]

        data_dict = dict(zip(date_list, weight_list))

        return dict(sorted(data_dict.items()))

    @classmethod
    def save_fig_to_memory(self, date_list, weight_list):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.grid(which = "major", axis = "y", color = "gray",
                alpha = 0.3, linestyle = "-", linewidth = 1)
        plt.plot(date_list, weight_list)
        plt.xticks(rotation=90)
        sio = io.BytesIO()
        plt.savefig(sio, format='png')

        plt.close(fig)

        return sio

    @classmethod
    def get_slack_token(self, path):
        with open(path, 'r') as f:
            return f.readline().rstrip('\n')


