import fpdf
from fpdf import FPDF

pdf = FPDF(orientation = "Portrait", format = "A4")
pdf.add_page()
#I first write the header of the image: "CS50 Shirtificate".
#for do this, I firstly have to define the font.
pdf.set_font('helvetica', 'B', 16)
pdf.image("shirtificate.png")
pdf.output("shirtificate_1.pdf")


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("../docs/fpdf2-logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")