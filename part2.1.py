import json

import pygments.token
from pygments.lexer import Lexer
from pygments.lexers.parsers import PythonLexer


source = "D:\\PyCharm\\Project\\Zadachki\\Yandex\\Лекция 6\\Zad2.1.py"


def new_token(source:str) -> list:
    with open(source, 'r', encoding='utf-8') as file:
        source_code = file.read()
    lexer = pygments.lexers.get_lexer_for_filename(source)
    tokens = Lexer.get_tokens(lexer, source_code)
    token_value = []
    for tokentype, tokenvalue in tokens:
        if tokentype == pygments.token.Name:
            token_value.append(tokenvalue)
    return token_value




token_value = new_token(source)

with open('New_tokens.txt', 'w', encoding='utf-8') as new_f:
    json.dump({'token_value':token_value}, new_f)

