from PyPDF2 import PdfReader
from src.views.ModalsView import ModalsView


def pdf_info(file_path:str):
    try:
        info_pdf = {}
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            info_pdf['total_pages'] = len(pdf_reader.pages)
        return [info_pdf, True]
    except Exception as error:
        ModalsView().exceptions_message(exception=error)
        return [None, False]



