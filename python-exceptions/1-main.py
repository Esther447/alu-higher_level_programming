#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe _print_innteger(value)
if not has_been_print:
    print("{} is not  an integer".format(value))


value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))


value = "School"
has_been_prinnt = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
