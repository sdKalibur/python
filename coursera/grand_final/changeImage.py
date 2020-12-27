#!/usr/bin/env python3

from PIL import Image
import os.path, sys

home = os.environ.get('HOME')
img_dir = home + "/supplier-data/images/"

def tiff_to_jpg(im_file):
    im = Image.open(img_dir + im_file)
    im_rgb = im.convert('RGB')
    im_size = im_rgb.resize((600,400))
    im_file,_ = im_file.split('.')
    im_size.save(img_dir + im_file + '.jpeg','JPEG')
    print('Done with {}.'.format(im_file))

for i in os.listdir(img_dir):
    if 'tiff' in i.lower():
        print(i)
        tiff_to_jpg(i)
