import re

xmasRegex = re.compile(r'\d+\s\w+')

xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans') # 6 geese, 5 rings, 4 birds, 12 doves, 1 partridge')
