import copy


# removing empty values in a key value pair dictionary
def remove_empty_keys(x):
    d = copy.copy(x)
    for item in x:
        for k in item.viewvalues():
            if k == '':
                d.remove(item)
    return d
