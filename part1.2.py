import json
import pygments.token
from pygments.lexer import Lexer
from pygments.lexers.parsers import PythonLexer


inverted_index = {}
source_dict = {}

# creating tokens for all received files
def make_token(source: str):
    with open(source, 'r', encoding='utf-8') as file:
        source_code = file.read()

    lexer = pygments.lexers.get_lexer_for_filename(source)
    tokens = Lexer.get_tokens(lexer, source_code)

    for tokentype, tokenvalue in tokens:
        if tokentype == pygments.token.Name:
            # filling dictionary, key = file location, value = list of token
            if source not in source_dict:
                source_dict[source] = []
                source_dict[source].append(tokenvalue)
            else:
                source_dict[source].append(tokenvalue)
            # filling dictionary, key = list of token, value = dictionary of file_location : count
            if tokenvalue not in inverted_index:
                inverted_index[tokenvalue] = {}
                inverted_index[tokenvalue][source] = 1
            if source in inverted_index[tokenvalue]:
                inverted_index[tokenvalue][source] += 1
            else:
                inverted_index[tokenvalue][source] = 1


with open('files.txt', 'r', encoding='utf-8') as ff:
    all_sources = ff.read().split('\n')
    for source in all_sources:
        source = source.strip()
        if source == 'D:\PyCharm\Project\JetBrains\part1.py':
            continue
        if source:
            make_token(source)


# record the received information in json
with open('data_json.txt', 'w', encoding='utf-8') as json_file:
    json.dump(inverted_index, json_file)

with open('data_json_source.txt', 'w', encoding='utf-8') as json_file:
    json.dump(source_dict, json_file)