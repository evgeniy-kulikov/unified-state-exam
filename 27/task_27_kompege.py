""" task """
"""
24562 24985 25364
"""


# 24562 (Уровень: Базовый)
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


# 24985 (Уровень: Базовый)
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


# 25364 (Уровень: Базовый)
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

