#!/usr/bin/env python3

import reports
import emails
from datetime import date
import os,sys

attachment = '/tmp/processed.pdf'
subject = "Upload Completed Online Fruit Store"
body = "All fruits are uploaded to our website successfully.  A detailed list is attached to this email"
title = "Processed Update on {}".format(date.today().strftime("%d %B %Y"))

def main(argv):
    summary = reports.get_all_fruits()

    reports.generate_report(attachment, title , summary)
    
    message = emails.generate_email('automation@example.com', 'student-01-1599e58e4165@example.com', subject, body, attachment)

    emails.send_email(message)

if __name__ == '__main__':
    main(sys.argv)

