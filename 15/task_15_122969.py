""""""
"""
Task 15
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""

# https://stepik.org/lesson/1038706/step/2?unit=1062774
def f(x):
    # return (x&103 == 0 and x&94 != 0) <= (x&a != 0)
    return x & 103 or not x & 94 or x & a

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 24
        break


# https://stepik.org/lesson/1038706/step/3?unit=1062774
# course_122968/pic_01
def f(x):
    p = 13 <= x <= 19
    q = 17 <= x <= 23
    a = a1 <= x <= a2
    # return (not ((not p) <= q)) <= (a <= ((not q) <= p))
    return not a or q or p

d = [i * 0.5 for i in range(100)]
MX = 0
for a1 in d:
    for a2 in d:
        if all(f(x) for x in d):
            MX = max(MX, a2 - a1)
print(int(MX))  # 10


# https://stepik.org/lesson/1038706/step/4?unit=1062774
def f(x, y):
    return(x+y <= 30) or (y <= x+2) or (y >= a)

for a in range(1000, 0, -1):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
        print(a)  # 17
        break


# https://stepik.org/lesson/1038706/step/5?unit=1062774
def f(x, y):
    # return any([(not (108 % x)) <= x % y, x + y > 80, a - y > x])
    return any([108 % x, x % y, x + y > 80, a - y > x])

for a in range(1, 100):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)  # 73
        break


# https://stepik.org/lesson/1038706/step/7?unit=1062774
def f(x):
    return (x & 52 and not(x & 36)) <= x & a

for a in range(1, 100):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 16
        break


# https://stepik.org/lesson/1038706/step/8?unit=1062774
from math import ceil
def f(x):
    p = 10 <= x <= 45
    q = 35 <= x <= 78
    a = a1 <= x <= a2
    # return (not p) <= q and (not a)
    return (p or q) and not a

d = [i*0.5 for i in range(1, 500)]
MN = 10**6
for a1 in d:
    for a2 in d:
        if all(not f(x) for x in d):
            MN = min(MN, a2 - a1)
print(ceil(MN))  # 68

# ищем все f(x) а не not f(x)
from math import ceil
def f(x):
    p = 10 <= x <= 45
    q = 35 <= x <= 78
    a = a1 <= x <= a2
    return not p and not q or a

d = [i*0.5 for i in range(1, 500)]
MN = 10**5
for a1 in d:
    for a2 in d:
        if all(f(x) for x in d):
            MN = min(MN, a2 - a1)
print(ceil(MN))  # 68


# https://stepik.org/lesson/1038706/step/9?unit=1062774
def f(x, y):
    return (x+y <= 32) or (y <= x+4) or y >= a

MX = 0
for a in range(100):
    if all(f(x,y) for x in range(1000) for y in range(1000)):
        MX = max(MX, a)
print(MX)  # 19


# https://stepik.org/lesson/1038706/step/9?unit=1062774
def f(x):
    b = 70 <= x <= 90
    return (not x % a) or (b <= x % 22 )

MX = 0
for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        MX = max(MX, a)
print(MX)  # 88


# https://stepik.org/lesson/1038706/step/12?unit=1062774
def f(x):
    # return (x & 39 == 0) or ((x & 11 == 0) <= (not (x & a == 0)))
    return not x & 39 or x & 11 or x & a

for a in range(1000):
    if all(f(x) for x in range(1000)):
        print(a)
        break


# https://stepik.org/lesson/1038706/step/13?unit=1062774
from math import ceil
def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    # return p <= ((q and not a) <= (not p))
    # return not p or (not (q and (not a)) or (not p))
    return not p or not q or a

MN = 1000
d = [k * 0.3 for k in range(300)]
for a1 in d:
    for a2 in d:
        if all(f(x) for x in d):
            MN = min(MN, a2 - a1)
print(ceil(MN))  # 19


# https://stepik.org/lesson/1038706/step/14?unit=1062774
def f(x, y):
    return (a > y) or (3*x + 2*y > 53) or (a > x)

for a in range(1, 1000):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)  # 11
        break


# https://stepik.org/lesson/1038706/step/15?unit=1062774
def f(x):
    return x % 3 or x % 5 or x + a >= 90

for a in range(1, 100):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 75
        break


""" 3.2 Практика: 15 номер. """
# https://stepik.org/lesson/1228673/step/2?unit=1242206
def f(x):
    return x % 33 or not x % a or x % 242

for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 726
        break


# https://stepik.org/lesson/1228673/step/3?unit=1242206
# При каком наибольшем целом A
# найдутся !!!  такие целые неотрицательные x и y, что выражение будет ложным?
def f(x, y):
    return (3*x + y > 48) or (x > y) or (4*x + y < a)

for a in range(100, 0, -1):
    if any(not f(x, y) for x in range(1, 500) for y in range(1, 500)):
        print(a)  # 60
        break
