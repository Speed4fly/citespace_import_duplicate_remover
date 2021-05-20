# import re
#
# match = re.compile(r'[a-zA-Z0-9]{2}[ ]')
import os


def hash_tools(hash_dict, title, indexes, log):
    if hash_dict.__contains__(title):
        log.append([title, indexes])
        log.append([title, hash_dict[title]])
    else:
        hash_dict[title] = indexes


file_list = os.listdir('cnki')
original = []
file_number = 0
for file_name in file_list:
    if file_name[-4:] == '.txt':
        # print(file_name)
        with open('cnki/' + file_name, 'r+', encoding='utf-8') as f:
            # print(len(original))
            file_number += 1
            original += f.readlines()
with open('total.txt', 'w', encoding='utf-8') as t:
    for line in original:
        t.write(line)
print(file_number)
last_index = 0
count = 0
log = []
titles = []
hash_dict = {}
for index in range(len(original)):
    key = original[index][0:3]
    if key == 'T1 ':
        title = original[index][3:-1]

    elif key == 'A1 ':
        author = original[index][3:-1]
    elif key == 'DS ':
        count += 1
        hash_tools(hash_dict, title + author, [last_index, index], log)
        author = ''
        title = ''
        last_index = index + 1

with open('result.txt', 'w', encoding='utf-8') as r:
    keys = []
    for key in hash_dict.keys():
        keys.append(key)
    keys.sort()
    for key in keys:
        value = hash_dict[key]
        for index in range(value[0], value[1] + 1):
            r.write(original[index])
        r.write('\n')
print(len(hash_dict))
print(count)
with open('count.txt', 'w', encoding='utf-8') as c:
    c.write('Total: ' + str(count) + '\n')
    c.write('After: ' + str(len(hash_dict)))
with open('log.txt', 'w', encoding='utf-8') as l:
    for item in log:
        l.write(str(item) + '\n')

with open('title.txt', 'w', encoding='utf-8') as t:
    for item in keys:
        t.write(item + '\n')
