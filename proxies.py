import random

# List of zabbix proxies for different zabbix instances
dc1_proxies = [
    'dc1zabbixproxy01',
    'dc1zabbixproxy02'
]
dc2_proxies = [
    'dc2zabbixproxy01',
    'dc2zabbixproxy02'
]
dc3_proxies = [
    'dc3zabbixproxy01',
    'dc3zabbixproxy02'
]
dc4_proxies = [
    'dc4zabbixproxy01',
    'dc4zabbixproxy02'
]
""" In this scenario dc5 proxies will be connected to dc1 zabbix server"""
dc5_proxies = [
    'dn5zabbixproxy01',
    'dn5zabbixproxy02'
]


def proxyassigned(location):
    if location == "dc1":
        proxy = random.choice(dc1_proxies)
        return proxy

    if location == "dc2":
        proxy = random.choice(dc2_proxies)
        return proxy

    if location == "dc3":
        proxy = random.choice(dc3_proxies)
        return proxy

    if location == "dc4":
        proxy = random.choice(dc4_proxies)
        return proxy

    if location == "dc5":
        proxy = random.choice(dc5_proxies)
        return proxy
