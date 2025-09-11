#!/usr/bin/python3

def common_elements(set_1, set_2):
    final_set = set()
    for element in set_1:
        for element2 in set_2:
            if element == element2:
                final_set.add(element)
    return final_set
