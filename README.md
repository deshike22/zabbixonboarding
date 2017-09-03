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
4. pip install oauth
5. pip install zabbix

### For Debian based installations
1. apt-get install python
2. apt-get install python-pip
3. pip install gspread
4. pip install zabbix

## Configuration
### Configuring Google Spreadsheet
Create a new Google spreadsheet with following information
* Spreadsheet Name : Servers
* Sheet Name : Sheet1

| hostname | ip | dns | os | environment | product | sub system | {$SERVICES} | status | onboarding status |
|----------|----|-----|----|-------------|---------|------------|--------|--------|-------------------|
| eg: server1  |10.1.1.1|server1.local|Linux|production|ERP|SD|httpd,mssql|add| |

### Configuring oauth for Google



### Configuring Cronjob










