#!/usr/bin/env python3

from PIL import Image

import sys, os


img_ext = "jpeg"
source_dir = "tmp/test/"
output_dir = "/tmp/" 
#  /opt/icons/

os.path.isfile


def img_resize_rotate(file):
    """Resize and rotate an image file then save it"""
    orig_file = source_dir + file  
    new_file = output_dir + file
    #print("source {} output {}".format(orig_file, new_file))
    
    # Image.open('newauctionsheet.jpg').convert(mode="L").show()
    img = Image.open( orig_file).resize((128,128)).rotate(90)
    new_img = img.convert('RGB').resize((128,128))
    new_img.save(output_dir + "/" + file, format="JPEG")

def get_image_list(source_dir):
    """" Gets list of images in given path/directory"""

    dir_list = os.path.os.listdir(source_dir)
#    print(dir_list)
    image_list = []
    os.chdir(source_dir)
    for file in dir_list:
        print("Inspecting.... : {}".format(file))

        try:
            if Image.open(file).format:
                image_list.append(file)
                print("{} :  is an image".format(file))
        except Exception as e:
            print("{} :  failed the imageness test.i \n {}".format(file, e))
            continue

#    print(image_list)
    return image_list

print(get_image_list(source_dir))


#img_resize_rotate(get_image_list(source_dir))

for i in get_image_list(source_dir):
    img_resize_rotate(i)