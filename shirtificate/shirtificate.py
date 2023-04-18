import fpdf
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.image("shirtificate.png", x = 20, y = 60)
pdf.output("shirtificate_1.pdf")