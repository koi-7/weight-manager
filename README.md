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
- `slack_channel_url`: Slack のチャンネル URL
- `slack_token`: Slack のトークン

![](https://github.com/koi-7/weight-manager/assets/61448492/1ed13ebd-ead9-4c68-9169-60a3bab3722b)

Notion、Slack の設定等については省略

hint: ディレクトリ構成

```
weight-manager
|-- README.md
|-- data
|   |-- notion_database_url
|   |-- notion_token
|   |-- slack_channel_url
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

実行するとその月の体重遷移グラフが Slack に投稿される

![](https://github.com/koi-7/weight-manager/assets/61448492/7c58300c-2aba-453e-b9a3-11bf88ff5bca)

## Example

スクリプトをサーバ上において例えば以下のように Cron を設定しておけば月末にはその月のグラフレポートを Slack 上で確認できる

``` bash
$ crontab -e
```

```
CRON_TZ=Asia/Tokyo
PYTHONPATH=$PYTHONPATH:/opt/weight-manager/
55 23 28-31 * * /usr/bin/test $(date -d '+1 day' +\%d) -eq 1 && /usr/bin/python3 -m weight-manager
```
