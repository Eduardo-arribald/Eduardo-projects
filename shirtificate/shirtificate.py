from fpdf import FPDF
from PIL.Image import Image

class PDF(FPDF):
    def header(self):
        #self.set_margin(0)
        #Putting the shirt.
        #The size is not ready.
        self.image("shirtificate.png", x = "C", w = pdf.epw*(1.5/2))
        #
        self.set_font("Times", "", 40)
        self.set_y(20)
        #Centering the text "CS50 Shirtificate".
        #self.cell(80)
        #Printing the title
        self.cell(0, 10, "CS50 Shirtificate", align="C")


    def shirtname(self, shirtname):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(100)
        # Setting font: helvetica italic 8
        self.set_font("Times", "", 30)
        # Printing page number:
        self.cell(0, 10, f"{shirtname} took CS50", align="C")


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
