# https://kompege.ru/variant?kim=25163454
# КИМ № 25163454
# БР № 2832503195017

# 01
# 45

# 02
def f(x,y,w,z):
    return (not z and y and x and not w) or (not z and y and not x and not w) or (z and y and x and not w)

for m1,m2,m3,m4,m5,m6,m7 in product((0,1), repeat=7):
    t = [(m1,1,m2,m3), (m4,0,1,m5), (0,m6,0,m7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,1]:
                print(''.join(p))  # wzxy


# 03
# 736


# 04
# 22

# 05
for n in range(4, 1000):
    b = f'{n:b}'
    if not n % 3:
        b += b[-3:]
    else:
        b += f'{(n % 3) * 3:b}'
    r = int(b, 2)
    if 120 <= r <= 140:
        print(n, r)  # 31 127
"""
15 127
31 127  ***
34 139
"""


# 06
from turtle import *
tracer(0)
lt(90)
screensize(2000, 2000)
k = 30
for _ in range(2):
    fd(3 * k)
    lt(90)
    bk(10 * k)
    lt(90)

pu()
bk(10 * k)
rt(90)
fd(8 * k)
lt(90)
pd()

for _ in range(2):
    fd(16 * k)
    rt(90)
    fd(8 * k)
    rt(90)

pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot()
# done()
print((3 * 10 + 8 * 16) - 2 * 3)  # 152


# 07
from math import ceil, log2
for i in range(1, 100):
    if ceil(192 * 960 * i / 8) * 0.85 > 90 * 1024:
        print(2 ** (i-1))  # 16
        break


# 08
from itertools import *
c = 0
res = 0
for p in product('upctyz', repeat=5):
    c += 1
    p = ''.join(p)
    if p.count('u') == 2 and 'zz' not in p:
        res = c
print(res)  # 7525


# 09
f = open('add/KIM_25163454/9_27621.txt').readlines()
c = 0
for i in f:
    c += 1
    n = sorted(map(int, i.split()))
    if len(set(n)) == 5 and n[-1] - n[0] == sum(n[1:-1]):
        print(c)  # 1321
        break


# 10
# 73 - 22 = 51


# 11
from math import ceil, log2
i = ceil(log2(10 + 26 + 8164))
for n in range(1, 1000):
    if ceil(n * i / 8) * 835 > 156 * 1024:
        print(n)  # 110
        break


# 12
# 27624 Апробация 04.03.26 (Уровень: Базовый)
s = f'{800:b}'
q = 2
r = ''
for i in range(len(s)):
    if q == 2:
        r += s[i]
        if s[i] == '1':
            q = 3
    elif q == 3:
        if s[i] == '0':
            r += s[i]
        else:
            r += '0'
            q = 4
    else:  # q == 4
        r += s[i]
print(int(r, 2))  # 544
# print(r)  # 1000100000


# 13
from ipaddress import *
c = 0
net = ip_network('172.16.96.0/255.255.224.0', 0)
for i in net:
    b = f'{i:b}'
    if not b.count('1') % 2:
        c += 1
print(c)  # 4096


# 14
res = 10**10
for x in range(1, 2031):
    n = 6**2030 + 6**100 - x
    c = 0
    while n:
        c += not n % 6
        n //= 6
    res = max(res, c)
print(res)  # 1930


# 15
def f(x):
    return x % 25 or not x % a or x % 60
for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 300
        break


# 16
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

[f(i) for i in range(1, 2025)]
print((f(2024) - 5 * f(2023)) // f(2022))  # 4084437


# 17
f = open('add/KIM_25163454/17_27629.txt').readlines()
d = [*map(int, f)]
c = 0
res = 0
n_43 = max(k for k in d if len(str(abs(k))) == 4 and str(abs(k))[-2:] == '43')
for i in range(len(d) - 1):
    num = d[i:i+2]
    n4 = [k for k in num if len(str(abs(k))) == 4]
    if n4:
        if sum(num)**2 < n_43**2:
            c += 1
            res = max(res, sum(num)**2)
print(c, res)  # 1218 98843364


# 19-21
# 27631 Апробация 04.03.26 (Уровень: Базовый)
def f(a, b, m):
    if a+b >= 211:
        return not m % 2
    if not m:
        return 0
    g = [f(a + 1, b, m-1), f(a * 2, b, m-1), f(a, b + 1, m-1), f(a, b * 2, m-1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)
    # return any(g)

# print([s for s in range(2, 194) if f(17, s, 2)][0])  #  49   return any(g)
print(*[s for s in range(2, 194) if f(17, s, 3) and not f(17, s, 1)])  #  88 96
print([s for s in range(2, 194) if f(17, s, 4) and not f(17, s, 2)][0])  # 87
"""
49
88 96
87
"""


# 22
# 16



# 23
def f(st, en):
    if st == en:
        return 1
    if st < en:
        return 0
    return f(st-1, en) + f(st // 2, en)

print(f(40, 17) * f(17, 6))  # 56


# 24
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


# 25
from fnmatch import *

for n in range(171, 10**8 + 1, 171):
    if fnmatch(str(n), '1*23??56'):
        print(n, n // 171)
"""
1237356 7236
10231956 59836
12232656 71536
14233356 83236
16234056 94936
18234756 106636
"""


# 26
# 27636 Апробация 04.03.26 (Уровень: Базовый)
f = open('add/KIM_25163454/26_27636.txt').readlines()
S, N = map(int, f[0].split())  # грузоподъёмность, кол-во контейнеров
d = sorted(map(int, f[1:]))  # значения масс контейнеров
c = sm = 0
for i in range(N):
    if sm + d[i] <= S:
        sm += d[i]
        c += 1
    else:
        break
print(N - c, sum(d) - sm)  # 7347 472188


# 27
# 27637 Апробация 04.03.26 (Уровень: Базовый)
from math import dist
def get_centr(ls: list):
    r = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        r.append((sm, i))
    return min(r)[1]

for w in 'AB':
    data = open(f'add/KIM_25163454/27_{w}_27637.txt').readlines()
    dt = [[*map(float, i.replace(',', '.').split())] for i in data]
    if w == 'A':
        clust = [[], []]
        for i in dt:
            if i[1] > 15:
                clust[0] += [i]
            else:
                clust[1] += [i]
        clust.sort(key=len)
        a1 = len(clust[0])
        center = [get_centr(i) for i in clust]
        a2 = int(sum(dist((-1.0, 1.3), i) for i in center) * 10_000)
        print(a1, a2)  # 301 319272

    else:
        clust = [[], [], []]
        for i in dt:
            if i[1] > 22:
                clust[0] += [i]
            elif i[0] > 24:
                clust[2] += [i]
            else:
                clust[1] += [i]
        clust.sort(key=len)
        center = [get_centr(i) for i in clust]

        b1 = sum(1 for i in clust[1] if dist(center[1], i) <= 1.6 and i != center[1])
        b2 = int(max(dist(i, center[2]) for i in clust[2]) * 10_000)
        print(b1, b2)  # 182 26825
"""
301 319272
182 26825
"""

























