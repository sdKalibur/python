#!/usr/bin/env python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': '2eddkjlwodclldhkzb',
             'blog' : 'dkncnbvmndasklhdhjkw',
             'luggage': '12345'
             }

import sys,pyperclip

if len(sys.argv) < 2:
    print('Usage: pyton pw.py [account] - coppy account password')
    sys.exit()

account = sys.argv[1] # First command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Pass for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
          


