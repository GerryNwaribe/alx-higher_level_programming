#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = set()
    sum = 0
    for a in my_list:
        if a not in result:
            result.add(a)
            sum = sum + a

    return sum
