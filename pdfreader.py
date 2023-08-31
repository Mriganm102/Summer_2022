import PyPDF2

pdf_name = input('Name of PDF:')
pdfFileObj = open(pdf_name, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
pages = int(len(pdfReader.pages)) // 2
file = open('pdf_text.txt', 'a')
file.truncate(0)


for i in range(pages):
    pageObj = pdfReader.pages[i]
    text = pageObj.extract_text().split("  ")
    for i in range(len(text)):
        file.write(text[i])
file.close()
pdfFileObj.close()