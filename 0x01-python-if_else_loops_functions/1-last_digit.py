#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
msg = "and is less than 6 and not 0"

if (number < 0):
    print(f"Last digit of {number} is {-1 * last_digit} {msg}")
elif (last_digit < 6 and last_digit != 0):
    print(f"Last digit of {number} is {last_digit} {msg}")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
