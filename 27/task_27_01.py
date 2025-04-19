""""""
"""
Task 27
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

# https://stepik.org/lesson/1670113/step/2?unit=1693135
with open('demo_2025_27_A1.txt') as fl:
    data = list(tuple(map(float, el.replace(',', '.').split())) for el in fl)

cluster = [s for s in data if all([-2 <= s[0] <= 1, 0 <= s[1] <= 3])]
cnt = len(cluster)
srX = sum(s[0] for s in cluster) / cnt
srY = sum(s[1] for s in cluster) / cnt
print(cnt, srX, srY)


# https://stepik.org/lesson/1670113/step/3?unit=1693135
with open('demo_2025_27_A1.txt') as fl:
    data = list(tuple(map(float, el.replace(',', '.').split())) for el in fl)

cluster = [s for s in data if all([1 <= s[0] <= 5, 3 <= s[1] <= 7])]
cnt = len(cluster)
srX = sum(s[0] for s in cluster) / cnt
srY = sum(s[1] for s in cluster) / cnt
print(cnt, srX, srY)


# https://stepik.org/lesson/1670113/step/4?unit=1693135
with open('demo_2025_27_A1.txt') as fl:
    data = list(tuple(map(float, el.replace(',', '.').split())) for el in fl)
cluster = [s for s in data if all([1 <= s[0] <= 5, 3 <= s[1] <= 7])]
x = min(s[0] for s in cluster)
y = max(s[1] for s in cluster)
print(x, y)


# https://stepik.org/lesson/1670113/step/5?unit=1693135
with open('demo_2025_27_A1.txt') as fl:
    data = list(tuple(map(float, el.replace(',', '.').split())) for el in fl)
cluster = [s for s in data if all([1 <= s[0] <= 5, 3 <= s[1] <= 7])]
ls_x = sorted(s[0] for s in cluster)
ls_y = sorted(s[1] for s in cluster)
x = abs(ls_x[0] - ls_x[-1])
y = abs(ls_y[0] - ls_y[-1])
print(x, y)


# https://stepik.org/lesson/1670113/step/6?unit=1693135
with open('demo_2025_27_A1.txt') as fl:
    data = list(tuple(map(float, el.replace(',', '.').split())) for el in fl)
cluster = [s for s in data if all([-2 <= s[0] <= 1, 0 <= s[1] <= 3])]
res = [(k[0]**2 + k[1]**2)**0.5 for k in cluster]
print(max(res))


# https://stepik.org/lesson/1670113/step/7?unit=1693135
# пример 2: Найдите сумму расстояний от звезд кластера до центра координатной плоскости
from math import dist
with open('demo_2025_27_A1.txt') as fl:
    data = list(tuple(map(float, el.replace(',', '.').split())) for el in fl)
cluster = [s for s in data if all([-2 <= s[0] <= 1, 0 <= s[1] <= 3])]
res = 0
for z in cluster:
    res += dist((0, 0), z)
print(res)


# https://stepik.org/lesson/1670113/step/7?unit=1693135
# пример 3: Найдите центроид кластера - ту звезду, сумма расстояний от которой до всех звезд кластера минимальна
from math import dist
import sys

with open('demo_2025_27_A1.txt') as fl:
    data = list(tuple(map(float, el.replace(',', '.').split())) for el in fl)
cluster = [s for s in data if all([-2 <= s[0] <= 1, 0 <= s[1] <= 3])]
min_n = sys.maxsize
for z1 in cluster:
    s = 0
    for z2 in cluster:
        s += dist(z1, z2) # сумма всех расстояниц от z1 до остальных звезд
    if s < min_n:
        min_n = s
        center = z1  # координаты текущего центроида
print(center[0], center[1])


# https://stepik.org/lesson/1670113/step/8?unit=1693135
from math import dist
from sys import maxsize

with open('demo_2025_27_A1.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]
claster = [el for el in data if 1 <= el[0] <= 5 and 3 <= el[1] <= 7]
min_n = maxsize
center = None
for z1 in claster:
    sm = 0
    for z2 in claster:
        sm += dist(z1, z2)
    if sm < min_n:
        min_n = sm
        center = z1
print(center[0], center[1])


# https://stepik.org/lesson/1670113/step/9?unit=1693135
from math import dist
from sys import maxsize

with open('demo_2025_27_A1.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]

claster = [el for el in data if -2 <= el[0] <= 1 and 0 <= el[1] <= 3]
min_n = maxsize
center = None
for z1 in claster:
    sm = 0
    for z2 in claster:
        sm += dist(z1, z2)
    if sm < min_n:
        min_n = sm
        center = z1
print(int(center[0] * 1000), int(center[1] * 1000))


# https://stepik.org/lesson/1670113/step/10?unit=1693135
from math import dist
from sys import maxsize

with open('demo_2025_27_A1.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]

claster_1 = [el for el in data if -2 <= el[0] <= 1 and 0 <= el[1] <= 3]
claster_2 = [el for el in data if 1 <= el[0] <= 5 and 3 <= el[1] <= 7]
min_n1 = min_n2 = maxsize
center_1 = center_2 = None

for z1 in claster_1:
    sm_1 = 0
    for z2 in claster_1:
        sm_1 += dist(z1, z2)
    if sm_1 < min_n1:
        min_n1 = sm_1
        center_1 = z1

for z1 in claster_2:
    sm_2 = 0
    for z2 in claster_2:
        sm_2 += dist(z1, z2)
    if sm_2 < min_n2:
        min_n2 = sm_2
        center_2 = z1

print(int((center_1[0] + center_2[0]) / 2 * 10000), int((center_1[1] + center_2[1]) / 2 * 10000))


# https://stepik.org/lesson/1670114/step/2?unit=1693136
from math import dist
from sys import maxsize

with open('27-1a.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]

# смещение x +1.5, смещение y +1.0
claster_1 = [el for el in data if 1.5 <= el[0] <= 4.5 and 1 <= el[1] <= 4]
claster_2 = [el for el in data if -1.5 <= el[0] <= 1.5 and -2 <= el[1] <= 1]
min_n1 = min_n2 = maxsize
center_1 = center_2 = None

for z1 in claster_1:
    sm_1 = 0
    for z2 in claster_1:
        sm_1 += dist(z1, z2)
    if sm_1 < min_n1:
        min_n1 = sm_1
        center_1 = z1

for z1 in claster_2:
    sm_2 = 0
    for z2 in claster_2:
        sm_2 += dist(z1, z2)
    if sm_2 < min_n2:
        min_n2 = sm_2
        center_2 = z1
print(int((center_1[0] + center_2[0]) / 2 * 10000), int((center_1[1] + center_2[1]) / 2 * 10000))


# https://stepik.org/lesson/1670114/step/3?unit=1693136
# УЛУЧШЕННЫЙ ВАРИАНТ
from math import dist

def centroid(claster):
    res = []
    for i in claster:
        res.append((sum(dist(i, j) for j in claster), i))
    return min(res)[1]

with open('27-1b.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]
    clasters = [[] for _ in range(3)]
    for i in data:
        if i[0] < 0:
            clasters[0].append(i)
        elif i[0] > 0 and i[1] > 3.5:
            clasters[1].append(i)
        else:
            clasters[2].append(i)

res = [centroid(i) for i in clasters]
cx = int(sum(i[0] for i in res) / 3 * 10_000)
cy = int(sum(i[1] for i in res) / 3 * 10_000)
print(cx, cy)


# https://stepik.org/lesson/1670114/step/4?unit=1693136
from math import dist

def centroid(claster):
    res = []
    for i in claster:
        res.append((sum(dist(i, j) for j in claster), i))
    return min(res)[1]

with open('27-2a.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]
    clasters = [[] for _ in range(2)]
    for i in data:
        if i[1] > -1.5:
            clasters[0].append(i)
        else:
            clasters[1].append(i)

res = [centroid(i) for i in clasters]
cx = int(sum(i[0] for i in res) / 2 * 10_000)
cy = int(sum(i[1] for i in res) / 2 * 10_000)
print(cx, cy)


# https://stepik.org/lesson/1670114/step/5?unit=1693136
from math import dist

def centroid(cl):
    res = []
    for i in cl:
        res.append((sum(dist(i, j) for j in cl), i))
    return min(res)[1]

with open('27-2b.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]
    clasters = [[] for _ in range(3)]
    for i in data:
        if i[1] > -0.5:
            clasters[0].append(i)
        elif i[1] < -0.5 and i[0] < 4:
            clasters[1].append(i)
        else:
            clasters[2].append(i)

res = [centroid(i) for i in clasters]
cx = int(sum(i[0] for i in res) / 3 * 10_000)
cy = int(sum(i[1] for i in res) / 3 * 10_000)
print(cx, cy)
# 36881 -14309


# https://stepik.org/lesson/1670114/step/6?unit=1693136
from math import dist

def centroid(cl):
    res = []
    for i in cl:
        res.append((sum(dist(i, j) for j in cl), i))
    return min(res)[1]

with open('27-10a.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]
    clasters = [[] for _ in range(2)]
    for i in data:
        if i[0] < 1:
            clasters[0].append(i)
        else:
            clasters[1].append(i)

res = [centroid(i) for i in clasters]
cx = int(sum(i[0] for i in res) / 2 * 10_000)
cy = int(sum(i[1] for i in res) / 2 * 10_000)
print(cx, cy)
# 8734 76647


# https://stepik.org/lesson/1670114/step/7?unit=1693136
from math import dist

def centroid(cl):
    res = []
    for i in cl:
        res.append((sum(dist(i, j) for j in cl), i))
    return min(res)[1]

with open('27-10b.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]
    clasters = [[] for _ in range(3)]
    for i in data:
        if i[1] > 0.5:
            clasters[0].append(i)
        elif i[0] > 2:
            clasters[1].append(i)
        else:
            clasters[2].append(i)

res = [centroid(i) for i in clasters]
cx = int(sum(i[0] for i in res) / 3 * 10_000)
cy = int(sum(i[1] for i in res) / 3 * 10_000)
print(cx, cy)
# 7881 -5340

