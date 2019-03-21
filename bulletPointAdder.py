#!/usr/bin/env python3
# bulletPointAdder.py - Adds wikipedia bullets poijts to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# print( text + '\n'  + ' = ' * 30)

# Separete lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):  # Loop through all indexes in the "lines" list.
    lines[i] = '* ' + lines[i] # add start to each string in "lines" list

# TODO: Separate lines and add stars.
# print(lines)
text = '\n'.join(lines)
print(text)
pyperclip.copy(text)
