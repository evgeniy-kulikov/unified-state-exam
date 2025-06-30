# https://kompege.ru/variant?kim=25104458
# КИМ № 25104458
# БР № 2832503195017   Windows + Shift + S

# 01
# № 23260
from itertools import permutations
g = 'CF FG GE EA AD DC AH HG DB BH BC'.split()
t = '346 348 12 127 678 15 458 257'.split()
print(*'12345678')
for p in permutations('ABCDEFGH'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
# 1 2 3 4 5 6 7 8
# G A E H C F B D
# C>B=24 + A>H=23 = 47


# 02
# № 23261
from itertools import product, permutations
def f(x,y,w,z):
    return not (w <= (x==y)) and (z <= x)

for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    t = [(a1, 0, 1, 0), (0, a2, a3, 0), (a4, 1, 1, a5)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, v))) for v in t):
                print(''.join(p))  # yxwz



# 03
# № 23263
# 513000


# 04
# № 23263
# 16


# 05
# № 23264
def f(n):
    s = ''
    while n:
        s = str(n % 3) + s
        n //= 3
    return s

m = 100**100
for n in range(1, 5000):
    r = f(n)
    if not n % 3:
        r += r[-2:]
    else:
        r += f(n % 3 * 5)
    d = int(r, 3)
    if d > 150:
        m = min(m, d)
print(m)  # 162


# 06
# № 23265
from turtle import *
tracer(0)
lt(90)
pd()
screensize(2000, 2000)
k = 25
for _ in range(2):
    fd(20*k)
    lt(270)
    fd(12*k)
    rt(90)
pu()
fd(9*k)
rt(90)
fd(7*k)
lt(90)
pd()
for _ in range(2):
    fd(13*k)
    rt(90)
    fd(6*k)
    rt(90)
pu()
for x in range(-5, k+20):
    for y in range(-5, k+20):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
# done()
print(21 * 13 + 7 * 2 + 12)  # 299


# 07
# № 23266
from math import ceil
I = ceil(2560 * 1440 * 22 / 8) / 1024
Iz = ceil(1920 * 1080 * 20 / 8) / 1024
print(int((I - Iz) * 130))  # 628875


# 08
# № 23267
""" есть неточность в задании: говорят про букву  Л """
from itertools import product

c = 0
for p in product('AKOPCT', repeat=5):
    c += 1
    # if p[0] not in 'AK' and p.count('C') == 1 and c % 2 == 1:
    if p[0] not in 'A' and p.count('C') == 1 and c % 2 == 1:
        print(c, ''.join(p))  # 7775 TTTTC


# variant
def f(n):
    a = 'AKOPCT'
    s = ''
    while n:
        s = a[n % 6] + s
        n //= 6
    return s.rjust(5, 'A')

for n in range(0, int('55555', 6) + 1):  # 7775
    r = f(n)
    # if r[0] not in 'AK' and r.count('C') == 1 and (n + 1) % 2 == 1:
    if r[0] not in 'A' and r.count('C') == 1 and (n + 1) % 2 == 1:
        print(n + 1, r)  # 7775 TTTTC


# 09
# № 23268
c = 0
with open('kompege/09.txt') as fl:
    for f in fl:
        c += 1
        d = list(map(int, f.split()))
        d1 = [i for i in d if d.count(i) == 1]
        d2 = [i for i in d if d.count(i) == 2]
        if len(d1) == 3 and len(d2) == 4:
            if sum(d2) / 4 < max(d1):
                print(c)  # 17
                break


# 10
# № 23269
# 8


# 11
# № 23270
from math import  *
i = ceil(log2(10 + 27))
for n in range(500):
    if ceil(n * i / 8) * 3548 / 1024 > 12:
        print(n)  # 5
        break


# 12
# № 23271
m = 0
for n in range(4, 4000): # 2689
    s = '1' + '2' * n
    while '12' in s or '322' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '2222' in s:
            s = s.replace('2222', '3', 1)
    r = sum(map(int, s))
    m = max(m, r)
print(m)  # 89


# 13
# № 23272
from ipaddress import  *
net = ip_network('205.99.68.249/255.255.248.0', 0)
print(str(net[-2]).replace('.', ''))  # 2059971254


