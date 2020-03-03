#splitting my resume to one page and get rid of that annopying blank 2nd page that won't go away.
#why should I have to pay 40$ to adobe for just this?

from PyPDF2 import PdfFileReader, PDFFileWriter

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PDFFileWriter
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        
if __name__ == '__main__':
    path = 'Wiley_Rummel_Resume.pdf'
    split(path, 'resume_page')