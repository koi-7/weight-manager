# Weight manager with Notion

Fetch weight data in Notion and show, list its data.

# Usage

Set your database URL and Notion API token.

``` bash
$ ./main --set
Input DB URL: https://www.notion.so/<username>/<DB ID>?v=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Input Token: secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Show or list your data with option.

``` bash
$ ./main <option>
```

# Options

|  option  |  description  |
| ---- | ---- |
| -h, --help | show help message |
| --list N | show recent N records |
| --graph | show graph |
| --set | set db_url and token |
