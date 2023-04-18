import fpdf
from fpdf import FPDF

pdf = FPDF(orientation = "Portrait", format = "A4")
pdf.add_page()
pdf.image("shirtificate.png", x = 20, y = 60)
pdf.output("shirtificate_1.pdf")