""""""
"""
Task 27
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""


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