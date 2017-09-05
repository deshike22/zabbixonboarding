import sys


# Function to check hostgroup already exists
def hostgroupexists(hostgroup, zapi):
    if zapi.hostgroup.get({"output": "extend", "filter": {"name": [hostgroup]}}):
        return True
    else:
        return False


# Function for creating hostgroups based on the group name provided
def create_group(hostgroup, zapi):
    if hostgroupexists(hostgroup, zapi) is False:
        try:
            create = zapi.hostgroup.create({'name': hostgroup})
            result = create['groupids'][0]
            print "hostgroup created with id ", result
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

    else:
        result = (zapi.hostgroup.get({
            "filter": {
                "name": hostgroup}})[0]['groupid'])
    return result
