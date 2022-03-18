# pip install fpdf2

from fpdf import FPDF
pdf = FPDF()
ip = "192.168.1.0"
text = f"""
Lorem Ipsum {ip} is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
def reportGenerator():
    pdf.add_page()
    

    pdf.set_font("helvetica", "", 12)
    # Setting background color
    pdf.set_fill_color(200, 220, 255)
    # Printing chapter name:
    # pdf.cell(0, 6, f"Chapter {num} : {label}", 0, 1, "L", True)
    pdf.cell(0, 6, f"Chapter 1 : Coder", 0, 1, "M", True)
    # Performing a line break:
    pdf.ln(4)


    pdf.set_font("Helvetica", size=14)
    # pdf.cell(200, 10, txt="Welcome to PythonGuides", ln=1, align="L")
    # pdf.cell(50,50,txt=text)
    pdf.multi_cell(0, 5, text)
    pdf.output("python.pdf")

    return "python.pdf"

reportGenerator()




