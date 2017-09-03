# zabbixonboarding
Onboarding large no of servers to Zabbix using Google spreadsheet

##Requirements
python 2.7
gspread
oauth

##Installation
For RedHat based installations
yum install python
yum install python-pip
pip install gspread
pip install oauth
pip install zabbix

For Debian based installations
apt-get install python
apt-get install python-pip
pip install gspread
pip install zabbix

##Configuration
###Configuring Google Spreadsheet
Create a new Google spreadsheet with following information
Spreadsheet Name = Servers
Sheet Name = Sheet1
Sheet1 Column names starting at row 1
    hostname
    ip
    dns
    os
    environment
    product
    sub system
    MACROS
    status
    onboarding status







