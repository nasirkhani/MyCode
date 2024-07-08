import PyPDF2
with open('1.pdf', 'rb') as pdf:
    read_pdf = pypdf2.pdffilereader(pdf)
    pdf_page=read_pdf.getpage(1)
    pdf_content=pdf_page.extractText()
    print(pdf_content)
