#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Attempt to print the integer at the index i
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (IndexError, ValueError):
            # Ignore IndexError for out of range and ValueError for non-integers
            continue
    print()  # Print a new line at the end
    return count
