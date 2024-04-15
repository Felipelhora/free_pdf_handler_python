from src.views.ModalsView import ModalsView


def get_pages_inside_range(range_input:list) -> list or bool:
    '''
    range[0] -> inicio
    range[1] -> fim
    -> cria um range com valor de entrada, se houver dois valores o primeiro é o inicio do range, se houver apenas um valor ele é duplicado
    '''
    list_range = []
    try:
        valor_inicial = int(range_input[0])
        valor_final = int(range_input[1])
        if valor_inicial < valor_final:
            for number in range(valor_inicial,valor_final):
                list_range.append(number)
            list_range.append(valor_final)
        else:
            ModalsView().message_error(f'O valor {valor_inicial} é maior ou igual ao valor {valor_final}, corrija e refaça a operação')
            return False
    except:
            ModalsView().message_error(f'o valor {number}, possui erro no lançamento verifique e refaça novamente a operação')
            return False
    return list_range


def convert_str_to_int(number:str) -> bool or int:
    '''
        -> recupera tão somente o valor da string retornando o mesmo como inteiro
    '''
    try:
        int_page = int(number.strip())
        if int_page <=0:
            ModalsView().message_error(f'O valor {number} está errado, não pode ser menor ou igual a 0')     
            return False
        return int_page
    except:
        ModalsView().message_error(f'O valor {number} está errado, provavelmente não é um numero') 
        return False


def decode_input_with_str_to_list_int(input_str:str, repetition:bool=None) ->list or bool:
    '''
        number -> recebe parámetros de uma string e converte em uma lista ex: 1,2,5-7, onde separa por ',' e obtem o intervalo entre '-'
        repetition -> retira os arquivos repetidos, por padrão retorna sem repetido, qualquer valor de entrada permite o retorno de itens repetidos
    '''
    list_numbers = []
    pages = input_str.strip()
    pages = pages.split(',')
    for page in pages:
        page = page.strip()
        # verifica se é um arquivo único
        if '-' not in page:
            valor = convert_str_to_int(page)
            # verifica se o retorno não é falso
            if valor != False:
               list_numbers.append(valor)
            else:
                return False
        else:
            range_pages = page.split('-')
            pages_from_range = get_pages_inside_range(range_input=range_pages)
            if pages_from_range != False:
                list_numbers = list_numbers + pages_from_range
            else:
                return False
    if repetition == None:
       return list(set(list_numbers))
    else:
        return list_numbers

def decode_input_with_str_to_list_blocks(input_str:str, len_pages:int) -> list or bool:
    '''
        number -> recebe parámetros de uma string e converte em listas com primeiro e último número ex: 1,2,5-7, onde separa por ',' se  obtem [1,1], [2,2] 
        e com '-' se obtem [5,7]
    '''
    temp_list = []
    list_by_virg = input_str.split(',')
    for page_number in list_by_virg:
        page_number = page_number.strip()
        if '-' not in page_number:
            valor = convert_str_to_int(page_number)
            if valor != False:
               temp_list.append([(valor - 1), (valor - 1)])
            else:
                return False
        else:
            splited = page_number.split('-')
            try:
                value_init = int(splited[0])
                value_end = int(splited[1])
                if value_init <= 0 or value_end <= 0:
                    ModalsView().message_error(f'O valor {page_number} não é uma página válida')  
                    return False
                if value_init > len_pages or value_end > len_pages:
                    ModalsView().message_error(f'O valor {splited} contem um número que é maior que o numero de páginas')    
                    return False
                if value_init > value_end:
                    ModalsView().message_error(f'O valor {value_init} é maior que o valor de {value_end} refaça a operação')    
                    return False
                temp_list.append([(value_init-1), (value_end-1)])
            except:
                ModalsView().message_error (f'O valor {page_number} não é um número ou não está no padrão correto, por favor refaça a operação')
                return False
    return temp_list




