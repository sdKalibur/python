#!/usr/bin/env python3

def spam():
    global eggs
    eggs = 'spam'
    print(eggs)

eggs = 'global'
spam()
print(eggs)
