#splitting my resume to one page and get rid of that annopying blank 2nd page that won't go away.
#why should I have to pay 40$ to adobe for just this?

from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger


pdf_document = "./Wiley_Rummel_Resume.pdf"
pdf = PdfFileReader(pdf_document)

for page in range(pdf.getNumPages()):
    pdf_writer = PdfFileWriter()
    current_page = pdf.getPage(page)
    pdf_writer.addPage(current_page)

    outputFileName = f"Wiley_Rummel_Resume{page}.pdf"
    with open(outputFileName, "wb") as out:
        pdf_writer.write(out)

        print("Created: ", outputFileName)
