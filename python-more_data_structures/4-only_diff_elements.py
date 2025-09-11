#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    final_set = set()
    final_set = set_1.symmetric_difference(set_2)
    return final_set
