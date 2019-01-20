#!/usr/bin/env python3

def spam():
    print(eggs)
    eggs = 'spam local'

eggs = 'global'
spam()
print(eggs)
