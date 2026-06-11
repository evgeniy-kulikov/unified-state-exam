""" https://kompege.ru/task """
"""
216 307 432 627 743 752 753 754 762 764
1015 1127 1198 1234 1276 1295 1409 1968 2078 2080 2123 3156 4988 7086 7265 7353 7817 8159 8676 9370 9545 
11665 12247 12469 13082 17528 17871 19980
20905 21710 24988 25279 25354

🍒 отрезки
🍓 множества
⌛ конъюнкция
🆗 x и y
"""



# 216 Джобс 14.09.2020 (Уровень: Базовый) ⌛ конъюнкция
def f(x):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))

for a in range(1, 100):
    if all(f(x) for x in range(1, 10_000)):
        print(a)  # 2
        break


# 307 Джобс 28.09.2020 (Уровень: Средний)  🍒 отрезки
def f(x):
    p = 3 <= x <= 15
    q = 14 <= x <= 25
    a = a1 <= x <= a2
    # return not (p == q) or not a
    return p != q or not a

n = [i for k in (3,14,15,25) for i in (k-0.1, k, k+0.1)]
res = 0
for a1 in n:
    for a2 in n:
        if a1 < a2 and all(f(x) for x in n):
            res = max(res, a2 - a1)
print(round(res))  # 11  (10.9)


# 432 Джобс 05.10.2020 (Уровень: Средний)
def f(x):
    return (x % 84 or x % 90) <= x % a

for a in range(1, 2_000):
    if all(f(x) for x in range(1, 5_000)):
        print(a)  # 1260
        break


# 627 Джобс 02.11.2020 (Уровень: Базовый)  🆗 x и y
def f(x, y):
    return (x * y > a) and (x > y) and (x < 8)

for a in range(1, 1000):
    if all(not f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)  # 42
        break


# 743 (Уровень: Средний)  🍓 множества
def f(x):
    P = x in {1, 3, 5, 7, 9, 11}
    Q = x in {3, 6, 9, 12}
    A = x in a
    # return not P or not Q or A
    return not (P and Q) or A
    # return not (P & Q) or A  # (решение руками)
    # return x not in {9, 3} or A  # (решение руками)

a = set()  # {9, 3}
for x in range(1, 100):
    if not f(x):
        a.add(x)
print(sum(a))  # 12


""" Взято на мой курс """
# 752 (Уровень: Средний) 🍓 множества
def f(x):
    P = x in {3, 6, 9, 12}
    Q = x in {1, 2, 3, 4, 5, 6}
    A = x in a
    # return not (not A and P) or not Q
    return A or not P or not Q

a = set()  # {3, 6}
for x in range(1, 100):
    if not f(x):
        a.add(x)
print(len(a))  # 2


# 753 (Уровень: Средний)  🍒 отрезки
def f(x):
    p = 5 <= x <= 30
    q = 14 <= x <= 23
    a = a1 <= x <= a2
    return (p != q) or not a

res = 0
n = [i for k in (5,30,14,23) for i in (k-0.1, k , k +0.1)]
for a1 in n:
    for a2 in n:
        if a1 < a2 and all(f(x) for x in n):
            res = max(res, a2 - a1)
print(round(res))  # 9


# 754 (Уровень: Средний)
def f(x):
    A = x in a
    P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x in {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
    # return (A <= P) and (Q <= (not A))
    # return (not A or P) and (not Q or not A)
    return not A or (not Q and P)

a = set(range(1, 1000))
for x in range(1, 100000):
    if f(x) == 0:
        a.remove(x)
# print(a)  # {2, 4, 6, 8, 12, 14, 16, 18}
print(len(a))  # 8



""" Взято на мой курс """
# 762 (Уровень: Базовый)
def f(x):
    return (not x % a and not x % 24 and x % 16) <= (x % a != 0)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 16
        break


# 764 (Уровень: Базовый)
def d(n, m):
    return not n % m
def f(x):
    return (d(x, 15) and not d(x, 21)) <= (not d(x, a) or not d(x, 15))

# def f(x):  # обычный вариант
#     return not (not x % 15 and x % 21) or (x % a or x % 15)

for a in range(1, 100):
    if all(f(x) for x in range(1, 10_000)):
        print(a)  # 7
        break




# 1015 100 базовых задач Е. Джобс (Уровень: Базовый)  🆗 x и y
def f(x, y):
    return (x > 39) or (y > 26) or (2 * x) + 4 * y < a

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)  # 183
        break


