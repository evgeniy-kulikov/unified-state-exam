""" https://kompege.ru/task """
"""
887 934 1147 1866 6029 8510
10105 16333 17535 17878 19149
24895 24977 25361 26077 26491 26551 26549 27069 27634 27777
"""

"""
https://stepik.org/course/233165
21 
1040 1302 1428 1975
2251 2420 2422 2423 2425 2426 2427 2428
4113 4546 4602 4627 4643
5171 6734 8510 9169 9552 9753
10105 10724 11954 12476 13715 17535 17563 17641 17878 18597 19967 19969
20813 21421 21717 23206 23281 23381 23568 23762
"""


"""
Не решенные задачи ⛔
24613
"""




# 887 Джобс 25.12.2020 (Уровень: Средний)
from string import ascii_uppercase as alf
s = open('add/24/24_887.txt').read()
d = {i: 0 for i in alf}
for i in range(1, len(s)):
    if s[i-1] == 'X':
        d[s[i]] += 1
res = max((v, k) for k, v in d.items())
print(res[1], res[0], sep='')  # U1618


# 934 Джобс 08.02.2021 (Уровень: Средний)  # 👍 сложная задача
s = open('add/24/24_934.txt').read()
w = s[0]
res = 0
for i in range(1, len(s)):
    if s[i] >= w[-1]:
        w += s[i]
    else:
        w = s[i]
    if len(set(w)) == 3:
        res = max(res, len(w))
    if len(set(w)) == 4:
        idx = w.count(w[0])
        w = w[idx:]
        res = max(res, len(w))
print(res)


# 1147 (Уровень: Средний)
from string import ascii_uppercase as alf
s = open('add/24/24_1147.txt').read()
d = {i: 0 for i in alf}
for i in range(len(s) - 2):
    if s[i+1] == s[i+2]:
        d[s[i]] += 1
res = [(v, k) for k, v in d.items()]
res.sort(key=lambda x: (-x[0], x[1]))
print(res[0][1], res[0][0], sep='')  # X1560


# 1866 Основная волна 2021 (Уровень: Базовый)
s = open('add/24/24_1866.txt').read()
s = s.replace('ad', 'a d').replace('da', 'd a').split()
print(len(max(s, key=len)))  # 2252
# s.sort(key=len)
# print(len(s[-1]))  # 2252

# variant
s = open('add/24/24_1866.txt').read()
c, res = 0, 1
for i in range(len(s) - 1):
    if s[i: i+2] in 'ada':
        c = 1
    else:
        c += 1
    res = max(res, c)
print(res)


# 6029 ФИПИ 03.02.23 (Уровень: Базовый)
s = open('add/24/24_6029.txt').read()
s = s.replace('D', ' ')
s = s.replace('EE', 'E E').replace('EE', 'E E')  # EEEEEE >> E EE EE E >> E E E E E E
s = s.replace('FF', 'F F').replace('FF', 'F F')  # FFFFFF >> F FF FF F >> F F F F F F
s = s.split()
print(len(max(s, key=len)))

# variant
from re import *
s = open('add/24/24_6029.txt').read()
a = '(?:EF)+E?'
b = '(?:FE)+F?'
res = 0
for i in (a, b):  # исключаем наложение подстрок
    reg = rf'{i}'
    ls = findall(reg, s)
    res = max(res, len(max(ls, key=len)))
print(res)  # 11


# 8510 Апробация 17.05 (Уровень: Средний)
s = open('add/24/24_8510.txt').read()
s = s.replace('N', 'O').replace('P', 'O')
s = s.replace('OO', 'O O').replace('OO', 'O O')
s = s.split()
print(len(max(s, key=len)))  # 57

# variant
s = open('add/24/24_8510.txt').read()
from itertools import product
for p in product('NOP', repeat=2):
    s = s.replace(''.join(p), f'{p[0]} {p[1]}').replace(''.join(p), f'{p[0]} {p[1]}')
s = s.split()
print(len(max(s, key=len)))  # 57

# variant
s = open('add/24/24_8510.txt').read()
c, res = 1, 0
for i in range(1, len(s)):
    if s[i-1] in 'NOP' and s[i] in 'NOP':
        c = 1
    else:
        c += 1
        res = max(res, c)
print(res)  # 57





# 10105 Демоверсия 2024 (Уровень: Средний)
st = open('24_10105.txt').readline()
res = c = l = 0
for r in range(len(st)):
    if st[r] == 'T':
        c += 1
    while c > 100:
        if st[l] == 'T':
            c -= 1
        l += 1
    if c == 100:
        res = max(res, r - l + 1)
print(res)  # 133


# 16333 Открытый вариант 2024 (Уровень: Базовый)
from re import *
s = open('add/24/24_16333.txt').read()
reg = r'\d?(?:\D\d)+\D?'
# reg = r'\D?(?:\d\D)+\d?'  # проверка пересечений подстрок
res = findall(reg, s)
print(len(max(res, key=len)))  # 17

# variant
s = open('add/24/24_16333.txt').read()
s = s.replace('Q', 'W').replace('R', 'W')
s = s.replace('2', '1').replace('4', '1')
c = res = 1
for a, b in zip(s, s[1:]):
    if a != b:
        c += 1
        res = max(res, c)
    else:
        c = 1
print(res)  # 17


# 17535 Основная волна 07.06.24 (Уровень: Средний)
with open('24_17535.txt') as f:
    s = f.read().replace('CD', 'C D').split()
    n = 160 + 1  # ✅ поленьев на 1 больше, чем распилов бревна
    res = 0
    for i in range(len(s) - n - 1):
        r = s[i:i + n]
        res = max(res, len(''.join(r)))
print(res)  # 9712


