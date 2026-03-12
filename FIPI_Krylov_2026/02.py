""" var 02 """

# 02
from itertools import *
def f(x,y,w,z):
    return ((z <= y) and (not y == x)) <= (not w)

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(m1,1,1,m2), (0,m3,m4,0), (m5,0,1,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t]==[0,0,0]:
                print(''.join(p))  # xywz


# 05
res = 0
for n in range(4, 10000):
    b = f'{n:b}'
    if not n % 3:
        b += b[-3:]
    else:
        b += f'{(n % 3 - 1) * 3:b}'
    r = int(b, 2)
    if r < 416:
        res = max(res, r)
print(res)  # 411


# 06
from turtle import *
tracer(0)
lt(90)
screensize(2500,2500)
k = 25
for _ in range(4):
    fd(19 *k)
    lt(180)
    bk(10 *k)
    rt(90)
pu()
bk(5 *k)
lt(90)
fd(4 *k)
rt(90)
pd()
for _ in range(2):
    fd(15 *k)
    lt(90)
    fd(8 *k)
    lt(90)
pu()
for x in range(-40, 10):
    for y in range(-10, 40):
        goto(x*k, y*k)
        dot('red') if not x*y else dot()
done()
print(30*30 + 16*9 - 11*9)  # 945


# 07
from math  import ceil
I1 = ceil(3200*1600*24 / 8)
I2 = ceil(1200*800*8 / 8)
print(int((I1 - I2) * 50 / 1024))  # 703125


# 08
from itertools import *
c = res = 0
for p in product('aelpct', repeat=5):
    c += 1
    if p[0] not in 'act' and p.count('e') == 2 and 'ee' not in ''.join(p) and c % 2:
        res = c
print(res)  # 4295


# 09
c = 0
for s in open('9var02.txt'):
    c += 1
    d = [*map(int, s.split())]
    n1 = [i for i in d if d.count(i) == 1]
    n4 = [i for i in d if d.count(i) == 4]
    if len(n1) == 3 and len(n4) == 4:
        if sum(n1) < sum(n4):
            print(c)  # 6327
            break


# 11
from math  import ceil, log2
i = ceil(log2(50 + 10))
for n in range(1, 1000):
    if ceil(n * i / 8) * 1_567_123 > 20 * 2**20:
        print(n)  # 18
        break

# 12
'0' * 119 + '1' + '0' * 213  # исходная  (119 + 213 = 332)
'0' * 119 + '0' + '1' * 213  # результирующая


# 14
n = 4 *2187**2101 + 729**2000 - 5*243**2100 + 81**2200 - 3*27**2250 - 26244
c = 0
while n:
    c += n%27 > 9
    n //= 27
print(c)  # 3432


# 15
def d(n):
    r = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

def f(x, y):
    A = 7 <= x <= 26
    B = x in {7, 11}  # d(77)
    C = x in d(y)
    return (not C) or (A and not B)

for y in range(2, 100000):
    if d(y):
        if all(f(x,y) for x in range(2, 10000)):
            print(y, d(y))  # 169 {13}
            break


# 16
from functools import lru_cache
@ lru_cache(None)
def f(n):
    if n == 1:
        return 15
    return 2 * f(n - 1) - n

[f(i) for i in range(1, 2026)]
print((f(2025) - f(2023) - 2) // 2**2022)  # 36


# 17
d = [*map(int, open('17var02.txt'))]
f = [i for i in d if 100 <= abs(i) < 1000]
sm = min(f) + max(f)
c = 0
for i in range(len(d) - 3):
    n = d[i:i+3]
    n3 = [i for i in n if 100 <= abs(i) < 1000]
    c += len(n3) >= 2 and sum(n) > sm
print(c)  # 14


# 19-21
def f(a, m):
    if a <= 65:
        return not m % 2
    if not m:
        return 0
    g = [f(a-3, m-1), f(a-5, m-1), f(a//4, m-1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print([a for a in range(66, 500) if f(a, 2)][0])
print(*[a for a in range(66, 500) if f(a, 3) and not f(a, 1)][:2])
print([a for a in range(66, 500) if f(a, 4) and not f(a, 2)][0])
"""
264
267 268
272
"""


# 23
def f(st, en):
    if st == en:
        return 1
    if st > en:
        return 0
    if int(str(st)[-2]) < st % 10:
        a = str(st)[-2]
        b = str(st)[-1]
        r = str(st)[:-2] + b + a
        return f(st + 1, en) + f(int(r), en)
    return f(st + 1, en)

print(f(110, 154))  # 34


# 24
res  = 0
st = open('24var02.txt').read()
for i in '0246':
    st = st.replace(i, '8')
st = st.split('L')
st = [i for i in st if i.count('8') >= 14]
for s in st:
    s += '8'  # если в строке оказалось ровно 14  '8'-ок
    c = 0
    for i in range(len(s)):
        if s[i] == '8':
            c += 1
        if c == 15:  # обрезаем строку после 15-ой  '8'-ке (она скомпенсирует убранную сплитом 'L')
            res = max(res, i + 1)  # индекс начинается с нуля
            break
print(res)  # 173


# 25
# 0пределяем подходящие степени тройки (можно это и не делать - будут лишние итерации)
# for n in range(100):
#     if 3**n > 10**6:
#         print(n, 3**n)  # 13 1594323
#         break
c = 5
for n in range(10 ** 5, 10 ** 6):
    if '0' not in str(n):
        for i in range(1, 13):
            d = n - 3**i
            if d % 2 and (not d % 113) and d > 0:  # d - это натуральное число ✅
                print(n, i)
                c -= 1
    if not c:
        break
"""
111142 10
111232 7
111312 8
111314 2
111322 5
"""

# 26
f = open('26var02.txt').readlines()
N, M = map(int, f[0].split())  # кол-во команд / самолетов
data = [int(i) for i in f[1:]]
user = [i for i in data[:N]]  # кол-во человек в команде
plane = [[i, 0] for i in data[N:]]  # вместимость самолета  # [i, 0]  0-означает что самолет без пассажиров
user.sort(reverse=True)
plane.sort()
mx = 0
for i in range(N):  # user
    for k in range(M):  # plane
        if not plane[k][1] and plane[k][0] >= user[i]:
            plane[k][1] = 1  # самолет загружен
            mx = max(mx, user[i])
            break

pl = sum(i[1] for i in plane)
print(pl, mx)  # 716 193997


# 27
from math import dist
def get_center(ls: list):
    r = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        r.append((sm, i))
    return min(r)[1]

def get_clust(p):
    clust = [i for i in data if dist(p, i) < k]
    [data.remove(i) for i in clust]
    nex_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in nex_clust]
    return clust

for w, k in zip('AB', (1, 0.2)):
    f = open(f'27var02{w}.txt')
    data = [[*map(float,i.replace(',', '.').split())] for i in f]
    # print(len(data))
    clust = []
    while data:
        p = data.pop()
        clust.append(get_clust(p) + [p])
    # [print(len(i)) for i in clust]
    # print(sum(len(i) for i in clust))
    clust = [i for i in clust if len(i) > 1]
    if w == 'A':
        center = [get_center(i) for i in clust]
        px = int(abs(min([i[0] for i in center]) * 10_000))
        py = int(abs(min([i[1] for i in center]) * 10_000))
        print(px, py)  # 35503 115495
    else:
        clust.sort(key=len)
        q1 = len(clust[0])
        q2 = len(clust[-1])
        print(q1, q2)  # 98 397
"""
35503 115495
98 397
"""
