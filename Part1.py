import json
import os
import time

import zipfile
from zipfile import ZipFile

import pygments.lexers
import pygments.token
from pygments.util import ClassNotFound
from pygments.lexer import Lexer


found_files = {}
inverted_index = {}
source_dict = {}


def what_lexer(path:str) -> str:
    try:
        lexer = pygments.lexers.get_lexer_for_filename(path)
        lexer = str(lexer).split('.')[-1][:-1]
        return lexer
    except ClassNotFound:
        if path.split('.')[-1] == 'zip':
            return 'zip'


def add_found_file_depend_lang(path:str, lexer: str):
    if lexer not in found_files:
        found_files[lexer] = []
    found_files[lexer].append(path)


# Search the archive for the necessary files
def archive_zip_info(path_archive: str):
    zip_file = ZipFile(path_archive)
    informations = [text_file.filename for text_file in zip_file.infolist()]
    flag = False
    required_file = []
    for info in informations:
        lexer = what_lexer(info)
        if lexer:
            flag = True
            required_file.append((info, lexer))
    if flag:
        with zipfile.ZipFile(path_archive, 'r') as f_zip:
            for name, lexer in required_file:
                new_file = f'from_archive/{time.time()}'
                f_zip.extract(f'{name}', new_file)
                add_found_file_depend_lang(f'{new_file}/{name}', lexer)


# Bypass folders to find the necessary files
def folder_processing(path: str):
    for i in os.listdir(path):
        if os.path.isdir(f'{path}/{i}'):
            newpath = f'{path}/{i}'
            folder_processing(newpath)
        else:
            lexer = what_lexer(f'{path}/{i}')
            if lexer == 'zip':
                archive_zip_info(f'{path}/{i}')
            elif lexer:
                add_found_file_depend_lang(f'{path}/{i}', lexer)
            else:
                continue


def get_files(path:str):
    folder_processing(path)
    # write to the file all the files that we found
    with open('files.json', 'w', encoding='utf-8') as json_f:
        json.dump(found_files, json_f)


# creating tokens for received file
def make_token(source: str, lang: str):

    with open(source, 'r', encoding='utf-8') as file:
        source_code = file.read()

    lexer = pygments.lexers.get_lexer_for_filename(source)
    tokens = Lexer.get_tokens(lexer, source_code)

    for tokentype, tokenvalue in tokens:
        if 'Name' in str(tokentype).strip('.'):     #tokentype == pygments.token.Name:
            # filling dictionary, key = file location, value = list of token
            if lang not in source_dict:
                source_dict[lang] = {}
            if source not in source_dict[lang]:
                source_dict[lang][source] = [tokenvalue]
            else:
                source_dict[lang][source].append(tokenvalue)
            # filling dictionary, key = list of token, value = dictionary of file_location : count
            if lang not in inverted_index:
                inverted_index[lang] = {}
            if tokenvalue not in inverted_index[lang]:
                inverted_index[lang][tokenvalue] = {}
                inverted_index[lang][tokenvalue][source] = 1
            elif source in inverted_index[lang][tokenvalue]:
                inverted_index[lang][tokenvalue][source] += 1
            else:
                inverted_index[lang][tokenvalue][source] = 1


def get_tokens_from_found_files():
    with open('files.json', encoding='utf-8') as json_f:
        found_files = json.load(json_f)
        for lexer in found_files:
            for source in found_files[lexer]:
                source = source.strip()
                if source:
                    make_token(source, lang=lexer)


if __name__ == '__main__':
    path = input('Enter the path to be processed:\n')
    get_files(path)

    get_tokens_from_found_files()

    # record the received information in json
    with open('data_json.json', 'w', encoding='utf-8') as json_file:
        json.dump(inverted_index, json_file)
    with open('data_json_source.json', 'w', encoding='utf-8') as json_file:
        json.dump(source_dict, json_file)