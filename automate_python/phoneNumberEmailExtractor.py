#!/usr/bin/env python3
# page 165

import re
import sys

memo = 'This is a document packedg with phone numbers such as 0201234567 \
        and email address such as ginger@palmtree.com\
        extra rubbish @ me sir.'

def getEmail(doc):
    getEmailRegex = re.compile(r'[a-z0-9\.\-\_]+\@[a-z0-9\.\-\_]+', re.IGNORECASE | re.VERBOSE | re.DOTALL)



def getPhoneRegex(doc):
