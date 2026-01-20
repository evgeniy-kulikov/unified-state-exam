""""""
"""
Task 27
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 27.1 Задание 27 ЕГЭ | Урок 1 """
# https://stepik.org/lesson/1729157/step/2?unit=1752979
# https://kompege.ru/task   № 17916 (Уровень: Базовый)
from math import dist
def cntr(cl: list):
    res = []
    for i in cl:
        res.append((sum(dist(i, k) for k in cl), i))
    return min(res)[1]

A = open('add/course_233165/27-1_01_A.txt').readlines()
a = [[], []]
for i in A[1:]:
    d = tuple(map(float, i.replace(',', '.').split()))
    if d[1] < 8:
        a[0].append(d)
    else:
        a[1].append(d)
c_a = [cntr(i) for i in a]
Px_a = sum(x for x, y in c_a) / 2 * 10**4
Py_a = sum(y for x, y in c_a) / 2 * 10**4
print(int(Px_a), int(Py_a))  # 119766 83062

B = open('add/course_233165/27-1_01_B.txt').readlines()
b = [[], [], [], [], []]
for i in B[1:]:
    d = tuple(map(float, i.replace(',', '.').split()))
    if d[1] < 5 and d[0] < 7:
        b[0].append(d)
    elif 5 < d[1] < 8:
        b[1].append(d)
    elif 9 < d[1] < 13:
        b[2].append(d)
    elif d[1] > 13:
        b[3].append(d)
    else:
        b[4].append(d)
c_b = [cntr(i) for i in b]
Px_b = sum(x for x, y in c_b) / 5 * 10**4
Py_b = sum(y for x, y in c_b) / 5 * 10**4
print(int(Px_b), int(Py_b))  # 90275 74960
"""
119766 83062
90275 74960
"""



# https://stepik.org/lesson/1729157/step/3?unit=1752979
# https://kompege.ru/task   № 18051 (Уровень: Средний)
from math import dist
def cntr(ls):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return min(res)[1]

A = open('add/course_233165/27-1_02_A.txt').readlines()
a = [[], []]
for d in A[1:]:
    d = list(map(float, d.replace(',', '.').split()))
    x, y = d
    if y > 6.1 and x < 1.1:
        a[0].append(d)
    else:
        a[1].append(d)
c_a = [cntr(i) for i in a]
p_x = sum(x for x, y in c_a) / 2 * 10**4
p_y = sum(y for x, y in c_a) / 2 * 10**4
print(int(p_x), int(p_y))  # 10410 66711

with open('add/course_233165/27-1_02_B.txt') as file:
    B = file.readlines()
    b = [[], [], []]
    for d in B[1:]:
        d = list(map(float, d.replace(',', '.').split()))
        y, x = d
        if x > 0.7 and y < 8.1:
            b[0].append(d)
            pass
        elif (x > 0.3 and y > 8.6) or ((0 <= x <= 0.3) and (y > 9.1)):
            b[1].append(d)
        else:
            b[2].append(d)
c_b = [cntr(i) for i in b]
p_x = sum(x for x, y in c_b) / 3 * 10**4
p_y = sum(y for x, y in c_b) / 3 * 10**4
print(int(p_x), int(p_y))  # 81775 7384
"""
10410 66711
81775 7384
"""


# https://stepik.org/lesson/1729157/step/5?unit=1752979
# https://kompege.ru/task   № 18314 (Уровень: Базовый)
from math import dist
def cntr(ls):
    c = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        c.append([sm, i])
    return min(c)[1]

A = open('add/course_233165/27-1_05_A.txt').readlines()
a = [[], []]
for d in A[1:]:
    d = [*map(float, d.replace(',', '.').split())]
    x, y = d
    if x > 23.5:
        a[0].append(d)
    else:
        a[1].append(d)
res = [cntr(i) for i in a]
p_x = sum(x for x, y in res) / 2 * 10**4
p_y = sum(y for x, y in res) / 2 * 10**4
print(int(p_x), int(p_y))  # 231302 6353

