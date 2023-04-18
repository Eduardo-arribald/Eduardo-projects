import fpdf
from fpdf import FPDF

pdf = FPDF(orientation = "Portrait", format = "A4")
pdf.add_page()
pdf.set_font('helvetica', 'B', 16)
pdf.image("shirtificate.png")
pdf.output("shirtificate_1.pdf")