#!/usr/bin/python3
# pw.py - An insecure password program

PASSWORDS = {'email': 'sklahlkdshgiusdhuioe',
             'blog': 'jsdhfkjhwieuyrwigbx',
             'luggage': '12345'
             }

import sys,pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

print('Working with : ' + account)

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copped to clipboard.')
else:
    print('There is no account named' + account)
