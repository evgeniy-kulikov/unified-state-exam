"""
Демонстрационный вариант
контрольных измерительных материалов
единого государственного экзамена 2025 года
по ИНФОРМАТИКЕ
https://fipi.ru/ege/demoversii-specifikacii-kodifikatory#!/tab/151883967-5
"""

# 01
from itertools import permutations
print(*'1234567')
g = 'FC EGA CB DA FGB EGD FDC'
t = '457 46 567 12 136 235 13'
g = {frozenset(i) for i in g.split()}
for p in permutations('ABCDEFG'):
    tp = t
    for i in range(len(p)):
        tp = tp.replace(str(i + 1), p[i])
    tp = {frozenset(i) for i in tp.split()}
    if tp == g:
        print(*p)
# 1 2 3 4 5 6 7
# C B F A G D E
# DG + AC = 8 + 30 = 38


# 02
from itertools import product
print(*'zywx')
for p in product((0, 1), repeat=4):
    z, y, w, x = p
    f = ((w <= y) <= x) or not z
    if not f:
        print(*p)  # z y w x

# variant
print(*'zywx')
for i in range(2**4):
    p = f'{i:b}'.zfill(4)
    z, y, w, x = map(int, p)
    f = ((w <= y) <= x) or not z
    if not f:
        print(*p)
"""
z y w x
1 1 1 0
1 0 0 0
1 1 0 0
"""

#  05
mx = 0
for n in range(1, 13):
    b = f'{n:b}'
    if not n % 2:
        b = '10' + b
    else:
        b =  '1' + b + '01'
    mx = max(mx, int(b, 2))
print(mx)  # 109


#  07
from math import log2, ceil

I = 1024 * 768 * ceil(log2(4096))  # bit
P = 1_310_720 * 300  # bit
res = P // I
print(res)  # 41 снимок


# 8
alf = '0123456789ab'
def b12(n):
    s = ''
    while n:
        s += str(alf[n % 12])
        n //= 12
    return s[::-1]

cnt = 0
for i in range(int('10000', 12), int('bbbbb', 12) + 1):
    n12 = b12(i)
    ls = [i for i in n12 if alf.index(i) > 8]
    if n12.count('7') == 1 and len(ls) <= 3:
        cnt += 1
print(cnt)  # 67476


# 9
cnt = 0
with open('01_Demo/add/demo_2025_9.txt') as fl:
    for f in fl:
        f = list(map(int, f.split()))
        n1 = [i for i in f if f.count(i) == 1]
        n3 = [i for i in f if f.count(i) == 3]
        if len(n1) == len(n3):
            cnt += sum(n3) ** 2 > sum(n1) ** 2
print(cnt)  # 273


# 10
import re
reg1 = r'[Пп]о'
reg2 = r'\s[Пп]о\s'
with open('01_Demo/add/demo_2025_10.txt', encoding='utf-8') as fl:
    d = fl.read()
n1 = re.findall(reg1, d)
n2 = re.findall(reg2, d)
print(len(n1) - len(n2))  # 103


# 11
from math import log2, ceil
i = ceil(log2(10 + 52 + 963))  # 11  bit
I = (693 * 2**10) // 2000  # 354 byte
for n in range(1000):
    if ceil(n * i / 8) > I:
        print(n - 1)  # 257
        break


# 12
s = '1' * 81
while '11111' in s or '888' in s:
    if '11111' in s:
        s = s.replace('11111', '88', 1)
    else:
        s = s.replace('888', '8', 1)
print(s)  # 881


# 13
from ipaddress import *
cnt = 0
net = ip_network('172.16.168.0/255.255.248.0', 0)
for n in net:
    b = ''.join(f'{int(i):b}' for i in str(n).split('.'))
    cnt += b.count('1') % 5 != 0
print(cnt)  # 1663


