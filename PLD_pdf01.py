# Program for PDF Resume Creator

# Steps:

# Note: + Install fpdf2 in terminal 
# Type "pip install fpdf2" in terminal 

# Import library
from fpdf import FPDF

# Import pdf reader 

# create fpdf objec

# Layout ('P', 'L')
# Unit ('mm', 'cm', 'in')
# Format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100, 150))
pdf = FPDF('P', 'mm', 'Letter')

# Add page
pdf.add_page()

# Set auto page break
pdf.set_auto_page_break(auto=1, margin =15)
#Cool

# Selecting specific font
#fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats,')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., (BU)) 
pdf.set_font('helvetica', '', 16)

#Add text
# w = width
# h = height

pdf.cell(40, 30, 'Computer Engineer Resume', ln=1) 
pdf.cell(40, 10, 'Resume details:', ln=1)
pdf.cell(40, 10, 'John Rengel O. Jaylo', ln=1)
pdf.cell(40, 10, 'Email: johnrengelo.jaylo1211@gmail', ln=1)
pdf.cell(40, 20, 'Summary:', ln=1)

pdf.cell(40, 10, 'Young and always eager to learn computer engineer with a lot of experience ', ln=1)
pdf.cell(40, 10, 'in computer programming and hardware trouble shooting. ', ln=1)

pdf.cell(40, 10, ' ', ln=1)

pdf.cell(40, 10, 'Experience:', ln=1)
pdf.cell(40, 10, '-Oversaw design and development', ln=1)
pdf.cell(40, 10, '-Developing testing methods and prototypes', ln=1)
pdf.cell(40, 10, '-Supervising attributes of microprocessor and microcontroller design', ln=1)

pdf.cell(40, 10, ' ', ln=1)

pdf.cell(40, 10, 'Education: ', ln=1)

pdf.cell(40, 10, ' ', ln=1)

pdf.cell(40, 10, '-Bachelor of Science and Computer Engineering (BSCOE)', ln=1)
pdf.cell(40, 10, '-Relevant Coursework: Computer Engineering Fundamentals, Wireless Communication ', ln=1)
pdf.cell(40, 10, 'and Networking, Computational Algorithms, Natural Language Processing, Software and hardware Engineering', ln=1)

pdf.cell(40, 10, ' ', ln=1)

pdf.cell(40, 10, 'Certifications:', ln=1)
pdf.cell(40, 10, '-Certified Master of Computer Engineering', ln=1)
pdf.cell(40, 10, '-Certified Master of Compute Electrical and Engineering', ln=1)

pdf.cell(40, 10, ' ', ln=1)

pdf.cell(40, 10, 'Memberships:', ln=1)

pdf.cell(40, 10, ' ', ln=1)

pdf.cell(40, 10, '-Association for Computing Machinery', ln=1)
pdf.cell(40, 10, '-Association for Advancement of Artificial Intelligence', ln=1)

pdf.cell(40, 10, ' ', ln=1)

pdf.cell(40, 10, 'Languages:', ln=1)

pdf.cell(40, 10, ' ', ln=1)


pdf.cell(40, 10, '-English', ln=1)
pdf.cell(40, 10, '-Filipino', ln=1)
pdf.cell(40, 10, '-Mandarin', ln=1)

pdf.cell(40, 10, ' ', ln=1)


pdf.cell(40, 10, '(Note: These are examples only for assignment)', ln=1)

pdf.output('pdf_resume01.pdf') 

# Program successfully running

