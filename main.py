# import re
#
# match = re.compile(r'[a-zA-Z0-9]{2}[ ]')


def hash_tools(hash_dict, title, indexes, log):
    if hash_dict.__contains__(title):
        log.append([title, indexes])
        log.append([title, hash_dict[title]])
    else:
        hash_dict[title] = indexes


with open('source.txt', 'r+', encoding='utf-8') as f:
    original = f.readlines()
    last_index = 0
    count = 0
    log = []
    titles = []
    hash_dict = {}
    for index in range(len(original)):
        key = original[index][0:3]
        if key == 'T1 ':
            title = original[index][3:]

        elif key == 'A1 ':
            author = original[index][3:]
        elif key == 'DS ':
            count += 1
            hash_tools(hash_dict, title + author, [last_index, index], log)
            author = ''
            title = ''
            last_index = index

    with open('result.txt', 'w', encoding='utf-8') as r:
        keys = []
        for key in hash_dict.keys():
            keys.append(key)
        keys.sort()
        for key in keys:
            value = hash_dict[key]
            for index in range(value[0], value[1]):
                r.write(original[index])
            r.write('\n')
    print(len(hash_dict))
    print(count)
    with open('log.txt', 'w', encoding='utf-8') as l:
        for item in log:
            l.write(str(item) + '\n')

    with open('title.txt', 'w', encoding='utf-8') as t:
        for item in keys:
            t.write(item)