# 17878 Демоверсия 2025 (Уровень: Сложный)
from re import *
s = open('24.txt').read()
n = r'(?:0|[6-9][06-9]*)'
reg = rf'{n}(?:[*-]{n})+'
res = findall(reg, s)
res = max(res, key=len)
print(len(res))  # 154


# 19149 (Уровень: Гроб)
from re import *
s = open('add/24/24_19149.txt').read()
num = r'\d+(?:\+\d+)+'
reg = rf'(?:\({num}\))'
res = findall(reg, s)
res = [i for i in res if not eval(i) % 2]
print(len(max(res, key=len)))  # 78





# 24895 (Уровень: Средний)
from re import *
cnt = 0
s = open('add/24/24_24895.txt').read()
s = s.replace('+', '*')
reg = r'\d+(?:\*\d+)+'
ls = findall(reg, s)
for st in ls:
    n = st.count('*')
    if n > 39:
        st = st.split('*')
        for i in range(len(st) - 39):
            cnt = max(cnt, len(''.join(st[i: i+40])) + 39)
    else:
        cnt = max(len(st), cnt)  # 343
print(cnt)  # 368


# 24977 (Уровень: Средний)
s = open('add/24/24_24977.txt').read()
l = c = res = 0
for r in range(6, len(s)):
    if s[r-6]+s[r-4]+s[r-2]+s[r] == '2026':
        c += 1
    while c > 10:
        if s[l]+s[l+2]+s[l+4]+s[l+6]=='2026':
            c -= 1
        l += 1
    res = max(res, r - l + 1)
print(res)  # 942


# 25361 ЕГКР 13.12.25 (Уровень: Базовый)
s = open('add/24/24_25361.txt').read()
for w in '02468':
    s = s.replace(w, ' ')
ls = s.split()[1:]  # в первои элементе не было четной цифры
ls = [i for i in ls if i.count('F') >= 76]  # убираем лишнее
res = 0
for st in ls:
    c = 0
    for i in range(len(st)):
        c += st[i] == 'F'
        if c == 76:
            res = max(res, i + 2)  # +2  индекс с нуля + четная цифра
print(res)  # 163


# 26077 (Уровень: Базовый)
s = open('add/24/24_26077.txt').read()
for w in '3579':
    s = s.replace(w, '1')
ls = s.replace('G', ' ').split()[1:]  # в первом элементе не было символа 'G'
ls = [i for i in ls if i.count('1') >= 45]  # убираем лишнее
res = 0
for st in ls:
    c = 0
    for i in range(len(st)):
        c += st[i] == '1'
        if c == 45:
            res = max(res, i + 2)  # +2  индекс с нуля + символ 'G'
print(res)  # 76


# 26491 (Уровень: Сложный)
from re import *
s = open('add/24/24_26491.txt').readline()
n = r'(?:[1-9]\d*)'
reg = rf'{n}(?:[*+]{n})+'
res = findall(reg, s)
res.sort(key=len, reverse=True)
for i in res:
    if eval(i) % 2:
        print(len(i))  # 247  (230  - not eval(i) % 2)
        break


# 26551 (Уровень: Базовый)
from re import *
s = open('add/24/24_26551.txt').read()
reg = r'[1-9A-D][0-9A-D]*[0248AC]'  # четное
res = findall(reg, s)
print(len(max(res, key=len)))  # 2598


# 26549 (Уровень: Базовый)
"""сложность 4 из 5"""
s = open('add/24/24_26549.txt').read()
l = 0
c = 0
res = 0
for r in range(len(s)):
    if s[r-3:r+1] == '2025':
        c += 1
    while c > 50:
        if s[l:l+4] == '2025':
            c -= 1
        l += 1
    if s[r-3:r+1] != '2025':
        continue
    else:
        if s[l:r+1].count('2025') == 50:
            if s[l:r + 1].count('Y') >= 140:
                res = max(res, r - l + 1)
print(res)  # 938


# 27069 (Уровень: Средний)
from re import *
s = open('add/24/24_27069.txt').read()
w1 = r'(?:[A-Z][a-z]*)'
w2 = r'(?:\s[A-Za-z][a-z]*)*'
reg = rf'{w1}{w2}\.'
res = findall(reg, s)
ans = max(res, key=len)
print(ans)  # You are a genius.
print(len(ans.split()))  # 4


# 27634 Апробация 04.03.26 (Уровень: Базовый) ✔️
"""поиск минимальной длины строки"""
res = 10**10
l = c = 0
s = open('add/KIM_25163454/24_27634.txt').readline().strip()
for r in range(len(s)):
    if s[r] == 'Z':
        c += 1
    while c > 269:  # 270 - 1
        if s[l] == 'Z':  # в начале и конце строки стоит 'Z' и их ровно 270
            res = min(res, r - l + 1)
            c -= 1
        l += 1
print(res)  # 1058


# 27777 Апробация 04.03.26 (Уровень: Базовый)
"""Простая регулярка"""
f = open('add/KIM_25164989/24_27777.txt').read()
from re import *
reg = r'[1-9AB]+'
res = findall(reg, f)
res.sort(key=len)
print(len(res[-1]))  # 18





# ⌛ ⌛ ⌛ Не решенные задачи ⌛ ⌛ ⌛

# 24613 (Уровень: Средний) ⛔  Очень сложная задача
cnt = l = 0
w = ('TRICK', 'TREAT', 'HALLOWEEN')
s = open('add/24/24_24613.txt').read()
for r in range(len(s)):
    st = s[l: r + 1]
    while any(st.count(i) > 5 for i in w):
        l += 1
    if all(st.count(i) == 5 for i in w):
        cnt += 1
print(cnt)  # ❌ 144470   [2657017]


