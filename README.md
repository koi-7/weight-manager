<p align="center">
  <img src="https://github.com/koi-7/weight-manager/assets/61448492/b76b819d-3d0c-40c8-929d-54be87a600e6">
</p>

# weight-manager

日々 Notion に記録した体重の記録をグラフにして Slack で通知する

## usage

### ダウンロード

``` bash
$ cd ~
$ git clone https://github.com/koi-7/weight-manager.git
```

### `config/config.ini` の準備

`config/sample.ini` を参考に、Notion と Slack についての設定ファイル `config/config.ini` を作成する

### requirements

``` bash
$ pip3 install -r requirements.txt
```

### 好きな場所に配置（例: `/opt/` 配下）

``` bash
$ sudo mv weight-manager/ /opt/
```

### 実行

``` bash
$ cd /opt/weight-manager/
$ python3 -m weight-manager
```

実行するとその月の体重遷移グラフが Slack に投稿される

![](https://github.com/koi-7/weight-manager/assets/61448492/7c58300c-2aba-453e-b9a3-11bf88ff5bca)

## Example

スクリプトをサーバ上において例えば以下のように Cron を設定しておけば月末にその月のグラフレポートが Slack で通知される

``` bash
$ crontab -e
```

```
CRON_TZ=Asia/Tokyo
PYTHONPATH=$PYTHONPATH:/opt/weight-manager/
55 23 28-31 * * /usr/bin/test $(date -d '+1 day' +\%d) -eq 1 && /usr/bin/python3 -m weight-manager
```

タイムゾーンを反映するために cron 再起動

```
$ sudo systemctl restart cron
```
