#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            # Access the list element
            value = my_list[i]
            # Check if the element is an integer
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
    except IndexError:
        # Explicitly raise the exception to mimic the desired behavior
        raise IndexError("list index out of range")
    print()  # Print a newline at the end
    return count
