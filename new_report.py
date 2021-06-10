#!/usr/bin/env python3
from fpdf import FPDF
from PIL import Image, ImageFilter
import time
import concurrent.futures

width = 210
height = 297
size = (1200, 1200)

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'BU', 16)
pdf.cell(0, 0, 'Hello World, my name is David!', 0, 0, 'C')

img = ('/media/david/SSD-FILES/scripts/photo-1549692520-acc6669e2f0c.jpg')

pdf.image(img, 50, 30, width-100, height-100)

pdf.output('tuto1.pdf', 'F')
