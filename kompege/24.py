""" https://kompege.ru/task """
"""
21 887 934 1147 1866 1874 1975 2250 2424 2425 2428 2577 3018 3375 3792 4710
5810 5955 6029 6275 7356 7624 8510 9753 9791 9845
10105 11954 12254 14647 15339 16333 16388 17535 17563 17641 17878 19149 19254 19717
21421 23762 24895 24977 25361 26077 26078 26491 26551 26549 27069 27634 27777 28765 31368
"""


"""
https://stepik.org/course/233165
1040 1302 1428
2251 2420 2422 2423 2425 2426 2427
4113 4546 4602 4627 4643
5171 6734 9169 9552
10105 10724 11954 12476 13715 18597 19967 19969
20813 21717 23206 23281 23381 23568
"""


"""
Не решенные задачи ⛔
24613
"""



# 21 Демоверсия 2021 (Уровень: Базовый)
f = open('24_21.txt').readline()
res, c = 0, 1
for i in range(1, len(f)):
    if f[i-1] != f[i]:
        c += 1
        res = max(res, c)
    else:
        c = 1
print(res)

# variant 1
f = open('24_21.txt').readline()
res, c = 0, 1
for a, b in zip(f, f[1:]):
    if a != b:
        c += 1
        res = max(res, c)
    else:
        c = 1
print(res)

# variant 2
f = open('24_21.txt').readline()
ls = [1] * len(f)
for i in range(1, len(f)):
    if f[i-1] != f[i]:
        ls[i] = ls[i-1] + 1
print(max(ls))


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


# 1874 (Уровень: Базовый)
s = open('add/24/24_1874.txt').read().replace('QW', 'Q W').split()
print(len(max(s, key=len)))  # 5267


# 1975 Демоверсия 2022 (Уровень: Базовый)
s = open('add/24/24_1975.txt').read()
c = cnt = 1
for a, b in zip(s, s[1:]):
    if a+b == 'PP':
        c = 1
    else:
        c += 1
        cnt = max(c, cnt)
print(cnt)  # 188

# variant
while 'PP' in s:
    s = s.replace('PP', 'P P')
s = s.split()
print(len(max(s, key=len, default=['*'])))  # 188


# 2250 (Уровень: Базовый)
s = open('add/24/24_2250.txt').read()
res = 0
s = s.split('A')
for a,b in zip(s, s[1:]):
    res = max(len(a+b) + 1, res)
print(res)  # 337


# 2424 (Уровень: Базовый)
from re import *
res = 0
for s in open('24_2424.txt').readlines():
    ls = findall(r'(?:XYZ)+', s)
    res = max(res, len(max(ls, key=len, default='')))
print(res)


# № 2425 (Уровень: Базовый)
s = open('24_2425.txt').read()
c = cnt = 3
ok = False
for i in range(len(s) - 3):
    if s[i:i+4] == 'DBAC':
        ok = True  # ✅ отсечка неполных начал
    if ok and s[i:i+4] in 'DBACDBA':  # без ok будут попадать начала, 'DBAC' и хвосты
        c += 1
        cnt = max(c, cnt)
    else:
        c = 3
        ok = False
print(cnt)  # 95

# variant
s = s.replace('DBAC', '****').replace('*DBA', '****').replace('*DB', '***').replace('*D', '**')  # + неполные хвосты
for i in 'ABCDEF':
    s = s.replace(i, ' ')  # отсечка лишнего и ✅неполных начал
res = max(len(i) for i in s.split())
print(res)  # 95


# 2428 (Уровень: Средний)
from re import *
res = 0
reg = r'(?:Z|YZ)(?:XYZ)+(?:X|XY)'
for s in open('24_2428.txt').readlines():
    ls = findall(reg, s)
    res = max(res, len(max(ls, key=len, default='')))
print(res)

# ✅ Неполная цепочка как в начале, так и в конце ✅
res = 0
cnt = 2
s = open('24_2428.txt').readline()
for i in range(len(s) - 2):
    if s[i:i + 3] in 'XYZXY':
        cnt += 1
        res = max(res, cnt)
    else:
        cnt = 2
