#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is empty, return None if true
    if len(my_list) == 0:
        return None

    # Initialize the maximum value as the first element of the list
    max_val = my_list[0]

    # Iterate through the list and compare each element to find the largest one
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val
