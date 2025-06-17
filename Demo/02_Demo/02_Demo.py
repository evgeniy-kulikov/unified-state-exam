"""
Демонстрационный вариант
контрольных измерительных материалов
единого государственного экзамена 2024 года
по ИНФОРМАТИКЕ
https://fipi.ru/ege/demoversii-specifikacii-kodifikatory#!/tab/151883967-5
https://doc.fipi.ru/ege/demoversii-specifikacii-kodifikatory/2024/inf_11_2024.zip
"""

# 01
from itertools import permutations
print(*'1234567')
g = 'dc ecb dcf ecg acf cg bdefga'
t = '234567 17 157 156 134 14 123'
g = {frozenset(i) for i in g.split()}
for p in permutations('abcdefg'):
    tp = t
    for i in p:
        tp = tp.replace(str(p.index(i) + 1), i)
    tp = {frozenset(i) for i in tp.split()}
    if tp == g:
        print(*p)
# 1 2 3 4 5 6 7
# c a f d e b g
# c b e g f a d
# 35


# 02
print(*'wzyx')
for i in range(2**4):
    w,z,y,x = map(int, f'{i:b}'.zfill(4))
    f = (x and not y) or (y == z) or not w
    if not f:
        print(w,z,y,x)
# wzyx
"""
w z y x
1 1 0 0
1 0 1 0
1 0 1 1
"""


# 05
nm = 100_000
for i in range(1, 100_000):
    b = f'{i:b}'
    if not i % 3:
        b += b[-3:]
    else:
        b += f'{(i % 3) * 3:b}'
    n = int(b, 2)
    if n > 151: nm = min(nm, n)
print(nm)  # 163


# 06.1
from turtle import *
tracer(0)
lt(90)
k = 50
screensize(2000, 2000)
for _ in range(7):
    fd(10 * k)
    rt(120)
pu()
for x in range(-1, k):
    for y in range(-1, k):
        goto(x * k, y * k)
        dot('red') if not x*y else dot()
done()
# 38

# 06.2
from turtle import *
tracer(0)
lt(90)
k = 30
screensize(2000, 2000)
for _ in range(2):
    fd(8*k)
    rt(90)
    fd(18*k)
    rt(90)
pu()
fd(4*k)
rt(90)
fd(10*k)
lt(90)
pd()
for _ in range(2):
    fd(17*k)
    rt(90)
    fd(7*k)
    rt(90)
pu()
for x in range(-1, k):
    for y in range(-1, k):
        goto(x * k, y * k)
        dot('red') if not x*y else dot()
done()
# 171 + 104 = 275


# 07
from math import ceil, log2
i = ceil(log2(4096))  # 12
I = 1024 * 768 * i / 8
res = I * 256 / 2**20
print(res)  # 288


# 08
def f(s: str):
    for i in range(4):
        if set(s[i:i+2]) <= set('1357') or set(s[i:i+2]) <= set('0246'):
            return False
    return True

a = int('20000', 8)
b = int('77777', 8)
cnt = 0
for i in range(a, b + 1):
    n = oct(i)[2:]
    cnt += all(['1' not in n, len(set(n)) == 5, f(n)])
print(cnt)  # 180


# 09
cnt = 0
with open('02_Demo/add/9_2024.txt') as fl:
    for f in fl:
        f = [*map(int, f.split())]
        two = [i for i in f if f.count(i) == 2]
        one = [i for i in f if f.count(i) == 1]
        if len(one) == 3 and len(two) == 4:
            if sum(two) / 4 < sum(f) / 7:
                cnt += 1
print(cnt)  # 83


# 10
from re import *
reg = r'\w*[Вв]се\w+|\w+[Вв]се\w*'
cnt = 0
with open('02_Demo/add/10_2024_.txt',  encoding='utf-8') as fl:
    s = list(finditer(reg, fl.read()))
    # for i in s:
    #     print(i.group())
    print(len(s))  # 299   Ответ 9 - явная ошибка!!!


# 11
from math import log2, ceil
I = 60 * ceil(log2(10 + 250)) / 8  # 67.5 byte
print(ceil(I) * 65_536 / 1024)  # 4352 KB


# 12
for n in range(4, 10_000):
    s = '5' + '2' * n
    while any(['52' in s, '2222' in s, '1122' in s]):
        if '52' in s: s = s.replace('52', '11', 1)
        if '2222' in s: s = s.replace('2222', '5', 1)
        if '1122' in s: s = s.replace('1122', '25', 1)
    if sum(map(int, s)) == 64: print(n)   # 156
    if len(s) > 100:
        break


# 13
from ipaddress import *
cnt = 0
net = ip_network('192.168.32.160/255.255.255.240', 0)
# for n in net.hosts():  # без 2-х адресов (сеть и броуд)
for n in net:
    b = ''.join(f'{int(i):b}' for i in str(n).split('.'))
    cnt +=  not b.count('1') % 2
print(cnt)  # 8


