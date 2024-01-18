#!/usr/bin/python3
import sys

num_args = len(sys.argv)
total = 0
for i in range(1, num_args):
        total = total + int(sys.argv[i])
print("{}".format(total))