print(res)  # 69


# 2577 (Уровень: Базовый)  # ❗Ловушка❗: необходимо совмещение 2-х методов 👍
s = open('24_2577.txt').read().split('Y')
res = 0
for el in s:
    c = l = 0
    for r in range(len(el)):
        c += el[r]=='.'
        while c > 5:
            c -= el[l] == '.'
            l += 1
        res = max(res, r-l+1)
print(res)


# 3018 (Уровень: Средний)
s = open('24_3018.txt').read()
s = s.split('A')[1:-1]
print(sum(len(i) >= 15 and not i.count('B') for i in s))  # 597


# 3375 Джобс 22.04.2022 (Уровень: Базовый) ✅ зеркальность внутри пары ❗❗
f = open('24_3375.txt').read()
f = f.replace('B', ' ').split()
res = 0
for s in f:
    # AAAAACC  k=0 AAAA, CC,   k = 1 AAAACC  (разный вариант чтения строки)
    for k in (0, 1):
        c = 0
        for i in range(k, len(s), 2):
            if s[i:i+2] in ('AA', 'CC'):
                c += 1
                res = max(res, c)
            else:
                c = 0
print(res)  # 5


# 5139 /dev/inf 11.22 (Уровень: Средний)
from re import *
s = open('24_5139.txt').read()
for i in 'EU':
    s = s.replace(i, 'A')
for i in 'CDF':
    s = s.replace(i, 'B')
