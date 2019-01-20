#!/usr/bin/env python3

# This is a flow control with if elif else statements
print('What is your name? ')
name = input()
print('How old are you? ')
age = input()
age = int(age)
# print(age)

if name == 'Alice':
    print('Hi, Alice. ')

elif age < 12:
    print('You are not Alice, kiddo. ')

elif age < 100:
    print('You are not Alice, grannie. ')

elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire. ')

