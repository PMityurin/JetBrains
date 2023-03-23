import json
import os
import zipfile
from zipfile import ZipFile
import time
import pygments.lexers
from pygments.util import ClassNotFound

from config import base_path

# insert the path to the file to be compared
path = base_path

found_files = {}

def what_lang(path:str):
    try:
        lexer = pygments.lexers.get_lexer_for_filename(path)
        lexer = str(lexer).split('.')[-1][:-1]
        if lexer not in found_files:
            found_files[lexer] = []
        found_files[lexer].append(path)
    except ClassNotFound:
        if path.split('.')[-1] == 'zip':
            archive_info(path)


# Search the archive for the necessary files
def archive_info(path_archive: str):
    zip_file = ZipFile(path_archive)
    informations = [text_file.filename for text_file in zip_file.infolist()]
    flag = False
    required_file = []
    for info in informations:
        if info.split('.')[-1] == 'py':
            flag = True
            required_file.append(info)
    if flag:
        with zipfile.ZipFile(path_archive, 'r') as f_zip:
            for name in required_file:
                new_file = f'from_archive/{time.time()}'
                f_zip.extract(f'{name}', new_file)
                what_lang(f'{new_file}/{name}')


# Bypass folders to find the necessary files
def get_files(path: str):
    for i in os.listdir(path):
        if os.path.isdir(f'{path}/{i}'):
            newpath = f'{path}/{i}'
            get_files(newpath)
        else:
            what_lang(f'{path}/{i}')


def get_files(path:str):
    obhod_papok(path)
    # write to the file all the files that we found
    with open('files.json', 'w', encoding='utf-8') as json_f:
        json.dump(found_files, json_f)


get_files(path)