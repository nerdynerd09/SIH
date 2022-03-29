# pip install fpdf2
import yagmail
from fpdf import FPDF

pdf = FPDF()
# currentIP = "192.168.1.0"
# currentMAC = "A1:B2:C3:D4:E5:F6"
# text = f"""
# Host IP: {currentIP}\n
# Host MAC: {currentMAC}
# """
# networkList = [['192.168.1.100','A1:B2:C3:D4:E5:F6','Samsung'],['192.168.1.100','A1:B2:C3:D4:E5:F6','Apple'],['192.168.1.100','A1:B2:C3:D4:E5:F6','Samsung']]
# cveList = [['192.168.1.100','dnsmaq','CVE-2021-4568'],['192.168.1.100','dnsmaq','CVE-2021-4568'],['192.168.1.100','dnsmaq','CVE-2021-4568']]
def initialReportGenerator(networkIPs,networkMAC,vendor,currentIP,currentMAC,cveList):
    # global currentIP
    # global currentMAC
    # global networkList
    networkIPs=networkIPs
    networkMAC=networkMAC
    vendor=vendor
    cveList=cveList 
    currentIP=currentIP
    currentMAC=currentMAC

    col_widths=(52, 55, 49)
    pdf.add_page()

    # PDF Heading
    # Rendering logo:
    pdf.image("atulya.png", 10, 8, 10)
    # Setting font: helvetica bold 15
    pdf.set_font("helvetica", "B", 15)
    # Moving cursor to the right:
    pdf.cell(80)
    # Printing title:
    pdf.cell(30, 10, "Network Report", 0, 0, "C")
    # Performing a line break:
    pdf.ln(20)


    # Current IP and MAC
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(40,10,f"CurrentIP: {currentIP}")
    pdf.ln()
    pdf.cell(40,10,f"CurrentMAC: {currentMAC}")
    pdf.ln()


    # Connected Devices Table
    pdf.ln(5)
    pdf.set_font("helvetica", "B", 16)
    # Setting background color
    pdf.set_fill_color(200, 220, 255)
    # Printing chapter name:
    pdf.cell(0, 6, f"Devices in Your Network", 0, 1, "C", True)
    # Performing a line break:
    pdf.ln(4)

    pdf.set_fill_color(255, 100, 0)
    pdf.set_text_color(255)
    pdf.set_draw_color(255, 0, 0)
    pdf.set_line_width(0.3)
    pdf.set_font(style="B")

    
    pdf.cell(col_widths[0],7,"IP",1,0,"C",True)
    pdf.cell(col_widths[1],7,"MAC",1,0,"C",True)
    pdf.cell(col_widths[2],7,"Vendor",1,0,"C",True)
    pdf.ln()

    pdf.set_fill_color(224, 235, 255)
    pdf.set_text_color(0)
    pdf.set_font()
    fill = False
    for i in range (len(networkMAC)):
        pdf.cell(col_widths[0], 6, networkIPs[i][0], "LR", 0, "L", fill)
        pdf.cell(col_widths[1], 6, networkMAC[i], "LR", 0, "L", fill)
        pdf.cell(col_widths[2], 6, vendor[i], "LR", 0, "L", fill)
        pdf.ln()
        fill = not fill
    pdf.cell(sum(col_widths), 0, "", "T")


    # CVEs Table
    pdf.ln(5)
    pdf.set_font("helvetica", "B", 16)
    # Setting background color
    pdf.set_fill_color(200, 220, 255)
    # Printing chapter name:
    pdf.cell(0, 6, f"Vulnerable to CVEs", 0, 1, "C", True)
    # Performing a line break:
    pdf.ln(4)

    pdf.set_fill_color(255, 100, 0)
    pdf.set_text_color(255)
    pdf.set_draw_color(255, 0, 0)
    pdf.set_line_width(0.3)
    pdf.set_font(style="B")

    
    pdf.cell(col_widths[0],7,"IP",1,0,"C",True)
    pdf.cell(col_widths[1],7,"Service",1,0,"C",True)
    pdf.cell(col_widths[2],7,"CVE",1,0,"C",True)
    pdf.ln()

    pdf.set_fill_color(224, 235, 255)
    pdf.set_text_color(0)
    pdf.set_font()
    fill = False
    for i in range (len(cveList)):
        pdf.cell(col_widths[0], 6, cveList[i][0], "LR", 0, "L", fill)
        pdf.cell(col_widths[1], 6, cveList[i][1], "LR", 0, "L", fill)
        pdf.cell(col_widths[2], 6, cveList[i][2], "LR", 0, "L", fill)
        pdf.ln()
        fill = not fill
    pdf.cell(sum(col_widths), 0, "", "T")

    pdf.output("initialreport.pdf")

    filename = "initialreport.pdf"
    sendInitialMail(filename)
    return "initialreport.pdf"


def sendInitialMail(filename):
    yag = yagmail.SMTP('sendermail', 'senderMailPass')
    receiver="aliashhar3@gmail.com"
    body = "Below attached is the Report of your Network."
    # filename = initialReportGenerator()
    filename = filename
    print(filename)
    yag.send(
        to=receiver,
        subject="Network Report",
        contents=body, 
        attachments=filename,
    )

# sendInitialMail()
# initialReportGenerator()