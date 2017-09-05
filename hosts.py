import sys
from validate import remove_empty_keys
from hostgroups import create_group
from templates import create_template


# Function to check host already exists
def hostexists(hostname, zapi):
    if zapi.host.get(
            {
                "output": "extend",
                "filter":
                    {
                        "name": [hostname]
                    }
            }
    ):
        return True
    else:
        return False


# Function to add host information.
# Based on the parameters this will perform various task.
# if macro value has not defined both macro and value are removed
def create_host(i, INFO, zapi, worksheet):
    macro_dict = [
        {
            "macro": "{$SERVICES}",
            "value": INFO['services']
        }
    ]
    macro_params = remove_empty_keys(macro_dict)
    essential_param = {
        "host": INFO['hostname'],
        "interfaces": [{
            "type": 2 if INFO['isagent'] is None else 1,
            "main": 1,
            "useip": 1 if INFO['ip'] else 0,
            "ip": INFO['ip'],
            "dns": INFO['dns'],
            "port": 161 if INFO['isagent'] is None else 10050,
        }],
        "groups": [{
            "groupid": create_group(group, zapi)} for group in INFO['groups'] if group],
        "templates": [{
            "templateid": create_template('os', INFO['templates']['os'], zapi)}],
        "proxy_hostid": zapi.proxy.get({
            "output": "extend",
            "selectInterface": "extend",
            "filter": {"host": INFO['proxy']}})[0]['proxyid'], }
    if len(macro_params) > 0:
        essential_param['macros'] = macro_params
    if hostexists(INFO['hostname'], zapi) is False:
        print essential_param
        try:
            create = zapi.host.create(essential_param)
            result = create['hostids']
            print INFO['hostname'] + " created"
            worksheet.update_cell(i, 11, 'completed')
            worksheet.update_cell(i, 12, '')
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    else:
        result = (zapi.host.get({"filter": {"name": INFO['hostname']}})[0]['hostid'])
        print "host with a " + INFO['hostname'] + " already exists"
        worksheet.update_cell(i, 12, 'host already exists')
    return result


# Function for updating existing host information.
def update_host(i, INFO, zapi, worksheet):
    macro_dict = [
        {
            "macro": "{$SERVICES}",
            "value": INFO['services']
        }
    ]
    macro_params = remove_empty_keys(macro_dict)
    print INFO['isagent']
    host_interface_id = zapi.hostinterface.get({
        "filter": {
            "hostid": INFO['hostid'],
            "type": 2 if INFO['isagent'] is None else 1,
            "main": 1}})[0]['interfaceid']
    interface_param = {
        "interfaceid": host_interface_id,
        "type": 2 if INFO['isagent'] is None else 1,
        "main": 1,
        "useip": 1 if INFO['ip'] else 0,
        "dns": INFO['dns'],
        "ip": INFO['ip'],
        "port": 161 if INFO['isagent'] is None else 10050}
    interface_update = zapi.hostinterface.update(interface_param)
    print "hostname updated with new interface id ", \
        interface_update['interfaceids'][0]
    essential_param = {
        "hostid": INFO['hostid'],
        "host": INFO['hostname'],
        "groups": [{
            "groupid": create_group(group, zapi)} for group in INFO['groups'] if group],
        "templates": [{
            "templateid": create_template('os', INFO['templates']['os'], zapi)}],
        "inventory_mode": 0,
        "inventory": {
            "os_short": INFO['inv_os'],
            "tag": INFO['inv_tag'],
            "contact": INFO['inv_contact'],
            "notes": INFO['remarks']},
        "macros": macro_params,
        "status": 1 if 'Decommissioned' in INFO['groups'] else 0}
    try:
        print essential_param
        update = zapi.host.update(essential_param)
        result = update['hostids']
        print INFO['hostname'] + " updated"
        print i
        worksheet.update_cell(i, 11, 'completed')
        worksheet.update_cell(i, 12, '')
        return result
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


def findhost(zapi, ip):
    hostid = zapi.hostinterface.get(
        {
            "output": "extend",
            "searchWildcardsEnabled": "true",
            "search":
                {
                    "ip": ip
                }
        })[0]['hostid']
    print hostid
    return hostid


def findhostproxy(zapi, ip):
    hostid = findhost(zapi, ip)
    proxyid = zapi.host.get({
        "output": "extend",
        "filter": {
            "hostid": [
                hostid
            ]
        }
    })[0]['proxy_hostid']
    proxyname = zapi.proxy.get({
        "output": "extend",
        "filter": {
            "proxyid": proxyid
        }
    })[0]['host']
    return proxyname
