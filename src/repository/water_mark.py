from PyPDF2 import PdfReader, PdfWriter, errors
from src.repository.ExecutorActions import ExecutorActions
import PyPDF2
from src.views.ModalsView import ModalsView
from src.config import CONFIG
import os
from uuid import uuid4
from PIL import Image
from io import BytesIO



def __remove_temp_file(path_mark_water:str) -> None:
    try:
            os.remove(path_mark_water)
    except:
            ...

def __check_extension_mark_water(mark_water_path:str, path_output_file:str) -> list:
    try:
        path_temp_file = path_output_file.split(CONFIG['bar_system'])
        del path_temp_file[-1]
        path_temp_file = f'{CONFIG["bar_system"]}'.join(path_temp_file)
        extension = mark_water_path.split('.')[-1]
        if extension == 'pdf':
           return [mark_water_path, False]
        elif extension in CONFIG['extensions_images_suporte']:
            mark_water = PyPDF2.PdfWriter()
            file = Image.open(mark_water_path)
            imagem_pdf = file.convert("RGB")
            buffer = BytesIO()
            imagem_pdf.save(buffer, format="PDF")
            mark_water.add_page(PyPDF2.PdfReader(buffer).pages[0])
            buffer.close()
            path_save_temp_file = f"{path_temp_file}{CONFIG['bar_system']}{str(uuid4())}.pdf"
            with open(path_save_temp_file, "wb") as pdf_arquivo:
                mark_water.write(pdf_arquivo)
            return [path_save_temp_file, True]
    except:
        return [mark_water_path, False]


        
        
def water_mark(pdf_file_origin:str, path_output_file:str, mark_water:str):
    try:
        writer = PdfWriter()
        reader = PdfReader  (pdf_file_origin)
        mark_water = __check_extension_mark_water(mark_water_path=mark_water, path_output_file=path_output_file)
        for page in range(0, len(reader.pages)):
            content_page = reader.pages[page]
            mediabox = content_page.mediabox
            read_marc = PdfReader(mark_water[0])
            image_page = read_marc.pages[0]
            image_page.merge_page((content_page))
            image_page.mediabox = mediabox
            writer.add_page(image_page)
        with open (path_output_file, 'wb') as pdf:
            writer.write(pdf)
        # verifica se houve a conversão de foto para PDF e se foi criado arquivo temp
        # se sim ele exclui o arquivo temp
        if mark_water[1] == True:
            __remove_temp_file(mark_water[0])
        ModalsView().message_success('Operação concluida com sucesso')
        os.startfile(os.path.dirname(path_output_file)) 
    except Exception as error:
        if mark_water[1] == True:
            __remove_temp_file(mark_water[0])
        ModalsView().exceptions_message(error)


def execute_mark_water(pdf_file_origin:str, path_output_file:str, mark_water:str):
    execucao = ExecutorActions(water_mark, pdf_file_origin, path_output_file, mark_water)
    execucao.execute_with_loading()
    return True