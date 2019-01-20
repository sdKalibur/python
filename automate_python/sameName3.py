#!/usr/bin/env python3

def spam():
    global eggs
    eggs = 'spam'
    print(eggs)

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)

    

eggs = '42'
spam()
print(eggs)
