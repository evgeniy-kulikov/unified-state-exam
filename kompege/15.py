""" https://kompege.ru/task """
"""
307

1127 1276 7086 7265 7353 7817 8159 8676 9370 9545 
11665 12247 12469 17528
21710 24988 25279 25354

  🍒 отрезки
"""




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






# 1127 (Уровень: Базовый)
def f(x):
    return not a % 7 and (240 % x or not a % x or 780 % x)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 420
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


# 9370 Джобс 10.06.23 (Уровень: Сложный)  🍒 отрезки
def f(x):
    p = 5 <= x <= 54
    q = 50 <= x <= 93
    return p or not q or x > a

for a in range(1000):
    if sum(1 for i in range(1000) if not f(i)) == 20:
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