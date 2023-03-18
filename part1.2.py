import json
import pygments.token
from pygments.lexer import Lexer
from pygments.lexers.parsers import PythonLexer



# source = 'D:\\PyCharm\\Project\\JetBrains\\main.py'
inverted_index = {}
source_dict = {}

def make_token(source: str):
    with open(source, 'r', encoding='utf-8') as file:
        source_code = file.read()

    lexer = pygments.lexers.get_lexer_for_filename(source)
    tokens = Lexer.get_tokens(lexer, source_code)

    for tokentype, tokenvalue in tokens:
        if tokentype == pygments.token.Name:
            if source not in source_dict:
                source_dict[source] = []
                source_dict[source].append(tokenvalue)
            else:
                source_dict[source].append(tokenvalue)
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


# with open('inverted_index.txt', 'w', encoding='utf-8') as f:
#     for i in inverted_index:
#         f.write(f'{i}: {inverted_index[i]}\n\n')

with open('data_json.txt', 'w', encoding='utf-8') as json_file:
    json.dump(inverted_index, json_file)

with open('data_json_source.txt', 'w', encoding='utf-8') as json_file:
    json.dump(source_dict, json_file)