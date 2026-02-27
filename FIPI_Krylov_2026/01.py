""" var 01 """

# 02
from itertools import *
def f(x,y,w,z):
    return not x or not ((y <= z) and (z == (not w)))

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(0,m1,m2,0), (m3,1,1,m4), (m5,1,0,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # wxzy


# 05
res = 0
for n in range(4, 10000):
    b = f'{n:b}'
    if not n % 3:
        b += b[-3:]
    else:
        b += f'{(n % 3 + 1) * 3:b}'
    r = int(b, 2)
    if r <= 416:
        res = max(res, r)
print(res)  # 411


# 06
from turtle import *
tracer(0)
lt(90)
screensize(2000, 2000)
k = 30
for _ in range(4):
    fd(9 * k)
    lt(180)
    bk(10 * k)
    rt(90)
pu()
bk(7 * k)
lt(90)
fd(3 * k)
rt(90)
pd()
for _ in range(2):
    fd(17 * k)
    lt(90)
    fd(20 * k)
    lt(90)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()
print(20*20 + 18*21 - 11*17)   # 591


# 07
from math import ceil
I1 = ceil(2000 * 1000 * 25 / 8)
I2 = ceil(800 * 700 * 15 / 8)
print((I1 - I2) * 40 // 2**10) # 203125


# 08
from itertools import *
c = res = 0
for p in product('aelpct', repeat=5):
    p = ''.join(p)
    c += 1
    if not c % 2 and p[0] not in 'act' and 'll' not in p and p.count('l') == 2:
        res = c
print(res)  # 4518


# 09
c = res = 0
f = open('9var01.txt')
for i in f:
    c += 1
    d = [*map(int, i.split())]
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n1) == 4 and len(n3) == 3 and sum(n1) > sum(n3):
        res = c
print(res)  # 11597


# 11
from math  import ceil, log2
i = ceil(log2(10 + 70))  # 7
for n in range(1, 100):
    if ceil(n * i / 8) * 1234567 > 24 * 2**20:
        print(n)  # 23
        break


# 12
'0' * 124 + '1' + '0' * 395  # исходная  (124 + 395 = 519)
'0' * 124 + '0' + '1' * 395  # результирующая


# 13
from ipaddress import *
net = ip_network('77.180.176.14/255.255.254.0', 0)
res = str(net[-2]).replace('.', '')
print(res)  # 77180177254


# 14
n = 3 * 2187**1801 + 729**2000 - 4*243**2100 + 81**2200 - 2*27**2400 - 13122
c = 0
while n:
    c += n % 27 > 8
    n //= 27
print(c)  # 3432


# 15
def dv(n):
    r = set()
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

def f(x, b, c):
    a = x in [*range(3, 61)]
    b = x in b  # {3, 59}
    c = x in c  # {53}
    return not c or (a and not b)

b = dv(177)
for y in range(10_000, 1, -1):
    c = dv(y)
    if c:
        if all(f(x, b, c) for x in range(1, 10_000)):
            print(y)  # 2809  {59, 3, 53}
            break

# вариант
# все множество C (делителей числа Y) должны быть внутри отрезка A и не равны 3 и 59
for d in range(10_000, 1, -1):
    t = dv(d)
    if t:
        if 3 not in t and 59 not in t:
            if all(3 < i <= 60 for i in t):
                print(d)  # 2809 {53}
                break

# 16
from functools import lru_cache
@ lru_cache(None)
def f(n):
    if n == 1:
        return 2
    return 3 * f(n-1) - n

[f(i) for i in range(2, 2026)]
print((f(2025) - f(2023) - 1) / 3**2022)  # 6


# 17
c = 0
D = [*map(int, open('17var01.txt'))]
m = [i for i in D if 10 <= abs(i) < 100]
R = min(m) + max(m)
res = -10**6
for i in range(len(D) - 2):
    d = D[i:i+3]
    if sum(1 for i in d if 10 <= abs(i) < 100) >= 2 and sum(d) > R:
        c += 1
        res = max(res, sum(d))
print(c, res)  # 8 99191


# 19
def f(a, m):
    if a <= 60:
        return not m % 2
    if not m:
        return 0
    g = [f(a - 3, m - 1), f(a - 5, m - 1), f(a // 4, m - 1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print([i for i in range(61, 600) if f(i, 2)][0])
print(*[i for i in range(61, 600) if f(i, 3) and not f(i, 1)][:2])
print([i for i in range(61, 600) if f(i, 4) and not f(i, 2)][0])
"""
244
247 248
252
"""


# 23
def f(st, en):
    if st == en:
        return 1
    if st > en:
        return 0
    if st > 11 and str(st)[-2] < str(st)[-1]:
        r = str(st)
        r = r[:-2] + r[-1] + r[-2]
        return f(st + 1, en) + f(int(r), en)
    return f(st + 1, en)

print(f(101, 154))  # 89


# 24
res = 0
s = open('24var01.txt').read()
for i in '3579':
    s = s.replace(i, '1')
s = s.replace('S', ' ').split()
for w in s:
    if w.count('1') >= 35:
        w = w[::-1]
        for i in range(len(w)):
            if w[i:].count('1') == 35:
                res = max(res, len(w[i:]) + 1)
                break
print(res)  # 272


# 25
# сложное понимание сути задания 👎
c = 5
n3 = [3**i for i in range(1, 13)]
for n in range(10**5, 10**6):
    s = str(n)
    if not s.count('1'):
        for i in range(1, 13):
            d = n - 3**i
            if d % 2 and not d % 103:
                print(n, i)
                c -= 1
    if not c:
        break
"""
200004 4
200034 6
200036 9
200050 7
200056 10
"""


# 26
# Логика: в меньший по вместимости самолет сажаем максимально возможную по численности команду
f = open('26var01.txt').readlines()
N, M = map(int, f[0].split())  # кол-во команд / самолетов
data = [*map(int, f[1:])]
user = [[i, 1] for i in data[:N]]  # кол-во человек в команде  # [i, 1]  1-означает что команда не в самолете
flow = [[i, 1] for i in data[N:]]  # вместимость самолета  # [i, 1]  1-означает что самолет без пассажиров
user.sort(reverse=True)
flow.sort()
for f in range(M):
    for u in range(N):
        if flow[f][1] and user[u][1] and user[u][0] <= flow[f][0]:
            flow[f][1] = 0  # 0-означает что самолет взял пассажиров
            user[u][1] = 0  # 0-означает что пассажиры летят
            break
res_u = sum(not i[1] for i in user)  # сколько команд взято на борт
res_max = max(i[0] for i in user if not i[1])  # максимальная по численности команда взятая на борт
print(res_u, res_max)  # 679 194496


# 27
from math import dist
def get_center(ls: list):
    res = []
    for p in ls:
        sm = sum(dist(p, i) for i in ls)
        res.append([sm, p])
    return min(res)[1]

def get_clust(p):
    clust = [i for i in d if dist(p, i) < 3]
    [d.remove(i) for i in clust]
    next_cl = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_cl]
    return clust

def f_a(p, ls, k):
    if k:
        return max(dist(i, p) for i in ls)
    return min(dist(i, p) for i in ls)

def f_b(p, ls):
    return sum(dist(i, p) for i in ls if i != p) / (len(ls) - 1)

for w in 'AB':
    d = [[*map(float, i.replace(',', '.').split())] for i in open(f'27var01{w}.txt')]
    # print(len(d))
    clust = []
    while d:
        p = d.pop()
        clust.append(get_clust(p) + [p])
    clust = [i for i in clust if len(i) > 1]
    clust.sort(key=len)
    # [print(len(i)) for i in clust]
    # print(sum(len(i) for i in clust), '\n')
    center = [get_center(i) for i in clust]
    if w == 'A':
        p1 = int(min([f_a(center[0], clust[1], 0), f_a(center[1], clust[0], 0)]) * 10_000)
        p2 = int(max([f_a(center[0], clust[1], 1), f_a(center[1], clust[0], 1)]) * 10_000)
        print(p1, p2)  # 83354 110525
    else:
        q1 = int(f_b(center[0], clust[0]) * 10_000)
        q2 = int(f_b(center[-1], clust[-1]) * 10_000)
        print(q1, q2)  # 8580 9126
"""
83354 110525
8580 9126
"""
