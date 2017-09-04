# zabbixonboarding
Onboarding large no of servers to Zabbix using Google spreadsheet

## Requirements
* python 2.7
* gspread
* oauth

## Installation
### For RedHat based installations
1. yum install python
2. yum install python-pip
3. pip install gspread
4. pip install --upgrade oauth2client 
5. pip install zabbix_api

### For Debian based installations
1. apt-get install python
2. apt-get install python-pip
3. pip install gspread
4. pip install --upgrade oauth2client
5. pip install zabbix_api

## Configuration
### Configuring Google Spreadsheet
Create a new Google spreadsheet with following information
* Spreadsheet Name : Servers
* Sheet Name : Sheet1

| hostname | ip | dns | os | environment | product | sub system | {$SERVICES} | status | onboarding status |
|----------|----|-----|----|-------------|---------|------------|--------|--------|-------------------|
| eg: server1  |10.1.1.1|server1.local|Linux|production|ERP|SD|httpd,mssql|add| |

### Configuring oauth for Google

* Go to https://console.developers.google.com/apis/credentials
* Create a new project
* Create new JSON service account key under credentials
* Place your JSON file in the project folder
* Share your Google spreadsheet with the email id specified in the JSON credential file.


Obtain Google api credentials as instruct in [Using OAuth2 for Authorization
](http://gspread.readthedocs.io/en/latest/oauth2.html) section

### Configuring Cronjob










