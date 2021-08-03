#!/usr/bin/env python3

import reports, os, sys
from datetime import date
import emails

user = str(os.environ.get('USER') )
recipient = user + "@example.com"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

file = 'processed.pdf'
home = os.environ.get('HOME')
desc_dir = home + "/supplier-data/descriptions/"

date = date.today().strftime("%B %d, %Y")
title = "Processed Update on " + date


def main(argv):
    #reports.main()
    tbl = reports.get_all_fruits()
    # for _ in reports.get_all_fruits().split('\n'):
    #     tbl.append(_)
    print(tbl)
    print(type(tbl))
    reports.generate_report(file, title, tbl)

    msg = emails.generate_email('automation@example.com', recipient, "Upload Completed - Online Fruit Store",body, file)
    emails.send_email(msg)

if __name__ == '__main__':
    main(sys.argv)
