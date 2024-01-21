#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    if my_list is None:
        return None
    if length == 0:
        return my_list
    i = 0
    while (i < length):
        print("{:d}".format(my_list[length - 1 - i]))
        i = i + 1