# 14.1
from string import ascii_lowercase
alf = '0123456789' + ascii_lowercase[:10]
for x in range(18, -1, -1):
    n = int(f'98897{alf[x]}21', 19) + int(f'2{alf[x]}923', 19)
    if not n % 18:
        print(n // 18)  # 469034148
        break

# 14.2
from string import ascii_lowercase
alf = '0123456789' + ascii_lowercase[:16]
def fn(n):
    s = ''
    while n:
        s = s + alf[n % 25]
        n //= 25
    return s

n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
n = fn(n)
print(n.count('0'))  # 9


# 15
def fn(a):
    for x in range(62):
        for y in range(1000):
            f = any([(x + 2*y) < a, y > x, x > 60])
            if not f: return 0
    return 1

nm = 10**10
for n in range(200):
    if fn(n): nm = min(nm, n)
print(nm)  # 181


# 16
"""
f2022 / f2024 = (2022 * f2023) / f2024 = (2022 * 2023 * f2024) / f2024 = 2022 * 2023
"""
# 4_090_506


# 17
cnt = 0
sm = 0
with open('02_Demo/add/17_2024.txt') as fl:
    ls = list(map(int, fl.readlines()))
n13 = max([i for i in ls if str(i)[-2:] == '13'])
for i in  range(len(ls) - 2):
    l = ls[i:i + 3]
    if len([i for i in l if len(str(i)) == 3]) == 2 and sum(l) <= n13:
        cnt+=1
        sm = max(sm, sum(l))
print(cnt, sm)  # 959 97471

# 18  02_Demo/add/18_2024.xls

# 19 - 21
def f(st, mv):
    if st >= 129: return not mv % 2
    if mv == 0: return 0
    gm = [f(st + 1, mv - 1), f(st * 2, mv - 1)]
    if not (mv - 1) % 2: return any(gm)
    return all(gm)
print(*[i for i in range(1, 129) if f(i, 2)])  # 64
print(*[i for i in range(1, 129) if f(i, 3) and not f(i, 1)])  # 32 63
print(*[i for i in range(1, 129) if f(i, 4) and not f(i, 2)])  # 62

# 22  02_Demo/add/22_2024.xls

# 23
def f(st, en):
    if st > en or st == 11: return 0
    if st == en: return 1
    return f(st + 1, en) + f(st * 2, en) + f(st**2, en)
print(f(2, 20)) # 37


# 24
with open('02_Demo/add/24_2024.txt') as fl:
    s = fl.read()
t_idx = [i for i, k in enumerate(s) if k == 'T']
mx = max(t_idx[100], len(s) - t_idx[-101] - 1) # отдельно смотрим голову и хвост
for i in range(0, len(t_idx) - 101): # смотрим тело (без головы и хвоста)
    mx = max(mx,  t_idx[i + 101] - t_idx[i] - 1)
# for x in zip(t_idx, t_idx[101:]):  # как в варианте из сети
#     mx = max(mx, x[1] - x[0] - 1)
print(mx)  # 133

# Вариант из сети
with open('02_Demo/add/24_2024.txt') as fl:
    s = fl.read()
t_idx = [-1] + [i for i, k in enumerate(s) if k == 'T'] + [len(s)]
mx = []
for x in zip(t_idx, t_idx[101:]):
    mx.append(x[1] - x[0] - 1)
print(max(mx))  # 133


# 25
from fnmatch import *
for n in range(0, 10**10, 2024):
    n = str(n)
    if n[0] == '1' and n[2:6] == '2157' and n[-1] == '4':
        print(n, end='\n\n') # 142157664
        break

for i in range(142157664, 10**10 + 1, 2024):
    if fnmatch(str(i), '1?2157*4'):
        print(i, i//2024)


# 26
with open('02_Demo/add/26_2024.txt') as fl:
    ln = int(next(fl).strip())
    d = [tuple(map(int, i.split())) for i in fl]
    d.sort(key=lambda x: x[1])
res = [d[0]]
for i in range(1, ln):
    if d[i][0] >= res[-1][1]:
        res.append(d[i])
print(len(res))  # 32

# Наибольший перерыв
before = res[-2][1]
idx_before = d.index(res[-2]) # 925
relax = 0
for x in d[idx_before:]:
    start = x[0]
    if start >= before:
        relax = max(relax, start - before)
print(relax)  # 15
# [(596, 600), (600, 619), (635, 647), (660, 676), (681, 685), (704, 709), (716, 730), (751, 755), (763, 772),
# (799, 817), (825, 840), (840, 842), (848, 850), (862, 892), (897, 903), (903, 936), (947, 959), (965, 989),
# (1002, 1011), (1019, 1027), (1030, 1033), (1035, 1057), (1060, 1089), (1094, 1114), (1122, 1128), (1134, 1146),
# (1172, 1183), (1199, 1221), (1226, 1245), (1246, 1259), (1264, 1273), (1288, 1298)]
