# zabbixonboarding
Onboarding large no of servers to Zabbix using Google spreadsheet. In this project there are four zabbix servers located in dc1, dc2, dc3, dc4 and a zabbix proxy in dn5. Hosts are located in all of the data centres and monitored via proxies to distribute load.

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
* Spreadsheet Name : server_details
* Sheet Name : servers

| hostname | ip | dns | location | os | environment | product | sub system | {$SERVICES} | isAgent | status | onboarding status |
|----------|----|-----|----------|----|-------------|---------|------------|-------------|---------|--------|-------------------|
| eg: server1  |10.1.1.1|server1.local|dc1|Linux|production|ERP|SD|httpd,mssql|yes|add| |

### Configuring oauth for Google

* Go to https://console.developers.google.com/apis/credentials
* Create a new project
* Create new JSON service account key under credentials
* Place your JSON file in the project folder
* Share your Google spreadsheet with the email id specified in the JSON credential file.


Obtain Google api credentials as instruct in [Using OAuth2 for Authorization
](http://gspread.readthedocs.io/en/latest/oauth2.html) section

### Configuring Cronjob










