import PyPDF2
from PyPDF2 import PdfWriter, errors
from src.repository.ExecutorActions import ExecutorActions
from src.views.ModalsView import ModalsView
import os

def add_password_to_pdf(pdf_file_origin, output_pdf_path, password):
    try:
        with open(pdf_file_origin, 'rb') as input_file:
            pdf_reader = PyPDF2.PdfReader(input_file)
            # Cria um objeto PDFWriter para escrever o PDF de saída
            pdf_writer = PyPDF2.PdfWriter()
            # Itera pelas páginas do PDF de entrada e as adiciona ao PDFWriter
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            # Define a senha para o PDF
            pdf_writer.encrypt(password)
            # Escreve o PDF de saída com a senha
            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer.write(output_file)
        ModalsView().message_success('Operação concluida com sucesso')
        os.startfile(os.path.dirname(output_pdf_path))  
    except Exception as error:
        ModalsView().exceptions_message(error)


def execute_protect(pdf_file_origin:str, path_output_file:str,  password:str) ->bool:
    execucao = ExecutorActions(add_password_to_pdf, pdf_file_origin, path_output_file, password)
    execucao.execute_with_loading()
    return True


