#!/usr/bin/python3
import sys

num_args = len(sys.argv)
if num_args > 1:
    if(num_args == 2):
        print("{} argument:".format(num_args - 1))
    else:
        print("{} arguments:".format(num_args - 1))

    for i in range(1, num_args):
        print("{}: {}".format(i, sys.argv[i]))
else:
    print("0 arguments")
