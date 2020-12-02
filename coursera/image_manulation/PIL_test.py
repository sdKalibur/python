#! /usr/bin/env python3

from PIL import Image
import sys

img_ext = "jpeg"
file = "cookie.jpg"


def img_resize_rotate(file):
    """Resize and rotate an image file then save it."""
    new_img = Image.open(file).resize((640,480)).rotate(90)
    new_img.save( file + "90deg_640x480", format=img_ext)

#    image.open(file + "_90deg_640x480." + img_ext)

#img_resize_rotate(file)

file = sys.argv[1]

img_resize_rotate(file)

