import json
import pygments.token
from pygments.lexer import Lexer
from pygments.lexers.parsers import PythonLexer
from config import new_path
from pygments.util import ClassNotFound


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
    with open(source[1:], 'r', encoding='utf-8') as file:
        source_code = file.read()
    lexer = pygments.lexers.get_lexer_for_filename(source)
    tokens = Lexer.get_tokens(lexer, source_code)
    token_value_dict, lang = what_lang(source)
    for tokentype, tokenvalue in tokens:
        if 'Name' in str(tokentype).strip('.'):
            token_value_dict.get(lang, []).append(tokenvalue)
    with open('New_tokens.json', 'w', encoding='utf-8') as new_f:
        json.dump(token_value_dict, new_f)
    return token_value_dict


# the function compares two lists and returns a number (the longest common substring)
def lcs(list1:list, list2:list) -> int:
    start_list1 = [0] + list1
    start_list2 = [0] + list2
    dp = []
    for i in range(len(start_list2)):
        temp = []
        for j in range(len(start_list1)):
            temp.append(0)
        dp.append(temp)
    for i in range(1, len(start_list2)):
        for j in range(1, len(start_list1)):
            if start_list2[i] == start_list1[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(list2)][len(list1)]


def file_comparison(path:str) -> str:
    matrix_repetitions = []
    # get previously processed data
    with open('data_json.json', encoding='utf-8') as json_file:
        inverted_index = json.load(json_file)
    with open('data_json_source.json', encoding='utf-8') as json_file:
        sources_dict = json.load(json_file)
    with open('New_tokens.json', encoding='utf-8') as json_file:
        token_values_new = json.load(json_file)

    for i in token_values_new:
        new_token_values = token_values_new[i]  # getting a list with new tokens
        lang = i

    all_token_values = []
    for key in inverted_index[lang]:
        if key in new_token_values:
            all_token_values.append(key)    # filled out a list with tokens, where there is at least one match with new tokens

    set_sources = set()
    for key in all_token_values:
        for info in inverted_index[lang][key]:
            set_sources.add(info)       # created a set with the location of files where there is at least one match

    list_sources = list(set_sources)
    needed_sources = []
    for one_source in list_sources:
        count_token_name = len(sources_dict[lang][one_source])
        if len(new_token_values) / count_token_name >= 0.85:
            needed_sources.append(one_source)       # removed files that, with a complete match, do not give 85%

    count_match = []
    for source1 in needed_sources:
        token_list = sources_dict[lang][source1]
        temp_count = lcs(token_list, new_token_values)
        procen = temp_count / len(sources_dict[lang][source1])
        procen = float(str(procen)[:5]) * 100
        if procen < 85:
            count_match.append(['OK', temp_count, procen])
            print('OK', f'{temp_count} matches', f'{procen} %')
        else:
            count_match.append([f'{source1}', temp_count, procen])
            print(f'{source1}', f'{temp_count} matches', f'{procen} %')
    for i in count_match:
        if i[0] != 'OK':
            return f'{i[0]} | {i[1]} matches | {i[2]} %'
    else:
        for tokenvalue in new_token_values:
            # filling dictionary, key = file location, value = list of token
            if lang not in sources_dict:
                sources_dict[lang] = {}
            if path not in sources_dict[lang]:
                sources_dict[lang][path] = [tokenvalue]
            else:
                sources_dict[lang][path].append(tokenvalue)
            # filling dictionary, key = list of token, value = dictionary of file_location : count
            if lang not in inverted_index:
                inverted_index[lang] = {}
            if tokenvalue not in inverted_index[lang]:
                inverted_index[lang][tokenvalue] = {}
                inverted_index[lang][tokenvalue][path] = 1
            elif path in inverted_index[lang][tokenvalue]:
                inverted_index[lang][tokenvalue][path] += 1
            else:
                inverted_index[lang][tokenvalue][path] = 1
            # record the received information in json
            with open('data_json.json', 'w', encoding='utf-8') as json_file:
                json.dump(inverted_index, json_file)
            with open('data_json_source.json', 'w', encoding='utf-8') as json_file:
                json.dump(sources_dict, json_file)
        return f'OK'