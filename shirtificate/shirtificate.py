from fpdf import FPDF
from PIL.Image import Image

class PDF(FPDF):
    def header(self):
        #self.set_margin(0)
        #Putting the shirt.
        #The size is not ready.
        self.image("shirtificate.png", y = 80, x = "C", w = pdf.epw*(3.8/4))
        #
        self.set_font("Courier", "B", 40)
        self.set_y(20)
        #Centering the text "CS50 Shirtificate".
        #self.cell(80)
        #Printing the title
        self.cell(0, 15, "CS50 Shirtificate", align="C")


    def shirtname(self, shirtname):
        self.set_y(150)
        self.set_font("Times", "", 30)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"{shirtname} took CS50", align="C")


#pdf = FPDF(orientation = "Portrait", format = "A4")
pdf = PDF(orientation = "Portrait", format = "A4")
pdf.add_page()
#I first write the header of the image: "CS50 Shirtificate".
#for do this, I firstly have to define the font.
#pdf.set_font('helvetica', 'B', 16)
#pdf.image("shirtificate.png")
pdf.shirtname("John Harvard")
pdf.output("shirtificate_1.pdf")




pdf = PDF()
