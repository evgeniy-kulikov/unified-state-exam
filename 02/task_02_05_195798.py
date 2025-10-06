""""""
"""
Task 02
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""

""" 5.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1219618/step/7?unit=1232947
from itertools import *
def f(x,y,w,z):
    f1 = (x<=y) or ((not w)==z)
    f2 = (x<=y) == ((not z) and w)
    return f1 == f2

for a1,a2,a3,a4,a5,a6 in product((0,1), repeat=6):
    t = [(a1,a2,a3,0), (a4,a5,0,0), (a6,0,0,0)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [1,1,1]:
                print(''.join(p))  # wyxz


# https://stepik.org/lesson/1219618/step/8?unit=1232947
from itertools import *
def f(x,y,w,z):
    f1 = (w==x) and (y<=z)
    f2 = (w<=x) <= (y==z)
    return f1, f2

for a1,a2,a3,a4 in product((0, 1), repeat=4):
    t = [(1,a1,1,1), (a2,1,0,0), (a3,0,0,a4)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [(f(**dict(zip(p, d)))) for d in t] == [(1,0),(1,1),(0,0)]:
                print(''.join(p))  # zywx
# [(1,0),(1,0),(0,0)]  не имеет решений


# https://stepik.org/lesson/1219618/step/9?thread=solutions&unit=1232947
from itertools import *
def f(x,y,w,z):
    f1 = (w<=y) == (x and z)
    f2 = (not x) or (not y) or (not z) or w
    f3 = (z or w) and y and x
    return f1, f2, f3

t = [(1,0,1,0), (0,1,1,1), (1,1,1,0)]
for p in permutations('xywz'):
    if [f(**dict(zip(p, t[0])))[0], f(**dict(zip(p, t[1])))[1], f(**dict(zip(p, t[2])))[2]] == [1,0,1]:
        print(''.join(p))  # wyxz


# https://stepik.org/lesson/1219618/step/10?unit=1232947
from itertools import *
def f(x,y,w,z):
    return (z<=w) and y and (not x)

for a1,a2,a3,a4,a5 in product((0, 1), repeat=5):
    t = [(0,1,a1,0), (a2,0,a3,a4), (0,1,1,a5)]
    for p in permutations('xywz'):
        if [f(**dict(zip(p, d))) for d in t] == [1,1,0]:
            print(''.join(p))


""" 11.4 Закрепление """
# https://stepik.org/lesson/1221460/step/2?unit=1234864
from itertools import product, permutations
def f(x,y,w,z):
    return (x and y) or (y == z) or w

for a1,a2,a3,a4 in product((0,1), repeat=4):
    t = [(a1,1,0,0), (0,a2,1,a3), (0,1,a4,1)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))


""" 12.4 Закрепление """
# https://stepik.org/lesson/1221558/step/2?unit=1234968
from itertools import product, permutations
def f(x,y,w,z):
    return ((not z or w) and (not x == y)) <= (x and z)

for p in permutations('xywz'):
    for a1,a2,a3,a4 in product((0,1), repeat=4):
        t = [(0,0,a1,0),(1,1,1,a2),(1,0,a3,a4)]
        if len(set(t)) == 3:
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))
                print(t)
"""
wzyx
[(0, 0, 1, 0), (1, 1, 1, 0), (1, 0, 0, 1)]

wzyx
[(0, 0, 1, 0), (1, 1, 1, 0), (1, 0, 1, 0)]
"""

""" 14.4 Закрепление """
# Задача повышенной сложности !!!
# https://stepik.org/lesson/1222740/step/2?unit=1236143
from itertools import product, permutations
def fn1(x, y, w, z):
    return (x or not y) <= (w == z)

def fn2(x, y, w, z):
    return (x or not y) == (w <= z)

a, b = set(), set()
for p in permutations('xywz'):
    for a1, a2, a3, a4, f1, f2 in product((0, 1), repeat=6):
        t = [(0, a1, 0, 0, 0, 0), (a2, 1, 1, a3, 0, f2), (a4, 0, 0, 0, f1, 0)]
        if len(set(t)) == 3:
            if [(fn1(**dict(zip(p, d)))) for d in t] == [0, 0, f1]:
                a.add(''.join(p))
            if [(fn2(**dict(zip(p, d)))) for d in t] == [0, f2, 0]:
                b.add(''.join(p))
# print(a)
# print(b)
print(*(a & b))  # ywxz

""" 15.3 Закрепление """
# https://stepik.org/lesson/1223041/step/2?unit=1236528
from itertools import permutations, product
def f(x,y,w,z):
    return (z and y) or ((x <= z) == (y <= w))

for p in permutations('xywz'):
    for a1,a2,a3,a4,a5,a6 in product((0,1), repeat=6):
        t = [(a1,a2,a3,1), (1,a4,a5,1), (1,a6,1,1)]
        if len(set(t)) == 3:
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # wzyx


""" 16.4 Закрепление """
# https://stepik.org/lesson/1223083/step/2?unit=1236572
from itertools import permutations, product
def f(x,y,w,z):
    return (x and not y) or y==z or not w

for p in permutations('xywz'):
    for a1,a2,a3,a4 in product((0,1), repeat=4):
        t = [(0,a1,a2,0), (0,1,0,1), (a3,1,0,a4)]
        if len(set(t)) == 3:
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # xwzy

# https://stepik.org/lesson/1223105/step/2?unit=1236594
from itertools import permutations, product
def f(x,y,w,z):
    return (x and y and not z) == (y or z or not w)

for p in permutations('xywz'):
     for a1,a2,a3,a4,a5 in product((0,1), repeat=5):
         t = [(1,1,a1,1), (a2,0,a3,0), (1,a4,a5,1)]
         if len(set(t)) == 3:
             if [f(**dict(zip(p, d))) for d in t] == [1,1,1]:
                 print(''.join(p))  # wyzx


""" 18.4 Закрепление """
# https://stepik.org/lesson/1224003/step/2?unit=1237500
from itertools import permutations, product
def f(x,y,w,z):
    return (x and not y) or (x==z) or w

for p in permutations('xywz'):
     for a1,a2,a3,a4 in product((0,1), repeat=4):
         t = [(a1,a2,0,1), (1,0,a3,1), (1,1,0,a4)]
         if len(set(t)) == 3:
             if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                 print(''.join(p))  # yxwz




