#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

import os.path, sys

ip = '35.192.100.193'

home = os.environ.get('HOME')
img_dir = home + "/supplier-data/images/"
url = "http://{}/upload/".format(ip)



def post_jpg(jpg):
    with open(img_dir + jpg, 'rb') as opened:
        r = requests.post(url, files={'file': opened})


for i in os.listdir(img_dir):
    if 'jpeg' in i.lower():
        print(i)
        post_jpg(i)
