import PyPDF2
from PyPDF2 import errors
from PIL import Image
from io import BytesIO
from src.repository.ExecutorActions import ExecutorActions
from src.views.ModalsView import ModalsView
import os
from src.config import CONFIG
from docx2pdf import convert
import time

def images_to_pdf(files:list, path_output_file:str):
    pdf_writer = PyPDF2.PdfWriter()
    try:
        for file in files:
            file = Image.open(file)
            imagem_pdf = file.convert("RGB")
            buffer = BytesIO()
            imagem_pdf.save(buffer, format="PDF")
            pdf_writer.add_page(PyPDF2.PdfReader(buffer).pages[0])
            buffer.close()
        with open(path_output_file, "wb") as pdf_arquivo:
            pdf_writer.write(pdf_arquivo)
        ModalsView().message_success('Operação concluida com sucesso')
        os.startfile(os.path.dirname(path_output_file))  
        return True
    except errors.FileNotDecryptedError as error:
        ModalsView().message_error(f'O arquivo {file} está protegido por senha, não é possível juntar')
        return False
    except errors.PdfReadError as error:
        ModalsView().message_error(f'O arquivo {file} não pode ser carregado, ou está corrompido ou não é um PDF, verifique melhor a lista de arquivos')
        return False
    except Exception as e:
        ModalsView().message_error('Algo errado, refaça a operação')
        return False


def convert_document_docx_to_pdf_windows(file:str, path_output_file:str):
    try:
        convert(file, path_output_file)
        time.sleep(1)
        return True
    except Exception as error:
        ModalsView().exceptions_message(error)
        return False

def convert_documents_to_pdf_windows(files:list, path_output_file:str):
    for file in files:
        bar = CONFIG['bar_system']
        splitted_file = file.split(bar)[-1]
        extension = splitted_file.split('.')[-1]
        name_file = splitted_file.split('.')[0]
        path_output_file_with_name_file = f'{path_output_file}{bar}{name_file}.pdf'
        if extension == 'docx':
           convert_document_docx_to_pdf_windows(file, path_output_file_with_name_file) 
        else:
            ModalsView().exceptions_message(f'Documento {file}, não está na extensão correta')
            return False
    ModalsView().message_success('Operação concluida com sucesso')    
    os.startfile(path_output_file)



def convert_documents_to_pdf(files:list, path_output_file:str):
    if CONFIG['system'] == 'Windows':
       convert_documents_to_pdf_windows(files, path_output_file)
       return True
    else:
        return False
       



def execute_imagens_para_pdf(files:list, path_output_file:str):
    execucao = ExecutorActions(images_to_pdf, files, path_output_file)
    execucao.execute_with_loading()
    return True


def execute_document_to_pdf(files:list, path_output_file:str):
    execucao = ExecutorActions(convert_documents_to_pdf, files, path_output_file)
    execucao.execute_with_loading()
    return True