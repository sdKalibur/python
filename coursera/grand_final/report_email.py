#!/usr/bin/env python3

import reports
from datetime import date
import emails


attachment = 'processed.pdf'
home = os.environ.get('HOME')
desc_dir = home + "/supplier-data/descriptions/"

title = "Processed Update on "
date = date.today().strftime("%d %B %Y")


def main(argv):
    summary = reports.get_all_fruits

    reports.generate_report(attachment,title, summary)


if name == '__name__':
    main(sys.argv)
