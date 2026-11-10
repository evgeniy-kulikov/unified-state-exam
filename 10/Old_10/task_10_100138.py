""""""
"""
Task 10
ЕГЭ Питоныч
https://stepik.org/course/100138
"""


""" 39.2 Падежи и словоформы """
# https://stepik.org/lesson/768214/step/2?unit=770573
cnt = 0
with open('add/course_100138/10_Onegin.txt', encoding='utf-8') as fl:
    for f in fl:
        s = f.lower().strip().split()
        for el in s:
            if 'роман' in el:
                cnt += 1
                print(cnt, el)
# 26 - 4 = 22


# https://stepik.org/lesson/768214/step/3?unit=770573
cnt = 0
with open('add/course_100138/10_Onegin.txt', encoding='utf-8') as fl:
    for f in fl:
        s = f.lower().strip().split()
        for el in s:
            if 'плод' in el:
                cnt += 1
                print(cnt, el)
# 11 - 3 = 8


# https://stepik.org/lesson/768214/step/5?unit=770573
import re
reg = r'(?i)\bс[он][аеуон][м]*\b'
cnt = 0
with open('add/course_100138/10_Onegin.txt', encoding='utf-8') as fl:
    data = fl.read()
    d = re.findall(reg, data)
    for s in d:
        if s != 'снам':
            cnt += 1
            print(cnt, s)

# длиннее
import re
reg = r'с[он][аеуон][м]*\W*'
cnt = 0
with open('add/course_100138/10_Onegin.txt', encoding='utf-8') as fl:
    for f in fl:
        s = f.lower().strip().split()
        for el in s:
            if re.fullmatch(reg, el) and el[:4] != 'снам':
                cnt += 1
                print(cnt, el)  # 35
"""
и - сон *
р - сна *
д - сну *
в - сон 
т - сном *
п - сне *
"""

# https://stepik.org/lesson/768214/step/6?unit=770573
import re
reg = r'(?i)\bдруг[ауое]*[м]*\b'
cnt = 0
with open('add/course_100138/10_Onegin.txt', encoding='utf-8') as fl:
    data = fl.read()
    d = re.findall(reg, data)
    for s in d:
        if s != 'другое':
            cnt += 1
            print(cnt, s)
# 44 (принимается ответ 40)
"""
и - друг *
р - друга *
д - другу *
в - друга 
т - другом *
п - друге 
"""

# https://stepik.org/lesson/768214/step/7?unit=770573
import re
reg = r'(?i)\bмоскв[аыеуо]+[йю]*\b'
cnt = 0
with open('add/course_100138/10_Onegin.txt', encoding='utf-8') as fl:
    data = fl.read()
    d = re.findall(reg, data)
    for s in d:
        cnt += 1
        print(cnt, s)
# 14
"""
и - москва *
р - москвы *
д - москве *
в - москву * 
т - москвой *  москвою *
п - москве
"""


# https://stepik.org/lesson/768214/step/6?unit=770573
import re
reg = r'\bсчастие\b'
cnt = 0
with open('add/course_100138/10_Carenina.txt', encoding='utf-8') as fl:
    data = fl.read()
    d = re.findall(reg, data)
    for s in d:
        cnt += 1
        print(cnt, s)
# 7


# https://stepik.org/lesson/768214/step/8?unit=770573
import re
reg = r'\bсол[иь]ю*\b'
cnt = 0
with open('add/course_100138/10_Carenina.txt', encoding='utf-8') as fl:
    data = fl.read()
    d = re.findall(reg, data)
    for s in d:
        cnt += 1
        print(cnt, s)
# 3
"""
соль
соли
солью
"""


""" 39.3 Фрагменты слов и дефис """

# https://stepik.org/lesson/1401039/step/2?unit=1418001
import re
reg = r'(?i)\w*все\w+'
cnt = 0
with open('add/course_100138/10_2024.txt', encoding='utf-8') as fl:
    data = fl.read()
    d = re.findall(reg, data)
    for s in d:
        cnt += 1
        print(cnt, s)
# 9
