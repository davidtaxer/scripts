#!/usr/bin/env python3
import os
import sys
from PIL import Image

cwd = os.getcwd()
path = cwd + '/images/'
new_path = '/opt/icons/'

#location = '/media/david/SSD-FILES/scripts/images'

if not os.path.exists(new_path):
    os.makedirs(new_path)

for files in os.listdir(path):
    #try:
        if not files.startswith('.'):
            with Image.open(path + files) as im:

        #im = Image.open(path + files)
                im=im.convert('RGB').resize((128, 128)).rotate(-90)
                im=im.save(new_path + files, 'jpeg', quality=100)
                #im.close()
#    except Exception as e:
#        print("{} for {}".format(e, files))

#print(os.listdir(path))
