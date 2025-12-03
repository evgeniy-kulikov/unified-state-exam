""""""
"""
Task 24
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 24.1 Задание 24 ЕГЭ | Урок 1 """
# https://stepik.org/lesson/1720694/step/2?unit=1744230
# https://kompege.ru/task   № 2420 (Уровень: Базовый)
from re import findall
s = open('add/course_233165/24-1__02.txt').read()
reg = r'[ABEF]+'
d = findall(reg, s)
res = max(findall(reg, s), key=len)
print(len(res))  # 20

# variant
s = open('add/course_233165/24-1__02.txt').read()
s = s.replace('C', ' ').replace('D', ' ').split()
res = max(s, key=len)
print(len(res))  # 20


# https://stepik.org/lesson/1720694/step/3?unit=1744230
# https://kompege.ru/task   № 2426 (Уровень: Базовый)
from re import *
s = open('add/course_233165/24-1__03.txt').read()
reg = r'\d+'
res = max(map(len, findall(reg, s)))
print(res)  # 20


# https://stepik.org/lesson/1720694/step/4?unit=1744230
# https://kompege.ru/task   № 1040 100 базовых задач Е. Джобс (Уровень: Базовый)
from re import *
reg = r'\d+'
s = open('add/course_233165/24-1__04.txt').readline()
res = max(len(i) for i in findall(reg, s))
print(res)  # 12


# https://stepik.org/lesson/1720694/step/5?unit=1744230
# https://kompege.ru/task   № 1428 (Уровень: Базовый)
s = open('add/course_233165/24-1__05.txt').readline()
s = s.replace('XZ', 'X Z').replace('XY', 'X Y').split()
res = max(len(i) for i in s)
print(res)  # 25


# https://stepik.org/lesson/1661195/step/4?unit=1684068
# https://kompege.ru/task   № 1975 Демоверсия 2022 (Уровень: Базовый)
s = open('add/course_233165/24-1__06.txt').readline().strip()
while 'PP' in s:
    s = s.replace('PP', 'P P')
MX = max(len(i) for i in s.split())
print(MX)

# variant
MX, cnt = 0, 1
s = open('add/course_233165/24-1__06.txt').readline().strip()
for r in range(1, len(s)):
    if s[r - 1:r + 1] != 'PP':
        cnt += 1
        MX = max(MX, cnt)
    else:
        cnt = 1
print(MX)


# https://stepik.org/lesson/1720694/step/7?unit=1744230
# https://kompege.ru/task   № 1302 Открытый вариант КЕГЭ (Уровень: Базовый)
s = open('add/course_233165/24-1__07.txt').readline().strip()
s = s.replace('XZZY', 'XZZ ZZY').split()
MX = max(len(i) for i in s)
print(MX)  # 1713


