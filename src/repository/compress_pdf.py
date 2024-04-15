import fitz
from src.views.ModalsView import ModalsView
from src.repository.ExecutorActions import ExecutorActions
import os




def compress_pdf(pdf_file_origin:str, path_output_file:str, quality_dpi:int=85, colorspace=fitz.csRGB, garbage=3): 
    try:
        doc = fitz.Document(pdf_file_origin)
        doc_new = fitz.Document()
        for page in doc:
            pixmap = page.get_pixmap(colorspace=colorspace, dpi=quality_dpi, annots=False)
            new_page = doc_new.new_page(-1)
            xref = new_page.insert_image(rect=new_page.bound(), pixmap=pixmap)
        doc_new.save(path_output_file, garbage=garbage, deflate=True, deflate_images=True, deflate_fonts=True, pretty=True)
        doc.close()
        doc_new.close()
        ModalsView().message_success('Operação concluida com sucesso')
        os.startfile(os.path.dirname(path_output_file))  
    except Exception as error:
        ModalsView().exceptions_message(error)


def execute_compress(pdf_file_origin:str, path_output_file:str, quality_dpi:int) ->None:
    execucao = ExecutorActions(compress_pdf, pdf_file_origin, path_output_file, quality_dpi)
    execucao.execute_with_loading()
    return True
