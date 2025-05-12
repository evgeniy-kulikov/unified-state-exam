""""""
"""
Task 15
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 18.1 Задачи на делимость """

# https://stepik.org/lesson/559882/step/3?unit=553927
for a in range(1, 1000):
    for x in range(1, 1000):
        f = (not x % a) <= ((x % 24) + (not x % 32))
        if not f:
            break
    if f:
        print(a)  # 32
        break


# https://stepik.org/lesson/559882/step/6?unit=553927
for a in range(1, 1000):
    for x in range(1, 1000):
        f = ((not x % 35) or (not x % 49)) <= (not x % a)
        if not f:
            break
    if f:
        max_a = a
print(max_a)  #


# https://stepik.org/lesson/559882/step/7?unit=553927
def fn(x):
    return ((not x % a) and (x % 12 != 0)) <= (not x % 29)

for a in range(1, 100):
    if all(fn(x) for x in range(1, 1000)):
        print(a)  # 12
        break


""" 18.1 Задачи на делимость """

# https://stepik.org/lesson/559882/step/12?unit=553927
def fn(x):
    return ((not x % 35) or (not x % 49)) <= (not x % a)

for a in range(1, 100):
    if all(fn(x) for x in range(1, 1000)):
        max_a = a
print(max_a)  # 7


""" 18.2 Задачи на неравенства """

# https://stepik.org/lesson/559881/step/2?unit=553926
def fn(x, y):
    return (x * y > a) or (x > y) or (8 > x)

for a in range(1, 1000):
    if all(fn(x, y) for x in range(1, 100) for y in range(1, 1000)):
        max_a = a
print(max_a)  # 63


# https://stepik.org/lesson/559881/step/7?unit=553926
def fn(x, y):
    return (x + 5 * y > 50) or ((y - x) > a) or ((y - 3 * x) < -30)

for a in range(-100, 100):  # наибольшего целого числа А
    if all(fn(x, y) for x in range(1, 100) for y in range(1, 100)):
        max_a = a
print(max_a)  # -10


# https://stepik.org/lesson/559881/step/8?unit=553926
def fn(x, y):
    return ((y - x**2) != 40) or (a < (5*x - 55)) or (a < (y**2 + 4))

for a in range(1500, 2000):
    if all(fn(x, y) for x in range(1, 100) for y in range(1, 100)):
        max_a = a
print(max_a)  # 1684


""" 18.3 Задачи на побитовое умножение """

# https://stepik.org/lesson/559883/step/2?unit=553928
def fn(x):
    return not x & 39 or x & 41 or x & a
    # return (not (x & 39)) or ((not (x & 41)) <= (x & a != 0))

for a in range(100):
    if all(fn(x) for x in range(1, 100)):
        print(a)
        break


# https://stepik.org/lesson/559883/step/9?unit=553928
def fn(x):
    return not x & 39 or (not x & 41) <= x & a

for a in range(100):
    if all(fn(x) for x in range(1, 100)):
        print(a)
        break


""" 18.4 Задачи на множества """

# https://stepik.org/lesson/734492/step/3?unit=736056
def fn(x):
    return not x in p or x in q or x in a

p = {1, 2, 3, 4, 5, 6, 7}
q = {2, 4, 6, 8, 10}
a = set()  # найти минимально возможное множество 'a'

for x in range(1 , 100):
    if not fn(x):
        a.add(x)
# print(a)  # {1, 3, 5, 7}
print(sum(a))  # 16


# https://stepik.org/lesson/734492/step/4?unit=736056
from math import prod
def fn(x):
    return not x in p or x in q or x in a

p = {3, 4, 5, 6, 7}
q = {4, 6, 8, 10, 12}
a = set()  # найти минимально возможное множество 'a'

for x in range(1 , 100):
    if not fn(x):
        a.add(x)
print(a)  # {3, 5, 7}
print(prod(a))  # 105  (значение произведения элементов)


# https://stepik.org/lesson/734492/step/8?unit=736056
def fn(x):
    # return ((x in a) <= (x in p)) and ((x in q) <= (not x in a))
    # return (not x in a or x in p) and ((not x in q) or ( not x in a))
    return (not x in a or x in p) and not (x in q and x in a)