# 1127 (Уровень: Базовый)
def f(x):
    # return  not a % 7 and  ((240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)))
    return  (not a % 7) and (240 % x or (not a % x) or 780 % x)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 10_000)):
        print(a)  # 420
        break


# 1198 Апробация 27.04 (Уровень: Средний)  🍒 отрезки
def f(x):
    b = 18 <= x <= 52
    c = 16 <= x <= 41
    a = a1 <= x <= a2
    return (b <= a) and (not c or a)

d = [y for x in (18,52,16,41) for y in (x-0.1, x, x+0.1)]
res = 1000
for a1 in d:
    for a2 in d:
        if a1 < a2:
            if all(f(i) for i in d):
                res = min(res, a2 - a1)
print(round(res))  # 36


# 1234 (Уровень: Базовый)
def f(x):
    b = 120 <= x <= 130
    return not b or x % 7 or a > 2*x

for a in range(1000):
    if all(f(x) for x in range(1000)):
        print(a)  # 253
        break


# 1276 (Уровень: Средний)  🍒 отрезки
def f(x):
    p = 15 <= x <= 33
    q = 35 <= x <= 48
    a = a1 <= x <= a2
    # return (a and not q) <= (p or q)
    return not a or q or p

res = 0
n = [i for k in (15,33,45,68) for i in (k-0.2, k, k+0.2)]
for a1 in n:
    for a2 in n:
        if a2 > a1 and all(f(x) for x in n):
            res = max(res, a2-a1)
print(res)  # 18


# 1295 Открытый вариант КЕГЭ (Уровень: Средний)  🍒 отрезки
def f(x):
    p = 17 <= x <= 54
    q = 37 <= x <= 83
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))

d = [y for x in (17,54,37,83) for y in (x-0.1, x, x+0.1)]
res = 1000
for a1 in d:
    for a2 in d:
        if a1 < a2:
            if all(f(i) for i in d):
                res = min(res, a2 - a1)
print(round(res))  # 17


# 1409 (Уровень: Средний) 🍓 множества
from math import prod
def f(x):
    P = x in p
    Q = x in q
    R = x in r
    A = x in a
    # return (not A) <= ((P and Q) <= R)
    return not P or not Q or R or A

a = set()  # {6, 18}
p = {*range(2, 21, 2)}
q = {*range(3, 31, 3)}
r = {12, 24, 36, 48, 60}
for x in range(1, 100):
    if not f(x):
        a.add(x)
print(prod(a))  # 108


""" Взято на мой курс """
# 1968 Демоверсия 2022 (Уровень: Средний)  🍒 отрезки
def f(x):
    d = 17 <= x <= 58
    c = 29 <= x <= 80
    a = a1 <= x <= a2
    # return d <= ((not c and (not a)) <= (not d))
    return not d or c or a

d = [y for x in (17,58,29,80) for y in (x-0.1, x, x+0.1)]
res = 1000
for a1 in d:
    for a2 in d:
        if a1 < a2:
            if all(f(i) for i in d):
                res = min(res, a2 - a1)
print(round(res))  # 12


""" Взято на мой курс """
# 2078 (Уровень: Базовый) ⌛ конъюнкция
def f(x):
    # return (((x & 13 != 0) or (x & a != 0)) <= ((x & 13 != 0))) or ((x & a != 0) and (x & 39 == 0))
    return not (x & 13 or x & a) or x & 13 or (x & a and (not x & 39))

for a in range(100, 0, -1):
    if all(f(x) for x in range(1, 10_000)):
        print(a)  # 13
        break


# 2080 (Уровень: Базовый)  🆗 x и y
def f(x, y):
    return (x**2 - 10*x + 16 > 0) or (y**2 - 10*y + 21 > 0) or (x*y < 2*a)

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)  # 29
        break


""" Взято на мой курс """
# 2123 Danov2201 (Уровень: Базовый)  🆗 x и y
def f(x, y):
    return (2 * x + y != 70) or (x < y) or (a < x)

