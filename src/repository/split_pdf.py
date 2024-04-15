from PyPDF2 import PdfWriter, PdfReader, errors
from src.views.ModalsView import ModalsView
from src.repository.ExecutorActions import ExecutorActions
import os


def split_by_block(pdf_file_origin:str, list_split:list):
    '''
        list_split -> recebe os valores ja convertidos de n. de páginas para um array, já que o array começa em 0 e as páginas em 1
    
    '''
    try:
        with open(pdf_file_origin, 'rb') as file:
            pdf_reader = PdfReader(file)
            pdf_writer = PdfWriter()
            init_parameter = int(list_split[0])
            end_parameter = int(list_split[1])
            for page_number in range (init_parameter, (end_parameter + 1)):
                pdf_writer.add_page(pdf_reader.pages[int(page_number)])
            return pdf_writer
    except Exception as error:
        ModalsView().exceptions_message(error)
    
'''
Pega o caminho e inclui de forma a evitar erros adicionais ao nome, como sequenciais ou demontrativos de qualidade
'''
def __rename_file(path_output_file:str, name_to_add:str):
    new_name_path = path_output_file.split('.')
    extensao = new_name_path[-1]
    del new_name_path[-1]
    new_output_path = f"{' '.join(new_name_path)}_{name_to_add}.{extensao}"
    return new_output_path


def split_by_lists(pdf_file_origin:str, path_output_file:str, arrays_blocks:list):
    try:
        for index, array_blocks in enumerate(arrays_blocks):
            page_splited = split_by_block(pdf_file_origin, array_blocks)
            new_output_path = __rename_file(path_output_file=path_output_file, name_to_add=index)
            with open(new_output_path, 'wb') as output_pdf:
                page_splited.write(output_pdf)
        ModalsView().message_success('Operação concluida com sucesso')
        os.startfile(os.path.dirname(path_output_file)) 
    except Exception as error:
        ModalsView().exceptions_message(error)
        return False

def make_list_blocks(pdf_file_origin:str, value:int) ->list:
    number_pages = 0
    list_blocks = []
    lista_intermediaria = []
    try:
        with open(pdf_file_origin, 'rb') as file:
            pdf_reader = PdfReader(file)
            number_pages =  len(pdf_reader.pages)
    except Exception as error:
        ModalsView().exceptions_message(error)
        return False
    if number_pages <= value or value == 0:
        ModalsView().message_error(f'O valor do bloco não pode ser 0 nem maior ou igual que o numero de páginas do arquivo')
        return False
    if number_pages == 2:
       return [[0,0], [1,1]] 
    for number in range(value,number_pages,value):
        lista_intermediaria.append(number)
    lista_intermediaria.append(number_pages)
    for index, last_page_selecionada in enumerate((lista_intermediaria)):
        list_temp = []
        if index == 0 and number_pages > 2:
           list_temp = [(last_page_selecionada - (value)),(last_page_selecionada - 1)]
           list_blocks.append(list_temp)
        elif index == (len(lista_intermediaria) -1):
            list_temp = [(list_blocks[-1][1] + 1), (last_page_selecionada -1)]
            list_blocks.append(list_temp) 
        else:
           list_temp = [(last_page_selecionada - (value)), (last_page_selecionada - 1)]
           list_blocks.append(list_temp)     
    return list_blocks

def split_odd_even(pdf_file_origin:str, path_output_file:str, paramters:list)->None:
    '''
        parameter -> True or False, para imprimir apenas par impar ou os dois, parameter[0] => par, parameter[1] => impar, 
    '''
    try:
        with open(pdf_file_origin, 'rb') as file:
            pdf_reader = PdfReader(file)
            pdf_writer_odd = PdfWriter()
            pdf_writer_even = PdfWriter()
            number_pages =  len(pdf_reader.pages)
            for index, page in enumerate(range(number_pages)):
                # Necessário adicionar o 1, porque as páginas começam do n. 1 e a lista do n. 0
                if ((index + 1) % 2 ) ==0 and paramters[0] == True:
                    pdf_writer_even.add_page(pdf_reader.pages[page])
                if ((index +1 )% 2) == 1 and paramters[1] == True:
                    pdf_writer_odd.add_page(pdf_reader.pages[page])    
            if  paramters[0] == True:
                new_name_output_file = __rename_file(path_output_file=path_output_file, name_to_add='par')
                with open(new_name_output_file, 'wb') as output_pdf_odd:
                    pdf_writer_even.write(output_pdf_odd)
            if  paramters[1] == True:
                new_name_output_file = __rename_file(path_output_file=path_output_file, name_to_add='impar')
                with open(new_name_output_file, 'wb') as output_pdf_even:
                    pdf_writer_odd.write(output_pdf_even)
            ModalsView().message_success('Operação concluida com sucesso')
            os.startfile(os.path.dirname(path_output_file))
    except Exception as error:
        ModalsView().exceptions_message(error)

def split_remove_pages(pdf_file_origin:str, path_output_file:str, list_pages_to_remove:list):
    try:
        with open(pdf_file_origin, 'rb') as file:
            pdf_reader = PdfReader(file)
            pdf_output = PdfWriter()
            number_pages =  len(pdf_reader.pages)
            for index, page in enumerate(range(number_pages)):
                # Necessário adicionar o 1, porque as páginas começam do n. 1 e a lista do n. 0
                if (index + 1) not in list_pages_to_remove:
                    pdf_output.add_page(pdf_reader.pages[page])
            with open(path_output_file, 'wb') as removed_pages_pdf:
                    pdf_output.write(removed_pages_pdf)
            ModalsView().message_success('Operação concluida com sucesso')
            os.startfile(os.path.dirname(path_output_file))
    except Exception as error:
        ModalsView().exceptions_message(error)


##### CHAMADAS ASSINCRONAS

def execute_split_remove_pages_async(pdf_file_origin:str, path_output_file:str,  list_pages_to_remove:list) ->None:
    execucao = ExecutorActions(split_remove_pages,pdf_file_origin, path_output_file, list_pages_to_remove)
    execucao.execute_with_loading()
    return True

def execute_split_async(pdf_file_origin:str, path_output_file:str,  arrays_blocks:list) ->None:
    execucao = ExecutorActions(split_by_lists,pdf_file_origin, path_output_file, arrays_blocks)
    execucao.execute_with_loading()
    return True

def split_odd_even_async(pdf_file_origin:str, path_output_file:str, paramters:list):
    execucao = ExecutorActions(split_odd_even,pdf_file_origin, path_output_file, paramters)
    execucao.execute_with_loading()
    return True