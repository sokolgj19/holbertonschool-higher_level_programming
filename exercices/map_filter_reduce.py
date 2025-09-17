from functools import reduce

# 1. Double numbers
def double_numbers_loop(numbers):
    result = []
    for x in numbers:
        result.append(x * 2)
    return result

def double_numbers_map(numbers):
    return list(map(lambda x: x * 2, numbers))


# 2. Keep only even numbers
def filter_even_loop(numbers):
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x)
    return result

def filter_even_filter(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


# 3. Sum of numbers
def sum_numbers_loop(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

def sum_numbers_reduce(numbers):
    return reduce(lambda acc, x: acc + x, numbers)