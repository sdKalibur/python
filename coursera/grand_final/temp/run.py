#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

import os.path, sys
ip = '35.192.100.193'

home = os.environ.get('HOME')
desc_dir = home + "/supplier-data/descriptions/"
url = "http://{}/fruits/".format(ip)

def  read_desc(desc_file):
    with open(desc_file) as f:
        #name,weight,desc = f.readline().split('\n')
        name,weight,desc = f.readlines()[:3]
    return name.strip('\n'), int(weight.strip('lbs\n')), desc.strip('\n')

def post_json(name,weight,desc,im_file):
    p = requests.post(url, json={'name': name,'weight': weight, 'description': desc, 'image_name': im_file})
    return p.ok



for i in os.listdir(desc_dir):
    if '.txt' in i.lower():
        desc_file = desc_dir + i
        im_file = i.strip('txt') + 'jpeg'
#        print(desc_file)
#        print(read_desc(desc_file))
        name,weight,desc = read_desc(desc_file)
        print('Name {} weight {} desc {} jpeg {}'.format(name,weight,desc[:10],im_file))
        post_json(name,weight,desc,im_file)
