""" https://kompege.ru/variant?kim=25104364 """

# 01 №23185
from itertools import *
g = 'dg ga ah hf fe ed hb fb bc cg'.split()
t = '478 38 256 15 34 37 168 127'.split()
print(*'12345678')
s = 'abcdefgh'
for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
# 1 2 3 4 5 6 7 8
# f a g e d c b h
# f c g e d a h b
# ed=34  gd=11  --> 45


# 02  №23186
from itertools import *
def fn(x,y,w,z):
    return (x <= y) and z and (not w)

for a1,a2,a3,a4,a5,a6 in product((0,1), repeat=6):
    for p in permutations('xywz'):
        t = [(0,1,a1,a2),(1,1,a3,a4),(1,a5,1,a6)]
        if len(set(t)) == 3:
            if all(fn(**dict(zip(p,k))) for k in t):
                print(''.join(p))  # yzxw


# 03  №23187
#  111436500


# 03  №23188
#  14


# 05  №23189
mx = 0
for n in range(4, 10000):
    b = f'{n:b}'
    if not n % 3:
        b += b[-3:]
    else:
        b += f'{n % 3 * 3:b}'
    r = int(b, 2)
    if r < 130:
        mx = max(mx, n)
print(mx)  # 31



# 06  №23190
from turtle import *

tracer(0)
lt(90)
pd()
k = 30
screensize(2000, 2000)

for _ in range(2):
    fd(3 * k)
    rt(90)
    fd(20 * k)
    rt(90)

pu()
fd(-8 * k)
rt(90)
fd(9 * k)
lt(90)
pd()

for _ in range(2):
    fd(16 * k)
    rt(90)
    fd(8 * k)
    rt(90)

pu()
for x in range(-k + 20, k + 20):
    for y in range(-k + 20, k):
        goto(x * k, y * k)
        dot('red') if not x * y else dot()
done()
print(17 * 9 + 4 * 3 + 9 * 3)  # 201


# 07  №23191
from math import *
I = ceil(1920*1080*23/8)
Iz = ceil(1280*1024*21/8)
print((I - Iz) / 1024 * 120)  # 295425


# 08  №23192
def f(n):
    alf = 'ЕИОРТЯ'
    s = ''
    while n:
        s = alf[n % 6] + s
        n //= 6
    return s

cnt = res = 0
en = int('555555' , 6) + 1
for n in range(0, en):
    cnt += 1
    b = f(n).rjust(6, 'Е')
    if b[0] not in 'РТЯ' and b.count('И') >= 2 and cnt % 2:
        res = cnt
    # if cnt == 23159: print(b)  # ОЯЯИИТ
print(res)  # 23159


# 09  №23193
cnt = res = 0
with open('kompege/9.txt') as fl:
    for f in fl:
        cnt += 1
        d = list(map(int, f.split()))
        d1 = [i for i in d if d.count(i) == 1]
        d3 = [i for i in d if d.count(i) == 3]
        if len(d3) == 3 and len(d1) == 3:
            if d3[0] > sum(d1) / 3:
                res = cnt
                # print (d)  # [33, 77, 58, 77, 77, 32]
print(res)  # 10493


# 10  №23194
# все = 13   отдельн.слово=1   --> 12


# 11  №23195
from math import *
for i in range(1, 1000):
    if (ceil(172 * i / 8) * 356_984)/ 2**20 > 54:
        print(2**(i-1) + 1)  # 129
        break


# 12  №23196
for n in range(4, 10_000):
    s = '7' + '8' * n
    while '78' in s or '688' in s or '8888' in s:
        if '78' in s:
            s = s.replace('78', '8', 1)
        if '688' in s:
            s = s.replace('688', '87', 1)
        if '8888' in s:
            s = s.replace('8888', '6', 1)
    if sum(map(int, s)) == 61:
        print(n) # 348
        break


# 13  №23197
from ipaddress import *
net = ip_network('45.172.106.203/255.255.252.0', 0)
print(str(net[-2]).replace('.', ''))  # 45172107254


# 14  №23198
def f(n):
    s = ''
    while n:
        s = str(n % 9) + s
        n //= 9
    return s

for n in range(1, 3001):
    ex = 9**150 + 9**30 - n
    if f(ex).count('0') == 122:
        print(n)  # 81
        break


# 15  №23199
def f(a):
    for x in range(100):
        for y in range(100):
            if not ((x*y > a) or (x > y) or (11 > x)):
                return 0
    return 1

for a in range(1000, 0, -1):
    if f(a):
        print(a)  # 120
        break


# 16  №23200
# Динамический подход
d = []
for n in range(6251):
    if n < 10:
        d.append(n)
    else:
        d.append(3 * n + d[n - 3])