res = findall(r'(?:BAB)+', s)
res = max(res, key=len)
print(len(res) // 3)  # 6

# variant
s = open('24.txt').read()
for i in 'EU':
    s = s.replace(i, 'A')
for i in 'CDF':
    s = s.replace(i, 'B')
s = s.replace('BAB', '*').replace('A', ' ').replace('B', ' ').split()
print(len(max(s, key=len)))


# 3792 (Уровень: Базовый)
from re import *
s = open('24_3792.txt').read()
res = findall(r'[ABC]+', s)
print(len(max(res, key=len)))  # 16

# variant
s = open('24_3792.txt').read()
for i in 'DE':
    s = s.replace(i, ' ')
print(max(len(i) for i in s.split()))  # 16


# 4710 Демоверсия 2023 (Уровень: Базовый)
f = open('24_1.txt').readline()
f = f.replace('D', 'C').replace('F', 'C')
f = f.replace('O', 'A').replace('CA', '*')
f = f.replace('A', ' ').replace('C', ' ').split()
print(len(max(f, key=len)))  # 95


# 5810 (Уровень: Сложный)
from re import *
res = 0
reg1 = r'(?:XY)+'
reg2 = r'(?:YZ)+'
reg3 = r'(?:YZ)*|(?:XYZ)*|(?:XY)*'
for s in open('24_5810.txt').readlines():
    for i in (reg1, reg2, reg3):
        ls = findall(i, s)
        res = max(res, len(max(ls, key=len, default='')))
print(res)  # 44


# 5955 (Уровень: Средний)
s = open('24_5955.txt').read()
s = s.replace('O', 'A').replace('C', 'F').replace('D', 'F')
s = s.replace('FAAF', 'FAA AAF').split()
print(len(max(s, key=len)))  # 599


# 6029 ФИПИ 03.02.23 (Уровень: Базовый)
s = open('add/24/24_6029.txt').read()
s = s.replace('D', ' ')
s = s.replace('EE', 'E E').replace('EE', 'E E')  # EEEEEE >> E EE EE E >> E E E E E E
s = s.replace('FF', 'F F').replace('FF', 'F F')  # FFFFFF >> F FF FF F >> F F F F F F
s = s.split()
print(len(max(s, key=len)))  # 11

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


# 6275 Danov2302 (Уровень: Сложный)
def f(st):
    alf = '0123456789ABCDEF'
    return all(i in st for i in alf)

s = open('24_6275.txt').read()
l = 0
res = 10**10
for r in range(15, len(s)):
    while f(s[l:r + 1]):
        res = min(res, r-l+1)
        l += 1
print(res)  # 42


# 7356 (Уровень: Средний)
s = open('24_7356.txt').readline().replace('O', 'A').replace('C', 'F').replace('D', 'F').replace('FA', '**')
l = res = 0
for r in range(len(s)):
    while s[l:r+1].count('**') > 5:
        l += 1
    res = max(res, r-l+1)
print(res) # 27

# variant
s = open('24_7356.txt').readline().replace('O', 'A').replace('C', 'F').replace('D', 'F').replace('FA', 'F A').split()
N = 5
res = 0
for i in range(len(s) - N):
    w = ''.join(s[i:i+N + 1])
    res = max(res, len(w))
print(res)  # 27


# 7624 Досрочная волна 2023 (Уровень: Базовый)
f = open('24_7624.txt').readline()
f = f.replace('Y', 'X').replace('Z', 'X')
f = f.replace('XX', 'X X')
print(len(max(f.split(' '), key=len)))  # 786


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


# 9753 Основная волна 19.06.23 (Уровень: Сложный)
s = open('24_9753.txt').read().strip()
res = c = l = 0
for r in range(len(s)):
    c += s[r] == 'Y'
    while c > 150:
        c -= s[l] == 'Y'
        l += 1
    res = max(res, r-l+1)
print(res)  # 244

# variant
s = open('24_9753.txt').readline().strip().split('Y')
res, Y = 0, 150
for i in range(len(s) - Y):
    res = max(res, len('Y'.join(s[i:i+Y+1])))
print(res)  # 244


# 9791 Основная волна 20.06.23 (Уровень: Средний)
# Ничего не сказано, про отсутствие незначащих нулей
from re import *
s = open('24_9791.txt').read()
reg = r'[0-9A-F]+'
res = findall(reg, s)
print(len(max(res, key=len)))  # 21

# variant
from string import ascii_uppercase as alf
f = open('24_9791.txt').readline()
for i in alf[6:]:
    f = f.replace(i, ' ')
print(len(max(f.split(), key=len)))  # 21


# 9845 Основная волна 27.06.23 (Уровень: Базовый)
s = open('24_9845.txt').read()
s = s.replace('B', 'A').replace('C', 'A').replace('9', '8')
while 'AA' in s or '88' in s:
    s = s.replace('AA', 'A A')
    s = s.replace('88', '8 8')
print(len(max(s.split(),key=len)))  # 18

from re import *
s = open('24_9845.txt').read()
reg = r'(?:\d\D)+|(?:\D\d)+'
res = findall(reg, s)
print(max(len(i) for i in res))  # 18





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
        res = max(res, r - l + 1)  # считаем пока указатель 'r' не окажется перед 101-й 'T'
print(res)  # 133


# 11954 (Уровень: Средний)
st = open('24.txt').read().split('Y')
st = [i for i in st if i.count('X') >= 500]
res = 10**10
for s in st:
    l = c = 0
    for r in range(len(s)):
        c += s[r]=='X'
        while c > 500:
            c -= s[l]=='X'
            l += 1
        if c==500:
            res = min(res, r-l+1)
print(res) # 68500

# variant
s = open('24.txt').readline()
res = 10**10
l = c = 0
for r in range(len(s)):
    if s[r]=='Y':
        l = r+1
        c = 0
    c += s[r] == 'X'
    while c > 500:
        c -= s[l] == 'X'
        l += 1
    if c == 500:
        res = min(res, r - l + 1)
print(res)



# 12254 ЕГКР 16.12.23 (Уровень: Базовый)
s = open('24_12254.txt').readline().replace('RSQ', '*')
c = res = 2
for i in range(2, len(s)):
    w = s[i-2:i+1]
    if w in 'RSQRS':
        c += 1
        res = max(res, c)
    else:
        c = 2
print(res)  # 54


# 14647 Открытый курс "Слово пацана" (Уровень: Базовый)
s = open('24.14_14647.txt').read()
l = res = 0
x = y = 0
for r in range(len(s)):
    x += s[r] == 'X'
    y += s[r] == 'Y'
    while x > 1 or y > 1:
        x -= s[l] == 'X'
        y -= s[l] == 'Y'
        l += 1
    if x==y==1:
        res = max(res, r-l+1)
print(res)  # 225


# 15339 Досрочная волна 2024 (Уровень: Средний)
f = open('24_15339.txt').readline()
f = f.replace('B', 'A').replace('C', 'A')
f = f.replace('7', '6').replace('8', '6').replace('9', '6')
while 'AA' in f or '66' in f:
    f = f.replace('AA', 'A A')
    f = f.replace('66', '6 6')
print(len(max(f.split(), key=len))) # 22


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


# 16388 ЕГКР 27.04.24 (Уровень: Базовый)
s = open('24_16388.txt').read()
c = cnt = 3
for i in range(len(s) - 3):
    if s[i:i+4] in 'KLMNKLM':  # ✅ учитываем неполные НАЧАЛА и ХВОСТЫ
        c += 1
        cnt = max(c, cnt)
    else:
        c = 3
print(cnt)  # 182


# 17535 Основная волна 07.06.24 (Уровень: Средний)
with open('24_17535.txt') as f:
    s = f.read().replace('CD', 'C D').split()
    n = 160  # ✅ поленьев на 1 больше, чем распилов бревна
    res = 0
    for i in range(len(s) - n ):
        r = s[i:i + n + 1]
        res = max(res, len(''.join(r)))
print(res)  # 9712

# variant
s = open('24_17535.txt').read().strip()
l = c = res = 0
for r in range(1, len(s)):
    c += s[r-1:r+1] == 'CD'
    while c > 160:
        c -= s[l:l + 2] == 'CD'
        l += 1
    if c == 160:
        res = max(res, r-l+1)
print(res)  # 9712


# 17563 Основная волна 08.06.24 (Уровень: Сложный) 🌶️
from re import *
n = r'[7-9]+\d*'
reg = rf'{n}(?:[*-]{n})+'
# reg = r'[1-9]+\d*(?:[*-][1-9]+\d*)+'
s = open('add/course_233165/24-4__04.txt').readline().strip()
res = findall(reg, s)
print(max(map(len, res)))  # 40

# variant
from re import *
n = r'7+\d*'
reg = rf'{n}(?:-{n})+'
# reg = r'7+\d*(?:-7+\d*)+'
s = open('add/course_233165/24-4__04.txt').readline().strip()
s = s.replace('8', '7').replace('9', '7').replace('*', '-')
res = findall(reg, s)
print(max(map(len, res)))  # 40



# 17641 Основная волна 19.06.24 (Уровень: Гроб) 🌶️ 🌶️ 🌶️
from re import *
s = open('24.txt').read()
# 1) находим правильные арифметические строки
n = f'(?:0|[1-9]\d*)'
reg = rf'{n}(?:[*+]{n})+'
res = findall(reg, s)
MX = 0
# 2) в найденых строках находим строки дающие ноль
for i in res:
    ls = i.split('+')
    cnt = 0
    for i in ls:
        # if not eval(i):  # дольше
        if any([i[-2:]=='*0', i[:2]=='0*', '*0*' in i, i=='0']):  # быстрее
            cnt += len(i) + 1  # + 1 это за '+'
            MX = max(MX, cnt - 1)  # - 1 это за лишний '+'
        else:
            cnt = 0
print(MX)  # 142

# variant
from re import *
file = open('24.txt').read().strip()
n = r'(?:0|[1-9]\d*)'  # числа без нулей слева
num = rf'(?:{n}(?:[+*]{n})*)'  # правильные арифметические строки 4*0*102+102+5*0
res = 0
ls = findall(num, file)
for s in ls:
    r = ''
    for i in s.split('+'):
        if any([i[:2]=='0*', '*0*' in i, i[-2:]=='*0', i=='0']):
            r += i + '+'
        else:
            r += ' '  # убираем между плюсами выражения не равные нулю
    res = max(res, len(max([i.strip('+') for i in r.split()], key=len, default='')))
print(res)

# variant
from re import *
s = open("24.txt").readline()
n = f'(?:0|[1-9]\d*)'
n_mul = f'(?:{n}\*)*'  # 1*
mul_n = f'(?:\*{n})*'  # *2
mult = rf'(?:{n_mul}0{mul_n})'  # 1*0*2
reg = rf'(?:{mult}(?:\+{mult})*)'  # 1*0*2+1*0*2
print(max(len(i) for i in findall(reg, s)))



# 17878 Демоверсия 2025 (Уровень: Сложный)
from re import *
s = open('24.txt').read().strip()
n = r'(?:0|[1-9]\d*)'
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


# 19254 ЕГКР 21.12.24 (Уровень: Базовый)
s = open('24.txt').read().strip()
l = c = res = 0
for r in range(3, len(s)):
    c += s[r-3:r+1] == 'FSRQ'
    while c > 80:
        c -= s[l:l+4] == 'FSRQ'
        l += 1
    if c == 80:
        res = max(res, r-l+1)
print(res)  # 2379

# Через split()
s = open('24.txt').read().strip()
# print(s[:4], s[-4:]) # проверка концов: должны отличаться от 'FSRQ'
res = 0
s = s.split('FSRQ')
n = 80
for i in range(len(s) - n):
    # 'k' это прибавка еще от двух 'FSRQ'  >>  'SRQ' + ... + 'FSR'
    k = 6 if 0 < i < len(s) - n-1 else 3  # учет изменения прибавки для первой и последней выборки
    r = sum(map(len, s[i:i + n+1])) + 4 * n + k
    res = max(res, r)
print(res)  # 2379


# 19717 (Уровень: Средний)
s = open('24.5_1971724.5_19717.txt').read()
l = c = res = 0
for r in range(len(s)):
    if s[r] == 'M':
        c += 1
    while c > 278:
        if s[l] == 'M':
            c -= 1
        l += 1
    if c <= 278:
        res = max(res, r - l + 1)
print(res)  # 2471




# 21421 Досрочная волна 2025 (Уровень: Базовый)
from re import findall
reg = r'(?:[1-9AB][0-9AB]*[02468A])'
s = open('24_21421.txt').readline()
f = findall(reg, s)
print(len(max(f, key=len)))  # 19



# 23762 Демоверсия 2026 (Уровень: Средний)
# (~ 3 sec)
s = open('24_23762.txt').readline().split('Y')
res = 0
n = 80  # кол-во Y
for i in range(len(s) - n):
    r = ''.join(s[i:i + (n+1)])
    if r.count('2025') >= 90:
        res = max(res, len(r) + n)
print(res)  # 2981

# variant 1 (~ 21 sec)
s = open('24_23762.txt').readline()
c = l = res = 0
for r in range(len(s)):
    c += s[r]=='Y'
    while c > 80:
        c -= s[l]=='Y'
        l += 1
    if c == 80 and s[l:r+1].count('2025') >= 90:
        res = max(res, r-l+1)
print(res)  # 2981

# variant 2 (~ 23 sec)
s = open('24_23762.txt').read()
m = 1
for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r]
        if c.count('Y') > 80:
            break
        if c.count('Y') == 80 and c.count('2025') >= 90:
            m = max(m, len(c))
