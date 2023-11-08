#!/usr/bin/python3
def common_elements(set_1, set_2):
    for a in set_1:
        for b in set_2:
            if a in set_2:
                return a
