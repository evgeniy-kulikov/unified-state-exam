""""""
"""
https://kompege.ru/task
Анализ данных
"""
# last 25441
"""
21931 21932 
25442 25443 25444 25445 25446 25447 25448
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
        clusters.append(
            clust)
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

def getClust(p:tuple):
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
