"""
😉
🙂
🤔
👍
🌶
"""
""""""
# ЕГЭ Информатика 2026 | Полный Курс
# https://stepik.org/course/233165
# variant
""" Варианты """
# variant  (high speed)
# variant  (slow speed)



# https://stepik.org/lesson/1729157/step/9?unit=1752979
# https://kompege.ru/task  № 186788888
from math import dist
A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_09_A.txt').readlines()[1:]]
B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27-1_09_B.txt').readlines()[1:]]
data = A[:]
# data = B[:]
print(len(data))  # проверка 1

def getCluster(p: tuple):
    cluster = [i for i in data if dist(i, p) < 1]
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

print(len(B), '=', sum(len(i) for i in clusters))   # проверка 3

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
108874 7612
"""