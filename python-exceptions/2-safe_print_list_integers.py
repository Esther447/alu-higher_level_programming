#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            for i in range(x):
                value = my_list[i]
       if isinstance(value, int):
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            # Ignore IndexError for out of range and ValueError for non-integers
        raise IndexError("list index out of range")
    print()  # Print a new line at the end
    return count
