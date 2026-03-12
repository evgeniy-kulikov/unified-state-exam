# https://kompege.ru/variant?kim=25163454
# КИМ № 25164989
# БР № 2832503195017
""""""

# 01
# 27756 Апробация 04.03.26 (Уровень: Базовый)
from itertools import *
print(*'12345678')
g = 'ah hb bf fg ge ea de dg cf ca ch'.split()
t = '247 148 467 123 68 358 13 256'.split()
for p in permutations('abcdefgh'):
    if all(str(p.index(a) + 1) in t[p.index(b)] for a,b in g):
        print(*p)
"""
1 2 3 4 5 6 7 8
h a f c d g b e
"""
# 65


# 02
# 27757 Апробация 04.03.26 (Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return (not x and y and z and not w) or \
        (not x and y and not z and not w) or \
        (x and y and z and not w)

for m1,m2,m3,m4,m5,m6,m7 in product((0,1), repeat=7):
    t = [(1,m1,m2,m3), (0,m4,1,m5), (m6,0,0,m7)]
    if len(t) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,1]:
                print(''.join(p))  # xwzy

# 03
# 1498

# 04
# 25

# 05
# 27760 Апробация 04.03.26 (Уровень: Базовый)
res = 10**10
for n in range(19, 100000):
    b = f'{n:b}'
    if not n % 2:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b, 2)
    res = min(res, r)
print(res)  # 84


# 06
# 27761 Апробация 04.03.26 (Уровень: Базовый)
from turtle import *
tracer(0)
lt(90)
screensize(2000,2000)
k = 30

for _ in range(2):
    fd(1 * k)
    lt(270)
    fd(16 * k)
    rt(90)
pu()
bk(4 * k)
rt(90)
fd(10 * k)
lt(90)
pd()
for _ in range(2):
    fd(17 * k)
    rt(90)
    fd(7 * k)
    rt(90)
pu()
for x in range(-5, k):
    for y in range(-k, k):
        goto(x*k, y*k)
        dot()
done()
print(1*16 + 7*17 - 6)  # 129


# 07
# 27762 Апробация 04.03.26 (Уровень: Базовый)
I = 2 * 24_000 * 8 * 180
sec = I / 48_000
print(sec)  # 1440


# 08
# 27763 Апробация 04.03.26 (Уровень: Базовый)
c = 0
from itertools import *
for p in product('0123456', repeat=5):
    p = ''.join(p)
    if p[0] != '0':
        if p.count('0') == 1 and p.count('1') <= 2:
            c += 1
print(c)  # 5100


# 09
# 27764 Апробация 04.03.26 (Уровень: Базовый)
f = open('add/KIM_25164989/9_27764.txt').readlines()
c = 0
for i in f:
    n = sorted(map(int, i.split()))
    if len(set(n)) == 5:
        if 2 * (n[0] + n[-1]) == sum(n[1:-1]):
            c += 1
print(c)  # 5019

# 10
# 27765 Апробация 04.03.26 (Уровень: Базовый)
# 66


# 11
# 27766 Апробация 04.03.26 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 26 + 34))  # 7
for n in range(1, 1000):
    if ceil(n * i / 8) * 1142 > 305 * 1024:
        print(n)  # 313
        break


# 12
# 27624 Апробация 04.03.26 (Уровень: Базовый)
s = f'{800:b}'
r = ''
q = 2
for i in range(len(s)):
    if q == 2:
        r += s[i]
        if s[i] == '1':
            q = 3
    elif q == 3:
        r += '0'
        if s[i] == '1':
            q = 4
    else:
        r += s[i]
print(int(r, 2))  # 544


# 13
# 27768 Апробация 04.03.26 (Уровень: Базовый)
from ipaddress import *
c = 0
net = ip_network('172.16.160.0/255.255.240.0', 0)
for i in net:
    c += not f'{i:b}'.count('1') % 2
print(c)  # 2048


