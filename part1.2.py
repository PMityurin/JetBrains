import json
import pygments.token
from pygments.lexer import Lexer
from pygments.lexers.parsers import PythonLexer


inverted_index = {}
source_dict = {}

# creating tokens for all received files
def make_token(source: str, lang: str):
    with open(source, 'r', encoding='utf-8') as file:
        source_code = file.read()

    lexer = pygments.lexers.get_lexer_for_filename(source)
    tokens = Lexer.get_tokens(lexer, source_code)

    for tokentype, tokenvalue in tokens:
        if 'Name' in str(tokentype).strip('.'):#tokentype == pygments.token.Name:
            # filling dictionary, key = file location, value = list of token
            if lang not in source_dict:
                source_dict[lang] = {}
            if source not in source_dict[lang]:
                source_dict[lang][source] = []
                source_dict[lang][source].append(tokenvalue)
            else:
                source_dict[lang][source].append(tokenvalue)
            # filling dictionary, key = list of token, value = dictionary of file_location : count
            if lang not in inverted_index:
                inverted_index[lang] = {}
            if tokenvalue not in inverted_index[lang]:
                inverted_index[lang][tokenvalue] = {}
                inverted_index[lang][tokenvalue][source] = 1
            if source in inverted_index[lang][tokenvalue]:
                inverted_index[lang][tokenvalue][source] += 1
            else:
                inverted_index[lang][tokenvalue][source] = 1


with open('files.json', encoding='utf-8') as json_f:
    found_files = json.load(json_f)
    for lang in found_files:
        for source in found_files[lang]:
            source = source.strip()
            if source:
                make_token(source, lang)


# record the received information in json
with open('data_json.json', 'w', encoding='utf-8') as json_file:
    json.dump(inverted_index, json_file)

with open('data_json_source.json', 'w', encoding='utf-8') as json_file:
    json.dump(source_dict, json_file)