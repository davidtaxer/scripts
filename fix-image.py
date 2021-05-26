#!/usr/bin/env python3
import os
import sys
from PIL import Image

cwd = os.getcwd()
path = cwd + '/images/'
new_path = '/opt/icons/'

if not os.path.exists(new_path):
    os.makedirs(new_path)

for files in os.listdir(path):
        if not files.startswith('.'):
            with Image.open(path + files) as im:
                im=im.convert('RGB').resize((128, 128)).rotate(-90)
                im=im.save(new_path + files, 'jpeg', quality=100)
