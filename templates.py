# Function to create templates for service monitoring.
def create_template(servicetype, service, zapi):
    service = str(service)
    priority = 5
    status = 0
    if servicetype == "ssh":
        templatename = "Template SSH " + service
        applicationname = service
        itemname = service
        item_type = 13
        item_key = "ssh.run[" + service + "]"
        serviceuser = "{$SSH_GLOBAL_USR}"
        servicepass = "{$SSH_GLOBAL_PWD}"
        value_type = 4
        params = "ps -aux | grep " + service
        triggername = service + " Service Failed on {HOST.NAME}"
        expression = "{" + templatename + ":" + item_key + ".str(root)}=0"

    if servicetype == "os":
        templatename = service
        templateid = zapi.template.get({
            "filter": {"name": templatename}})[0]["templateid"]
        return templateid

    if zapi.template.exists({"name": templatename}):
        templateid = zapi.template.get({
            "filter": {"name": templatename}})[0]["templateid"]
        zapi.template.update({"templateid": templateid, "name": templatename})
        if zapi.application.exists({"name": applicationname}):
            applicationid = zapi.application.get({
                "filter": {"name": applicationname}})[0]["applicationid"]
            zapi.application.update({
                "applicationid": applicationid, "name": applicationname})
            if zapi.item.exists({"name": itemname}):
                itemId = zapi.item.get({
                    "filter": {"name": itemname}})[0]["itemid"]
                zapi.item.update({
                    "applications": [applicationid],
                    "itemid": itemId,
                    "name": itemname,
                    "key_": item_key,
                    "type": item_type,
                    "value_type": value_type,
                    "params": params
                })
                if zapi.trigger.exists({"expression": expression}):
                    triggerid = zapi.trigger.getobjects({
                        "description": triggername})[0]['triggerid']
                    zapi.trigger.update({
                        "triggerid": triggerid,
                        "description": triggername,
                        "expression": expression,
                        "priority": priority,
                        "status": status
                    })
        return templateid
    else:
        print templatename
        groupid = zapi.hostgroup.get({
            "output": "extend",
            "filter": {"name": ["Templates"]}})[0]['groupid']

        print "Template Group created with Group Id", groupid
        templateid = zapi.template.create({
            "host": templatename,
            "groups": {"groupid": groupid[0]}})['templateids']
        print "Template created with template id ", templateid[0]
        applicationid = zapi.application.create({
            "name": applicationname,
            "hostid": templateid[0]})['applicationids']
        print "Application created with application id ", applicationid[0]
        itemId = zapi.item.create({
            "name": itemname,
            "key_": item_key,
            "hostid": templateid[0],
            "username": serviceuser,
            "password": servicepass,
            "params": params,
            "type": item_type,
            "value_type": value_type,
            "delay": 30,
            "history": 7,
            "applications": [applicationid[0]]})['itemids']
        print "Item created with item id ", itemId[0]
        triggerid = zapi.trigger.create({
            "description": triggername,
            "expression": expression,
            "priority": priority,
            "status": status})['triggerids']
        print "Trigger created with trigger id ", triggerid[0]
        print "Template Created Successfully with id ", templateid[0]
        return templateid[0]
