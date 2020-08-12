import PyPDF2

pdf = open('C:\\Users\\AWAL-MER\\Downloads\\Class-IX-Registration_20200808_0001-pages-2 (1) (1).pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
pages = pdfReader.numPages