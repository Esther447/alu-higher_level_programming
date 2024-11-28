#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

#Test cases
print_square(4)
print("")  # Newline for separation
print_square(10)
print("")  # Newline for separation
print_square(0)
print("")  # Newline for separation
print_square(1)
print("")  # Newline for separation

# Handling exceptions
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")  # Newline for separation

# Test for invalid input
try:
    print_square(2.5)
except Exception as e:
    print(e)
