#!/usr/bin/python3

from urllib.request import urlopen

def fetch_words():
    with urlopen("http://sixty-north.com/cd/t.txt") as story:
story_words = ([ ])

