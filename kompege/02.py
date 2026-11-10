""" https://kompege.ru/task """

"""
332 2408 2695 5424 5483 5741 5867 6283 6837 6841 6843 6989 6992 7664 9357
12671 13077
23261 23361 27614 27757 28750 28923 29334 29953
31109 31140 31210 31348 31499
"""



# 332 (Уровень: Сложный) 🌶️🌶️🌶️
from itertools import *
def f(x,y,w,z):
    return x or y and (not z) and (not w)

res = set()
t = [(1,0,0,0), (0,0,1,0), (0,1,0,1)]
for p in permutations('xywz', 4):
    if [f(**dict(zip(p, d))) for d in t] == [1,1,0]:
        res.add(p)
print(len(res))  # 4



# 2408 (Уровень: Сложный) 🌶️🌶️🌶️
from itertools import *
def f(c, a, b, w):
    return eval(f'not a {w} (not c and b)')

simbol = ('and', '==', '<=', 'or')
for w in simbol:
    t = [(0, 0, 0, w), (0, 0, 1, w), (0, 1, 0, w), (0, 1, 1, w),
         (1, 0, 0, w), (1, 0, 1, w), (1, 1, 0, w), (1, 1, 1, w)]
    if [f(**dict(zip('cabw', d))) for d in t] == [1,1,0,1,1,1,0,0]:
        print(simbol.index(w) + 1)  # 4


# 2695 Пробный 02.2022 /dev/inf Middle level(Уровень: Сложный) 🌶️🌶️🌶️
from itertools import *
def f(x,y,w,z):
    return (w or y) and (not x or not z) and not w

res = set()
for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(m1,0,m2,0), (1,m3,m4,m5), (1,1,0,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,1]:
                res.add(p)
print(len(res))  # 4


# 5424 Джобс 21.12.22(Уровень: Сложный) 🌶️🌶️🌶️
from itertools import *
def f(p1,p2,p3,p4):
    # return (p3 <= p1) <= (p4 or (not p2))
    return not p1 and p3 or p4 or not p2

for m1,m2,m3,m4 in product((0,1), repeat=4):
    t = [(0,0,m1,1), (0,1,m2,1), (1,1,m3,m4)]
    if len(set(t)) == 3:
        for p in permutations(['p1','p2','p3','p4'], 4):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(*p)  # p3 p1 p4 p2  -->  x  y  z  w  --> ywxz



""" Взято на мой курс """
# 5483 (Уровень: Средний)
from itertools import *
def f(x,y,w,z):
    return (z == (not x)) <= ((w <= (not y)) and (y <= x))

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(1,1,1,0), (m1,m2,0,0), (m3,0,m4,m5)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [1,0,0]:
                print(''.join(p))  # yzxw


#  5741 (Уровень: Сложный) 🌶️🌶️🌶️
from itertools import *
def f(x,y,z, w):
    return (x == (not y)) or eval(f'((not x) {w} z)')

res = set()
oper = ['or', 'and', '==', '<=']
for w in oper:
    for m1,m2,m3,m4,m5,m6 in product((0,1), repeat=6):
        t = [(0,m1,m2,w), (m3,0,m4,w), (m5,m6,1,w)]
        if len(set(t)) == 3:
            for p in permutations('xyz', 3):
                p = [*p] + ['w']
                if [f(**dict(zip(p, d))) for d in t] == [0,1,0]:
                        res.add(oper.index(w) + 1)
print(*sorted(res), sep='')  # 23


# 5867 Danov 2301(Уровень: Средний)
from itertools import *
def f(x,y,w,z):
    return (w == (z <= x)) and y

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(m1,0,m2,0), (1,m3,1,1), (m4,m5,0,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [1,0,1]:
                print(''.join(p))  # ywzx



# 6283 (Уровень: Сложный) 🌶️🌶️
from itertools import *
def f(x,y,w,z):  # похоже, что отсутствующий "y" и дает нужный ответ (без него будет 2)
    return not (not (x <= (not w)) and z) and (not w <=z) and (x <= (not z))

res = set()
for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(1,0,m1,0), (1,0,m2,m3), (m4,1,m5,1)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [1,0,0]:
                res.add(p)
print(len(res))  # 8


""" Взято на мой курс """
# 6837 (Уровень: Средний) 👍
from itertools import *
def f(x1,x2,x3,x4,x5):
    return ((x1 or (not x2) or (not x3) or x4 or (not x5)) and
            ((not x1) or (not x2) or x3 or x4 or x5) and
            (x1 or (not x2) or (not x3) or (not x4) or x5))

for a,b,c,d,e in product((0,1), repeat=5):
    t = [(0,1,1,0,a), (0,1,1,1,0), (0,1,c,d,1), (0,0,0,1,0)]
    if len(set(t)) == 4:
        p = ('x1','x2','x3','x4','x5')
        if [f(**dict(zip(p, k))) for k in t] == [1, b, 0, e]:
            print(a,b,c,d,e, sep='')  # 00101


#  6841 (Уровень: Средний)
from itertools import *
def f(x,y,w,z):
    return w and ((y <= x) <= z)

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(m1,m2,0,1), (0,m3,m4,0), (0,1,m5,1)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,0]:
                print(''.join(p))  # zwyx


