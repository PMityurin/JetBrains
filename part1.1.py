import os
import zipfile
from zipfile import ZipFile
import time

from config import base_path

# insert the path to the file to be compared
path = base_path

found_files = []

# Search the archive for the necessary files
def archive_info(path_archive: str, path_start: str) -> list:
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
                found_files.append(f'{path_start}/{new_file}/{name}')


# Bypass folders to find the necessary files
def obhod_papok(path: str, path_start: str):
    for i in os.listdir(path):
        if os.path.isdir(f'{path}/{i}'):
            newpath = f'{path}/{i}'
            obhod_papok(newpath, path_start)
        else:
            if i.split('.')[-1] == 'py':
                found_files.append(f'{path}/{i}')
            elif i.split('.')[-1] == 'zip':
                archive_info(f'{path}/{i}', f'{path_start}')


obhod_papok(path, path)

# write to the file all the files that we found
with open('files.txt', 'w', encoding='utf-8') as f:
    for file in found_files:
        file = '/'.join(file.split('\\'))
        f.write(f'{file} \n')
