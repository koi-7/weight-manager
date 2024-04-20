<p align="center">
  <img src="https://github.com/koi-7/weight-manager/assets/61448492/b76b819d-3d0c-40c8-929d-54be87a600e6">
</p>

# weight-manager

Notion に記録した体重の記録をグラフにして Slack で通知する

## usage

### ダウンロード

``` bash
$ cd ~
$ git clone https://github.com/koi-7/weight-manager.git
```

### `weight-manager/config/config.ini` の準備

`weight-manager/config/template.ini` を参考に、Notion と Slack についての設定ファイル `weight-manager/config/config.ini` を作成する

### requirements

``` bash
$ pip3 install -r weight-manager/requirements.txt
```

### 好きな場所に配置（例: `/opt/` 配下）

``` bash
$ sudo mv ~/weight-manager/ /opt/
```

### 実行

実行すると引数として指定した年 / 年月の体重遷移グラフが Slack に投稿される

月指定

``` bash
$ cd /opt/weight-manager/
$ python3 -m weight-manager 2024/01
```

![](https://github.com/koi-7/weight-manager/assets/61448492/c583ef4e-34fb-41f4-9ba4-7d6ae5968d81)

年指定

``` bash
$ cd /opt/weight-manager/
$ python3 -m weight-manager 2024
```

![](https://github.com/koi-7/weight-manager/assets/61448492/343241fb-886d-47be-95b6-9354a714e4a7)

## Example

スクリプトをサーバ上において例えば以下のように Cron を設定しておけば月末にその年 / 月のグラフレポートが Slack で通知される（環境: Ubuntu）

``` bash
$ crontab -e
```

```
CRON_TZ=Asia/Tokyo
PYTHONPATH=$PYTHONPATH:/opt/weight-manager/
55 23 28-31 * * /usr/bin/test $(date -d '+1 day' +\%d) -eq 1 && /usr/bin/python3 -m weight-manager $(date +\%Y/\%m)
56 23 31 12 * /usr/bin/python3 -m weight-manager $(date +\%Y)
```

タイムゾーンを反映するために cron 再起動

```
$ sudo systemctl restart cron
```