# 14
# № 23273
from string import printable
alf = printable[:29]
for s in alf:
    n = int(f'463{s}7921', 29) + int(f'8241{s}153', 29)
    if not n % 28:
        print(n // 28)  # 7567913105
        break


# 15
# № 23274
def f(a):
    for x in range(1000):
        for y in range(1000):
            f = ((2 * x + y) != 110) or (x < y) or (a < x)
            if not f: return 0
    return 1

for a in range(100, 0, -1):
    if f(a):
        print(a)  # 36
        break


# 16
# № 23275
from functools import lru_cache
@ lru_cache
def g(n):
    if n < 10:
        return 2 * n
    return g(n - 2) + 1
def f(n):
    return 2 * (g(n-3) + 8)

for n in range(15500): g(n)
print(f(15548))  # 15588


# 17
# № 23276
m = c = 0
with open('kompege/17_23276.txt') as fl:
    ls = list(map(int, fl.readlines()))
    mx = max(i for i in ls if str(i)[-2:] == '25')  # 84725
    for i in range(len(ls) - 2):
        d = ls[i: i + 3]
        f = [k for k in d if len(str(abs(k))) == 4]
        # f = [k for k in d if 0 < abs(k) // 1000 < 10]
        if len(f) <= 2 and sum(d) <= mx:
            c += 1
            m = max(m, sum(d))
print(c, m)  # 6315 84523


# 18
# № 23277
# 2300 897


# 19-21
# № 23278
def fn(s, mv):
    if s <= 16: return not mv % 2
    if mv < 0: return 0
    g = [fn(s - 3, mv - 1), fn(s - 8, mv - 1), fn(s // 3, mv - 1)]
    if not (mv - 1) % 2: return any(g)
    return all(g)

print(min(s for s in range(17, 100) if fn(s, 2)))  # 51
print(*[s for s in range(17, 100) if fn(s, 3) and not fn(s, 4)][:2])  # 54 55
print(min(s for s in range(17, 100) if fn(s, 4) and not fn(s, 2)))  # 57


# 22
# № 23279
# 14


# 23
# № 23280
def fn(st, en):
    if st == en: return 1
    if st < en or st == 8: return 0
    return fn(st - 1, en) + fn(st - 4, en) + fn(st // 3, en)
print(fn(19, 14) * fn(14, 2))  # 69


# 24
# № 23281
# двойной цикл
with open('kompege/24_23281.txt') as fl:
    s = fl.read()
    m = 0
    for l in range(len(s)):
        for r in range(l + m, len(s) + 1):
            st = s[l:r]
            if st.count('Y') > 80:
                break
            if st.count('Y') == 80 and st.count('2025') >= 90:
                m = max(m, len(st))
print(m)  # 2981



# 25
# № 23282

def dv(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n//i}
    return d

cnt = 0
for n in range(5_400_001, 6_000_000):
    if cnt == 5: break
    # not len(dv(i))  ищет простие числа среди делителей
    # не нужно писать отдельную функцию
    m = [i for i in dv(n) if not len(dv(i))]
    if m:
        res = min(m) + max(m)
        if res > 60_000 and str(res) == str(res)[::-1]:
            cnt += 1
            print(n, res)
# 5400042 900009
# 5400420 90009
# 5400866 158851
# 5406116 1351531
# 5406420 90109

# variant
def dv(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n//i}
    return d

def p(n):  # поиск простого числа
    if n==1: return 0
    return all(n % i for i in range(2, int(n**0.5 + 1)))

cnt = 0
for n in range(5_400_001, 6_000_000):
    if cnt == 5: break
    d = dv(n)
    m = [i for i in d if p(i)]
    if len(m):
        res = min(m) + max(m)
        if res > 60_000 and str(res) == str(res)[::-1]:
            cnt += 1
            print(n, res)




# 26
# № 23283
with open('kompege/26_23283.txt') as fl:
    win = int(fl.readline())
    people = int(fl.readline())
    data = sorted(tuple(map(int, i.split())) for i in fl)
    queue = [[] for  _ in range(win)]
    for p in data:
        for w in queue:
            if not len(w):
                w.append(p)
                break
            else:
                if w[-1][1] < p[0]:
                    w.append(p)
                    break

print(sum(len(i) for i in queue), end= ' ') # 793
res = [i[-1][0] for i in queue]
print(res.index(max(res)) + 1)  # 2
# 793 2



# 27
# № 23284
from math import dist
def fn(ls:list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return min(res)[1]

with open('kompege/27_A_23284.txt') as fa:
    _ = next(fa)
    da = [[], []]
    for f in fa:
        d = tuple(map(float, f.replace(',', '.').split()))
        if d[1] < 15:
            da[0].append(d)
        else:
            da[1].append(d)
ax = int(sum(fn(i)[0] for i in da) * 10_000)
ay = int(sum(fn(i)[1] for i in da) * 10_000)
print(ax, ay)  # 107002 323741

with open('kompege/27_B_23284.txt') as fb:
    _ = next(fb)
    db = [[], [], []]
    for f in fb:
        d = tuple(map(float, f.replace(',', '.').split()))
        if d[0] < 0 or d[0] > 30:
            continue
        elif 0 < d[0] < 10:
            db[0].append(d)
        elif 11 < d[0] < 19:
            db[1].append(d)
        else:
            db[2].append(d)
zb = [fn(i) for i in db]
res_b = [sum(dist(i, k) for k in zb) for i in zb]
print(int(min(res_b) * 10_000), int(max(res_b) * 10_000))  # 169653 262715
# 107002 323741
# 169653 262715



