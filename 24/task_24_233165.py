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


# https://stepik.org/lesson/1720694/step/9?unit=1744230
# https://kompege.ru/task   № 4602 Основная волна 2022 (Уровень: Базовый)
from re import *
reg = r'(?:[BCD][AO])+'
s = open('add/course_233165/24-1__09.txt').readline().strip()
res = findall(reg, s)
print(len(max(res, key=len)) // 2)  # 174

# variant
s = open('add/course_233165/24-1__09.txt').readline().strip()
s = s.replace('O', 'A').replace('C', 'B').replace('D', 'B')
s = s.replace('BA', '*').replace('A', ' ').replace('B', ' ').split()
print(len(max(s, key=len)))  # 174


# https://stepik.org/lesson/1720694/step/10?unit=1744230
# https://kompege.ru/task   № 4643 (Уровень: Базовый)
from re import *
reg = r'(?:\d{2}[AB])+'
s = open('add/course_233165/24-1__10.txt').readline()
res = findall(reg, s)
print(len(max(res, key=len)) // 3)  # 67

# variant
s = open('add/course_233165/24-1__10.txt').readline()
s = s.replace('B', 'A').replace('2', '1').replace('11A', '*')
s = s.replace('A', ' ').replace('1', ' ').split()
print(len(max(s, key=len)))  # 67


# https://stepik.org/lesson/1720694/step/11?unit=1744230
# https://kompege.ru/task   № 8510 Апробация 17.05 (Уровень: Средний)
s = open('add/course_233165/24-1__11.txt').readline()
s = s.replace('O', 'N').replace('P', 'N')
while 'NN' in s:  # иначе могут остаться NN  NNNA -> N NNA
    s = s.replace('NN', 'N N')
s = s.split()
print(len(max(s, key=len)))  # 57




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


# https://stepik.org/lesson/1720695/step/8?unit=1744231
# https://kompege.ru/task   № 2251 (Уровень: Базовый)
s = open('add/course_233165/24-2__08.txt').readline().strip()
cnt = l = MX = 0
for r in range(len(s)):
    if s[r] == 'D':
        cnt += 1
    while cnt > 2:
        if s[l] == 'D':
            cnt -= 1
        l += 1
    MX = max(MX, r - l + 1)
print(MX)  # 373


# https://stepik.org/lesson/1720695/step/9?unit=1744231
# https://kompege.ru/task   № 10105 Демоверсия 2024 (Уровень: Средний)
s = open('add/course_233165/24-2__09.txt').readline()
cnt = l = mx = 0
for r in range(len(s)):
    if s[r] == 'T':
        cnt += 1
    while cnt > 100:
        if s[l] == 'T':
            cnt -= 1
        l += 1
    if cnt == 100:
        mx = max(mx, r-l+1)
print(mx)  # 133


# https://stepik.org/lesson/1720695/step/10?unit=1744231
# https://kompege.ru/task   № 13715 (Уровень: Средний)
s = open('add/course_233165/24-2__10.txt').readline()
cnt = l = mx = 0
for r in range(1, len(s)):
    if s[r-1:r+1] == 'AB':
        cnt += 1
    while cnt > 50:
        if s[l:l+2] == 'AB':
            cnt -= 1
        l += 1
    if cnt == 50:
        mx = max(mx, r-l+1)
print(mx)  # 10128

# variant
mx = 0
s = open('add/course_233165/24-2__10.txt').readline()
s = s.replace('AB', 'A B').split()
for i in range(len(s) - 50):
    mx = max(mx, sum(map(len, s[i:i+51])))
print(mx)  # 10128





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


# https://stepik.org/lesson/1720696/step/5?unit=1744232
# https://kompege.ru/task   № 5171 (Уровень: Базовый)
from re import *
reg = r'(?:CA)+A?'
s = open('add/course_233165/24-3__05.txt').readline()
res = findall(reg, s)
print(len(max(res, key=len)))  # 54


# https://stepik.org/lesson/1720696/step/6?unit=1744232
# https://kompege.ru/task   № 2425 (Уровень: Базовый)
# Неполная цепочка в конце
mx = 0
cnt = 3
s = open('add/course_233165/24-3__06.txt').readline()
for i in range(len(s) - 3):
    if s[i:i + 4] in 'DBACDBA':
        cnt += 1
        mx = max(mx, cnt)
    else:
        cnt = 3
print(mx)  # 95


# https://stepik.org/lesson/1720696/step/7?unit=1744232
# https://kompege.ru/task   № 2428 (Уровень: Средний)
# Неполная цепочка как в начале, так и в конце
mx = 0
cnt = 2
s = open('add/course_233165/24-3__07.txt').readline()
for i in range(len(s) - 2):
    if s[i:i + 3] in 'XYZXY':
        cnt += 1
        mx = max(mx, cnt)
    else:
        cnt = 2
print(mx)  # 69


# https://stepik.org/lesson/1720696/step/8?unit=1744232
# https://kompege.ru/task   № 18597 (Уровень: Средний)
from re import *
s = open('add/course_233165/24-3__08.txt').readline()
n = r'[1-9]\d{3}\.\d+'
reg = rf'(?:{n}(?:&{n})+)'
# reg = r'(?:[1-9]\d{3}\.\d+(?:&[1-9]\d{3}\.\d+)+)'
res = findall(reg, s)
print(max(map(len, res)))  # 45
# 6122.27372&3813.88339566131561929530755870808






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


# https://stepik.org/lesson/1720697/step/5?unit=1744233
# https://kompege.ru/task   № 17641 Основная волна 19.06.24 (Уровень: Гроб)   142
# Hard task !!!
from re import *
n = f'(0|[1-9]\d*)'
reg = rf'{n}([*+]{n})+'
s = open('add/course_233165/24-4__05_1.txt').readline()
find = finditer(reg, s)
res = [i.group() for i in find]
# res = [i for i in res if len(i) > 100]  # 100 для ускорения
MX = 0
for i in res:
    d = i.split('+')
    cnt = 0
    for i in d:
        if not eval(i):
            cnt += len(i) + 1
            MX = max(MX, cnt - 1)
        else:
            cnt = 0
print(MX)  # 142


# https://stepik.org/lesson/1720697/step/6?unit=1744233
# https://kompege.ru/task   № 17878 Демоверсия 2025 (Уровень: Сложный)
from re import *
s = open('add/course_233165/24-4__06.txt').readline()
n = r'(?:[1-9]\d*|0)'
reg = rf'(?:{n}(?:[*-]{n})+)'
# reg = rf'(?:(?:[1-9]\d*|0)(?:[*-](?:[1-9]\d*|0))+)'
res = findall(reg, s)
# res = [i.group() for i in finditer(reg, s)]
print(max(map(len, res)))  # 154
# print(max(res, key=len))
# 79799-60-709*970*78680*797006866988009689*76687809-76796077-97079*990*8*9796-88977-6987790-87779*76-0-96-6-8766006666069770860808660*879097866096*8686*8*0




""""""
""" Варианты """
# 28.1 Вариант 1 | Часть 1
# https://stepik.org/lesson/1729565/step/10?unit=1753394
# https://kompege.ru/task  № 17878 Демоверсия 2025 (Уровень: Сложный)
from re import *
n = r'(?:[6-9]\d*|0)'
reg = rf'(?:{n}(?:[*-]{n})+)'
s = open('01_24.txt').read()
res = findall(reg, s)
print(len(max(res, key=len)))  # 154


# 29.1 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/10?unit=1753726
# https://kompege.ru/task  № 19254 ЕГКР 21.12.24 (Уровень: Базовый)
l = cnt = res = 0
f = open('02_24.txt').read().strip()
for r in range(3, len(f)):
    if f[r - 3:r + 1] == 'FSRQ':
        cnt += 1
    while cnt > 80:
        if f[l:l+4] == 'FSRQ':
            cnt -= 1
        l += 1
    if cnt == 80:
        res = max(res, r - l + 1)
print(res)  # 2379

# variant
n = 80
res = 0
f = open('02_24.txt').read().strip()
f = f.replace('FSRQ', ' ').split()
for i in range(len(f) - n):
    sm = sum(len(k) for k in f[i:i + n+1]) + 80 * 4 + 6
    # 81 строка где нет 'FSRQ'  +  80 подстрок 'FSRQ'  +  'FSR' + 'SRQ'
    # возможно будет ошибка если искомый участок будет вначале строки или в ее конце
    res = max(res, sm)
print(res)  # 2379


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730528/step/10?unit=1754357
# https://kompege.ru/task  № 20813 Апробация 05.03.25 (Уровень: Сложный)
from re import *
n = r'(?:[7-9]\d*|0)'
reg = rf'{n}(?:[*-]{n})+'
st = open('03_24.txt').readline().strip()
ls = findall(reg, st)
res = max(ls, key=len)
print(len(res))  # 111


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/10?unit=1760676
# https://kompege.ru/task  № 21421 Досрочная волна 2025 (Уровень: Базовый)
from re import *
reg = r'(?:[1-9AB][0-9AB]*[02468A])'
s = open('04_24.txt').readline()
f = findall(reg, s)
res = max(f, key=len)
print(len(res))  # 19


# 32.2 Вариант 5 | Часть 2
# https://stepik.org/lesson/1754189/step/10?unit=1778648
# https://kompege.ru/task  № 21717 ЕГКР 19.04.25 (Уровень: Средний)
# В поиске минимальной строки притаился замечательный скрытый камень 😉
s = open('05_24.txt').read().strip()
# s = 'QQQ' + 'RSQ' * 130 + 'SSSQ'  # проверка
cnt = l = 0
res = 10**10
for r in range(2, len(s)):
    if s[r-2:r+1] == 'RSQ':
        cnt += 1
    while cnt > 130:
        if s[l:l+3] == 'RSQ':
            cnt -= 1
        l += 1
    if cnt == 130 and s[r] != 'Q':
        # на сколько нужно убрать лишние символы перед первой слева подстрокой 'RSQ' 😉
        idx = s[l:r+1].index('RSQ')
        res = min(res, r - l - idx + 1)
print(res)  # 497


# 33.2 Вариант 6 | Часть 2
# https://stepik.org/lesson/1943171/step/10?unit=1969925
# https://kompege.ru/task  № 23206 Основная волна 10.06.25 (Уровень: Средний)
s = open('06_24.txt').readline().strip()
l = c = mx = 0
for r in range(len(s)):
    if s[r] in '02468':
        l = r
        c = 0
    if s[r] == 'S':
        c += 1
    if c == 35 and s[l] in '02468':
        mx = max(mx, r - l + 1)
print(mx)  # 292

# дольше по времени
s = open('06_24.txt').readline().strip()
for i in '2468':
    s = s.replace(i, '0')
mx = 0
for l in range(len(s)):
    for r in range(l+mx, len(s)):
        st = s[l:r+1]
        if any([st[0] != '0', st.count('0') > 1, st.count('S') > 35]):
            break
        if st[0] == '0' and st.count('S') == 35:
            mx = max(mx, len(st))
print(mx)  # 292



# 34.2 Вариант 7 | Часть 2
# https://stepik.org/lesson/1943174/step/10?unit=1969928
# https://kompege.ru/task  № 23281 Основная волна 11.06.25 (Уровень: Средний)
# Двойной указатель
s = open('07_24.txt').readline()
mx = l = c_y = 0
for r in range(len(s)):
    if s[r] == 'Y':
        c_y += 1
    while c_y > 80:
        if s[l] == 'Y':
            c_y -= 1
        l += 1
    if c_y == 80 and s[l: r+1].count('2025') >= 90:
        mx = max(mx, r-l+1)
print(mx)  # 2981

# Двойной цикл
m = 0
s = open('07_24.txt').readline()
for l in range(len(s)):
    for r in range(l+m, len(s)):
        st = s[l:r + 1]
        if st.count('Y') > 80:
            break
        if st.count('Y') == 80 and st.count('2025') >= 90:
            m = max(m, len(st))
print(m)  # 2981



# 35.2 Вариант 8 | Часть 2
# https://stepik.org/lesson/1943181/step/10?unit=1969936
# https://kompege.ru/task  № 23568 Пересдача 03.07.25 (Уровень: Средний)
a = ''
d = '0123456789'
cnt = idx = 0
res = []
s = open('08_24.txt').readline() + '*'  # + '*'   это костыль 🤔
for i in range(len(s) - 1):
    if s[i] not in d and s[i + 1] in d:
        a = s[i]
        idx = i
        cnt = 0
    elif s[i] in d:
        cnt += 1
    elif s[i] == a and cnt:
        res.append((cnt + 2, idx))
        a = s[i]
res.sort(key=lambda x: (-x[0], x[1]))
print(res[0][1])  # 310030


