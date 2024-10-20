#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':  # Corrected this line
            # Convert to uppercase by subtracting 32 from its ASCII value
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")  # Print the character
    print()  # Print a newline at the end
