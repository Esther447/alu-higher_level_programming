#!/usr/bin/python3
def list_divion(my_list_1, my_list_2, list_length):
    resulr = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            division = num1 / num2
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroError:
            print("division by 0")
            divion = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)
    return result
