"""
Демонстрационный вариант
контрольных измерительных материалов
единого государственного экзамена 2025-26 года
по ИНФОРМАТИКЕ
https://fipi.ru/ege/demoversii-specifikacii-kodifikatory#!/tab/151883967-5
https://doc.fipi.ru/ege/demoversii-specifikacii-kodifikatory/2026/inf_11_2026.zip
"""

# 01
from itertools import *
print(*'12345678')
g = 'da ac cb bh hd fh fe ge gc ga'.split()
t = '258 17 56 68 138 347 26 145'.split()
for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
"""
1 2 3 4 5 6 7 8
g e b d c h f a
g e d b a h f c
ge = 15
fh = 37
52
"""


# 02
from itertools import *
def f(x,y,w,z):
    return (x or y) and not (y==z) and not w

for a1, a2, a3, a4 in product((0,1), repeat=4):
    t = [(1,a1,1,a2), (0,1,a3,0),(a4,1,1,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p,d))) for d in t] == [1,1,1]:
                print(''.join(p))  # zyxw

# 03
# Demo/03_Demo/Доп_файлы/DEMO_3.ods
# 133228


# 04
# 16
# Demo/03_Demo/add/04.gif


# 05
for n in range(1, 200):
    b = f'{n:b}'
    if not n % 3:
        b += b[-3:]
    else:
        b += f'{(n % 3) * 3:b}'
    if int(b, 2) >= 200:
        print(n)  # 26
        break


# 06
from turtle import *
tracer(0)
lt(90)
screensize(3000, 3000)
k = 30

for _ in range(2):
    fd(14*k)
    lt(270)
    bk(12*k)
    rt(90)
pu()
fd(9*k)
rt(90)
bk(7*k)
lt(90)
pd()
for _ in range(2):
    fd(13*k)
    rt(90)
    fd(6*k)
    rt(90)
pu()
for x in range(-k, 3):
    for y in range(-3, k):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()
print(8*7 + 15*13)  # 251
# Demo/03_Demo/add/06.gif



# 07.1
I_1 = 1024*768*30/2**13
I_2 = 800*600*28/2**13
print((I_1 - I_2) * 100)  # 123937

# 07.2
"""
I_1 = 1 * Hz * i * sec = 35
I_2 = 2 * Hz*3.5 * i * sec = ?
"""
print(35 * 2 * 3.5)  # 245


# 08
from itertools import product
c = 0
for p in product('АКОРСТ', repeat=5):
    c += 1
    if p[0] not in 'АСТ' and p.count('О') == 2 and not c % 2:
        print(c, ''.join(p))  # 5058 РТООТ


