""""""
"""
Task 15
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 20.2 Практика (ур. базовый) """

# https://stepik.org/lesson/1226261/step/1?unit=1239748
def f(x, y):
    return (x + 2*y < a) or (y > x) or (x > 60)

for a in range(1000):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)  # 181
        break


# https://stepik.org/lesson/1226261/step/2?unit=1239748
def f(x, y):
    return (x + 2*y > a) or (y < x) or (x < 30)

for a in range(100, -1, -1):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)  # 89
        break


# https://stepik.org/lesson/1226261/step/3?unit=1239748
def f(x):
    return ((x & 103 == 0) and (x & 94 != 0)) <= (x & a != 0)

for a in range(1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 24
        break


# https://stepik.org/lesson/1226261/step/4?unit=1239748
def f(x):
    return (not x % 17) <= ((x not in b) or (a < x + 30))

b = list(range(80, 101))
for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 114
        break


# https://stepik.org/lesson/1226261/step/5?unit=1239748
def f(x):
    # return ((x & 500 != 0) and (x & 200 == 0)) <= (not (x & b == 0))
    return ((x & 500 != 0) and (not x & 200)) <= (x & b != 0)

for b in range(1000):
    if all(f(x) for x in range(1, 1000)):
        print(b)  # 308
        break


# https://stepik.org/lesson/1226261/step/6?unit=1239748
def f(x):
    # return ((x & 52 != 0) and (x & 36 == 0)) <= (not (x & a == 0))
    return (x & 52 and not (x & 36)) <= (x & a)

for a in range(1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 16
        break


# https://stepik.org/lesson/1226261/step/7?unit=1239748
def f(x):
    return ((not x % 13) <= (x not in b)) or (a < x + 20)

b = [*range(40, 61)]
for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 71
        break


# https://stepik.org/lesson/1226261/step/8?unit=1239748
def f(x):
    return ((x & 17 != 0) <= ((x & a != 0 ) <= (x & 58 != 0))) <= \
        ((x & 8 == 0) and (x & a != 0) and (x & 58 == 0))

b = [*range(40, 61)]
for a in range(1, 1000):
    if all(not f(x) for x in range(1, 1000)):
        print(a)  # 2
        break


# https://stepik.org/lesson/1226261/step/9?unit=1239748
def f(x, y):
    return (x + 2*y != 58) or ((a - x > 0) == (a + y > 0))

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)  # 57
        break


# https://stepik.org/lesson/1226261/step/10?unit=1239748
def f(x, y):
    return any([x**2 - 10*x + 16 > 0, y**2 - 10*y + 21 > 0, x*y < 2*a])

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)  # 29
        break


# https://stepik.org/lesson/1226261/step/11?unit=1239748
def f(x, y):
    return any([3*x+y>48, x>y, 4*x+y<a])

for a in range(1000, -1, -1):
    if any(not f(x, y) for x in range(100) for y in range(100)):
        print(a)  # 60
        break
# https://stepik.org/lesson/1226261/step/12?unit=1239748
def f(x):
    # return any([x & a == 0, not (x & 37 == 0), not (x & 12 == 0)])
    return any([not (x & a), x & 37, x & 12])

for a in range(100, 0, -1):
    if all(f(x) for x in range(10000)):
        print(a)  # 45
        break


# https://stepik.org/lesson/1226261/step/13?unit=1239748
def f(x, y):
    return any([x**2 + y**2 > 1024 - x, y < -2*x + a])

for a in range(100):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)  # 71
        break

# https://stepik.org/lesson/1226261/step/14?unit=1239748
def f(x):
    return all([a + x > 700 - a, a % 100 + 100 % x > 50])


for a in range(1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)  # 351
        break


# https://stepik.org/lesson/1226261/step/15?unit=1239748
def f(x):
    return any([(x in b) <= (x % 7 != 0), a > 2*x])

b = [*range(120, 131)]
for a in range(1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)  # 253
        break



""" 20.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1226262/step/1?unit=1239749
def f(x,y,z):
    return any([x|50 == x, y&34 != 0, z|24 != 24, x*y*z > a // 8])

for a in range(70, 0, -1):
    if all(f(x,y,z) for x in range(1, 300)
           for y in range(1, 300)
           for z in range(1, 300)):
        print(a)  # 63
        break


# https://stepik.org/lesson/1226262/step/2?unit=1239749
from math import gcd
def f(x):
    return any([(gcd(x, 42) != 1) <= (gcd(x, 7) == 1), (x + a) >= 25])

for a in range(1, 100):
    if all(f(x) for x in range(1, 1000)):
        print(a)  # 18
        break


# https://stepik.org/lesson/1226262/step/3?unit=1239749
def f(x, y, z):
    return any([y + 2*x + 2*z != 150, a < x, a < y, a < z])

for a in range(50, 0, -1):
    if all(f(x, y, z) for x in range(1, 200)
           for y in range(1, 200)
           for z in range(1, 200)):
        print(a)  # 29
        break






""" 20.4 Закрепление """
# https://stepik.org/lesson/1226263/step/15?unit=1239750
def f(x, y):
    return any([x*y < a, y > x, x >= 8])

for a in range(100):
    if all(f(x, y) for x in range(1, 500)
           for y in range(1, 500)):
        print(a)  # 50
        break


""" 23.5 Закрепление (ч. 2) """
# ОТРЕЗКИ
# https://stepik.org/lesson/1227732/step/5?unit=1241247
# pic/course_195798/001.gif
for x in [_ * 0.5 for _ in range(0, 250)]:
    p = 69 <= x <= 91
    q = 77 <= x <= 114
    f = not p or not q or p != q
    if not f:
        print(x)  # 91 - 77 = 14


""" 24.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1227747/step/5?unit=1241268
def f(x):
    return (x&a != 0) <= ((x&36 == 0) <= (x&6 != 0))

for a in range(1000, 0, -1):
    if all(f(x) for x in range(10000)):
        print(a)  # 38
        break
