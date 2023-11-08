#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for a in my_list:
        if a == search:
            result.append(replace)
        else:
            result.append(a)
    return result
