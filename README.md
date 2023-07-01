<p align="center">
  <img src="https://github.com/koi-7/weight-manager/assets/61448492/1551425f-bd35-4490-b020-cedbd36ae586">
</p>

# weight-manager

日々 Notion に記録した体重の記録をグラフにして Slack で通知する

## usage

### ダウンロード

``` bash
$ git clone https://github.com/koi-7/weight-manager.git
```

### ファイルの用意

`data` ディレクトリに以下のファイル（中身はそれぞれ 1 行）を入れておく

- `notion_database_url`: Notion の DB の URL
- `notion_token`: Notion のトークン
- `slack_channel_id`: Slack のチャンネル ID
- `slack_token`: Slack のトークン

Notion、Slack の設定等については省略

hint: ディレクトリ構成

```
weight-manager
|-- README.md
|-- data
|   |-- notion_database_url
|   |-- notion_token
|   |-- slack_channel_id
|   `-- slack_token
|-- requirements.txt
`-- weight-manager
    |-- __init__.py
    |-- __main__.py
    `-- functions.py
```

### requirements

``` bash
$ pip3 install -r requirements.txt
```

### 実行

``` bash
python3 -m weight-manager
```

実行すると**先月の**体重遷移グラフが Slack に投稿される

![](https://github.com/koi-7/weight-manager/assets/61448492/7c58300c-2aba-453e-b9a3-11bf88ff5bca)
