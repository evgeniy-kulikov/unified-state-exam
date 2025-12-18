""""""
"""
Task 15
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 15.1 Задание 15 | Урок 1 """
# https://stepik.org/lesson/1697214/step/3?unit=1720589
# https://kompege.ru/task   № 762 (Уровень: Базовый)
def f(x):
    return (not (x % a) and not (x % 24) and x % 16) <= x % a

for a in range(1, 100):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 16
        break


# https://stepik.org/lesson/1697214/step/4?unit=1720589
# https://kompege.ru/task   № 432 Джобс 05.10.2020 (Уровень: Средний)
def f(x):
    return (x % 84 or x % 90) <= (x % a)

for a in range(1, 10000):
    if all(f(x) for x in range(10000)):
        print(a)  # 1260
        break


# https://stepik.org/lesson/1697214/step/5?unit=1720589
# https://kompege.ru/task   № 764 (Уровень: Базовый)
def f(x):
    # return (not (not x % 15 and x % 21)) or (x % a or x % 15)
    return x % 15 or not x % 21 or x % a

for a in range(1, 1000):
    if all(f(x) for x in range(1000)):
        print(a)  # 7
        break


# https://stepik.org/lesson/1697214/step/6?unit=1720589
# https://kompege.ru/task   № 948 (Уровень: Базовый)
def f(x):
    return (x%4 !=3 or x%6 != 1) <= (x%36 != a)

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 7
        break


# https://stepik.org/lesson/1697214/step/7?unit=1720589
# https://kompege.ru/task   № 1127 (Уровень: Базовый)
def f(x):  # (a % x != 0) работает,  (a % x) не работает !!!
    return (not a % 7) and ((not 240 % x) <= ((a % x != 0) <= (780 % x)))

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 420
        break


# https://stepik.org/lesson/1697214/step/8?unit=1720589
# https://kompege.ru/task   № 216 Джобс 14.09.2020 (Уровень: Базовый)
def f(x):
    return (x & 26 != 0 or x & 13 != 0) <= ((x & 29 == 0) <= (x & a != 0))

for a in range(1, 100):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 2
        break


# https://stepik.org/lesson/1697214/step/9?unit=1720589
# https://kompege.ru/task   № 2078 (Уровень: Базовый)
def f(x):
    return ((x & 13 != 0 or x & a != 0) <= (x & 13 != 0)) or (x & a != 0 and x & 39 == 0)

for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 13
        break


# https://stepik.org/lesson/1697214/step/10?unit=1720589
# https://kompege.ru/task   № 2079 (Уровень: Базовый)
def f(x):
    return (x & 107 == 0) <= ((x & 55 != 0 ) <= (x & a != 0))

for a in range(1, 100):
    if all(f(x) for x in range(1, 2000)):
        print(a)  # 20
        break


# 👍 https://stepik.org/lesson/1697214/step/11?unit=1720589
# https://kompege.ru/task   № 2081 (Уровень: Средний)
# 8-битная цепочка должна начинаться с '1' (быть без незначащих нулей слева)
p = [i for i in range(256) if f'{i:b}'.zfill(8)[:2] == '11']
q = [*range(0, 256, 2)]
a = []
for x in range(256):
    f = (x in p) or (x not in q)
    if not f:
        a.append(x)
print(len(a))  # 96

# variant
cnt = 0
for x in range(256):
    cnt += not (f'{x:b}'.zfill(8)[:2] == '11' or x % 2)
print(cnt)  # 96


# https://stepik.org/lesson/1697214/step/12?unit=1720589
# https://kompege.ru/task   № 627 Джобс 02.11.2020 (Уровень: Базовый)
def f(x, y):
    return all([x*y > a, x > y, x < 8])

for a in range(1, 100):
    if all(not f(x,y) for x in range(1, 100) for y in range(1, 100)):
        print(a)  # 42
        break





""" 15.2 Задание 15 | Урок 2 """
# https://stepik.org/lesson/1697215/step/1?unit=1720590
# https://kompege.ru/task   № 1015 100 базовых задач Е. Джобс (Уровень: Базовый)
def f(x, y):
    return x > 39 or y > 26 or 2*x + 4*y < a

for a in range(-50,200):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)  # 183
        break


# https://stepik.org/lesson/1697215/step/2?unit=1720590
# https://kompege.ru/task   № 2123 Danov2201 (Уровень: Базовый)
def f(x, y):
    return (2 * x + y) != 70 or x < y or a < x

for a in range(100, 0, -1):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)  # 23
        break


# https://stepik.org/lesson/1697215/step/4?unit=1720590
# https://kompege.ru/task   № 743 (Уровень: Средний)
# not (x in b) or not (x in c) or x in a
# not (x in b and x in c) or x in a
b = {1, 3, 5, 7, 9, 11}
c = {3, 6, 9, 12}
a = b & c
print(sum(a))  # 12


# https://stepik.org/lesson/1697215/step/6?unit=1720590
# https://kompege.ru/task   № 754 (Уровень: Средний)
# (not a or p) and (not a or not q)
# not a or (p and not q)
p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
# p and not q   -->   p - (p & q)   -->   {2, 4, 6, 8, 12, 14, 16, 18}
a = p - (p & q)
print(len(a))  # 8


# https://stepik.org/lesson/1697215/step/7?unit=1720590
# https://kompege.ru/task   № 1409 (Уровень: Средний)
from math import prod
p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
r = {12, 24, 36, 48, 60}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

