#!/usr/bin/env python3

# collatz


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        number = number // 2
        return number
    elif number % 2 != 0 :
        print(3 * number + 1 )
        number = 3 * number + 1
        return number


try:
    print('Enter an interger: ')
    number = input()
    
    while int(number) > 1:
        number = collatz(int(number))
except ValueError:
        print('You must enter an interger, run the program again. ')
