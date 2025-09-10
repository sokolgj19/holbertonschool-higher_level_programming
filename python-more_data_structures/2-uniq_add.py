#!/usr/bin/python3

def uniq_add(my_list=[]):
    seen_numbers = []
    total = 0
    for number in my_list:
        if number not in seen_numbers:
            seen_numbers.append(number)
            total += number
    return total
