#!/usr/bin/env python3
import os
import sys
from PIL import Image

cwd = os.getcwd()
path = cwd + '/images/'
new_path = '/opt/icons/'
location = "/media/david/SSD-FILES/scripts/images"
size = (128, 128)

if not os.path.exists(new_path):
    os.makedirs(new_path)

for files in os.listdir(path):
    if not files.startswith('.'):
        im = Image.open(path + files)
        im.convert('RGB')
        im.resize(size)
        im.rotate(-90)
        im.save(new_path + files, '.jpg')
        im.close()

#print(os.listdir(location))