# 09
from statistics import mean
res = 0
with open('Demo/03_Demo/add/09.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        three = [i for i in d if d.count(i) == 3]
        if len(one) == 4 and len(three) == 3:
            if mean(one) <= mean(three):
                res = sum(d)
print(res)  # 901


# 10
# 13 - 0 = 13


# 11
from math import ceil
for i in range(1, 10):
    if ceil(2783 * i / 8) * 3_845_627 / 2**30 >= 11:
        print(2**(i-1) + 1)  # 257
        break


# 12
# Demo/03_Demo/add/12.gif
# 999


# 13
from ipaddress import *
net = ip_network('191.128.66.83/255.192.0.0', 0)
print(list(net.hosts())[-1]) # 191.191.255.254
# 191191255254



# 14.1
n = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
c = 0
while n:
    c += n % 27 > 9
    n //= 27
print(c)  # 3367

# 14.2
from string import ascii_lowercase, digits
alf = (digits + ascii_lowercase)[:29][::-1]
for x in alf:
    n = int(f'923{x}874', 29) + int(f'524{x}6152', 29)
    if not n % 28:
        print(n // 28)  # 3319197720
        break

# 14.3
alf = '0123456789a'
for x in range(3000, 0, -1):
    r = 9*11**210 + 8*11**150 - x
    c = 0
    while r:
        c += not r % 11
        r //= 11
    if c == 60:
        print(x)  # 2992
        break


# 15
# Demo/03_Demo/add/15.gif
for x in [i*0.5 for i in range(500)]:
    p = 25 <= x <= 64
    q = 40 <= x <= 115
    # f = p <= (q <= (not p))
    f = not p or not q
    if not f:
        print(x)  # 64 - 40 = 24


# 16
from functools import lru_cache
@lru_cache(None)
def g(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return g(n-2) + 1

def f(n):
    return 2 * (g(n-3) + 8)

for i in range(15_600):
    g(i)

print(f(15_548))  # 15588



# 17
with open('Demo/03_Demo/add/DEMO_17.txt') as fl:
    d = list(map(int, fl.readlines()))
    mn = min(i for i in d if 10 <= i < 100)
    c, ms = 0, 0
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if sum(1 for k in d[i:i+2] if 10 <= k < 100) == 1 and not (a+b) % mn:
            c += 1
            ms = max(ms, a+b)
    print(c, ms)  # 150 9930


# 18  2360  1205

# 19-21
def f(s, mv):
    if s <= 30:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s-3, mv-1), f(s-5, mv-1), f(s // 4, mv-1)]
    if not (mv-1)% 2:
        return any(g)
    return all(g)

print([s for s in range(31, 200) if f(s, 2)][0])  # 124
print(*[s for s in range(31, 200) if f(s, 3) and not f(s, 1)][:2])  # 127 128
print([s for s in range(31, 200) if f(s, 4) and not f(s, 2)][0])  # 132


# 22  12


# 23
def f(st, end):
    if st < end or st == 7:
        return 0
    if st == end:
        return 1
    return f(st-1, end) + f(st-4, end) + f(st // 3, end)

print(f(19, 13) * f(13, 2))  # 68


# 24
res = 0
with open('Demo/03_Demo/Доп_файлы/DEMO_24.txt') as fl:
    s = fl.read().strip()
    for l in range(len(s)):
        for r in range(l + res + 1, len(s) + 1):
            row = s[l:r]
            if row.count('Y') > 80:
                break
            if row.count('Y') == 80 and row.count('2025') >= 90:
                res = max(res, len(row))
        # if not l % 10**6:
        #     print(l, res)  # прогресс
print(res)  # 2981


# 25.1
def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    if len(d):
        return min(d) + max(d)
    return 0

c = 0
for n in range(800_000, 1_000_000):
    m = f(n)
    if m % 10 == 4:
        c += 1
        print(n, m)
        if c == 5:
            break
"""
800004 400004
800009 114294
800013 266674
800024 400014
800033 61554
"""

# 25.2.1
# дольше
from itertools import product
res = []
for x in range(10):
    for y in range(10):
        # пусто  +  одиночные  +  двойные разряды
        for z in [''] + [*'0123456789'] + [*product('0123456789', repeat=2)]:
            m = int(f'3{x}12{y}14{"".join(z)}5')
            if not m % 1917 and m <= 10**10:
                res.append((m, m // 1917))
res.sort()
for k in res:
    print(*k)
"""
351261495 183235
3212614035 1675855
3412614645 1780185
3712414275 1936575
3912414885 2040905
"""

# 25.2.2
from fnmatch import fnmatch
res = []
st = 30120145 - (30120145 % 1917)
msk = '3?12?14*5'
for n in range(st, 4000000000, 1917):
    if fnmatch(str(n), msk):
        res.append((n, n // 1917))
res.sort()
[print(*i) for i in res]
"""
351261495 183235
3212614035 1675855
3412614645 1780185
3712414275 1936575
3912414885 2040905
"""


# 26




# 27
from math import dist
def centr(clast:list):
    res = []
    for i in clast:
        res.append((sum(dist(i, k) for k in clast), i))
    return min(res)[1]

a1, a2 = [], []
with open('Demo/03_Demo/Доп_файлы/DEMO_27_A.txt') as fl:
    for f in fl:
        d = list(map(float, f.replace(',', '.').split()))
        if d[1] > 10:
            a1.append(d)
        else:
            a2.append(d)
centr_a1 = centr(a1)
centr_a2 = centr(a2)
p1 = int(min(centr_a1[0], centr_a2[0])*10_000)
p2 = int(min(centr_a1[1], centr_a2[1])*10_000)
print(p1, p2)  # 38471 61225

b1, b2, b3 = [], [], []
with open('Demo/03_Demo/Доп_файлы/DEMO_27_B.txt') as fl:
    for f in fl:
        d = list(map(float, f.replace(',', '.').split()))
        if 10 < d[1] < 20:
            b1.append(d)
        if 20 < d[1] < 30 and d[0] < 18:
            b2.append(d)
        if 20 < d[1] < 30 and d[0] >= 18:
            b3.append(d)
centr_b1 = [len(b1), centr(b1)]
centr_b2 = [len(b2), centr(b2)]
centr_b3 = [len(b3), centr(b3)]
d = sorted([centr_b1, centr_b2, centr_b3])
q1 = int(dist(d[0][1], d[-1][1])*10_000)
print(q1)  # 142058

a = max(dist(centr_b1[1], k) for k in b1)
b = max(dist(centr_b2[1], k) for k in b2)
c = max(dist(centr_b3[1], k) for k in b3)
print(int(max([a,b,c])*10_000))  # 25299
"""
38471   61225
142058  25299
"""
