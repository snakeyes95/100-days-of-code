#Program to read and get details from pdf files and extracting data from pdf files.
from PyPDF2 import PdfFileReader

def get_pdf_details(file_path):
    with open(file_path,'rb') as file:
        pdf_file=PdfFileReader(file)
        info=pdf_file.getDocumentInfo()
        info_dict={
            'author_name':info.author,
            'creator':info.creator,
            'producer':info.producer,
            'subject':info.subject,
            'title':info.title,
            'num_pages':pdf_file.getNumPages()
        }
        return info_dict

def get_text_from_file(file_path):
    with open(file_path,'rb') as file:
        pdf_file=PdfFileReader(file)
        page=pdf_file.getPage(0)
        result=page.extractText()
        return result

if __name__ == '__main__':
    path='./sample.pdf'
    print(get_pdf_details(path))
    print(get_text_from_file(path))