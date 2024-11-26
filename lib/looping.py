#!/usr/bin/env python3
def happy_new_year():
    count = 10
    while count >= 1:  
        print(count)  # Print the current number
        count -= 1  # Decrement the count by 1
    print("Happy New Year!")  # Print the final message after the loop


def square_integers(int_list):
    squared_list = []  # Initialize an empty list
    for num in int_list:
        squared_list.append(num ** 2)  # Square each number and append
    return squared_list  # Return the list of squared numbers


def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
fizzbuzz()


