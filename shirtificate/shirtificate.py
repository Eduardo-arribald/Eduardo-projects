import fpdf
from fpdf import FPDF

pdf = FPDF(orientation = "Portrait", format = "A4")
pdf.add_page()
#I first write the header of the image: "CS50 Shirtificate".
#for do this, I firstly have to define the font. 
pdf.set_font('helvetica', 'B', 16)
pdf.image("shirtificate.png")
pdf.output("shirtificate_1.pdf")