# a or r or (not p) or (not q)
a = ((p & q) - r)  # {18, 6}
print(prod(a))  # 108


# https://stepik.org/lesson/1697215/step/8?unit=1720590
# /pic/course_233165/001.gif
# https://kompege.ru/task   № 1968 Демоверсия 2022 (Уровень: Средний)
def f(x, l, r):
    d = 17 <= x <= 58
    c = 29 <= x <= 80
    a = l <= x < r
    return not d or c or a

res = 1000
for l in range(100):
    for r in range(l, 100):
        a = [*range(l, r)]
        if all(f(x, l, r) for x in range(1000)):
            res = min(res, len(a))
print(res)


# https://stepik.org/lesson/1697215/step/9?unit=1720590
# /pic/course_233165/002.gif
# https://kompege.ru/task   № 1295 Открытый вариант КЕГЭ (Уровень: Средний)
def f(x, a: list):
    # return (x not in p) or (not ((x in q) and (x not in a)) or (x not in p))
    return x not in p or not (x in q) or x in a

res = 1000
p = [*range(17, 55)]
q = [*range(37, 84)]
for l in range(100):
    for r in range(l, 300):
        a = [*range(l, r)]
        if all(f(x, a) for x in range(300)):
            res = min(len(a) - 1, res)
print(res)


# https://stepik.org/lesson/1697215/step/10?unit=1720590
# /pic/course_233165/003.gif
# https://kompege.ru/task   № 1198 Апробация 27.04 (Уровень: Средний)
def f(x, a: list):
    # return (((x not in b) or (x in a)) and ((x not in c) or (x in a)))
    # return (x in a) or ((x not in b) and (x not in c))
    return (x in a) or (x not in b + c)

res = 1000
b = [*range(18, 53)]
c = [*range(16, 42)]
for l in range(100):
    for r in range(l, 100):
        a = [*range(l, r)]
        if all(f(x, a) for x in range(100)):
            res = min(len(a) - 1, res)
print(res)  # 36



""" 15.3 Задание 15 | Задачи прошлых лет """
# https://stepik.org/lesson/1697216/step/1?unit=1720591
# https://kompege.ru/task   № 9746 Основная волна 19.06.23 (Уровень: Базовый)
def f(x,y):
    return x < a or y < a or (x + 2*y > 50)

for a in range(1000):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)  # 17
        break


# https://stepik.org/lesson/1697216/step/2?unit=1720591
def f(x, y):
    return (x*y < a) or x < y or 9 < x

for a in range(1000):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
        print(a)  # 82
        break


# https://stepik.org/lesson/1697216/step/3?unit=1720591
# https://kompege.ru/task   № 9838 Основная волна 27.06.23 (Уровень: Базовый)
def f(x, y):
    return (x + 2 * y > a) or y < x or x < 30

for a in range(100, 0, -1):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)  # 89
        break


# https://stepik.org/lesson/1697216/step/4?unit=1720591
# /pic/course_233165/004.gif
# https://kompege.ru/task   № 17871 Демоверсия 2025 (Уровень: Базовый)
def f(x, l, r):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = l <= x < r
    # return not p or (not (q and not a) or not p)
    return not p or not q or a

res = 1000
for l in range(80):
    for r in range(l, 100):
        a = [*range(l, r)]
        if all(f(x, l, r) for x in range(300)):
            res = min(res, len(a) - 1)
print(res)  # 19

# variant
# for l in range(80):
#     for r in range(l, 100):
#         a = [i*0.25 for i in range(l*4, r*4)]
#         if all(f(x, l, r) for x in range(300)):
#             res = min(res, int(a[-1] - a[0]))
# print(res)  # 19


# https://stepik.org/lesson/1697216/step/7?unit=1720591
def f(x, y):
    return x*y > a or x > y or 11 > x

for a in range(300, 0, -1):
    if all(f(x, y) for x in range(500) for y in range(500)):
        print(a)  # 120
        break


# https://stepik.org/lesson/1697216/step/10?unit=1720591
# /pic/course_233165/005.gif
# https://kompege.ru/task   № 23755 Демоверсия 2026 (Уровень: Базовый)
def f(x, l, r):
    p = 25 <= x <= 64
    q = 40 <= x <= 115
    a = l <= x < r
    # return not p or (not (q and not a) or not p)
    return a or not q or not p

res = 1000
for l in range(120):
    for r in range(l, 150):
        if all(f(x, l, r) for x in range(200)):
            res = min(res, r - l - 1)
print(res)  # 24





""""""
""" Варианты """
# 29.1 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/3?unit=1753726
# https://kompege.ru/task  № 19247 ЕГКР 21.12.24 (Уровень: Базовый)
def f (x, y):
    return (x - 3*y < a) or (y > 400) or (x > 56)

for a in range(1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)  # 54
        break


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730528/step/3?unit=1754357
# https://kompege.ru/task  № 20809 Апробация 05.03.25 (Уровень: Базовый)
def f(x, b):
    return not x % a or x not in b or x % 22

b = [*range(60, 81)]
for a in range(1000, 0, -1):
    if all(f(x, b) for x in range(1, 1000)):
        print(a)  # 66
        break


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/3?unit=1760676
# https://kompege.ru/task  № 21414 Досрочная волна 2025 (Уровень: Базовый)
def f(x, y):
    return (5<y) or (x>32) or ((x + 2*y) < a)
for a in range(1000):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
        print(a)  # 43
        break


