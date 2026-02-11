""" https://kompege.ru/task """
"""
7086 7265 7353 7817 8159 8676 9545
1127 11665 12247 12469
24988 25279 25354
"""


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


# 9545 Джобс 14.06.23 (Уровень: Базовый)
def f(x):
    return x % 10 or x % 26 or x < 300 or a <= x

for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 390
        break


# 1127 (Уровень: Базовый)
def f(x):
    return not a % 7 and (240 % x or not a % x or 780 % x)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 420
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


# 12469 (Уровень: Базовый)
from math import ceil
def f(x, a1, a2):
    c = 29 <= x <= 100
    d = 7 <= x <= 68
    a = a1 <= x <= a2
    return not d or c or a

N = [i / 2 for i in range(400)]
res = 400
for a1 in N:
    for a2 in N:
        if a1 < a2:
            if all(f(x, a1, a2) for x in N):
                res = min(res, a2 - a1)
print(ceil(res))  # 22


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
            r |= {i, n // i}
    return r
def f(x, y):
    a = 100 <= x <= 200
    # b = not x % 121 and (1 < x < 121)
    b = (x == 11)
    c = x in d(y)
    return (not c) or (a and (not b))

for y in range(10_000, 20_000):
    if all(f(x, y) for x in range(1, 20_000)) and d(y):  # множество C непустое
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