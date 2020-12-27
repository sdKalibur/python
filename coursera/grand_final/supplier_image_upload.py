#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

import os.path, sys

home = os.environ.get('HOME')
img_dir = home + "/supplier-data/images/"
url = "http://35.232.81.145/upload/"



def post_jpg(jpg):
    with open(img_dir + jpg, 'rb') as opened:
        r = requests.post(url, files={'file': opened})


for i in os.listdir(img_dir):
    if 'jpeg' in i.lower():
        print(i)
        post_jpg(i)