print(m) # 2981




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


# 26078 (Уровень: Базовый) ❗❗❗ Супер сложная задача ❗❗❗
# Сперва ищем строки типа '***W**2025****W***W***2025**W**2025**' ('W' ровно 90)
# На финише ищем подстроки типа '2025****W***W***2025' которые начинаются и оканчиваются на '2025' ('2025' ровно 110),
# а внутри ровно 90 символов 'W'

st = open('24_26078.txt').read().split('W')
n = 90
n25 = 110
res = 10 ** 10
for i in range(len(st) - n):
    # подстроки типа 'W***W**2025***W**2025**W' ('W' ровно 90)
    sw_90 = 'W' + 'W'.join(st[i + 1: i + n + 1 - 1]) + 'W'
    if sw_90.count('2025') >= n25:
        res = min(res, len(sw_90))  # 782

    # подстроки типа '***2025****W***W***2025**W*' ('W' ровно 90  и '2025' >= 110)
    s_w = 'W'.join(st[i: i + n + 1])  # 'W' ровно 90
    if s_w.count('2025') >= n25:
        i1 = s_w.index('2025')
        i2 = s_w.rindex('2025')
        s_w = s_w[i1:i2 + 4]  # отсекаем лишние концы справа и слева  '2025****W***W***2025' ('2025' ровно 110)
        s_2025 = s_w.split('2025')
        for i in range(1, len(s_2025) - n25 - 1 - 1):
            s = '2025' + '2025'.join(s_2025[i:i + n25 - 1]) + '2025'  # '2025' ровно 110
            if s.count('W') == n:
                res = min(res, len(s))  # 780
