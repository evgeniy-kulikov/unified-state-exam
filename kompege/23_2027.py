""" https://kompege.ru/task """
"""
31518 31523 31599 32025 32026 32027
"""


# 31518 Демоверсия 2027(Уровень: Базовый)
from math import inf
from functools import lru_cache
d = dict()
for el in open('23_31518.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@lru_cache()
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(t, en) + w for t, w in d[st])
print(f(1, 100))  # 10971

# variant
data = []
for i in open('add/23_2027/23_31518.txt'):
    a, b, w = i.split()
    data.append((int(a), int(b), float(w)))

res = [10**10] * 10_001  # кол-во вершин (по заданию) + 1 (страховка)
res[1] = 0  # 1 это откуда идти (по заданию), путь (вес) из 1 в 1 равен 0
for _ in range(201):  # Кол-во строк(ребер) в файле + 1
    for a, b, w in data:
        res[b] = min(res[b], res[a] + w)
print(int(res[100]))  # 10971


# 31523 (Уровень: Базовый)
from math import inf
from functools import lru_cache
d = dict()
for el in open('23_31523.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@lru_cache()
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(t, en) + w for t, w in d[st])
print(f(3, 97))  # 315

# variant
data = []
for i in open('add/23_2027/23_31523.txt'):
    a, b, w = i.split()
    data.append((int(a), int(b), float(w)))

res = [10**10] * 10_001  # кол-во вершин (по заданию) + 1 (страховка)
res[3] = 0  # 3 это откуда идти (по заданию), путь (вес) из 3 в 3 равен 0
for _ in range(201):  # Кол-во строк(ребер) в файле + 1
    for a, b, w in data:
        res[b] = min(res[b], res[a] + w)
print(int(res[97]))  # 315



# 31599 (Уровень: Базовый)
from math import inf
from functools import lru_cache
d = dict()
for el in open('23_31599.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@lru_cache()
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(b, en) + w for b, w in d[st])

# r = [w for b, w in d[25] if b==50][0]  #  вес ребра из вершины 25 в вершину 50
r = next(w for b, w in d[25] if b==50)  #  вес ребра из вершины 25 в вершину 50
print(int(f(9, 25) + r +  f(50, 92)))  # 852



# 32025 (Уровень: Базовый)
from math import inf
from functools import lru_cache
d = dict()
for el in open('23_32025.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@lru_cache()
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(t, en) + w for t, w in d[st])
print(f(4, 100))  # 12479


# 32026 (Уровень: Базовый)
from math import inf
from functools import lru_cache
d = dict()
for el in open('23_32026.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@lru_cache()
def f(st, en, good=0):
    good += st==400
    if st == en and good:
        return 0
    if not st in d:
        return inf
    return min(f(t, en, good) + w for t, w in d[st])
print(f(4, 298))  # 18711



# 32027 (Уровень: Базовый)
from math import inf
from functools import lru_cache
d = dict()
for el in open('23_32027.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@lru_cache()
def f(st, en, good=0):
    good += st==400
    if st == en and good:
        return 0
    if not st in d or st==96:
        return inf
    return min(f(t, en, good) + w for t, w in d[st])
print(f(4, 298))  # 19255