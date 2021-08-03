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
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Table
from reportlab.lib import colors

import os,sys
from datetime import date


filename = 'processed.pdf'
#home = os.environ.get('HOME')
desc_dir =  os.getcwd() + "/supplier-data/descriptions/"
date = date.today().strftime("%B d%, %Y")

title = "Processed Update on " + date

def generate_report(filename, title, table_data):
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    # report_data = Table(table_data, styles["h1"])
    #sreport_date = Paragraph(date, styles["h1"])
    report = SimpleDocTemplate(filename)
    table_style = [('GRID', (0,0), (0,0), 0, colors.white)]
    report_data = Paragraph(table_data)
    empty_line = Spacer(1,20)
    report.build([report_title,  empty_line, report_data, empty_line ])



def get_fruit_data(desc_file):
    with open(desc_file) as f:
        name, weight = f.readlines()[:2]
        #print(name, weight)
    return name.strip('\n'), weight.strip('\n')

def get_all_fruits():
    fruit_stats = []
    for i in os.listdir(desc_dir):
        if 'txt' in i.lower():
            desc_file = desc_dir + i
            name, weight = get_fruit_data(desc_file)
            fruit_stats.append([{'name': name}, {'weight': weight}])
    #print(fruit_stats)
        content = ''
        for k,v in fruit_stats:
            print(k,v)
            name, value = k['name'], v['weight']
            content += '<br></br>name: {} \n<br></br>weight: {}\n<br></br>\n'.format(name,value)
            print('{}'.format(content))
    return content

# table_data = [ _ for _ in get_all_fruits().split('\n') ]
print(get_all_fruits())

def main():
    generate_report(filename, title, table_data)

if "__name__" == "__main__":
    main(sys.argv)
