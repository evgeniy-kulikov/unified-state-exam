""""""
"""
https://kompege.ru/task
Анализ данных
"""

"""
18031 18150 19257 20294 20911
21425 21599 21911 21929 21930 21931 21932 23384 23766
25441 25442 25443 25444 25445 25446 25447 25448 27780 28776 29081 29357
"""

"""
✔️ course 233165
17882 17916 
18051 18314 18624 18625 18628 18676 18677 
20816 21720 23209 23284 23571 
"""





# 18031 (Уровень: Базовый)  ✅  нестандартная задача
from math import dist
def get_cluster(p):
    clust = [i for i in data_in if dist(p, i) < 1]
    [data_in.remove(i) for i in clust]
    next_clust = [get_cluster(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_min(a: list, b: list):  # ✅  нестандартная функция
    res = []
    for i in a:
        ls = [[dist(i, k), i, k] for k in b]
        ls.sort()
        res.append(ls[0])
    res.sort()
    return res[0]


for w in 'AB':
    f = open(f'27{w}.txt')
    data_in = [[*map(float, i.replace(',', '.').split())] for i in f]
    # print(len(data_in))
    clusters = []
    while data_in:
        p = data_in.pop()
        clusters.append(get_cluster(p) + [p])
    # [print(len(i)) for i in clusters]
    # print(sum(len(i) for i in clusters), '\n')
    min_clust = []
    n = len(clusters)
    for i in range(n):
        for k in range(i + 1, n):
            a, b = clusters[i], clusters[k]
            min_clust += [get_min(a, b)]
    min_clust.sort()
    a, b = min_clust[0][1], min_clust[0][2]
    sx = int((a[0] + b[0]) * 1000)
    sy = int((a[1] + b[1]) * 1000)
    print(sx, sy)

"""
1731 6256
18166 26588
"""



# 18150 (Уровень: Базовый)
from math import dist
def centr(ls: list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return min(res)[1]

f = open(f'add/27/18150_27_A.txt')
data = [[*map(float, i.replace(',', '.').split())] for i in f]
clust = [[], []]
for i in data:
    if i[0] > 0:
        clust[0].append(i)
    else:
        clust[1].append(i)
c = [centr(i) for i in clust]
px = int(sum(i[0] for i in c) / 2 * 1000)
py = int(sum(i[1] for i in c) / 2 * 1000)
print(abs(px), abs(py)) # 336 1859

f = open(f'add/27/18150_27_B.txt')
data = [[*map(float, i.replace(',', '.').split())] for i in f]
clust = [[], [], []]
for i in data:
    if i[0] < 0:
        clust[0].append(i)
    elif i[1] > 4:
        clust[1].append(i)
    else:
        clust[2].append(i)
c = [centr(i) for i in clust]
px = int(sum(i[0] for i in c) / 3 * 1000)
py = int(sum(i[1] for i in c) / 3 * 1000)
print(abs(px), abs(py)) # 2467 1343
"""
336 1859
2467 1343
"""


# 19257 ЕГКР 21.12.24 (Уровень: Базовый)
from math import dist
def get_clust(p, k):
    clust = [i for i in data if dist(i, p) < k]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i, k) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_center(ls):
    r = []
    for p in ls:
        sm = sum(dist(p,k) for k in ls)
        r += [(sm, p)]
    return min(r)[1]

for w, k in zip('AB', (3, 1)):
    data = [[*map(float, i.replace(',', '.').split())] for i in open(f'27_{w}.txt').readlines()]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clust = get_clust(p, k) + [p]
        clusters.append(clust)
    # [print(len(i)) for i in clusters]
    # print(sum(len(i) for i in clusters), '\n')
    center = [get_center(i) for i in clusters]
    px = int(abs((sum(i[0] for i in center) / len(center)) * 10_000))
    py = int(abs((sum(i[1] for i in center) / len(center)) * 10_000))
    print(px, py)
"""
43789 62202
14271 54727
"""




# 20294 (Уровень: Базовый)
from math import dist
def centr(ls:list):
    res = []
    for i in ls:
        ln = len([k for k in ls if dist(i, k) <= 1])
        res.append((ln, i[1], i))
    return min(res, key=lambda x: (x[0], -x[1]))[2]

def get_clust(p, k):
    clust = [i for i in data if dist(p, i) <= k]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i, k) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for i, k in zip('AB', (1, 0.4)):
    f = open(f'add/27/20294_27_{i}.txt')
    data = [[*map(float, i.replace(',', '.').split())] for i in f]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clust = [p] + get_clust(p, k)
        # print(len(clust))
        clusters.append(clust)
    # print(sum(len(i) for i in clusters), '\n')
    res = [centr(i) for i in clusters]
    Px = sum(i[0] for i in res) / len(res) * 100000
    Py = sum(i[1] for i in res) / len(res) * 100000
    print(int(Px), abs(int(Py)))
"""
135491 131265
232818 15126
"""






# 21425 Досрочная волна 2025 (Уровень: Базовый)
from math import dist
def centr(ls: list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return min(res)[1]

def get_clust(p):
    clust = [i for i in data if dist(i, p) < 3]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for s in 'AB':
    f = open(f'add/27/21425_27_{s}.txt').readlines()
    data = [[*map(float, i.replace(',', '.').split())] for i in f]
    cluster = []
    while data:
        p = data.pop()
        clust = [p] + get_clust(p)
        cluster += [clust]
    target = [centr(i) for i in cluster]
    px = int((sum(i[0] for i in target) / len(target)) * 10_000)
    py = int((sum(i[1] for i in target) / len(target)) * 10_000)
    print(px, py)
"""
167990 73043
122627 29105
"""



#  20911 Апробация 05.03.25 (Уровень: Базовый)
from math import dist
def get_cluster(p):
    clust = [i for i in data_in if dist(p, i) < 2]
    [data_in.remove(i) for i in clust]
    next_clust = [get_cluster(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_center(a: list):
    res = []
    for i in a:
        sm = sum(dist(i, k) for k in a)
        res.append([sm, i])
    return min(res)[1]

for w in 'AB':
    f = open(f'27{w}.txt')
    data_in = [[*map(float, i.replace(',', '.').split())] for i in f]
    # print(len(data_in))
    clusters = []
    while data_in:
        p = data_in.pop()
        clusters.append(get_cluster(p) + [p])
    # [print(len(i)) for i in clusters]
    # print(sum(len(i) for i in clusters), '\n')
    center = [get_center(i) for i in clusters]
    px = int(abs(sum(i[0] for i in center) / len(center)) * 10_000)
    py = int(abs(sum(i[1] for i in center) / len(center)) * 10_000)
    print(px, py)
"""
28603 10294
61260 11206
"""





# 21599 (Уровень: Средний)
# ✅ кластеры собираем вручную (без функции) через построение прямолинейного графика
from math import dist
def centr(ls: list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return min(res)[1]

f = open(f'add/27/21599_27_A.txt').readlines()
data = [[*map(float, i.replace(',', '.').split())] for i in f]
clust = [[], [], []]
for i in data:  # 0
    x, y = i
    k0 = 5 / 11
    # b0 = y - k0 * x = -5
    if y - k0 * x > -5:
        clust[0].append(i)
[data.remove((i)) for i in clust[0]]
for i in data:  # 2
    x, y = i
    if y < -7:
        clust[2].append(i)
[data.remove((i)) for i in clust[2]]
for i in data:  # 1
    clust[1].append(i)
cntr = [centr(i) for i in clust]
px = int(abs(sum(i[0] for i in cntr) / 3) * 10_000)
py = int(abs(sum(i[1] for i in cntr) / 3) * 10_000)
print(px, py)  # 178755 2896

f = open(f'add/27/21599_27_B.txt').readlines()
data = [[*map(float, i.replace(',', '.').split())] for i in f]
clust = [[], [], [], [], [], []]
# def g_clust(p) не помогает ✔️
# k0 = -5/2
# b0 = 13 * 2.5
# y = (5 - 0) / (15 - 13) * x - 13 * b
# y = -2.5 * x - 13 * 2.5
for i in data:  # 0
    x, y = i
    if -2.5 * x - y > 13 * 2.5:
        clust[0].append(i)
[data.remove(i) for i in clust[0]]
for i in data:  # 1
    x, y = i
    if x < -9.5:
        clust[1].append(i)
[data.remove(i) for i in clust[1]]
for i in data:  # 2
    x, y = i
    # k2 = 12 / 6  # 2
    # b2 = -6 * k2  # 12
    # y = 2 * x + 12
    if y - 2 * x > 12:
        clust[2].append(i)
[data.remove(i) for i in clust[2]]
for i in data:  # 3
    x, y = i
    # k3 = 3 / 5  # 3/5
    # b3 = 0 * k2  # 0
    # y = (3/5) * x
    if y - (3/5) * x > 0:
        clust[3].append(i)
[data.remove(i) for i in clust[3]]
for i in data:  # 4
    x, y = i
    if y > -5:
        clust[4].append(i)
[data.remove(i) for i in clust[4]]
for i in data:  # 5
    x, y = i
    if y < -5:
        clust[5].append(i)
[data.remove(i) for i in clust[5]]
cntr = [centr(i) for i in clust]
px = int(abs(sum(i[0] for i in cntr) / 6) * 10_000)
py = int(abs(sum(i[1] for i in cntr) / 6) * 10_000)
print(px, py)  # 37392 50998
"""
178755 2896
37392 50998
"""


# 21911 Открытый вариант 2025 (Уровень: Базовый)
# ✅ Из-за большого разброса точек, кластеры собираем вручную (без функции)
from math import dist
def centr(ls: list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return min(res)[1]

f = open(f'add/27/21911_27_A.txt')
data = [[*map(float, i.replace(',', '.').split())] for i in f]
clust = [[], []]
for i in data:
    if i[1] > 2:
        clust[0].append(i)
    else:
        clust[1].append(i)
c = [centr(i) for i in clust]
px = int(sum(i[0] for i in c) / 2 * 10_000)
py = int(sum(i[1] for i in c) / 2 * 10_000)
print(px, py) # 26216 24182

f = open(f'add/27/21911_27_B.txt')
data = [[*map(float, i.replace(',', '.').split())] for i in f]
clust = [[], [], []]
for i in data:
    if i[0] < 10:
        clust[0].append(i)
    elif i[0] > 20:
        clust[1].append(i)
    else:
        clust[2].append(i)
c = [centr(i) for i in clust]
px = int(sum(i[0] for i in c) / 3 * 10_000)
py = int(sum(i[1] for i in c) / 3 * 10_000)
print(px, py) # 150891 63754
"""
26216 24182
150891 63754
"""


# 21929 (Уровень: Базовый)
from math import dist
def centr(ls:list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return min(res)[1]

def get_clust(p:list):
    clust = [i for i in data if dist(p, i) <= 1]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for i in 'AB':
    f = open(f'add/27/21929_27_{i}.txt')
    data = [[*map(float, i.replace(',', '.').split())] for i in f]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        cl = [p] + get_clust(p)
        # print(len(cl))
        clusters.append(cl)
    # print(sum(len(i) for i in clusters), '\n')
    res = [centr(i) for i in clusters]
    Px = int(sum(i[0] for i in res) / len(res) * 10_000)
    Py = int(sum(i[1] for i in res) / len(res) * 10_000)
    print(Px, Py)
"""
45336 117141
167659 143170
"""


# 21930 (Уровень: Базовый)
from math import dist
def centr(ls:list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return max(res)[1]

def get_clust(p, k):
    clust = [i for i in data if dist(p, i) <= k]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i, k) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for i, k in zip('AB', (1, 1)):
    f = open(f'add/27/21930_27_{i}.txt')
    data = [[*map(float, i.replace(',', '.').split())] for i in f]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clust = [p] + get_clust(p, k)
        # print(len(clust))
        clusters.append(clust)
    # print(sum(len(i) for i in clusters), '\n')
    res = [centr(i) for i in clusters]
    Px = sum(i[0] for i in res) / len(res) * 10000
    Py = sum(i[1] for i in res) / len(res) * 10000
    print(int(Px), int(Py))
"""
18049 111324
174474 142246
"""


# № 21931 (Уровень: Базовый)
from math import dist
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(p, i) for i in ls)
        res.append((sm, p))
    return max(res)[1]

def get_cluster(p:tuple, k):
    clust = [i for i in data if dist(p, i) < k]
    [data.remove(i) for i in clust]
    next_clust = [get_cluster(i, k) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for k in zip('AB', (1, 1)):
    data = [tuple(map(float, i.replace(',', '.').split())) for i in open(f'21931_27_{k[0]}.txt')]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clust = [p] + get_cluster(p, k[1])
        # print(len(clust))
        clusters.append(clust)
    # print(sum(len(i) for i in clusters))
    clusters.sort(key=len)
    P = [center(i) for i in clusters]
    Px = int(P[0][0] * 10_000)
    Py = int(P[-1][1] * 10_000)
    print(Px, Py)
"""
1663 61127
147474 61934
"""



# № 21932 (Уровень: Базовый)
from math import dist
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(i, p) for i in ls)
        res.append((sm, p))
    return min(res)[1]

def getClust(p:list):
    clust = [i for i in data if dist(p, i) < 2]
    [data.remove(i) for i in clust]
    nextClust = [getClust(i) for i in clust]
    [clust.extend(i) for i in nextClust]
    return clust

A = [tuple(map(float, i.replace(',', '.').split())) for i in open('21932_27_A.txt')]
B = [tuple(map(float, i.replace(',', '.').split())) for i in open('21932_27_B.txt')]
# data = A[:]
data = B[:]
print(len(data))

clusters = []
while data:
    p = data.pop()
    clust = [p] + getClust(p)
    print(len(clust))
    clusters.append(clust)
clusters.sort(key=len)
print(sum(len(i) for i in clusters), 'total')

P = [center(i) for i in clusters]
Px = int(P[0][0] * 10_000)
Py = int(P[-1][1] * 10_000)
print(Px, Py)
"""
32865 70666
144062 61170
"""


# 23384 Резервный день 19.06.25 (Уровень: Базовый)
from math import dist
def get_clust(p):
    clust = [i for i in data if dist(p, i) < 1]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_center(ls):
    res = []
    for p in ls:
        sm = sum(dist(p, i) for i in ls)
        res.append((sm, p))
    return min(res)[1]


for w in 'AB':
    data = [[*map(float, i.replace(',', '.').split())] for i in open(f'27{w}.txt')]
    # print(len(data))
    clust = []
    while data:
        p = data.pop()
        cl = [p] + get_clust(p)
        if len(cl) > 1:
            clust += [cl]
    # [print(len(i)) for i in clust]
    # print(sum(len(i) for i in clust), '\n')
    center = [get_center(i) for i in clust]
    if w == 'A':
        px = int(abs(sum(i[0] for i in center) * 10_000))
        py = int(abs(sum(i[1] for i in center) * 10_000))
        print(px, py)  # 110156 196632
    else:
        q1 = int(min(dist(i, [0,0,]) for i in center) * 10_000)
        q2 = int(max(dist(i, [0,0,]) for i in center) * 10_000)
        print(q1, q2)  # 224871 273226
"""
110156 196632
224871 273226
"""


# 23766 Демоверсия 2026 (Уровень: Базовый)
from math import dist
def get_clust(p):
    clust = [i for i in data if dist(i, p) < 1]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_center(ls):
    res = []
    for p in ls:
        sm = sum(dist(i, p) for i in ls)
        res.append((sm, p))
    return min(res)[1]

for w in 'AB':
    data = [[*map(float, i.replace(',', '.').split())] for i in open(f'27{w}.txt')]
    # print(len(data))
    clust = []
    while data:
        p = data.pop()
        cl = [p] + get_clust(p)
        if len(cl) > 1:
            clust += [cl]
    # [print(len(i)) for i in clust]
    # print(sum(len(i) for i in clust), '\n')
    clust.sort(key=len)
    center = [get_center(i) for i in clust]

    if w == 'A':
        px = int(abs(min(i[0] for i in center)) * 10_000)
        py = int(abs(min(i[1] for i in center)) * 10_000)
        print(px, py)  # 38471 61225
    else:
        q1 = int(dist(center[0], center[-1]) * 10_000)
        mx = [max(dist(ce, i) for i in cl) for ce, cl in zip(center, clust)]
        q2 = int(max(mx) * 10_000)
        print(q1, q2) # 142058 25299
"""
38471 61225
142058 25299
"""





# № 25441
from math import dist
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(i, p) for i in ls)
        res.append((sm, p))
    return min(res)[1]

def center_B(ls:list, p):
    return max(dist(i, p) for i in ls)

def get_cluster(p:tuple, k):
    cluster = [i for i in data if dist(p, i) < k]
    [data.remove(i) for i in cluster]
    next_clust = [get_cluster(i, k) for i in cluster]
    [cluster.extend(i) for i in next_clust]
    return cluster

for s, k in zip('AB', (1, 0.2)):
    data = [tuple(map(float, i.replace(',','.').split())) for i in open(f'25441_27_{s}.txt')]
    # print(len(data))
    res = []
    while data:
        p = data.pop()
        clust = [p] + get_cluster(p, k)
        # print(len(clust))
        res.append(clust)
    # print(sum(len(i) for i in res))
    # input('>>> ')
    res = [i for i in res if len(i) > 2]
    res.sort(key=len)
    P = [center(i) for i in res]
    if s == 'A':
        px = int(abs(P[0][0] - P[1][0]) * 10_000)
        py = int(abs(P[0][1] - P[1][1]) * 10_000)
        print(px, py)
    else:
        a,b,c = P
        q1 = int(dist(a, c) * 10_000)
        q2 = int(max(center_B(cl, i) for cl, i in zip(res, P)) * 10_000)
        print(q1, q2)
"""
18236 93042
9163 1646
"""


# № 25442
from math import dist
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(p,i) for i in ls)
        res.append((sm, p))
    return min(res)[-1]

def centerA(p, ls:list):
    return max(dist(p, i) for i in ls)

def get_cluster(p:tuple):
    cluster = [i for i in data if dist(p,i) < 1]
    [data.remove(i) for i in cluster]
    next_clust = [get_cluster(i) for i in cluster]
    [cluster.extend(i) for i in next_clust]
    return cluster

for s in 'AB':
    data = [tuple(map(float, i.replace(',', '.').split())) for i in open(f'25442_27_{s}.txt')]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clust = [p] + get_cluster(p)
        # print(len(clust))
        clusters.append(clust)
    # print(sum(len(i) for i in clusters))
    # input('>>> ')
    clusters = [i for i in clusters if len(i) > 2]
    P = [center(i) for i in clusters]
    if s == 'A':
        p1 = int(dist(*P) * 10_000)
        p2 = int(max(centerA(p, l) for p,l in zip(P, clusters)) * 10_000)
        print(p1, p2)
    else:
        a,b,c = P
        q1 = int(min([dist(a,b), dist(a,c), dist(c,b)]) * 10_000)
        q2 = int(max([dist(a,b), dist(a,c), dist(c,b)]) * 10_000)
        print(q1, q2)
"""
69301 21668
70628 149088
"""



# № 25443
from math import dist
from statistics import mean
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(p,i) for i in ls)
        res.append((sm, p))
    return min(res)[-1]

def centerA(p, ls:list):
    return max(dist(p,i) for i in ls)

def get_cluster(p:tuple):
    cluster = [i for i in data if dist(p, i) < 1]
    [data.remove(i) for i in cluster]
    next_clust = [get_cluster(i) for i in cluster]
    [cluster.extend(i) for i in next_clust]
    return cluster

for s in 'AB':
    data = [tuple(map(float, i.replace(',', '.').split())) for i in open(f'25443_27_{s}.txt')]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clust = [p] + get_cluster(p)
        # print(len(clust))
        clusters.append(clust)
    # print(sum(len(i) for i in clusters))
    # input('>>> ')
    clusters = [i for i in clusters if len(i) > 2]
    p = [center(i) for i in clusters]
    if s == 'A':
        p1 = int(dist(p[0], p[-1]) * 10_000)
        p2 = int(max([centerA(i, k) for i, k in zip(p, clusters)]) * 10_000)
        print(p1,p2)
    else:
        q1 = int(mean(i[0] for i in p) * 10_000)
        q2 = int(mean(i[1] for i in p) * 10_000)
        print(q1, q2)
"""
160921 25049
189300 106295
"""



# № 25444 (Уровень: Базовый)
from math import dist
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(p, i) for i in ls)
        res.append((sm, p))
    return min(res)[-1]

def get_cluster(p:tuple, k):
    clust = [i for i in data if dist(p, i) < k]
    [data.remove(i) for i in clust]
    next_clust = [get_cluster(i, k) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for s, k in zip('AB', (1, 0.15)):
    data = [tuple(map(float, i.replace(',', '.').split())) for i in open(f'25444_27_{s}.txt')]
    # print(len(data))
    cluster = []
    while data:
        p = data.pop()
        clust = [p] + get_cluster(p, k)
        # print(len(clust))
        cluster.append(clust)
    # print(sum(len(i) for i in cluster))
    # input('>>> ')
    cluster = [i for i in cluster if len(i) > 2]
    P = [center(i) for i in cluster]
    if s == 'A':
        a = min(dist(P[0], i) for i in cluster[1])
        b = min(dist(P[1], i) for i in cluster[0])
        P1 = int(min([a, b]) * 10_000)
        c = max(dist(P[0], i) for i in cluster[1])
        d = max(dist(P[1], i) for i in cluster[0])
        P2 = int(max([c, d]) * 10_000)
        print(P1, P2)
    else:
        a, b, c = P
        Q1 = int(min([dist(a, b), dist(c, b), dist(a, c)]) * 10_000)
        Q2 = int(max([dist(a, b), dist(c, b), dist(a, c)]) * 10_000)
        print(Q1, Q2)
"""
59674 83769
5651 9761
"""



# № 25445 (Уровень: Базовый)
from math import dist
from statistics import mean
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(p, i) for i in ls)
        res.append((sm, p))
    return min(res)[-1]

def get_cluster(p:tuple):
    cluster = [i for i in data if dist(p, i) < 1]
    [data.remove(i) for i in cluster]
    next_clust = [get_cluster(i) for i in cluster]
    [cluster.extend(i) for i in next_clust]
    return cluster

for s in 'AB':
    data = [tuple(map(float, i.replace(',', '.').split())) for i in open(f'25445_27_{s}.txt')]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clust = [p] + get_cluster(p)
        # print(len(clust))
        clusters.append(clust)
    # print(sum(len(i) for i in clusters))
    # input('>>> ')
    clusters = [i for i in clusters if len(i) > 2]
    P = [center(i) for i in clusters]
    if s == 'A':
        Px = int(abs(P[0][0] - P[-1][0]) * 10_000)
        Py = int(abs(P[0][1] - P[-1][1]) * 10_000)
        print(Px, Py)
    else:
        Qx = int(abs(mean(i[0] for i in P)) * 10_000)
        Qy = int(abs(mean(i[1] for i in P)) * 10_000)
        print(Qx, Qy)
"""
27784 104799
210416 136231
"""



# № 25446 (Уровень: Базовый)
from math import dist
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(p, i) for i in ls)
        res.append((sm, p))
    return min(res)[-1]

def get_cluster(p:tuple, k):
    clust = [i for i in data if dist(p, i) < k]
    [data.remove(i) for i in clust]
    next_clust = [get_cluster(i, k) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for s, k in zip('AB', (1, 1)):
    data = [tuple(map(float, i.replace(',', '.').split())) for i in open(f'25446_27_{s}.txt')]
    # print(len(data))
    clusters = []

    while data:
        p = data.pop()
        clust = [p] + get_cluster(p, k)
        clusters.append(clust)
        # print(len(clust))
    # print(sum(len(i) for i in clusters))
    clusters = [i for i in clusters if len(i) > 5]
    clusters.sort(key=len)
    P = [center(i) for i in clusters]
    if s == 'A':
        Px = int(abs(max(i[0] for i in P)) * 10_000)
        Py = int(abs(max(i[-1] for i in P)) * 10_000)
        print(Px, Py)
    else:
        Q1 = int(dist(P[0], P[-1]) * 10_000)
        res = []
        for c, p in zip(clusters, P):
            sm = max(dist(p, i) for i in c)
            res.append(sm)
        Q2 = int(max(res) * 10_000)
        print(Q1, Q2)
"""
66679 127423
149088 25324
"""



# № 25447 (Уровень: Базовый)
from math import dist
from statistics import mean
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(i, p) for i in ls)
        res.append((sm, p))
    return min(res)[1]

def get_cluster(p:tuple, k):
    cluster = [i for i in data if dist(p, i) < k]
    [data.remove(i) for i in cluster]
    next_clust = [get_cluster(i, k) for i in cluster]
    [cluster.extend(i) for i in next_clust]
    return cluster

for s, k in zip('AB', (1, 1)):
    data = [tuple(map(float, i.replace(',', '.').split())) for i in open(f'25447_27_{s}.txt')]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clust = [p] + get_cluster(p, k)
        clusters.append(clust)
        # print(len(clust))
    # print(sum(len(i) for i in clusters))
    clusters = [i for i in clusters if len(i) > 5]
    clusters.sort(key=len)

    P = [center(i) for i in clusters]
    if s == 'A':
        Px = int(abs(min(i[0] for i in P)) * 10_000)
        Py = int(abs(min(i[1] for i in P)) * 10_000)
        print(Px, Py)
    else:
        Q1 = int(abs(mean(dist(P[0], i) for i in clusters[0] if i != P[0])) * 10_000)
        Q2 = int(abs(mean(dist(P[-1], i) for i in clusters[-1] if i != P[-1])) * 10_000)
        print(Q1, Q2)
"""
115252 58612
9202 8993
"""



# № 25448 (Уровень: Базовый)
from math import dist
from statistics import mean
def center(ls:list):
    res = []
    for p in ls:
        sm = sum(dist(p, i) for i in ls)
        res.append((sm, p))
    return min(res)[-1]

def get_cluster(p:tuple, k):
    clust = [i for i in data if dist(p, i) < k]
    [data.remove(i) for i in clust]
    next_clust = [get_cluster(i, k) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for fl in zip('AB', (1, 1)):
    data = [tuple(map(float, i.replace(',', '.').split())) for i in open(f'25448_27_{fl[0]}.txt')]
    # print(len(data))
    clusters = []
    while data:
        p = data.pop()
        clast = [p] + get_cluster(p, fl[1])
        clusters.append(clast)
        # print(len(clast))
    # print(sum(len(i) for i in clusters), end='\n\n')
    clusters = [i for i in clusters if len(i) > 5]
    clusters.sort(key=len)

    P = [center(i) for i in clusters]
    if fl[0] == 'A':
        Px = int(abs(P[0][0] - P[1][0]) * 10_000)
        Py = int(abs(P[0][1] - P[1][1]) * 10_000)
        print(Px, Py)
    else:
        Q1 = int(mean([dist(P[0], i) for i in clusters[0] if i != P[0]]) * 10_000)
        Q2 = int(mean([dist(P[-1], i) for i in clusters[-1] if i != P[-1]]) * 10_000)
        print(Q1, Q2)
"""
15342 115607
9762 9518
"""


# 27780 Апробация 04.03.26 (Уровень: Базовый)
from math import dist
def get_center(ls: list):
    r = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        r.append((sm, i))
    return min(r)[1]

def get_clust(p):
    clust = [i for i in data if dist(i, p) < 2]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

for w in 'AB':
    f = open(f'add/KIM_25164989/27{w}_27780.txt').readlines()
    data = [[*map(float, i.replace(',', '.').split())] for i in f]
    # print(len(data))
    clust = []
    while data:
        p = data.pop()
        clust.append([p] + get_clust(p))
    # [print(len(i)) for i in clust]
    # print(sum(len(i) for i in clust), '\n')
    clust.sort(key=len)
    center = [get_center(i) for i in clust]
    if w == 'A':
        a1 = len(clust[-1])
        a2 = int(sum(dist(i, (1.0, 1.5)) for i in center) * 10_000)
        print(a1, a2)  # 344 294354
    else:
        b1 = sum(1 for i in clust[1] if dist(i, center[1]) <= 1.2 and i != center[1])
        b2 = int(min(dist(i, center[-1]) for i in clust[-1] if i != center[-1]) * 10_000)
        print(b1, b2)
"""
344 294354
152 528
"""


# 28766 Досрочная волна 2026 (Уровень: Базовый)  ️✅ цветные разноразмерные звезды
# https://vk.com/video-205865487_456240544?t=1h31m45s
from math import dist
def get_clust(p):
    clust = [i for i in data if dist(i[:2], p[:2]) < 2]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_center(ls):
    r = []
    for p in ls:
        sm = sum(dist(i[:2], p[:2]) for i in ls)
        r.append((sm, p))
    return min(r)[1]

def get_b1(ls):
    # r = []
    # for p in ls:
    #     for k in ls:
    #         if p != k:
    #             r.append(dist(p[:2], k[:2]))
    r = [dist(p[:2], k[:2]) for p in ls for k in ls if p != k]
    return min(r)


for w in 'AB':
    data = [i.replace(',', '.').split() for i in open(f'27_{w}_28766.txt')]
    data = [[*map(float, i[:2])] + [i[2]] for i in data]
    # print(len(data))
    clust = []
    while data:
        p = data.pop()
        clust.append(get_clust(p) + [p])
    # [print(len(i)) for i in clust]
    # print(sum(len(i) for i in clust), '\n')
    if w == 'A':
        clust.sort(key=len)
        # center = [get_center(i) for i in clust]
        center = get_center(clust[0])[:2]
        # A = []
        # for k in clust[0] + clust[1]:
        #     if k[2][0]+k[2][-3:] == 'YIII':
        #         A.append(dist(center, k[:2]))
        A = [dist(center, k[:2]) for k in clust[0]+clust[1] if k[2][0]+k[2][-3:] == 'YIII']
        a1 = int(min(A) * 10_000)
        a2 = int(max(A) * 10_000)
        print(a1, a2)  # 4940 74302
    else:
        center = [get_center(i)[:2] for i in clust]
        B = [[], [], []]
        for i in range(3):
            for k in clust[i]:
                if k[-1][0] + k[-1][2:] == 'ZI':
                    B[i].append(k)
        b1 = int(min(get_b1(B[i]) for i in range(3) if len(B[i]) > 1) * 10_000)
        # ручной участок кода
        # print([len(i) for i in B])  # [9, 3, 1]  # определяем минимальное и максимальное количество жёлтых сверхгигантов
        b2 = int(dist(center[0], center[-1]) * 10_000)  # нужные индексы берем из строчки выше
        print(b1, b2)  # 1035 125591
"""
4940 74302
1035 125591
"""


# 29081 (Уровень: Средний) 🌶️✅ цветные разноразмерные звезды
from math import dist
def get_clust(p):
    clust = [i for i in data if dist(i[:2], p[:2]) < 2]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_center(ls):
    r = []
    for p in ls:
        sm = sum(dist(i[:2], p[:2]) for i in ls)
        r.append((sm, p))
    return min(r)[1]

for w in 'AB':
    data = [i.replace(',', '.').split() for i in open(f'27_{w}_29081.txt')]
    data = [[*map(float, i[:2])] + [i[2]] for i in data]
    # print(len(data))
    clust = []
    while data:
        p = data.pop()
        clust.append(get_clust(p) + [p])
    # [print(len(i)) for i in clust]
    # print(sum(len(i) for i in clust), '\n')
    if w == 'A':
        center = [get_center(i) for i in clust]
        a = []
        for i in range(len(clust)):
            a += [dist(center[i][:2], k[:2]) for k in clust[i] if k != center[i] and k[2] == 'VII']
        a1 = int(min(a) * 10_000)
        a2 = int(max(a) * 10_000)
        print(a1, a2)  # 1495 16955
    else:
        B = [[], [], []]
        [B[i].append(k[:2]) for i in range(3) for k in clust[i] if k[2][1] in '89']
        # for i in range(3):
        #     for k in clust[i]:
        #         if  k[2][1] in '89':
        #             B[i].append(k[:2])
        b1_1 = [dist(i, k) for i in B[0] for k in B[1] + B[2]]
        b1_2 = [dist(i, k) for i in B[1] for k in B[2]]
        b1 = int(min(b1_1 + b1_2) * 10_000)
        b2_0 = [dist(i, k) for i in B[0] for k in B[0] if i != k]
        b2_1 = [dist(i, k) for i in B[1] for k in B[1] if i != k]
        b2_2 = [dist(i, k) for i in B[2] for k in B[2] if i != k]
        B2 = b2_0 + b2_1 + b2_2
        b2 = int(sum(B2) / len(B2) * 10_000)
        print(b1, b2)
"""
1495 16955
54154 11641
"""


# 29357 Открытый вариант 2026 (Уровень: Средний) 🌶️✅ цветные разноразмерные звезды
from math import dist
def get_clust(p):
    clust = [i for i in data if dist(p, i[:2]) < 1]
    [data.remove(i) for i in clust]
    next_clust = [get_clust(i[:2]) for i in clust]
    [clust.extend(i) for i in next_clust]
    return clust

def get_center(ls):
    r = []
    for k in ls:
        sm = sum(dist(i[:2], k[:2]) for i in ls)
        r.append((sm, k))
    return min(r)[1]

for w in 'AB':
    data = [i.replace(',','.').strip().split(' ') for i in open(f'27_{w}_29357.txt').readlines()]
    data = [[*map(float, i[:2])] + [i[2]] for i in data]
    # print(len(data))
    cluster = []
    while data:
        p = data.pop()
        cluster.append(get_clust(p[:2]) + [p])
    # [print(len(i)) for i in cluster]
    # print(sum(len(i) for i in cluster), '\n')
    if w == 'A':
        cluster.sort(key=len)
        center = get_center(cluster[0])[:2]  # центр кластера, содержащий наименьшее количество точек
        a = min([dist(center, [x, y]), (x, y)] for x, y, z in cluster[0] if z[0] + z[-3:] == 'MIII')[1]  # красный гигант
        ax = int(abs(a[0] * 10_000))
        ay = int(abs(a[1] * 10_000))
        print(ax, ay)  # 44694 69754
    else:
        cluster.sort(key=lambda x: sum(1 for i in x if i[2][0] + i[2][-3:] == 'KIII'))  # оранжевый гигант
        center = [get_center(cluster[0])[:2], get_center(cluster[-1])[:2]]
        b1 = int(dist(*center) * 10_000)
        b = [[] for i in range(3)]
        for i in range(3):
            for k in cluster[i]:
                if k[2][0] + k[2][2:] == 'GV':  # жёлтый карлик
                    b[i].append(k[:2])
        r = [(dist(i, k)) for ls in b for i in ls for k in ls]
        b2 = int(max(r) * 10_000)
        print(b1, b2)  # 138716 34029
"""
44694 69754
138716 34029
"""