for a in range(100, 0, -1):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)  # 23
        break


# 3156 (Уровень: Средний) 🍓 множества
def f(x):
    P = x in p
    Q = x in q
    A = x in a
    # return (A <= P) and (Q <= (not A))
    # return (not A or P) and (not Q or (not A))
    return not A or (not Q and P)

p = {*range(2, 21, 2)}
q = {*range(5, 51, 5)}
a = {*range(1, 100)}
for x in range(1, 100):
    if not f(x):  # not f(x) ❗❗❗
        a.remove(x)
print(len(a))  # 8
# print(a)  # {2, 4, 6, 8, 12, 14, 16, 18}


""" Взято на мой курс """
# 4988 (Уровень: Базовый)  🍒 отрезки + делители
def f(x):
    b = 70 <= x <= 80
    return not x % 12 and b and x % a

c = 0
for a in range(1, 1000):
    if all(not f(x) for x in range(1, 1000)):
        c += 1
print(c)  # 12


# 7086 OpenFIPI (Уровень: Базовый)
def f(x):
    b = 50 <= x <= 70
    return not x % a or not b or x % 16

for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 64
        break


# 7265 OpenFIPI (Уровень: Базовый)s
def f(x):
    return x % 2 or x % 3 or (x + a >= 100)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 94
        break


# 7353 (Уровень: Базовый)
def f(x):
    b = 70 <= x <= 80
    return not x % a or not b or x % 18

cnt = 0
for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        cnt += 1
print(cnt)  # 12


# 7817 (Уровень: Базовый)
def f(x):
    b = 40 <= x <= 60
    return x % 13 or not b or (a < x + 20)

for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 71
        break


# 8159 /dev/inf 05.23 (Уровень: Базовый)
def f(x, y):
    b = 50 <= x <= 70
    return (2 * x + y != 150) or not b or a > y

for a in range(500):
    if all(f(x, y) for x in range(500) for y in range(500)):
        print(a)  # 51
        break


# 8676 (Уровень: Базовый)
def f(x):
    return not x & 500 or x & 200 or x & b

for b in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(b)  # 308
        break


""" Взято на мой курс """
# 9370 Джобс 10.06.23 (Уровень: Сложный)  🍒 отрезки
def f(x):
    p = 5 <= x <= 54
    q = 50 <= x <= 93
    # return (not p and q) <= (x > a)
    return p or not q or x > a

for a in range(1000):
    if sum(not f(i) for i in range(10_000)) == 20:
        print(a)  # 74
        break


# 9545 Джобс 14.06.23 (Уровень: Базовый)
def f(x):
    return x % 10 or x % 26 or x < 300 or a <= x

for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 390
        break




# 11665 (Уровень: Базовый)
def f(x):
    return (a + x > 700 - a) and (a % 100 + 100 % x > 50)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 351
        break


# 12247 ЕГКР 16.12.23 (Уровень: Базовый)
def f(x):
    return not x & a or x & 37 or x & 12

for a in range(1000, 0, -1):
    if all(f(x) for x in range(1000)):
        print(a)  # 45
        break


# 12469 (Уровень: Базовый)  🍒 отрезки
def f(x):
    c = 29 <= x <= 100
    d = 7 <= x <= 68
    a = a1 <= x <= a2
    return not d or c or a

n = [i for k in (7,29,68,100) for i in (k-0.1, k, k+0.1)]
res = 400
for a1 in n:
    for a2 in n:
        if a1 < a2 and all(f(x) for x in n):
            res = min(res, a2 - a1)
print(round(res))  # 22  (21.9)


# 13082 (Уровень: Базовый) 🆗 x и y
def f(x, y):
    return (3 * x + y > 48) or (x > y) or (4 * x + y < a)

for a in range(100, 0, -1):
    if any(not f(x, y) for x in range(1000) for y in range(1000)):  # ❗❗❗найдутся  ❗❗❗any()
        print(a)  # 60
        break


# 17528 Основная волна 07.06.24 (Уровень: Базовый)  🍒 отрезки
def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    return not p or not q or a

res = 1000
# n = [i * 0.25 for i in range(400)]  # перебор дольше по времени
n = [y for x in (15, 21, 40, 63) for y in (x-0.1, x, x+0.1)]  # ✅ критические точки: концы P,Q и сдвиги
for a1 in n:
    for a2 in n:
        if a1 < a2:
            if all(f(x) for x in n):
                res = min(res, a2-a1)
