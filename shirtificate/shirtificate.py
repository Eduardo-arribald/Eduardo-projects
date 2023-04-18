import fpdf
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png")
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(50, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        #self.ln(20)

    def shirtname(self, shirtname):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(50)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(100, 100, f"{shirtname} took CS50", align="C")


#pdf = FPDF(orientation = "Portrait", format = "A4")
pdf = PDF(orientation = "Portrait", format = "A4")
pdf.add_page()
#I first write the header of the image: "CS50 Shirtificate".
#for do this, I firstly have to define the font.
#pdf.set_font('helvetica', 'B', 16)
#pdf.image("shirtificate.png")
pdf.shirtname("Eduardo")
pdf.output("shirtificate_1.pdf")




pdf = PDF()
