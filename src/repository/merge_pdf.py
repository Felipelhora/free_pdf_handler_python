from PyPDF2 import PdfWriter, errors

from src.views.ModalsView import ModalsView
from src.repository.ExecutorActions import ExecutorActions
import os





def merge_pdf(files:list, path_output_file:str) -> str:
    '''
        files -> array com os caminhos dos pdfs que deseja juntas
        path_output_file -> Local onde deseja salvar os arquivos e o nome
    '''
    temp_atual = ''
    merger = PdfWriter()
    try:
        for file in files:
            with open(file, 'rb') as f:
                temp_atual = file
                merger.append(file)
        merger.write(path_output_file)
        merger.close()
        ModalsView().message_success('Operação concluida com sucesso')
        os.startfile(os.path.dirname(path_output_file))  
        return True
    except errors.FileNotDecryptedError as error:
        ModalsView().message_error(f'O arquivo {temp_atual} está protegido por senha, não é possível juntar')
        return False
    except errors.PdfReadError as error:
        ModalsView().message_error(f'O arquivo {temp_atual} não pode ser carregado, ou está corrompido ou não é um PDF, verifique melhor a lista de arquivos')
        return False
    except Exception as e:
        ModalsView().message_error('Algo errado, refaça a operação')
        return False

def execute_merge(files:list, path_output_file:str) ->None:
    execucao = ExecutorActions(merge_pdf, files, path_output_file)
    execucao.execute_with_loading()
    return True