print(res)  # 19


# 17871 Демоверсия 2025 (Уровень: Базовый)  🍒 отрезки
def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    # return p <= ((q and not a) <= (not p))
    return not p or not q or a

res = 100
n = [y for x in (15,21,40,63) for y in (x-0.1, x, x+0.1)]
for a1 in n:
    for a2 in n:
        if a2 > a1 and all(f(x) for x in n):
            res = min(res, a2 - a1)
print(round(res))  # 19



# 19980 (Уровень: Средний)  🍒 отрезки + числа ✅
def f(x):
    p = 52 <= x <= 105
    q = 0 <= x <= 53
    a = a1 <= x <= a2
    return (not p and not q and not a) <= (x**2 > 303601)  # 551**2 == 303601 ✅

res = 1000
n = [i for k in (0,53,52,105,551) for i in (k-0.1, k, k+0.1)][1:]  # убираем отрицательное значение
for a1 in n:
    for a2 in n:
        if a1 < a2 and all(f(x) for x in n):
            res = min(res, a2-a1)
print(round(res))  # 446




# 20905 Апробация 05.03.25 (Уровень: Базовый)  🍒 отрезки
def f(x):
    p = 17 <= x <= 58
    q = 29 <= x <= 80
    a = a1 <= x <= a2
    return not p or not q or a

res = 1000
n = [i for k in (17,58,29,80) for i in (k-0.1, k , k +0.1)]
for a1 in n:
    for a2 in n:
        if a1 < a2 and all(f(x) for x in n):
            res = min(res, a2 - a1)
print(round(res))  # 29


# 21710 ЕГКР 19.04.25 (Уровень: Базовый)  🍒 отрезки
def f(x):
    b = 36 <= x <= 75
    c = 60 <= x <= 110
    a = a1 <= x <= a2
    return (not a) <= (b == c)
    # return a or (b == c)

res = 0
n = [i for k in (36,75,60,110) for i in (k-0.1, k, k+0.1)]
for a1 in n:
    for a2 in n:
        if a2 > a1 and all(f(x) for x in n):
            res = max(res, a2-a1)
print(round(res))  # 74  (74.1999)


# 24988  (Уровень: Базовый)
# короче
def f(x, y):
    a = 100 <= x <= 200
    # b = not x % 121 and (1 < x < 121)
    b = (x == 11)
    c = not y % x and (1 < x < 121)
    return (not c) or (a and (not b))

for y in range(10_000, 20_000):
    if all(f(x, y) for x in range(1, 20_000)) and any(not y % x for x in range(2, y)):  # множество C непустое
        print(y)  # 10201
        break

# Длинно, но понятнее
def d(n):
    r = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n //i}
    return r

def f(x, y):
    a = 100 <= x <= 200
    c = x in d(y)
    b = x == 11 # d(121)  # {11}
    if d(y):  # множество C непустое
        return not c or (not b and a)
    return 0

for y in range(2, 20000):
    if all(f(x, y) for x in range(1, 20000)):
        print(y)  # 10201
        break



# 25279 (Уровень: Базовый)
# kompege/add/15/25279.gif
def f(x, l, r):
    p = 66 <= x <= 67
    q = 32 <= x <= 125
    t = 30 <= x <= 491
    a = l <= x <= r
    return a or p or not q or not t

res = []
for l in range(25, 500):
    for r in range(l, 500):
        if all(f(x, l, r) for x in range(25, 500)):
            res.append((r - l, (l, r)))
res.sort()
print(res[0][0])  # 93  (32, 125)


# 25354 ЕГКР 13.12.25 (Уровень: Средний)
# ❌ Кодом не решается. Только руками !!! ✅
# https://vk.com/video-205865487_456240524?t=47m11s
def f(x, y):
    return (78125 != y + 4*x) or (a > x) and (a > y)
    # return (78125 == y + 4*x) <= ((a > x) and (a > y))

for a in range(78100, 100000):
    for x in range(1, a):
        for y in range(78125 - 4 * x, a):
            if f(x, y):
                print(a)  # 78122
                exit()