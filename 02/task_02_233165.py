""""""
"""
Task 02
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 2.1 Задание 2 | Урок 1 """
# https://stepik.org/lesson/1650982/step/3?unit=1673684
from itertools import *
def f(x,y,w,z):
    return ((w <= y) <= x) or (not z)

for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    t = [(a1, a2, 1, a3), (a4, 0, a5, a6), (a7, 1, 0, 0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # zywx


# https://stepik.org/lesson/1650982/step/4?unit=1673684
from itertools import *
def f(x,y,w,z):
    return not (x <= w) or (y <= z) or not y

for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    t = [(a1, 1, a2, 0), (a3, 0, 1, a4), (a5, a6, 0, a7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # yxwz


# https://stepik.org/lesson/1650982/step/5?unit=1673684
from itertools import permutations
def f(x,y,z):
    return (not z) and x or x and y

t = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]
for p in permutations('xyz'):
    if [f(**dict(zip(p, d))) for d in t] == [0, 1, 0, 1, 0, 0, 0, 1]:
        print(''.join(p))  # zyx


# https://stepik.org/lesson/1650982/step/6?unit=1673684
# Особенность приоритета Питона и Алгебры
from itertools import *
def f(x,y,w,z):
    # return (not ((x==w) and (not z))) and ((y == x) and (not w))
    return not(x == (w and not z)) and (y == (x and not w))

for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    t = [(a1, a2, 0, a3), (a4, 0, a5, 0), (0, a6, 1, 0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,1]:
                print(''.join(p))  # wxyz


# https://stepik.org/lesson/1650982/step/7?unit=1673684
# https://kompege.ru/task   № 8547 (Уровень: Базовый)
from itertools import *
def f(a, b, c, t):
    return (not a or not b) and (c <= (not a)) and (t and not a or c and not b)

for p in permutations('abct'):
    t = [(1,0,0,1), (1,1,0,1), (0,0,0,1), (1,0,0,0)]
    if [f(**dict(zip(p, d))) for d in t] == [0,1,0,1]:
        print(''.join(p))  # ctab


# https://stepik.org/lesson/1650982/step/8?unit=1673684
# https://kompege.ru/task   № 659 Джобс 09.11.2020 (Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return ((z <= x) and (x <= w)) or (y == (z or x))

for a1, a2, a3, a4, a5, a6, a7 in product((0,1), repeat=7):
    t = [(a1,1,a2,a3), (a4,a5,1,1), (a6,1,a7,1)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # yxwz


# https://stepik.org/lesson/1650982/step/9?unit=1673684
# https://kompege.ru/task   № 6255 Danov2302 (Уровень: Базовый)
from itertools import *
def f(w, x, y, z):
    return w or (y <= z) and x

for a1, a2, a3, a4, a5, a6 in product((0,1), repeat=6):
    t = [(a1, a2, 0, 0), (1, 1, a3, a4), (1, a4, a5, 1)]
    if len(set(t)) == 3:
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, d))) for d in t] == [1, 0, 0]:
                print(''.join(p))  # yxwz


# https://stepik.org/lesson/1650982/step/10?unit=1673684
# https://kompege.ru/task   № ***
from itertools import *
def f(w, x, y, z):
    return (x or (not y)) and (not (y == z)) and w

for a1, a2, a3, a4 in product((0,1), repeat=4):
    t = [(0,1,a1,0), (a2,1,1,0), (1,a3,3,a4)]
    if len(set(t)) == 3:
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, d))) for d in t] == [1, 1, 1]:
                print(''.join(p))  # xwzy


# https://stepik.org/lesson/1650982/step/12?unit=1673684
from itertools import *
def f(x,y,w,z):
    # return (x <= y and not z) or w
    return (x <= (y and not z)) or w

for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    t = [(a1, a2, 1, 0), (0, a3, a4, 1), (1, a5, 1, a6)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # ywxz


                

""" 2.2 Задание 2 | Урок 2 """
# https://stepik.org/lesson/1650983/step/1?unit=1673685
from itertools import *
def f(x,y,w,z):
    return (x and not y) or (x==z) or w

for a1, a2, a3, a4, a5, a6 in product((0, 1), repeat=6):
    t = [(1, a1, a2, 1), (a3, 0, a4, 0), (1, a5, 1, a6)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # ywzx


# https://stepik.org/lesson/1650983/step/4?unit=1673685
# https://kompege.ru/task   № 816 Джобс 14.12.2020 (Уровень: Средний)
# Порядок выполнения операций в алгебре логики !!!
from itertools import *
def f(x,y,z):
    # return not (x == (y <= z))
    return x != (not y or z)

t = [(0,0,1), (0,1,1)]
for p in permutations('xyz'):
    if [f(**dict(zip(p, d))) for d in t] == [1,0]:
        print(''.join(p))  # yxz


# https://stepik.org/lesson/1650983/step/5?unit=1673685
# https://kompege.ru/task   № 1185 Апробация 27.04 (Уровень: Базовый)
# 6 ответов!!!
from itertools import *
def f(x,y,w,z):
    return (y <= x) or not ((x <= z) and (z <= x)) and (not w)

res = set()
for a1,a2,a3,a4,a5,a6 in product((0,1), repeat=6):
    t = [(0,0,0,a1), (a2,0,0,a3), (a4,a5,0,a6)]
    if len(t) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0, 0, 0]:
                # print(''.join(p))  # wzxy
                res.add(''.join(p))
[print(i) for i in res]
"""
xzwy
xwzy
wzxy
wxzy
zxwy
zwxy
"""


# https://stepik.org/lesson/1650983/step/6?unit=1673685
# https://kompege.ru/task   № 1267 Алексеев А. (Уровень: Базовый)
# 2 ответа!!!
from itertools import *
def f(x,y,w,z):
    return ((w <= y) or (not (y <= z))) and (not x) and (not ( x == z))

for a1,a2,a3,a4 in product((0,1), repeat=4):
    t = [(0, a1, 1, 1), (1, a2, a3, 1), (0, a4, 1, 1)]
    if len(t) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [1, 1, 1]:
                print(''.join(p))  # wxzy
"""
wxyz
wxzy
"""



""" 2.3 Задание 2 | Задачи прошлых лет """
# https://stepik.org/lesson/1650984/step/1?unit=1673686
# https://kompege.ru/task   № ***
# 2 ответа!!!
from itertools import *
def f(x,y,w,z):
    return (x and (not y)) or (x == z) or w

for a1,a2,a3,a4 in product((0,1), repeat=4):
    t = [(a1,a2,0,1), (1,0,a3,1), (1,1,0,a4)]
    if len(t) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # yxwz
"""
yxwz
yzwx
"""