# 14
alf = '0123456789abcdefghi'[::-1]
for x in alf:
    n = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if not n  % 18:
        print(n // 18)  # 469034148
        break

# другой вариант задания 14
from string import ascii_lowercase as lw
def f25(n):
    alf = '0123456789' + lw[:15]
    s = ''
    while n:
        s += alf[n % 25]
        n //= 25
    return s[::-1]
n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
n25 = f25(n)
print(n25.count('0'))  # 10


# другой вариант задания 14
def f7(n):
    s = ''
    while n:
        s = str(n % 7) + s
        n //= 7
    return s

for x in range(2030, 0, -1):
    n = 7**170 + 7**100 - x
    n7 = f7(n)
    if n7.count('0') == 71:
        print(x)  # 2029
        break


# 15
p = [*range(15, 41)]
q = [*range(21, 64)]
a = []

for x in range(0, 100):
    # f = (x in p) <= ((x in q and not x in a) <= (not x in p))
    f = not x in p or not x in q or x in a
    if not f:
        a.append(x)
# print(a)  # [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print(max(a) - min(a))  # 19


# 16
"""
f(2024) --> 2023 * f(2023)
f(2023) --> 2022 * f(2022)
f(2024) + 2 * f(2023)  -->  2023 * f(2023) + 2 * 2022 * f(2022)  --> 
 --> 2023 * 2022 * f(2022) + 2 * 2022 * f(2022)  --> f(2022) * (2023 * 2022 + 2 * 2022)
"""
print(2023 * 2022 + 2 * 2022)  # 4094550


# 17
cnt = 0
mx_sm = 0
with open('01_Demo/add/demo_2025_17.txt') as fl:
    ls = list(map(int, fl.read().split()))
    n_min = min(ls)  # 8
    for i in range(len(ls) - 1):
        if any(i % 16 == n_min for i in ls[i:i+2]):
            mx_sm = max(mx_sm, sum(ls[i:i+2]))
            cnt += 1
print(cnt, mx_sm)  # 1214 176024


# 19 - 21
def fn(st, mv):
    if st <= 19: return not mv % 2
    if mv == 0: return 0
    game = [fn(st - 2, mv - 1), fn(st - 5, mv - 1), fn(st // 3, mv - 1)]
    if not (mv - 1) % 2: return any(game)
    return all(game)

print(min([i for i in range(100, 21, -1) if fn(i, 2)]))  # 60
print(*[i for i in range(100, 21, -1) if not fn(i, 1) and fn(i, 3)][-2:][::-1])  # 62 63
print(min([i for i in range(100, 21, -1) if not fn(i, 2) and fn(i, 4)]))  # 64


# 23
def f(st, end):
    if st < end: return 0
    if st == end: return 1
    else:
        return f(st - 2, end) + f(st // 2, end)
print(f(38, 16) * f(16, 2))  # 36


# 24
from re import *
res = 0
n = r'(([6-9][06-9]*)|0)'
reg = rf'{n}([*-]{n})+'
# reg = r'(([6-9][06-9]*)|0)([*-]([6-9][06-9]*|0))+'
with open('01_Demo/add/demo_2025_24.txt') as fl:
    f = fl.read()
    for s in finditer(reg, f):
        res = max(res, len(s.group()))
print(res) # 154


# 25
def fn(n: int):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    # if len(d) >= 2:  # тоже верно (но пропустит ситуацию с одним делителем)
    if d: # учитывает ситуацию с одним единственным делителем (например для 822649)
        return min(d) + max(d)
    return 0

cnt = 5
for i in range(800_004, 10**6):
    d = fn(i)
    if d and d % 10 == 4:
        print(i, d)
        cnt -= 1
    if not cnt:
        break
# 800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554

# другой вариант задания 25
# Находим первое число подходящее маске 3?12?14*5, которое делится без остатка на 1917
# for i in range(30120145, 10**10):
#     if i % 1917 == 0 and str(i)[0] == '3' and str(i)[2:4] == '12' and str(i)[5:7] == '14' and str(i)[-1] == '5':
#         print(i) # 351261495
#         break

for i in range(351261495, 10**10 + 1, 1917):
    if str(i)[0] == '3' and str(i)[2:4] == '12' and str(i)[5:7] == '14' and str(i)[-1] == '5':
            print(i, i // 1917)
# 351261495 183235
# 3212614035 1675855
# 3412614645 1780185
# 3712414275 1936575
# 3912414885 2040905

# variant
from fnmatch import fnmatch
mask = '3?12?14*5'
for i in range(351261495, 10**10 + 1, 1917):
    if fnmatch(str(i), mask):
            print(i, i // 1917)
# 351261495 183235
# 3212614035 1675855
# 3412614645 1780185
# 3712414275 1936575
# 3912414885 2040905


# 26
from statistics import mean
with open('01_Demo/add/demo_2025_26.txt') as fl:
    n = int(next(fl))  # 9964
    d = list(tuple(map(int, f.split())) for f in fl)
good = [i for i in d if 2 not in i[1:]]
good.sort(key=lambda x: (-mean(x[1:]), x))
# two1 = sorted([i for i in d if i[1:].count(2) == 1])
# two2 = sorted([i for i in d if i[1:].count(2) == 2])
two3 = sorted([i for i in d if i[1:].count(2) == 3])
# two4 = sorted([i for i in d if i[1:].count(2) == 4])
user_good = good[n // 4 - 1][0]
user_bad = two3[0][0]
print(user_good)  # 52326
print(user_bad)  # 635



# 27
from math import dist
def centroid(cl: list):
    res = list()
    for i in cl:
        sm = 0
        for k in cl:
            sm += dist(i, k)
        res.append((sm, i))
    return min(res)[1]

with open('01_Demo/add/demo_2025_27_А.txt') as fl:
    d = []
    for f in fl:
        d.append(tuple(map(float, f.replace(',', '.').split())))
cl = [[] for _ in range(2)]
for i in d:
    if i[1] > 3:
        cl[0].append(i)
    else:
        cl[1].append(i)
z1, z2 = [centroid(i) for i in cl]
print(int((z1[0] + z2[0]) / 2 * 10_000), end=' ')
print(int((z1[1] + z2[1]) / 2 * 10_000))
# 10738 30730


with open('01_Demo/add/demo_2025_27_Б.txt') as fl:
    d = []
    for f in fl:
        d.append(tuple(map(float, f.replace(',', '.').split())))
cl = [[] for _ in range(3)]
for i in d:
    if i[0] < 5 and i[1] > 6:
        cl[0].append(i)
    elif i[0] > 5:
        cl[1].append(i)
    else:
        cl[2].append(i)
z1, z2, z3 = [centroid(i) for i in cl]
print(int((z1[0] + z2[0] + z3[0]) / 3 * 10_000), end=' ')
print(int((z1[1] + z2[1] + z3[1]) / 3 * 10_000))
# 37522 51277

