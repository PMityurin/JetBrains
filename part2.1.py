import json
import pygments.token
from pygments.lexer import Lexer
from pygments.lexers.parsers import PythonLexer
from config import new_path
from pygments.util import ClassNotFound


# insert the path to the file to be compared
source = new_path


def what_lang(path:str) -> tuple:
    try:
        lexer = pygments.lexers.get_lexer_for_filename(path)
        lexer = str(lexer).split('.')[-1][:-1]
        new_token_dict = {}
        new_token_dict[lexer] = []
        return new_token_dict, lexer
    except ClassNotFound:
        print('The downloaded file is in the wrong format, try again')



# create new token from new file
def new_token(source:str) -> dict:
    with open(source, 'r', encoding='utf-8') as file:
        source_code = file.read()
    lexer = pygments.lexers.get_lexer_for_filename(source)
    tokens = Lexer.get_tokens(lexer, source_code)
    token_value_dict, lang = what_lang(source)
    for tokentype, tokenvalue in tokens:
        if 'Name' in str(tokentype).strip('.'):
            token_value_dict[lang] = token_value_dict.get(lang, []) + [tokenvalue]
    return token_value_dict


token_value = new_token(source)


with open('New_tokens.json', 'w', encoding='utf-8') as new_f:
    json.dump(token_value, new_f)

