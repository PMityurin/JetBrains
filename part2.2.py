import json

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
