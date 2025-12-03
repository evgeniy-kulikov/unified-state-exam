""""""
"""
Task 27
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""


""" 7.44 ЕГЭ Тренировка 27 """



""" 7.46 ЕГЭ Тренировка 27 (Кластеризация по 2 задания) """
# https://stepik.org/lesson/1696173/step/1?unit=1719529
from math import dist
def centr(d:list):
    res = []
    for i in d:
        res.append((sum(dist(i, k) for k in d), i))
    return min(res)[-1]

with open('add/course_57248/file A.txt') as fl:
    data = list(tuple(map(float, i.replace(',', '.').split())) for i in fl)
    claster = [[], []]
    for i in data:
        if i[1] > 3:
            claster[0].append(i)
        else:
            claster[1].append(i)
res = [centr(i) for i in claster]
x = sum(i[0] for i in res) / 2 * 10_000
y = sum(i[1] for i in res) / 2 * 10_000
print(int(x), int(y))  # 10738 30730


# https://stepik.org/lesson/1696173/step/2?unit=1719529
from math import dist
def centr(ls: list):
    res = []
    for i in ls:
        res.append((sum(dist(i, k) for k in ls), i))
    f = 1
    return min(res)[-1]

with open('add/course_57248/file B.txt') as fl:
    clast = [[], [], []]
    data = [tuple(map(float, f.replace(',', '.').split())) for f in fl]
    for d in data:
        if d[1] > 7:
            clast[0].append(d)
        elif d[1] < 3.5:
            clast[1].append(d)
        else:
            clast[2].append(d)
res = [centr(i) for i in clast]
x = int(sum(i[0] for i in res) / 3 * 10_000)
y = int(sum(i[1] for i in res) / 3 * 10_000)
print(x, y)  # 37522 51277


# https://stepik.org/lesson/1696173/step/3?unit=1719529
from math import dist
def cntr(ls:list):
    res = []
    for i in ls:
        res.append((sum(dist(i, k) for k in ls), i))
    return min(res)[-1]

with open('add/course_57248/27-2a.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]
    clast = [[], []]
    for d in data:
        if d[1] > -1.2:
            clast[0].append(d)
        else:
            clast[1].append(d)
res = [cntr(i) for i in clast]
x = int(sum(i[0] for i in res) / 2 * 10_000)
y = int(sum(i[1] for i in res) / 2 * 10_000)
print(x, y)  # 751 -9101

