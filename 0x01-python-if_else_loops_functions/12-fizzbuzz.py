#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            print("{}".format('FizzBuzz'), end=' ')
        elif a % 3 == 0:
            print("{}".format('Fizz'), end=' ')
        elif a % 5 == 0:
            print("{}".format('Buzz'), end=' ')
        else:
            print("{}".format(a), end=' ')
