#!/usr/bin/python3

def fizzbuzz():
    for num in range(101):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizzbuzz ")
        elif num % 3 == 0:
            print("Fizz ")
        elif num % 5 == 0:
            print("Buzz ")
        else:
            print("{} ".format(num))
