#!/usr/bin/env python3

"""Processed Update on <Today's date>

[blank line]

name: Apple

weight: 500 lbs

[blank line]

name: Avocado

weight: 200 lbs

[blank line]
"""
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph

import os,sys
from datetime import date


filename = 'processed.pdf'
home = os.environ.get('HOME')
desc_dir = home + "/supplier-data/descriptions/"

title = "Processed Update on "
date = date.today().strftime("%d %B %Y")


def generate_report(filename, title, info):
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    report_date = Paragraph(date, styles["h1"])
    report_info = Paragraph(info, styles["BodyText"])
    report = SimpleDocTemplate(filename)
    empty_line = Spacer(1,20)
    report.build([report_title, report_date,  empty_line, report_info, empty_line ])



def get_fruit_data(desc_file):
    with open(desc_file) as f:
        name, weight = f.readlines()[:2]
        #print(name, weight)
    return name.strip('\n'), weight.strip('\n')

def get_all_fruits():
    fruit_stats = ""
    for i in os.listdir(desc_dir):
        if 'txt' in i.lower():
            desc_file = desc_dir + i
            name, weight = get_fruit_data(desc_file)
            fruit_stats += "\n{}\n{}\n".format(name,weight)
    return fruit_stats

summary = get_all_fruits()


generate_report(filename, title, summary)
