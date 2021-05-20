from PyInquirer import prompt

last_index = 0
choose = []
abstract = ''
author = ''
title = ''
index_title = {}
with open('result.txt', 'r', encoding='utf-8') as t:
    original = t.readlines()
    for index in range(len(original)):
        key = original[index][0:3]
        if key == 'T1 ':
            title = original[index][3:-1]
        if key == 'A1 ':
            author = original[index][3:-1]
        if key == 'AB ':
            abstract = original[index][3:-1]
        if key == 'DS ':
            choose.append({'name': title + ' ' + author})
            index_title[title + ' ' + author] = [last_index, index]
            abstract = ''
            author = ''
            title = ''
            last_index = index + 1
    questions = [
        {
            'type': 'checkbox',
            'qmark': ':)',
            'message': '选择要保留的文献,<a>全选,<i>反选,方向键移动,空格选择.',
            'name': 'title',
            'choices': choose,
            'validate': lambda answer: '请至少选择一篇文献.' \
                if len(answer) == 0 else True
        }
    ]
    answers = prompt(questions)
    with open('manual.txt', 'w', encoding='utf-8') as m:
        for title in answers['title']:
            for index in range(index_title[title][0], index_title[title][1] + 1):
                m.write(original[index])
