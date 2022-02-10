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