B = open('add/course_233165/27-1_05_B.txt').readlines()
b = [[], [], []]
for d in B[1:]:
    d = [*map(float, d.replace(',', '.').split())]
    x, y = d
    if x < -10:
        b[0].append(d)
    elif x > 19:
        b[1].append(d)
    else:
        b[2].append(d)
res = [cntr(i) for i in b]
p_x = sum(x for x, y in res) / 3 * 10**4
p_y = sum(y for x, y in res) / 3 * 10**4
print(int(p_x), int(p_y))  # 30788 -47589
"""
231302 6353
30788 -47589
"""


# https://stepik.org/lesson/1729157/step/6?unit=1752979
# https://kompege.ru/task  № 18624 (Уровень: Средний)
from math import dist
A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_06_A.txt').readlines()[1:]]
B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_06_B.txt').readlines()[1:]]
# data = A[:]
data = B[:]
print(len(data))

def getCluster(p: tuple):
    # Последовательный сбор всех точек кластера из data по условию if dist(i, p) < 1 (0,7 ... 2)
    # из data собранные точки удаляются. Возвращается список собранных точек кластера.
    cluster = [i for i in data if dist(i, p) < 1.2]
    if cluster:
        for i in cluster:
            data.remove(i)
        next_cluster = [getCluster(i) for i in cluster]
        for c in next_cluster:
            cluster.extend(c)
    return cluster

clusters = []  # Список списков кластеров
while data:
    p = data.pop()
    cluster = [p] + getCluster(p)  # Список очередного кластера
    print(len(cluster))
    clusters.append(cluster)
# print(len(A), '=', sum(len(i) for i in clusters))

def center(cl: list):
    res = []
    for p in cl:
        d = sum(dist(i, p) for i in cl)
        res.append((d, p))
    return min(res)[1]

point = [center(i) for i in clusters]
px = sum(i[0] for i in point) / len(point) * 100000
py = sum(i[1] for i in point) / len(point) * 100000
print(int(px), int(py))
"""
455058 449904
366751 398174
"""


# https://stepik.org/lesson/1729157/step/7?unit=1752979
# https://kompege.ru/task  № 18628 (Уровень: Средний)
from math import dist
A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_07_A.txt').readlines()[1:]]
B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_07_B.txt').readlines()[1:]]
data = A[:]
# data = B[:]
print(len(data))

def getCluster(p: tuple):
    # Последовательный сбор всех точек кластера из data по условию if dist(i, p) < 1 (0,7 ... 2)
    # из data собранные точки удаляются. Возвращается список собранных точек кластера.
    cluster = [i for i in data if dist(i, p) < 1]
    if cluster:
        for i in cluster:
            data.remove(i)
        next_cluster = [getCluster(i) for i in cluster]
        for c in next_cluster:
            cluster.extend(c)
    return cluster

clusters = []  # Список списков кластеров
while data:
    p = data.pop()
    cluster = [p] + getCluster(p)  # Список очередного кластера
    print(len(cluster))
    clusters.append(cluster)
# print(len(A), '=', sum(len(i) for i in clusters))

def center(cl: list):
    res = []
    for p in cl:
        d = sum(dist(i, p) for i in cl)
        res.append((d, p))
    return min(res)[1]

point = [center(i) for i in clusters]
px = sum(i[0] for i in point) / len(point) * 100000
py = sum(i[1] for i in point) / len(point) * 100000
print(int(px), int(py))
"""
258853 499656
6165 372336
"""




# https://stepik.org/lesson/1729157/step/8?unit=1752979
# https://kompege.ru/task  № 18676 (Уровень: Средний)
from math import dist
A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_08_A.txt').readlines()]
B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_08_B.txt').readlines()]
data = A[:]
# data = B[:]
print(len(data))  # проверка 1

def getCluster(p: tuple):
    cluster = [i for i in data if dist(i, p) < 1.2]
    if cluster:
        for i in cluster:
            data.remove(i)
        next_cluster = [getCluster(i) for i in cluster]
        for c in next_cluster:
            cluster.extend(c)
    return cluster

clusters = []
while data:
    p = data.pop()
    cluster = [p] + getCluster(p)
    print(len(cluster))  # проверка 2
    clusters.append(cluster)

