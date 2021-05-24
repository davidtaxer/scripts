#!/usr/bin/env python3

from PIL import Image

file = "/media/david/SSD-FILES/scripts/photo-1493976040374-85c8e12f0c0e.jpg"
img = Image.open(file, "r")

img.show()