#  6843 (Уровень: Средний)
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



""" Взято на мой курс """
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



# 7664 (Уровень: Сложный) 🌶️🌶️🌶️
from itertools import *
def f(c,a,d,b,w):
    return ((a and b) == (not c)) and eval(f'(b {w} d)')

p = ('c','a','d','b','w')
z = ('and', '==', '<=', 'or')
for w in z:
    t = [(1, 0, 0, 0, w), (1, 0, 1, 0, w), (1, 0, 1, 1, w), (1, 1, 0, 0, w)]
    if [f(**dict(zip(p, d))) for d in t] == [1,1,1,1]:
        print(z.index(w) + 1, w)  # 3 <=



""" Взято на мой курс """
# 9357 Джобс 10.06.13_(23) (Уровень: Средний)
from itertools import *
def f1(x,y,w,z):
    return (x <= y) or ((not w) == z)  # В Python приоритет not ниже чем ==

def f2(x,y,w,z):
    return (x <= y) == (w and not z)

for m1, m2, m3, m4, m5, m6 in product((0, 1), repeat=6):
    t = [(m1,m2,m3,0), (m4,m5,0,0), (m6,0,0,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f1(**dict(zip(p, d))) for d in t] == [f2(**dict(zip(p, d))) for d in t]:
                print(''.join(p))  # wyxz



""" Взято на мой курс """
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



""" Взято на мой курс """
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




""" Взято на мой курс """
# 23261 Основная волна 11.06.25 (Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return not (w <= (x == y)) and (z <= x)

for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    t = [(a1, 0, 1, 0), (0, a2, a3, 0), (a4, 1, 1, a5)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, v))) for v in t):
                print(''.join(p))  # yxwz



# 23361 Резервный день 19.06.25 (Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return not (y <= (x == z)) and (w <= x)

for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    t = [(a1, 0, 0, a2), (0, a3, 0, a4), (a5, 1, a6, a7)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if all(f(**dict(zip(p, v))) for v in t):
                print(''.join(p))  # zxwy


# 27614 Апробация 04.03.26(Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    # return (not z and y and x and (not w)) or ((not z) and y and (not x) and (not w)) or (z and y and x and (not w))
    return not w and ((not z and y and x) or ((not z) and y and (not x)) or (z and y and x) )

for m1, m2, m3, m4, m5, m6, m7 in product((0, 1), repeat=7):
    t = [(m1,1,m2,m3), (m4,0,1,m5), (0,m6,0,m7)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,1]:
                print(''.join(p))  # wzxy



# 27757 Апробация 04.03.26(Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return (not x and y and z and (not w)) or (not x and y and( not z) and (not w)) or (x and y and z and (not w))

for m1, m2, m3, m4, m5, m6, m7 in product((0, 1), repeat=7):
    t = [(1,m1,m2,m3), (0,m4,1,m5), (m6,0,0,m7)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,1]:
                print(''.join(p))  # xwzy


# 28750 Досрочная волна 2026(Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    # return not (y <= w) or w==z or (not x)
    return not w and y or w==z or (not x)

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(0,0,1,m1), (m2,1,1,m3), (0,m4,m5,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # ywxz



# 28923 ЕГКР 18.04.26(Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return (not z and x and (not w)) or (not z and x and y)

for m1,m2,m3,m4,m5,m6,m7 in product((0,1), repeat=7):
    t = [(1,m1,m2,m3), (0,m4,1,m5), (m6,m7,0,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,1]:
                print(''.join(p))  # wxyz



# 29334 Открытый вариант 2026(Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    return ((z <= x) <= (x==y)) or (not w)

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(m1,0,1,0,), (0,m2,m3,0), (m4,1,1,m5)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # yxwz


# 29953 Апробация 14.05.26(Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    # return not ((x <= w) <= (w == z)) and y
    return (not x or w) and (w != z) and y

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
    t = [(m1,0,1,0,), (0,m2,m3,0), (m4,1,1,m5)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [1,1,1]:
                print(''.join(p))  # zwyx



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



# 31348 Пересдача 08.07.26(Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    # return (z <= (not (y <= x)))  or w
    return not z or w or (not x and y)

for m1,m2,m3,m4,m5,m6,m7 in product((0,1), repeat=7):
    t = [(m1,1,m2,m3), (m4,m5,0,0), (m6,0,1,m7)]
    if len(set(t)) == 3:
        for p in permutations('xywz', 4):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # zyxw


# 31499 Демоверсия 2027(Уровень: Базовый)
from itertools import *
def f(x,y,w,z):
    # return ((x == (not y)) <= (not(w <= x))) or (not z)
    return not y != x or not x and w or not z

for m1,m2,m3,m4,m5 in product((0,1), repeat=5):
     t = [(m1,0,1,0), (0,m2,m3,0), (m4,1,1,m5)]
     if len(set(t)) == 3:
         for p in permutations('xywz'):
             if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                 print(''.join(p))  # yxzw