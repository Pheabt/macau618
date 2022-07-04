# importing required modules
import PyPDF2
import os
file_path = os.path.abspath(os.path.dirname(__file__))
print(file_path)
 
# creating a pdf file object
pdfFileObj = open(file_path+'/test.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
print(pdfReader.numPages)
 
for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page)

    # extracting text from page
    text = pageObj.extractText()
    contents = text.split('\n')
    print(contents)

    
 
# closing the pdf file object
pdfFileObj.close()