#!/usr/bin/env python3
import os, sys
from PIL import Image


location = "/media/david/SSD-FILES/scripts/images"
size = (128, 128)

for file in location:
    newfile = os.path.splitext(file)[0] + ".jpg"
    if file != newfile:
        with Image.open(file) as im:
            im.resize((128, 128)).rotate(90).save(newfile, "JPEG")
