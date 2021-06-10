#!/usr/bin/env python3


from fpdf import FPDF

name ='David'
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, f'Hello World, my name is {name}!')
pdf.output('tuto1.pdf', 'F')
