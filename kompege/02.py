""" https://kompege.ru/task """

"""
6843 6989 6992 9357
12671 13077
23261 23361 
31109 31140 31210 
"""



# 6843 (Уровень: Средний)  # (Уровень: Базовый)
from itertools import *
def f1(x,y,w,z):
    return (not z or w) and y and not x

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(0,1,m1,0), (m2,0,m3,m4), (0,1,1,m5)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f1(**dict(zip(p, d))) for d in t] == [1, 1, 0]:
                print(''.join(p))  # zwyx


# 6989 (Уровень: Средний)
from itertools import *
def f1(x,y,z):
    return not x or y and z

t = [(0,1,0), (1,1,0)]
for p in permutations('xyz'):
    if [f1(**dict(zip(p, d))) for d in t] == [0, 0]:
        print(''.join(p))  # 2 (yxz, zxy)


# 6992 (Уровень: Средний)
from itertools import *
def f1(x,y,w,z):
    return (w <= y) == (x and z)

def f2(x,y,w,z):
    return not x or not y or not z or w

def f3(x,y,w,z):
    return (z or w) and y and x

t = [(1,0,1,0), (0,1,1,1), (1,1,1,0)]
for p in permutations('xywz'):
    if [f1(**dict(zip(p, t[0]))), f2(**dict(zip(p, t[1]))), f3(**dict(zip(p, t[2])))] == [1, 0, 1]:
        print(''.join(p))  # wyxz


# 9357 Джобс 10.06.23 (Уровень: Средний)
from itertools import *
def f1(x,y,w,z):
    return (x <= y) or (not w == z)

def f2(x,y,w,z):
    return (x <= y) == (w and not z)

for m1, m2, m3, m4, m5, m6 in product((0, 1), repeat=6):
    t = [(m1,m2,m3,0), (m4,m5,0,0), (m6,0,0,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f1(**dict(zip(p, d))) for d in t] == [f2(**dict(zip(p, d))) for d in t]:
                print(''.join(p))  # wyxz




# 12671 (Уровень: Средний)
from itertools import *
def f(x,y,w,z):
    # return not (x == w and not z) and (y == x and not w)  # алгебра логики ❗❗❗
    return not (x == (w and not z)) and (y == (x and not w))  # приоритеты операторов python ✔️

for m1, m2, m3, m4, m5, m6 in product((0, 1), repeat=6):
    t = [(m1,m2,0,m3), (m4,0,m5,0), (0,m6,1,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [1, 1, 1]:
                print(''.join(p))  # wxyz


# 13077 (Уровень: Средний)
from itertools import *
def f1(x,y,w,z):
    return (w == x) and (y <= z)

def f2(x,y,w,z):
    return (w <= x) <= (y == z)

for m1, m2, m3, m4 in product((0, 1), repeat=4):
    t = [(1, m1, 1, 1), (m2, 1, 0, 0), (m3, 0, 0, m4)]
    if len(set(t)) == 3:
        for n in (0,1 ):
            for p in permutations('xywz'):
                if [f1(**dict(zip(p, d))) for d in t] == [1, 1, 0] \
                        and [f2(**dict(zip(p, d))) for d in t] == [0, n, 0]:  # n = 1
                    print(''.join(p))  # zywx





# № 23261 Основная волна 11.06.25 (Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return not (w <= (x == y)) and (z <= x)

for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    t = [(a1, 0, 1, 0), (0, a2, a3, 0), (a4, 1, 1, a5)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, v))) for v in t):
                print(''.join(p))  # yxwz


# № 23361 Резервный день 19.06.25 (Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return not (y <= (x == z)) and (w <= x)

for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    t = [(a1, 0, 0, a2), (0, a3, 0, a4), (a5, 1, a6, a7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, v))) for v in t):
                print(''.join(p))  # zxwy





# 31109 Основная волна 18.06.26 (Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return ((w == (not x)) <= (not (z <= w))) or not y

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(m1,0,1,0), (0,m2,m3,0), (m4,1,1,m5)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # xwyz


# 31140 Основная волна 19.06.26 (Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    # return not (z <= x) or (y <= w) or not y
    return z and not x or not y or w

for m1,m2,m3,m4,m5,m6,m7 in product((0,1), repeat=7):
    t = [(0,1,m1,m2), (m3,0,m4,m5), (1,m6,0,m7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # zxwy


# 31210 Резерв 22.06.26 (Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return ((y <= w) <= x) or not z

for m1,m2,m3,m4,m5,m6,m7 in product((0,1), repeat=7):
    t = [(m1,m2,0,0), (m3,1,m4,m5), (m6,0,1,m7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # zywx

