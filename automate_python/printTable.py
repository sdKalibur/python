#!/usr/bin/env python3
# tablePrinter - Takes a list of strings and prints them in a pretty table
# printTable.py  - Feed me a list of strings.

tableData = [[ 'apples', 'pebbles' , 'cherries', 'banana'],
             [ 1, 100, 300, 'Stefanos is a jinx  guy' ],
             ['Alice', 'Diana', 'Humphrey', 'Kalima' ],
             ['Yellow' , 'Purple oragnish color', ' Meroon', 'Indigo' ]
             ]

colWidth = 1

def colWidth(tD):
    colWidth = 1
    for i in tD:
        z = 0 
        while z < len(i):

            if len(str(i[z])) > colWidth:
                colWidth = len(str(i[z]))
            z  += 1
            
    return colWidth
          
colWidth = colWidth(tableData)

for i in tableData:
    x = 0
    while x < len(i):
        print( str(i[x]).rjust(colWidth, "*"), end = " ")
        x = x +1
    print('')
# Next time try nexted for
print('plan B')

for i in tableData:
    for x in i:
        print( str(x).rjust(colWidth, "_"), end = " ")

    print('')