p = { 2, 6, 10, 14, 18, 22, 26, 30}
q = {5, 10, 15, 20, 25, 30}
a = set(i for i in range(1 , 1000))  # найти наибольшее возможное множество 'a'

for x in range(1 , 1000):
    if not fn(x):
        a.remove(x)
print(a)  # {2, 6, 14, 18, 22, 26}
print(len(a))  # 6


# https://stepik.org/lesson/734492/step/5?unit=736056
def fn(x):
    return (not x in p or x in q) or x in a

p = {1, 3, 5, 7, 9, 11, 13}
q = {3, 6, 9, 12}
a = set()

for x in range(1, 100):
    if not fn(x):
        a.add(x)
# print(a)  # {1, 5, 7, 11, 13}
print(sum(a))  # 37


# https://stepik.org/lesson/734492/step/9?unit=736056
def fn(x):
    return not x in a or x in p or x in q

p = {3, 6, 9, 12, 15}
q = {5, 10, 15, 20, 25}
a = set(i for i in range(1, 100))

for x in range(1, 100):
    if not fn(x):
        a.remove(x)
# print(a)  # {3, 5, 6, 9, 10, 12, 15, 20, 25}
print(sum(a))  # 105


""" 18.5 Задачи на отрезки. Программирование """

# https://stepik.org/lesson/1034588/step/2?unit=1042959
# 15/pic/course_100138/18-5_02.gif
def fn(x):
    return not(a1<=x<=a2) or 10<=x<=30 or 23<=x<=53

a = 0
res = []
for a1 in range(100):
    for a2 in range(a1 + 1, 100):
        if all(fn(x) for x in range(100)) and (a2 - a1) > a:  # длина проверяемого отрезка больше, чем текущее значение A
            a = a2 - a1  # Длина отрезка A на числовой прямой: разность между правым и левым концом отрезка A
            res.append((a, a1, a2))
res.sort()
print(res[-1])  # (43, 10, 53)


# https://stepik.org/lesson/1034588/step/3?unit=1042959
# 15/pic/course_100138/18-5_03.gif

# https://stepik.org/lesson/1034588/step/4?unit=1042959
# 15/pic/course_100138/18-5_04.gif

# https://stepik.org/lesson/1034588/step/5?unit=1042959
# 15/pic/course_100138/18-5_05.gif

# https://stepik.org/lesson/1034588/step/7?unit=1042959
# 15/pic/course_100138/18-5_07.gif

# https://stepik.org/lesson/1034588/step/8?unit=1042959
# 15/pic/course_100138/18-5_08.gif

# https://stepik.org/lesson/1034588/step/9?unit=1042959
# 15/pic/course_100138/18-5_09.gif

# https://stepik.org/lesson/1034588/step/10?unit=1042959
# 15/pic/course_100138/18-5_10.gif


# https://stepik.org/lesson/1034588/step/11?unit=1042959
# 15/pic/course_100138/18-5_11.gif
b = [i for i in range(70, 91)]
def fn(x):
    # return x % a == 0 or ((x in b) <= (x % 22 != 0))
    return (not x % a) or (not x in b) or x % 22

for a in range(1000, 0, -1):
    if all(fn(x) for x in range(1, 1000)):
        print(a)  # 88
        break

# https://stepik.org/lesson/1035783/step/6?unit=1044178
# 15/pic/course_100138/18-6_05.gif

# https://stepik.org/lesson/1035783/step/6?unit=1044178
# 15/pic/course_100138/18-6_06.gif

# https://stepik.org/lesson/1035783/step/7?unit=1044178
# 15/pic/course_100138/18-6_07.gif

# https://stepik.org/lesson/1035783/step/8?unit=1044178
# 15/pic/course_100138/18-6_08.gif

# https://stepik.org/lesson/1035783/step/10?unit=1044178
# 15/pic/course_100138/18-6_10.gif

# https://stepik.org/lesson/1035783/step/11?unit=1044178
# 15/pic/course_100138/18-6_11.gif

# https://stepik.org/lesson/1035783/step/13?unit=1044178
# 15/pic/course_100138/18-6_13.gif

# https://stepik.org/lesson/1035783/step/14?unit=1044178
# 15/pic/course_100138/18-6_14.gif

