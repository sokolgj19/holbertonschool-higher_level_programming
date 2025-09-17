from map_filter_reduce import double_numbers_loop, double_numbers_map, filter_even_loop, filter_even_filter, sum_numbers_loop, sum_numbers_reduce

numbers = [1, 2, 3, 4, 5]

print("Original:", numbers)

# 1. Double numbers
print("Double (loop):", double_numbers_loop(numbers))
print("Double (map):", double_numbers_map(numbers))

# 2. Filter even
print("Even (loop):", filter_even_loop(numbers))
print("Even (filter):", filter_even_filter(numbers))

# 3. Sum of numbers
print("Sum (loop):", sum_numbers_loop(numbers))
print("Sum (reduce):", sum_numbers_reduce(numbers))