# 14
# 27769 Апробация 04.03.26 (Уровень: Базовый)
from string import ascii_lowercase as lc
alf = '0123456789' + lc[:12]
for x in alf[::-1]:
    n = int(f'12313{x}57', 22) + int(f'1{x}34561', 22)
    if not n % 21:
        print(n // 21)  # 140914722
        break


# 15
# 27770 Апробация 04.03.26 (Уровень: Базовый)
def f(x):
    return x % 21 or not x % a or x % 77

for a in range(10_000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 231
        break


# 16
# 27771 Апробация 04.03.26 (Уровень: Базовый)
from functools import lru_cache
@lru_cache
def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

[f(i) for i in range(1, 2025)]
print((f(2024) - 2 * f(2023)) / f(2022))  # 4090506


# 17
# 27629 Апробация 04.03.26 (Уровень: Базовый)
c = 0
res = 0
f = open('add/KIM_25164989/17_27629.txt').readlines()
d = [*map(int, f)]
n_43 = max(i for i in d if len(str(abs(i))) == 4 and str(i)[-2:] == '43')
for i in range(len(d) - 1):
    num = d[i:i+2]
    if any(len(str(abs(k))) == 4 for k in num):
        if sum(num) ** 2 < n_43 ** 2:
            c += 1
            res = max(res, sum(num) ** 2)
print(c, res)  # 1218 98843364


# 18
# 27773 Апробация 04.03.26 (Уровень: Базовый)
# 2676 195


# 19-21
# 27774 Апробация 04.03.26 (Уровень: Базовый)
def f(a, b, m):
    if a + b >= 207:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)
    # return any(g)

# print([s for s in range(2, 190) if f(17, s, 2)][0])  # 48
print(*[s for s in range(2, 190) if f(17, s, 3) and not f(17, s, 1)])  # 86 94
print([s for s in range(2, 190) if f(17, s, 4) and not f(17, s, 2)][0])  # 85
"""
48
86 94
85
"""


# 22
# 27775 Апробация 04.03.26 (Уровень: Базовый)
# 8


# 23
# 27776 Апробация 04.03.26 (Уровень: Базовый)
def f(st, en):
    if st == en:
        return 1
    if st < en:
        return 0
    return f(st-1, en) + f(st//2, en)
print(f(40, 16) * f(16, 6))  # 60


# 24
# 27777 Апробация 04.03.26 (Уровень: Базовый)
f = open('add/KIM_25164989/24_27777.txt').read()
from re import *
reg = r'[1-9AB]+'
res = findall(reg, f)
res.sort(key=len)
print(len(res[-1]))  # 18


# 25
# 27778 Апробация 04.03.26 (Уровень: Базовый)
from fnmatch import *
for n in range(271, 10**8 + 1, 271):
    if fnmatch(str(n), '12??15*6'):
        print(n, n//271)
"""
1202156 4436
12001506 44286
12131586 44766
12421556 45836
12711526 46906
"""


# 26
# 27779 Апробация 04.03.26 (Уровень: Базовый)
f = open('add/KIM_25164989/26_27779.txt').readlines()
# f = open('add/KIM_25164989/test.txt').readlines()
N = int(f[0])
d = sorted(map(int, f[1:]), reverse=True)
c = 1
cur = d[0]
for i in range(N-1):
    if cur - d[i] >= 8:
        c += 1
        cur = d[i]
print(c, cur)  # 1159 57


# 27
# 27780 Апробация 04.03.26 (Уровень: Базовый)
from math import dist
def get_center(ls: list):
    r = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        r.append((sm, i))
    return min(r)[1]

def get_clust(p):
    clust = [i for i in data if dist(i, p) < 2]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for w in 'AB':
    f = open(f'add/KIM_25164989/27{w}_27780.txt').readlines()
    data = [[*map(float, i.replace(',', '.').split())] for i in f]
    # print(len(data))
    clust = []
    while data:
        p = data.pop()
        clust.append([p] + get_clust(p))
    # [print(len(i)) for i in clust]
    # print(sum(len(i) for i in clust))
    # print()
    clust.sort(key=len)
    center = [get_center(i) for i in clust]
    if w == 'A':
        a1 = len(clust[-1])
        a2 = int(sum(dist(i, (1.0, 1.5)) for i in center) * 10_000)
        print(a1, a2)  # 344 294354
    else:
        b1 = sum(1 for i in clust[1] if dist(i, center[1]) <= 1.2 and i != center[1])
        b2 = int(min(dist(i, center[-1]) for i in clust[-1] if i != center[-1]) * 10_000)
        print(b1, b2)
"""
344 294354
152 528
"""

