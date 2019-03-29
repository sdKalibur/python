#!/usr/bin/env python3
# page 165

import re
import sys
import pyperclip

memo = "This is a document packedg with phone numbers such as 0201234567 \
        and email address such as ginger@palmtree.com\
        extra rubbish @ me sir.\
        This is a multi dot email foo.bar@bacon.ham.net\n \
        newline@here. \
        consecutive dots not allowed on email.  consecutive...dots@not.allowed.\
        078-77-543123"

def getEmail(doc):
    getEmailRegex = re.compile(r'[a-z0-9\.\-\_]+\@[a-z0-9\.\-\_]+', re.IGNORECASE | re.VERBOSE | re.DOTALL)
    emails = getEmailRegex.findall(doc)
    return emails


def getPhoneRegex(doc):
    getPhoneRegex = re.compile(r'(\d{3}[\-\_\ ]*\d{2,3}[\-\_\ ]*\d+)')
    phoneNums = getPhoneRegex.findall(doc)
    return phoneNums

print("I extracted these email :" +\
    str(getEmail(memo)) +\
      "I also found this phone numbers" +\
      str(getPhoneRegex(memo)) \
      )