def center(cl: list):
    res = []
    for p in cl:
        d = sum(dist(i, p) for i in cl)
        res.append((d, p))
    return min(res)[1]

point = [center(i) for i in clusters]
px = sum(i[0] for i in point) / len(point) * 100000
py = sum(i[1] for i in point) / len(point) * 100000
print(int(px), int(py))
"""
566258 38951
591893 290926
"""


# https://stepik.org/lesson/1729157/step/09?unit=1752979
# https://kompege.ru/task  № 18056 (Уровень: Сложный)
# Ответ не принимается 🤔
from math import dist
A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_09_A.txt').readlines()[1:]]
B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_09_B_2.txt').readlines()[1:]]
# data = A[:]
data = B[:]
# print(len(data))  # проверка 1

def getCluster(p):
    clast = [i for i in data if dist(i, p) < 1]
    for i in clast:
        data.remove(i)
    new_clast = [getCluster(i) for i in clast]
    for i in new_clast:
        clast.extend(i)
    return clast

clusters = []
while data:
    p = data.pop()
    cluster = [p] + getCluster(p)
    # print(len(cluster))  # проверка 2
    clusters.append(cluster)

# print(len(B), '=', sum(len(i) for i in clusters))   # проверка 3

def center(cl: list):
    res = []
    for p in cl:
        d = sum(dist(i, p) for i in cl)
        res.append((d, p))
    return min(res)[1]

point = [center(i) for i in clusters if len(i) > 10]
px = sum(i[0] for i in point) / len(point) * 100000
py = sum(i[1] for i in point) / len(point) * 100000
print(int(abs(px)), int(abs(py)))
"""
43744 47901
108874 7612 🤔
"""




# https://stepik.org/lesson/1729157/step/10?unit=1752979
# https://kompege.ru/task  № 18625 (Уровень: Сложный)
from math import dist
A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_10_A.txt').readlines()[1:]]
B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_10_B.txt').readlines()[1:]]
# data = A[:]
data = B[:]
print(len(data))  # проверка 1

def getCluster(p):
    clast = [i for i in data if dist(i, p) < 1]
    for i in clast:
        data.remove(i)
    new_clast = [getCluster(i) for i in clast]
    for i in new_clast:
        clast.extend(i)
    return clast

clusters = []
while data:
    p = data.pop()
    cluster = [p] + getCluster(p)
    # print(len(cluster))  # проверка 2
    clusters.append(cluster)

# print(len(B), '=', sum(len(i) for i in clusters))   # проверка 3

def center(cl: list):
    res = []
    for p in cl:
        d = sum(dist(i, p) for i in cl)
        res.append((d, p))
    return min(res)[1]

point = [center(i) for i in clusters if len(i) > 10]
px = sum(i[0] for i in point) / len(point) * 100000
py = sum(i[1] for i in point) / len(point) * 100000
print(int(abs(px)), int(abs(py)))
"""
515933 498987
471077 409201
"""



# https://stepik.org/lesson/1729157/step/11?unit=1752979
# https://kompege.ru/task  № 18677 (Уровень: Сложный)
from math import dist
A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_11_A.txt').readlines()]
B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_11_B.txt').readlines()]
# data = A[:]
data = B[:]
# print(len(data))  # проверка 1

def getCluster(p):
    clast = [i for i in data if dist(i, p) < 1]
    for i in clast:
        data.remove(i)
    new_clast = [getCluster(i) for i in clast]
    for i in new_clast:
        clast.extend(i)
    return clast

clusters = []
while data:
    p = data.pop()
    cluster = [p] + getCluster(p)
    # print(len(cluster))  # проверка 2
    clusters.append(cluster)

# print(len(B), '=', sum(len(i) for i in clusters))   # проверка 3

def center(cl: list):
    res = []
    for p in cl:
        d = sum(dist(i, p) for i in cl)
        res.append((d, p))
    return min(res)[1]

point = [center(i) for i in clusters if len(i) > 10]
px = sum(i[0] for i in point) / len(point) * 100000
py = sum(i[1] for i in point) / len(point) * 100000
print(int(abs(px)), int(abs(py)))
"""
528073 71781
669946 370701
"""



