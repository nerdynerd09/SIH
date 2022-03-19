from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("ATULYA.png", 10, 8, 10)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "ARP SPOOFING DETECTED", 0, 0, "C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", 0, 0, "C")
    
    def body(self,name):
        with open (name,'rb') as fh:
            txt=fh.read().decode('latin-1')
        self.set_font("Times", size=12)
        self.multi_cell(0, 10,txt)
        self.ln()
    def body(self,name):
        with open (name,'rb') as fh:
            txt=fh.read().decode('latin-1')
        self.set_font("Times", size=12)
        self.multi_cell(0, 10,txt)
        self.ln()


# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font("helvetica", "BU", 15)
pdf.cell(0, 10, "DESCRIPTION:", 0, 1)
pdf.body('description.txt')
pdf.set_font("helvetica", "BU", 15)
pdf.cell(0, 10, "PREVENTION METHODS:", 0, 1)
pdf.set_font("helvetica", "B", 10)
pdf.cell(0, 10, "Static ARP Tables", 0, 1)
pdf.body('staticarp.txt')
pdf.set_font("helvetica", "B", 10)
pdf.cell(0, 10, "Switch Security ", 0, 1)
pdf.body('switchsecurity.txt')
pdf.set_font("helvetica", "B", 10)
pdf.cell(0, 10, "Physical Security", 0, 1)
pdf.body('physicalsecurity.txt')
pdf.set_font("helvetica", "B", 10)
pdf.cell(0, 10, "Network Isolation ", 0, 1)
pdf.body('networkisolation.txt')
pdf.set_font("helvetica", "B", 10)
pdf.cell(0, 10, "Encryption ", 0, 1)
pdf.body('encryption.txt')
pdf.output("ARP REPORT.pdf")