print((d[6250] + 2 * d[6244]) // d[6238])

# Рекурсивный подход
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 10:
        return n
    return 3 * n + f(n-3)

for n in range(6250): f(n)  # заполняем кэш памяти значениями
print((f(6250) + 2 * f(6244)) // f(6238))  # 3



# 17  №23201
with open('kompege/17.txt') as fl:
    ls = list(map(int, fl))
    n_min = min([x for x in ls if len(str(x)) == 3 and str(x)[-1] == '7'])
    cnt = 0
    min_d = 102_000
    for i in range(len(ls) - 1):
        d = ls[i:i+2]
        if any(len(str(x)) == 3 for x in d):
            if not sum(d) % n_min:
                cnt += 1
                min_d = min(min_d, sum(d))
print(cnt, min_d)  # 9 107


# 18  №23202
# 2132 663


# 19  №23203
# 20  №23203
# 21  №23203
def f(s, mv):
    if s <= 11: return not mv % 2
    if mv < 0: return 0
    g = [f(s-3, mv-1), f(s-7, mv-1), f(s//3, mv-1)]
    if not (mv - 1) % 2: return any(g)
    return all(g)

print([s for s in range(12, 100) if f(s, 2)][0])  # 36
print(*[s for s in range(12, 100) if f(s, 3) and not f(s, 1)][:2])  # 39 40
print([s for s in range(12, 100) if f(s, 4) and not f(s, 2)][0])  # 42


# 22  №23204
# 5


# 23  №23205
def f(st, en):
    if st < en or st == 13:
        return 0
    if st == en:
        return 1
    return f(st - 1, en) + f(st - 2, en) + f(st // 3, en)

print(f(19, 6) * f(6, 4))  # 212


# 24  №23206
# решение регулярным выражением
from re import *
reg = r'[02468][A-Z13579]*'
with open('kompege/24_23206.txt') as fl:
    s = fl.read()
    ls = finditer(reg, s)
    # список всех подходящих строк
    data = [i.group() for i in ls if i.group().count('S') >= 35]
res = 0
for k in data:
    if k.count('S') == 35:  # для строк имеющих ровно 35 символов 'S'
        res = max(res, len(k))
    else:  # для строк имеющих больше 35 символов 'S'
        k = k.replace('S', '*', 35)  # убираем слева 35 символов 'S'
        res = max(res, k.index('S')) # ищем положение 36-го символа 'S'
print(res)  # 292

# решение двойным указателем (l - left, r - right)
with open('kompege/24_23206.txt') as fl:
    s = fl.read()
l = cnt = res = 0
for r in range(len(s)):
    if s[r] in '02468':  # начало события
        l = r  # запоминаем начало в левом указателе
        cnt = 0  # сброс счетчика
    cnt += s[r]=='S'
    if s[l] in '02468' and cnt==35:  # окончание события
        res = max(res, r-l+1)
    # возможны холостые ходы
print(res)  # 292

# решение двойным циклом (l - left, r - right)
with open('kompege/24_23206.txt') as fl:
    s = fl.read()
    for c in '2468':
        s = s.replace(c, '0')
res = 1
for l in range(len(s)):
    for r in range(l + res, len(s) + 1):
        st = s[l:r]
        if st[0] != '0' or st.count('0') > 1 or st.count('S') > 35:
            break
        if st[0] == '0' and st.count('S') == 35:
            res = max(res, len(st))
print(res)  # 292


# 25  №23207
def dv(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n//i}
    return d

def sp(n):
    if n == 1:return 0
    for i in range(2, int(n**0.5 + 1)):
        if not n % i: return 0
    return 1
# def sp(n):  # короче
#     return n > 1 and all(n % i for i in range(2, int(n**0.5 + 1)))

cnt = 0
for n in range(1_324_728, 1_500_000):
    if cnt == 5: break
    d = [i for i in dv(n) if sp(i)]
    d = [i for i in d if str(i).count('5') == 1]
    if len(d) == 2 and d[0] * d[1] == n:
        cnt += 1
        print(n, max(d))
    if len(d) == 1 and d[0]**2 == n:
        cnt += 1
        print(n, *d)
# 1324795 264959
# 1324801 1151
# 1324903 2543
# 1325015 265003
# 1325029 5279


# 26 №23208
# решение через таблицу
# 503 478



# 27 №23209
from math import dist
def f(ls:list):
    res = []
    for i in ls:
        s = sum(dist(i, k) for k in ls)
        res.append((s, i))
    h = min(res)
    return len(ls), min(res)[1]

with open('kompege/27_A_23209.txt') as fl_a:
    _ = next(fl_a)
    d = [tuple(map(float, i.replace(',', '.').split())) for i in fl_a]
    d_a = [[], []]
    for i in d:
        if i[1] > 10:
            d_a[0].append(i)
        else:
            d_a[1].append(i)
    x_a = int(max(f(i)[1][0] for i in d_a) * 10_000)
    y_a = int(max(f(i)[1][1] for i in d_a) * 10_000)
print(x_a, y_a) # 69663 192156

with open('kompege/27_B_23209.txt') as fl_b:
    _ = next(fl_b)
    d = [tuple(map(float, i.replace(',', '.').split())) for i in fl_b]
    d_b = [[], [], []]
    for i in d:
        if i[1] > 30 or i[1] < 0:
            continue
        elif 0 < i[1] < 15:
            d_b[0].append(i)
        elif 15 < i[1] < 21:
            d_b[1].append(i)
        else:
            d_b[2].append(i)
    d_b = sorted([f(i) for i in d_b])
    x_b = abs(int((d_b[0][1][0] - d_b[2][1][0]) * 10_000))
    y_b = abs(int((d_b[0][1][1] - d_b[2][1][1]) * 10_000))
print(x_b, y_b) # 867 161306
# 69663 192156
# 867 161306