print(res)  # 780



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
"""❗❗❗ сложность 4 из 5 """
# быстро
st = open('24.txt').read().replace('2025', '2 025').split()
res = 0
for i in range(len(st) - 49):
    s = ''.join(st[i:i+50])
    if s.count('Y') >= 140:
        res = max(res, len(s) + 3)  # +3 == +025 на хвосте
print(res)  # 938

s = open('add/24/24_26549.txt').read()
l = res = d25 = 0
for r in range(3, len(s)):
    if s[r-3:r+1] == '2025':
        d25 += 1
    while d25 > 50:
        d25 -= s[l: l+4] == '2025'
        l += 1
    if s[r-3:r+1] != '2025':
        continue  # ускоряем
    if d25 == 50 and s[l:r + 1].count('Y') >= 140:
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
"""поиск минимальной ❗❗❗ длины строки"""
res = 10**10
l = c = 0
s = open('add/KIM_25163454/24_27634.txt').readline().strip()
for r in range(len(s)):
    if s[r] == 'Z':
        c += 1
    while c >= 270:
        if s[l] == 'Z':  # в начале и конце строки стоит 'Z' и их ровно 270
            res = min(res, r - l + 1)
            c -= 1
        l += 1
print(res)  # 1058

# variant
s = open('add/KIM_25163454/24_27634.txt').read()
A = 270
res = 10**10
s = s.split('Z')[1:-1]
for i in range(len(s) - A + 2):
    w = ''.join(s[i:i + A - 1])
    res = min(res, len(w) + A)
