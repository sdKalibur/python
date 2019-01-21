#!/usr/bin/python3
import urllib

from urllib.request import urlopen

with urlopen('http://ebay.com/index.html') as story:
    story_words = []
    for line in story:
#        line_words = line.decode('utf-8').split()
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

for word in story_words:
    print(word)
