from PyPDF2 import PdfWriter, PdfReader
from src.repository.ExecutorActions import ExecutorActions
import os
from src.views.ModalsView import ModalsView






def rotate_pdf(pdf_file_origin:str, path_output_file:str,  grau:int, list_pages:list) -> str:
    
    try:
        with open(pdf_file_origin, 'rb') as file:
            pdf_reader = PdfReader(file)
            writer = PdfWriter()
            for number_page in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[number_page]
                if number_page + 1 in list_pages:
                    pdf_reader.pages[number_page].rotate(grau)
                writer.add_page(page)
            with open(path_output_file, 'wb') as output_file:
                writer.write(output_file)
        ModalsView().message_success('Operação concluida com sucesso')    
        os.startfile(os.path.dirname(path_output_file))
    except Exception as error:
        ModalsView().exceptions_message(error)


def execute_rotate(pdf_file_origin:str, path_output_file:str, grau:int, list_pages:list):
    execucao = ExecutorActions(rotate_pdf, pdf_file_origin, path_output_file, grau, list_pages)
    execucao.execute_with_loading()
    return True