print(res)  # 1058



# 27777 Апробация 04.03.26 (Уровень: Базовый)
"""Простая регулярка"""
f = open('add/KIM_25164989/24_27777.txt').read()
from re import *
reg = r'[1-9AB]+'
res = findall(reg, f)
res.sort(key=len)
print(len(res[-1]))  # 18


# 28765 Досрочная волна 2026 (Уровень: Базовый)
s = open('24_28765.txt').readline()
l = m = k = 0
for r in range(len(s)):
    if s[r-1:r+1] ==  'BC':
        k += 1
    while k > 180:
        if s[l:l+2] == 'BC':
            k -= 1
        l += 1
    m = max(m , r-l+1)
print(m)  # 38442

# variant (дольше)
f = open('24_28765.txt').readline()
s = ''
m = k = 0
for r in range(len(f)):
    s += f[r]
    k += s[-2:]=='BC'
    while k > 180:
        k -= s[:2]=='BC'
        s = s[1:]
    m = max(m, len(s))
print(m)  # 38442


# 31368 Пересдача 08.07.26 (Уровень: Гроб)
from re import findall
s = open("24_31368.txt").readline()
n = r'(?:0|[1-9]\d*)'  # 0 or 120
n_mul = rf'(?:{n}\*)*'  # 1*0*2*
mul_n = rf'(?:\*{n})*'  # *3*4*0
mult = rf'(?:{n_mul}0{mul_n})'  # 1*0*2 * 0 * 3*4*0
reg = rf'(?:{mult}(?:\+{mult})*)'  # 1*0*2*0*3*4*0 + 1*0*2*0*3*4*0
print(max(len(i) for i in findall(reg, s)))  # 197





# ⌛ ⌛ ⌛ Не решенные задачи ⌛ ⌛ ⌛
