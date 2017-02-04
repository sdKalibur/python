#!/bin/python3

import random


print("Hello what is your favourite number?")

number = input()

print("Your favourite number is  "+ number "\n")

minNumber = 1
maxNumber = 10
magicNumber = random.randint(minNumber, maxNumber)

message = "The magic number is between {0} and {1}"

print(message.format(minNumber, maxNumber))

found = False

while not found:
    print("Guess what it is\n")
#    guess = input()
    guess = int(input())
    
    if guess == magicNumber:
        found = True
        print("****")
    if guess < magicNumber:
        print("Too Low!")

    if guess > magicNumber:
        print("Too High!")

print("You got it!")
