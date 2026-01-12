""" task """
"""
24562
24985
25364
25447
25448


"""


# https://kompege.ru/task   № 25448 (Уровень: Базовый)
from math import dist
def fab(ls: list):
    res = []
    for i in ls:
        p = sum(dist(i, k) for k in ls)
        res.append((p, i))
    return min(res)[1]

def fb(l: list, c:list):
    res = []
    for i in l:
        if i != c:
            res.append(dist(i, c))
    return sum(res) / (len(l) - 1)

A = [[*(map(float, i.replace(',', '.').split()))] for i in open('27_25448_A.txt')]
ca = [[], []]
for i in A:
    if 0 < i[0] < 10:
        if i[1] < 10:
            ca[0].append(i)
        else:
            ca[1].append(i)
zA = [fab(i) for i in ca]
Px = abs(zA[0][0] - zA[1][0]) * 10_000
Py = abs(zA[0][1] - zA[1][1]) * 10_000
print(int(Px), int(Py))  # 43050 143316

B = [[*(map(float, i.replace(',', '.').split()))] for i in open('27_25448_B.txt')]
cb = [[], [], []]
for i in B:
    if 10 < i[0] < 40:
        if i[0] > 23:
            cb[0].append(i)
        elif i[1] < 17:
            cb[1].append(i)
        else:
            cb[2].append(i)
cb.sort(key=len)
Q1 = fb(cb[0], fab(cb[0])) * 10_000
Q2 = fb(cb[-1], fab(cb[-1])) * 10_000
print(int(Q1),int(Q2))  # 9762 9518
"""
15342 115607
9762 9518
"""


# https://kompege.ru/task   № 25447 (Уровень: Базовый)
from math import dist
def fab(ls: list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append([sm, i])
    return min(res)[1]

def b(ls: list, cl: tuple):
    res = []
    for i in ls:
        if i != cl:
            res.append(dist(i, cl))
    return sum(res) / len(res)

A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27_25447_A.txt')]
la = [[], []]
for i in A:
    if i[1] > -10 and i[0] < 30:
        if i[0] < 16:
            la[0].append(i)
        else:
            la[1].append(i)
cl_a = [fab(i) for i in la]
px = abs(min(cl_a)[0]) * 10_000
py = abs(min(cl_a, key=lambda x: x[1])[1]) * 10_000
print(int(px), int(py))

B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27_25447_B.txt')]
lb = [[], [], []]
for i in B:
    if 5 < i[0] < 30:
        if i[1] < 5:
            lb[0].append(i)
        elif i[1] < 12.5:
            lb[1].append(i)
        else:
            lb[2].append(i)

lb.sort(key=len)
Q1 = abs(b(lb[0], fab(lb[0]))) * 10_000
Q2 = abs(b(lb[-1], fab(lb[-1]))) * 10_000
print(int(Q1), int(Q2))  # 9202 8993
"""
115252 58612
9202 8993
"""


# https://kompege.ru/task   № 25364 (Уровень: Базовый)
from math import dist
def fab(ls: list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res += [(sm, i)]
    return min(res)[1]

A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27_25364_A.txt')]
cla = [[], []]
for i in A:
    if i[1] < 9:
        cla[0].append(i)
    else:
        cla[1].append(i)
cntr = [fab(i) for i in cla]
p = (1.0, 1.0)
f1 = min(dist(p, k) for k in cntr)
f2 = max(dist(p, k) for k in cntr)
print(int(f1 * 10_000), int(f2 * 10_000))  # 58605 128643

B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27_25364_B.txt')]
clb = [[], [], []]
for i in B:
    if i[1] < 15:
        clb[0].append(i)
    elif i[1] < 22:
        clb[1].append(i)
    else:
        clb[2].append(i)

clb.sort(key=len)
cntr = fab(clb[-1])
q1 = sum(1 for i in clb[-1] if dist(cntr, i) <= 1.2)
q2 = sum(1 for i in clb[-1] if dist(cntr, i) <= 0.75)
print(q1, q2)  # 358 203
"""
58605 128643
358 203
"""


# https://kompege.ru/task   № 24985 (Уровень: Базовый)
from math import *
def ab(ls: list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return max(res)[1]

def b(ls: list, ct):
    return max(dist(ct, k) for k in ls)

A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27_24985_A.txt')]
cA = [[], []]
for i in A:
    if 0 < i[0] < 10:
        if i[1] < 10:
            cA[0].append(i)
        else:
            cA[1].append(i)
ctrA = [ab(i) for i in cA]
Fx = max(i[0] for i in ctrA)
Fy = max(i[1] for i in ctrA)
print(int(abs(Fx)*10_000), int(abs(Fy)*10_000))  # 27708 189345

B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27_24985_B.txt')]
cB = [[], [], []]
for i in B:
    if 10 < i[0] < 40:
        if i[1] < 10.5:
            cB[0].append(i)
        elif i[1] > 16:
            cB[2].append(i)
        else:
            cB[1].append(i)
cB.sort(key=len)
ctrB = [ab(i) for i in cB]
Q1 = dist(ctrB[0], ctrB[-1])
Q2 = max(b(x, y) for x, y in zip(cB, ctrB))
print(int(abs(Q1)*10_000), int(abs(Q2)*10_000))  # 187711 49105
"""
27708 189345
187711 49105
"""


# https://kompege.ru/task   № 24562 (Уровень: Базовый)
from math import *
def ab(ls: list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res.append((sm, i))
    return min(res)[1]

A = [tuple(map(float, i.replace(',', '.').split())) for i in open('27_24562_A.txt')]
cA = [[], []]
for i in A:
    if i[1] < 0:
        cA[0].append(i)
    else:
        cA[1].append(i)

ctA = [ab(i) for i in cA]
Sx = abs(sum(i[0] for i in ctA) * 10_000)
Sy = abs(sum(i[1] for i in ctA) * 10_000)
print(int(Sx), int(Sy))  # 694121 7716

B = [tuple(map(float, i.replace(',', '.').split())) for i in open('27_24562_B.txt')]
cB = [[], [], []]
for i in B:
    if i[0] < -30:
        cB[0].append(i)
    elif i[0] > 17.5:
        cB[1].append(i)
    elif 0 < i[0] < 10:
        cB[2].append(i)

ctB = [ab(i) for i in cB]
cB2 = [list(set(i) - {k}) for i, k in zip(cB, ctB)]
ctB2 = [ab(i) for i in cB2]
Qx = abs(sum(i[0] for i in ctB2) * 10_000)
Qy = abs(sum(i[1] for i in ctB2) * 10_000)
print(int(Qx), int(Qy))  # 132665 386247
"""
694121 7716
132665 386247
~ 35 min
"""






