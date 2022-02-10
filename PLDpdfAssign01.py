# Program for PDF Resume Creator

# Steps:

# Import library
from fpdf import FPDF

# Import pdf reader 

#create fpdf object

# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# Format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100, 150))
pdf = FPDF('P', 'mm', 'Letter')

# Add page
pdf.add_page()

# Selecting specific font
#fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats,')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., (BU)) 
pdf.set_font('helvetica', '', 16)

#Add text
# w = width
# h = height

pdf.cell(40, 10, 'Wonderful Code')
pdf.output('pdf_resume.pdfpython') 

