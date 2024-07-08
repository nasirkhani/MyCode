import PyPDF2
with open('1.pdf', 'rb') as pdf:
    read_pdf =PyPDF2.PdfFileReader(pdf)
    pdf_page=read_pdf.getNumPages()
    # pdf_content=pdf_page.extractText()
    print(pdf_page)
