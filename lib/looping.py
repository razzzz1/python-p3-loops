#!/usr/bin/env python3

def happy_new_year():
    x = 0
    while x <= 10:
        print(x)
        x += 1
        
        print("Happy New Year!")
        

    # code goes here!
    pass

def square_integers(int_list):
    squared_list = [i ** 2 for i in int_list]
    return squared_list

    # code goes here!
    pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)



    pass
