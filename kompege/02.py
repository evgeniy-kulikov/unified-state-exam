""" https://kompege.ru/task """

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
