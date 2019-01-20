#!/usr/bin/env python3
# pw.py

PASSWORDS = {'email': 'sklahlkdshgiusdhuioe',
             'blog': 'jsdhfkjhwieuyrwigbx',
             'luggage': '12345'
             }

import sys,pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

print(account)
