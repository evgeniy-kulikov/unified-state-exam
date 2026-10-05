""" https://kompege.ru/task """
"""
31518 31523 31583 31587 31598 31599 31600 31609 31618 31619 31620 31627 31635 31644 31650 31651 31663 31673 32025 32026 32027
"""


# 31518 Демоверсия 2027(Уровень: Базовый)
from math import inf
from functools import lru_cache
d = dict()
for el in open('23_31518.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@lru_cache(None)  # @lru_cache() передается maxsize=128 и далее таблица начинает затираться. @lru_cache(None) сделает кэш бесконечным
# @cache == @lru_cache(None)   начиная с Python 3.9
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


# 31583 (Уровень: Базовый)
from math import inf
from functools import cache
d = dict()
for row in open('20_31583.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en, c=0):
    c += st in(25, 50)
    if st == en and c == 2:
        return 0
    if not st in d:
        return inf
    return min(f(b, en, c) + w for b, w in d[st])
print(int(f(12, 88)))  # 1193
# variant без именного аргумента c=0 ✔️
# @cache
# def f(st, en):
#     if st == en:
#         return 0
#     if not st in d:
#         return inf
#     return min(f(b, en) + w for b, w in d[st])
# print(int(f(12, 25) + f(25, 50) + f(50, 88)))  # 1193 ✔️



# 31587 (Уровень: Базовый)
from math import inf
from functools import cache
d = dict()
for row in open('23_31587.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en, c=0):
    c += st==25
    if st == en and not c:
        return 0
    if not st in d:
        return inf
    return min(f(b, en, c) + w for b, w in d[st])
print(int(f(19, 83)))  # 420



# 31598 (Уровень: Базовый)
from math import inf
from functools import cache
d = dict()
for row in open('23_31598.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(b, en) + w for b, w in d[st])
r = next(w for b, w in d[25] if b == 50)
print(f(3, 25) + r + f(50, 97))  # 815



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


# 31600 (Уровень: Базовый)
from math import inf
from functools import cache
d = dict()
for row in open('23_31600.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(b, en) + w for b, w in d[st])
r = next(w for b, w in d[25] if b == 50)
print(f(17, 25) + r + f(50, 86))  # 810


# 31609 (Уровень: Базовый)
from math import inf
from functools import cache
d = dict()
for row in open('23_31609.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(b, en) + w for b, w in d[st])
print(f(170, 461))  # 14228


# 31618 (Уровень: Базовый)
from math import inf
from functools import cache
d = dict()
for row in open('23_31618.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return -inf
    return max(f(b, en) + w for b, w in d[st])
print(f(1, 100))  # 242730


# 31619 (Уровень: Базовый)
from math import inf
from functools import cache
d = dict()
for row in open('23_31619.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en, c=0):
    c += st == 180
    if st == en and c:
        return 0
    if not st in d:
        return inf
    return min(f(b, en, c) + w for b, w in d[st])
print(f(113, 316))  # 14067



# 31620 (Уровень: Базовый)
from math import inf
from functools import cache
d = dict()
for row in open('23_31620.txt'):
    a, b, w = map(float, row.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@cache
def f(st, en, c=0):
    c += st == 96
    if st == en and not c:
        return 0
    if not st in d:
        return inf
    return min(f(b, en, c) + w for b, w in d[st])
print(f(173, 238))  # 10585



# 31627 (Уровень: Базовый) ✔️✔️✔️
"""
Найдите целую часть длины кратчайшего пути из вершины с номером 173 в вершину с номером 523, 
проходящего через обе вершины с номерами 91 и 474 
и не проходящего по ребру из вершины с номером 474 в вершину с номером 523. 
"""
from math import inf
from functools import cache
d = dict()
for el in open('23_31627.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    if a==474 and b==523:
        continue  # Не добавляем запрещенное ребро из 474 в 523
    d[a].append((b, w))

@cache
def f(st, en, good=0):
    good += st in (91, 474)  # путь проходит через обе вершины с номерами 91 и 474
    if all([st==en, good==2]):
        return 0
    if not st in d:
        return inf
    return min(f(b, en, good) + w for b, w in d[st])
    # одной строчкой
    # return min([f(b, en, good) + w for b, w in d.get(st, [])], default=inf)
print(int(f(173, 523)))  # 21535



# 31635 (Уровень: Базовый)
from math import inf
from functools import cache
d = dict()
for el in open('23_31635.txt'):
    a, b, _ = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b))

@cache
def f(st, en):
    if st == en:
        return 1
    return sum(f(b, en) for b in d.get(st, []))
print(f(1, 238) * f(316, 100))  # 1156629792



# 31644 (Уровень: Средний)
from functools import cache
d = dict()
for el in open('23_31644.txt'):
    a, b, _ = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b))

@cache
def f(st, cnt, en=100):  # cnt - заданное кол-во ребер из вершины 1 в вершину 100
    if not cnt:
        return 1 if st == en else 0
    if not st in d:
        return 0
    return sum(f(b, cnt - 1) for b in d[st])  # sum - кол-во путей при нужном кол-во ребер из вершины 1 в вершину 100

# variant d.get(st, []) ✅ если ключа нет, то подставляется пустой список и из-за этого не будет итераций
# @lru_cache(None)
# @cache
# def f(st, cnt, en=100):
#     if not cnt:
#         return 1 if st == en else 0
#     return sum(f(b, cnt - 1) for b in d.get(st, []))
res = 0
for i in range(1, 11):
    res += f(1, i)
print(res)  # 137956


# 31650 (Уровень: Базовый)
from math import inf
from functools import lru_cache, cache
d = dict()
for el in open('23_31651.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

# @lru_cache(None)
@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return max(f(b, en) + 1 for b, w in d[st])

for i in range(1, 100):
    if f(1, 100) == i:
        print(i)  # 49
        break


# 31651 (Уровень: Базовый)
from math import inf
from functools import lru_cache, cache
d = dict()
for el in open('23_31651.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

# @lru_cache(None)
@cache
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(b, en) + 1 for b, w in d[st])

for i in range(1, 10):
    if f(1, 100) == i:
        print(i)  # 5
        break


# 31663 (Уровень: Базовый)
from functools import lru_cache, cache
d = dict()
for el in open('23_31663.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

# @cache
@lru_cache(None)
def f(st):
    if not st in d:
        return 0
    return max(f(b) + w for b, w in d[st])
print(int(f(2027)))  # 6030


# 31673 (Уровень: Базовый)
from math import inf
from functools import lru_cache
d = dict()
for el in open('23_31673.txt'):
    a, b, w = map(float, el.split())
    d.setdefault(a, [])
    d[a].append((b, w))

@lru_cache(None)
def f(st, en):
    if st == en:
        return 0
    if not st in d:
        return inf
    return min(f(b, en) + w for b, w in d[st])

r1 = next(w for b, w in d[2691] if b==2840)  #  вес ребра из вершины 2961 в вершину 2840
r2 = next(w for b, w in d[9180] if b==9514)  #  вес ребра из вершины 9180 в вершину 9514
print(int(r1 +  f(2840, 9180) + r2))  # 285



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