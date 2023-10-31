#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst_dig = abs(number) % 10
if number < 0:
    lst_dig = lst_dig * -1
if lst_dig > 5:
    print(f"Last digit of {number:d} is {lst_dig:d} and is greater than 5")
elif lst_dig < 6 and lst_dig != 0:
    print(f"Last digit of {number:d} is {lst_dig:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {lst_dig:d} and is 0")
