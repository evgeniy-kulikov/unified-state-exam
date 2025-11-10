""""""
"""
Task 24
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
"""

""" 23.1 Задачи на строки и подстроки """

# https://stepik.org/lesson/1247109/step/2?unit=1260932
with open('add/course_182932/24_2420.txt') as file:
    s = file.read().strip()
    s = s.replace('C', ' ').replace('D', ' ').split()
    print(max(len(i) for i in s))  # 20


# https://stepik.org/lesson/1247109/step/3?unit=1260932
with open('add/course_182932/24_2426.txt') as file:
    s = file.read().strip()
    s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ').split()
    print(max(len(i) for i in s))  # 20

# https://stepik.org/lesson/1247109/step/4?unit=1260932
from re import *
reg = r'(?:\d+)'
with open('add/course_182932/24_1040.txt') as file:
    s = file.read().strip()
    res = findall(reg, s)
    print(max(len(i) for i in res))  # 12


# https://stepik.org/lesson/1247109/step/5?unit=1260932
with open('add/course_182932/24_1428.txt') as file:
    s = file.read().strip()
    s = s.replace('XY', 'X Y').replace('XZ', 'X Z').split()
    print(max(len(i) for i in s))  # 25


# https://stepik.org/lesson/1247109/step/6?unit=1260932
with open('add/course_182932/24_1975.txt') as file:
    s = file.read().strip()
    while 'PP' in s:
        s = s.replace('PP', 'P P')
    print(max(len(i) for i in s.split()))  # 188


# https://stepik.org/lesson/1247109/step/7?unit=1260932
with open('add/course_182932/24_1302.txt') as file:
    s = file.read().strip()
    s = s.replace('XZZY', 'XZZ ZZY')
    print(max(len(i) for i in s.split()))  # 1713


# https://stepik.org/lesson/1247109/step/8?unit=1260932
from re import *
reg = r'(?:NPO|PNO)+'
with open('add/course_182932/24_4627.txt') as file:
    s = file.read().strip()
    res = findall(reg, s)
    print(max(len(i) for i in res) // 3)  # 327


# https://stepik.org/lesson/1247109/step/9?unit=1260932
from re import *
reg = r'(?:[BCD][AO])+'
with open('add/course_182932/24_4602.txt') as file:
    s = file.read().strip()
    res = findall(reg, s)
    print(max(len(i) for i in res) // 2)  # 174


# https://stepik.org/lesson/1247109/step/10?unit=1260932
from re import *
reg = r'(?:[12]{2}[AB])+'
with open('add/course_182932/24_4643.txt') as file:
    s = file.read().strip()
    res = findall(reg, s)
    print(max(len(i) for i in res) // 3)  # 67


# https://stepik.org/lesson/1247109/step/11?unit=1260932
with open('add/course_182932/24_8510.txt') as file:
    s = file.read().strip()
    s = s.replace('N', 'P').replace('O', 'P')
    while 'PP' in s:
        s = s.replace('PP', 'P P')
    print(max(len(i) for i in s.split()))  # 57


# https://stepik.org/lesson/1247109/step/12?unit=1260932
with open('add/course_182932/24_21.txt') as file:
    s = file.read().strip()
    cnt = 1
    MX = 0
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            cnt += 1
            MX = max(MX, cnt)
        else:
            cnt = 1
    print(MX)  # 35

with open('add/course_182932/24_21.txt') as file:
    s = file.read().strip()
    ls = [1] * len(s)
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            ls[i] += ls[i-1]
    print(max(ls))  # 35


# https://stepik.org/lesson/1247109/step/13?unit=1260932
with open('add/course_182932/24_2422.txt') as file:
    s = file.read().strip()
    ls = [1] * len(s)
    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            ls[i] += ls[i-1]
    print(max(ls))  # 15


# https://stepik.org/lesson/1247109/step/15?unit=1260932
with open('add/course_182932/24_9552.txt') as file:
    s = file.read().strip()
    ls = [1] * len(s)
    for i in range(1, len(s)):
        if s[i] > s[i-1]:
            ls[i] += ls[i-1]
    print(max(ls))  # 8


# https://stepik.org/lesson/1247109/step/14?unit=1260932
from re import *
reg = r'(?:PC|CSGO)+'
with open('add/course_182932/24_9552.txt') as file:
    s = file.read().strip()
    res = findall(reg, s)
    print(max(len(i) for i in res))  # 90



""" 1.4 Повторение 4 часть """
# https://stepik.org/lesson/1343760/step/4?unit=1359470
res = 0
with open('add/course_182932/24_22.txt') as file:
    s = file.read().strip().split('F')
    for i in range(len(s) - 1):
        # r = len(s[i] + s[i+1]) + 1
        r = len(s[i:i+2]) + 1
        res = max(res, r)
    print(res)  # 45


# https://stepik.org/lesson/1343760/step/5?unit=1359470
# через split('Y')
res = 0
with open('add/course_182932/24_33.txt') as file:
    s = file.read().strip().split('Y')
    for i in range(len(s) - 150):
        r = len(''.join(s[i:i+152])) + 150
        res = max(res, r)
    print(res)  # 244

# через цикл
res = 0
cnt = 0
l = 0
with open('add/course_182932/24_33.txt') as file:
    s = file.read().strip()
    for r in range(len(s)):
        if s[r] == 'Y':
            cnt += 1
        while cnt > 150:
            if s[l] == 'Y':
                cnt -= 1
            l += 1
        if cnt <= 150:
            res = max(res, r - l + 1)
    print(res)  # 244


# https://stepik.org/lesson/1343760/step/6?unit=1359470
# цикл
res = 0
cnt = 0
l = 0
with open('add/course_182932/24_44.txt') as file:
    s = file.read().strip()
    for r in range(1, len(s)):
        if s[r-1:r+1] == 'AB':
            cnt += 1
        while cnt > 50:
            if s[l:l+2] == 'AB':
                cnt -= 1
            l += 1
        if cnt == 50:
            res = max(res, r - l + 1)
    print(res)  # 10128

# через replace('AB', 'A B').split()
res = 0
with open('add/course_182932/24_44.txt') as file:
    s = file.read().strip().replace('AB', 'A B')
    s = s.split()
    for i in range(len(s) - 50):
        row = s[i: i + 50 + 1]
        res = max(res, len(''.join(row)))
    print(res)  # 10128


# https://stepik.org/lesson/1343760/step/7?unit=1359470
with open('add/course_182932/24_55.txt') as file:
    s = file.read().strip().replace('AXMM', 'AXM XMM')
    s = s.split()
    res = max(s, key=len)
    print(len(res))  # 689


# https://stepik.org/lesson/1343760/step/8?unit=1359470
# https://kompege.ru/task  № 16388 ЕГКР 27.04.24
MX = 0
cnt = 3
with open('add/course_182932/24_66.txt') as file:
    s = file.read().strip()
    for i in range(len(s) - 3):
        if s[i:i + 4] in 'KLMNKLM':
            cnt += 1
            MX = max(MX, cnt)
        else:
            cnt = 3
    print(MX)