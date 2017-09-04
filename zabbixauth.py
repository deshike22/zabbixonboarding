import sys
from zabbix_api import ZabbixAPI

# List of zabbix Server urls
server_dc1 = 'http://dc1zabbix.local'
server_dc2 = 'http://dc2zabbix.local'
server_dc3 = 'http://dc3zabbix.local'
server_dc4 = 'http://dc4zabbix.local'


# A common username and password for all zabbix instances
username = 'Admin'
password = 'zabbixpwd'

# Function to authenticate Zabbix using the credentials provided
def zabbix_auth(server, username, password):
    try:
        zapi = ZabbixAPI(server)
        zapi.login(username, password)
        return zapi
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


def serverassigned(location):
    # when your dc5 is monitored through a zabbix proxy and when it is connected to the same dc1 zabbix server
    if location in ('dc1','dc5'):
        zapi = zabbix_auth(server_dc1, username, password)
        return zapi

    if location == "dc2":
        zapi = zabbix_auth(server_dc2, username, password)
        return zapi

    if location == "dc3":
        zapi = zabbix_auth(server_dc3, username, password)
        return zapi

    if location == "dc3":
        zapi = zabbix_auth(server_dc4, username, password)
        return zapi