# https://stepik.org/lesson/1720694/step/8?unit=1744230
# https://kompege.ru/task   № 4627 Основная волна 2022 (Уровень: Базовый)
from re import *
reg = r'(?:NPO|PNO)+'
s = open('add/course_233165/24-1__08.txt').readline().strip()
res = findall(reg, s)
print(max(map(len, res)) // 3)  # 327

# variant
s = open('add/course_233165/24-1__08.txt').readline().strip()
s = s.replace('NPO', '*').replace('PNO', '*')
s = s.replace('N', ' ').replace('P', ' ').replace('O', ' ').split()
print(max(map(len, s)))  # 327





""" 24.2 Задание 24 ЕГЭ | Урок 2 """
# https://stepik.org/lesson/1720695/step/1?unit=1744231
# https://kompege.ru/task   № 21 Демоверсия 2021 (Уровень: Базовый)
res = 0
cnt = 1
s = open('add/course_233165/24-2__01.txt').read()
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        cnt += 1
    else:
        res = max(res, cnt)
        cnt = 1
print(res)  # 35

# variant
s = open('add/course_233165/24-2__01.txt').readline()
cnt = [1] * len(s)
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        cnt[i] = cnt[i - 1] + 1
print(max(cnt))  # 35


# https://stepik.org/lesson/1720695/step/2?unit=1744231
# https://kompege.ru/task   №  2422 (Уровень: Базовый)
cnt = 1
res = 0
s = open('add/course_233165/24-2__02.txt').readline()
for i in range(1, len(s)):
    if s[i-1] <= s[i]:
        cnt += 1
    else:
        res = max(res, cnt)
        cnt = 1
print(res)  # 15


# https://stepik.org/lesson/1720695/step/3?unit=1744231
# https://kompege.ru/task   № 2423 (Уровень: Базовый)
s = open('add/course_233165/24-2__03.txt').readline().strip()
cnt, MX = 1, 0
for i in range(1, len(s)):
    if s[i - 1] < s[i]:
        cnt += 1
        MX = max(MX, cnt)
    else:
        cnt = 1
print(MX)  # 8

# variant
s = open('add/course_233165/24-2__03.txt').readline().strip()
ls = [1] * len(s)
for i in range(1, len(s)):
    if s[i - 1] < s[i]:
        ls[i] = ls[i - 1] + 1
print(max(ls))  # 8


# https://stepik.org/lesson/1720695/step/4?unit=1744231
# https://kompege.ru/task   № 2427 (Уровень: Средний)
st = open('add/course_233165/24-2__04.txt').readline()
st += st[-1]
cnt = 1
s = ''
for i in range(1, len(st)):
    if st[i - 1] > st[i]:
        cnt += 1
    else:
        if cnt > len(s):
            s = st[i - cnt:i]
        cnt = 1
print(s)  # zrqjWRC1

# variant
st = open('add/course_233165/24-2__04.txt').readline()
ls = [1] * len(st)
for i in range(1, len(st)):
    if st[i - 1] > st[i]:
        ls[i] = ls[i - 1] + 1
mx = max(ls)
i = ls.index(mx)
s = st[i-mx+1: i+1]
print(s)  # zrqjWRC1


# https://stepik.org/lesson/1720695/step/5?unit=1744231
# https://kompege.ru/task   № 4113 (Уровень: Базовый)
st = open('add/course_233165/24-2__05.txt').readline()
ls = [0] * len(st)
for i in range(1, len(st)):
    if st[i-1:i+1] in ('BB', 'DD'):
        ls[i] = ls[i-2] + 1
print(max(ls))  # 317

# variant
# >>> DDBBBDDDD => DDBB  DD     # 4
# DDDDBB  DD <= DDBBBDDDD <<<   # 6
from re import *
MX = 0
reg = f'(?:BB|DD)+'
st = open('add/course_233165/24-2__05.txt').readline()
for n in (1, -1):
    res = findall(reg, st[::n])
    MX = max(MX, len(max(res, key=len)))
print(MX // 2)  # 317


# https://stepik.org/lesson/1720695/step/6?unit=1744231
# https://kompege.ru/task   № 9552 Джобс 14.06.23 (Уровень: Сложный)
s = open('add/course_233165/24-2__06.txt').readline().strip()
cnt = MX = i = 0
while i <= len(s):  # возможность прохода по строке с переменным шагом
    if s[i:i+2] == 'PC':
        cnt += 2
        i += 2
    elif s[i:i+4] == 'CSGO':
        cnt += 4
        i += 4
    else:
        MX = max(MX, cnt)
        cnt = 0
        i += 1
print(MX)  # 90

# variant
s = open('add/course_233165/24-2__06.txt').readline().strip()
ls = [0] * len(s)
for i in range(len(s)):
    if s[i-1:i+1] == 'PC':
        ls[i] = ls[i-2] + 2
    if s[i-3:i+1] == 'CSGO':
        ls[i] = ls[i-4] + 4
print(max(ls))  # 90


# https://stepik.org/lesson/1720695/step/7?unit=1744231
# https://kompege.ru/task   № 4546 (Уровень: Базовый)
from re import *
reg = r'(?:A.A|C.C)+'
s = open('add/course_233165/24-2__07.txt').readline().strip()
a = findall(reg, s)
a = max(map(len, a)) // 3
b = findall(reg, s[::-1])
b = max(map(len, b)) // 3
print(max(a, b))  # 21

# variant
s = open('add/course_233165/24-2__07.txt').readline().strip()
ls = [0] * len(s)
for i in range(2, len(s)):
    if s[i-2] + s[i] in ['AA', 'CC']:
        ls[i] += ls[i-3] + 1
print(max(ls))  # 21


# https://stepik.org/lesson/1720696/step/4?unit=1744232
# https://kompege.ru/task   № 9169 Джобс 06.06.2023 (Уровень: Сложный)
s = open('add/course_233165/24-3__04.txt').readline().strip()
cnt = l = 0
MN = 10**6
w = ('BAD', 'FAT')
for r in range(2, len(s)):
    if s[r-2:r+1] in w:
        cnt += 1
    while cnt == 3:
        if s[l:l+3] in w:
            cnt -= 1
        MN = min(MN, r-l+1)
        l += 1
print(MN)  # 10




""" 24.3 Задание 24 ЕГЭ | Урок 3 """
# https://stepik.org/lesson/1720696/step/1?unit=1744232
# https://kompege.ru/task   № 12476 PRO100 ЕГЭ 29.12.23 (Уровень: Сложный)
l = cnt = MX = 0
s = open('add/course_233165/24-3__01.txt').readline()
for r in range(1, len(s)):
    if r >= 2 and s[r - 2: r + 1] in 'OROR':
        cnt = 0
        l = r - 1
    if s[r - 1: r + 1] == 'RO':
        cnt += 1
    while cnt > 21:
        if s[l:l+2] == 'RO':
            cnt -= 1
        l += 1
    if cnt == 21:
        MX = max(MX, r - l + 1)
print(MX)  # 814


# https://stepik.org/lesson/1720696/step/2?unit=1744232
# https://kompege.ru/task   № 6734 (Уровень: Средний)
l = cnt = 0
MN = 10**6
s = open('add/course_233165/24-3__02.txt').readline()
for r in range(len(s)):
    if s[r] == '.':
        cnt += 1
    # Слева до 1-й точки не должно быть букв. Справа мы уже стоим на 7-й точке
    while cnt == 7:
        MN = min(MN, r - l + 1)
        if s[l] == '.':
            cnt -= 1
        l += 1
print(MN)  # 16


# https://stepik.org/lesson/1720696/step/3?unit=1744232
# https://kompege.ru/task   № 11954 (Уровень: Средний)
st = open('add/course_233165/24-3__03.txt').readline().strip()
st = st.replace('Y', ' ').split()
st = [i for i in st if i.count('X') >= 500]
MN = 10**6
for el in st:
    l = cnt = 0
    for r in range(len(el)):
        if el[r] == 'X':
            cnt += 1
        while cnt >= 500:
            MN = min(MN, r - l + 1)
            if el[l] == 'X':
                cnt -= 1
            l += 1
print(MN)  # 68500

# variant
st = open('add/course_233165/24-3__03.txt').readline().strip()
MN = 10**6
l = cnt = 0
for r in range(len(st)):
    if st[r] == 'Y':
        cnt = 0
        l = r + 1
    if st[r] == 'X':
        cnt += 1
    while cnt >= 500:
        MN = min(MN, r - l + 1)
        if st[l] == 'X':
            cnt -= 1
        l += 1
print(MN)  # 68500




""" 24.4 Задание 24 ЕГЭ | Задачи прошлых лет """
# https://stepik.org/lesson/1720697/step/1?unit=1744233
# https://kompege.ru/task   № 9753 Основная волна 19.06.23 (Уровень: Сложный)
cnt = l = MX = 0
s = open('add/course_233165/24-4__01.txt').readline()
for r in range(len(s)):
    if s[r] == 'Y':
        cnt += 1
    while cnt > 150:
        if s[l] == 'Y':
            cnt -= 1
        l += 1
    if cnt <= 150:
        MX = max(MX, r - l + 1)
print(MX)  # 244


# https://stepik.org/lesson/1720697/step/2?unit=1744233
# https://kompege.ru/task   № 10724 (Уровень: Базовый)
from string import ascii_uppercase as abc
s = open('add/course_233165/24-4__02.txt').readline().strip()
for i in abc[6:]:
    s = s.replace(i, ' ')
s = s.split()
print(max(map(len, s)))  # 21



# https://stepik.org/lesson/1720697/step/3?unit=1744233
# https://kompege.ru/task   № 17535 Основная волна 07.06.24 (Уровень: Средний)
s = open('add/course_233165/24-4__03.txt').readline().strip()
cnt = l = MX = 0
for r in range(1, len(s)):
    if s[r-1:r+1] == 'CD':
        cnt += 1
    while cnt > 160:
        if s[l: l+2] == 'CD':
            cnt -= 1
        l += 1
    if cnt == 160:
        MX = max(MX, r - l + 1)
print(MX)  # 9712

# variant
s = open('add/course_233165/24-4__03.txt').readline().strip()
MX = 0
s = s.replace('CD', '*').split('*')
for i in range(len(s) - 160):
    r = ''.join(s[i:i+161])
    MX = max(MX, len(r) + 320 + 2)
print(MX)  # 9712


# https://stepik.org/lesson/1720697/step/4?unit=1744233
# https://kompege.ru/task   № 17563 Основная волна 08.06.24 (Уровень: Сложный)
from re import *
a = r'7+\d*'
reg = rf'{a}(?:-{a})+'
# reg = r'7+\d*(?:-7+\d*)+'
s = open('add/course_233165/24-4__04.txt').readline().strip()
s = s.replace('8', '7').replace('9', '7').replace('*', '-')
res = findall(reg, s)
print(max(map(len, res)))  # 40

# variant
from re import *
a = r'[1-9]+\d*'
reg = rf'{a}(?:[*-]{a})+'
# reg = r'[1-9]+\d*(?:[*-][1-9]+\d*)+'
s = open('add/course_233165/24-4__04.txt').readline().strip()
res = findall(reg, s)
print(max(map(len, res)))  # 40

