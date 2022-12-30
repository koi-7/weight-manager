<p align="center">
  <img src="https://user-images.githubusercontent.com/61448492/210031735-1184ad44-0de3-45d1-a52c-da6279deacf2.png">
</p>

# Weight manager with Notion

This weight manager fetches the weight data in Notion, then shows and lists its data.

# Usage

## Notion

Type `/` and create a new database.

<img src="https://user-images.githubusercontent.com/61448492/209896805-8335e633-a994-4905-ac22-45ca74dfd617.png" height="40%" width="40%">

<img src="https://user-images.githubusercontent.com/61448492/209896812-62c7552a-6738-4d75-b2cf-a623e9c03b9a.png" height="40%" width="40%">

Change the type of the second column from `Multi-select` to `Number`.

<img src="https://user-images.githubusercontent.com/61448492/209896816-2747eb57-2e08-4782-8933-be17008a65c0.png" height="40%" width="40%">

Change the column name of `Name` and `Tags` to `Date` and `Weight`.

<img src="https://user-images.githubusercontent.com/61448492/209899345-1aeb05ce-7524-44dd-865f-48f172975f50.png" height="40%" width="40%">

Then record date and weight. My weight is TOP SECRET😎.

<img src="https://user-images.githubusercontent.com/61448492/209896820-f3fcd6b7-262b-4c56-8584-2c5de68f201a.png" height="40%" width="40%">

## Setup in command line

Set your database URL and Notion API token.

You can get the database URL to click `…` on the right top and `Copy link to view`.

<img src="https://user-images.githubusercontent.com/61448492/209898378-4826b67e-c483-4faf-a531-e2fa0cffc14a.png" height="40%" width="40%">

For Notion API token, please look up by yourself.

``` bash
$ ./main --set
Input DB URL: https://www.notion.so/.../...?v=...
Input Token: secret_...
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

# Examples

My weight is TOP SECRET😎😎.

## List

<img src="https://user-images.githubusercontent.com/61448492/209899610-94dfa7b5-c605-4b65-92a9-d958e986c291.png">

## Graph

<img src="https://user-images.githubusercontent.com/61448492/209900232-b908eb4d-7004-4a59-a361-ec5165504ff0.png">
