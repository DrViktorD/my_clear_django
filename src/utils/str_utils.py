from .console_utils import my_print

def gen_hash_from_str(input='') -> str:
    """Принимает строку, удаляет пробелы и знаки препинания,
        возвращает строку в нижнем регистре"""
    if not input:
        my_print(f'На вход gen_hash_from_str не переданы данные')
        return False        
    if not isinstance(input, str):
        my_print(f'На вход gen_hash_from_str передана не строка. input = {input}')
        return False
   
    try:
        result = ''.join(filter(str.isalnum, str(input)))
        return (result.lower())
    except:
        return False