# __author__ = 'deshike22'
import sys
import copy
from googledata import spreadsheetdata
from proxies import proxyassigned
from zabbixauth import serverassigned
from infotemplate import HOSTINFO
import hosts

# Server information Google spreadsheet details
GoogleSpreadsheetURL = 'https://goo.gl/zFkkA1'
GoogleSheetName = 'servers'

worksheet, values_list = spreadsheetdata(GoogleSpreadsheetURL, GoogleSheetName)
for line in values_list:
    i = line.row
    INFO = copy.deepcopy(HOSTINFO)
    INFO['hostname'] = worksheet.cell(i, 1).value.lower()
    INFO['ip'] = worksheet.cell(i, 2).value
    INFO['dns'] = worksheet.cell(i, 3).value.lower()
    INFO['location'] = worksheet.cell(i, 4).value.lower()
    os = worksheet.cell(i, 5).value
    environment = worksheet.cell(i, 6).value.lower()
    product = worksheet.cell(i, 7).value
    sub_sys = worksheet.cell(i, 8).value
    INFO['services'] = worksheet.cell(i, 9).value
    INFO['isagent'] = worksheet.cell(i, 10).value
    INFO['status'] = worksheet.cell(i, 11).value.lower()
    INFO['groups'].append(environment)
    INFO['groups'].append(os + " servers")
    INFO['groups'].append(product + " " + environment)
    INFO['groups'].append(sub_sys + " " + environment) if len(sub_sys) > 0 \
        else INFO['groups'].append('')
    if INFO['isagent'] == 'yes':
        INFO['templates']['os'] = "Template OS " + os
    else:
        INFO['templates']['os'] = "Template SNMP OS " + os
    if INFO['status'] == "add":
        try:
            zapi = serverassigned(INFO['location'])
            """Find if there are hosts already added """
            try:
                INFO['hostid'] = hosts.findhost(zapi, INFO['ip'])
                INFO['proxy'] = hosts.findhostproxy(zapi, INFO['ip'])
                hostid = hosts.update_host(i, INFO, zapi, worksheet)
            except:
                INFO['proxy'] = proxyassigned(INFO['location'])
                hostid = hosts.create_host(i, INFO, zapi, worksheet)
        except:
            print "Unexpected error:", sys.exc_info()
            worksheet.update_cell(i, 12, sys.exc_info())
            pass
    elif INFO['status'] == "update":
        try:
            zapi = serverassigned(INFO['location'])
            INFO['proxy'] = proxyassigned(INFO['location'])
            try:
                INFO['hostid'] = hosts.findhost(zapi, INFO['ip'])
            except:
                INFO['hostid'] = (zapi.host.get({"filter": {"name": INFO['hostname']}})[0]['hostid'])
            hostid = hosts.update_host(i, INFO, zapi, worksheet)
        except:
            print "Unexpected error:", sys.exc_info()
            worksheet.update_cell(i, 12, sys.exc_info())
            pass
    else:
        continue
