#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        # Print the combination without a leading comma for the first combination
        if i == 0 and j == 1:
            print("{}{}".format(i, j), end="")
        # Handle the last combination to avoid a trailing comma
        elif i == 8 and j == 9:
            print(", {}{}".format(i, j))
        else:
            print(", {}{}".format(i, j), end="")

