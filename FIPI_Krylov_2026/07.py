""" var 07 """


# 12
'1' * 126 + '0' * 129  # начало
'0' * 126 + '1' * 129  # после q1
'1' + '0' * 125 + '1' * 129  # после q2
# 129 min
'0' * 125 + '1' + '0' * 129  # начало
'1' * 125 + '0' + '1' * 129  # после q1
'0' * 125 + '1' + '1' * 129  # после q2
# 254 max  (решение вне задачи)

# 24
from re import *
f = open('24var07.txt').readline()
n = r'(?:0|[1-9]\d*)'
reg = rf'{n}(?:[*-]{n})+'
res = findall(reg, f)
print(len(max(res, key=len)))  # 356


# 25
def f(n):
    res = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            res |= {i, n //i}
    return res
c = 5
for n in range(800_000, 10**10):
    r = sum(f(n))
    if r % 10 == 3:
        c -= 1
        print(n, r)
    if not c:
        break
"""
800002 571453
800006 405273
800022 800033
800026 403813
800032 845023
"""


# 26
f = open('26var07.txt').readlines()
N, R, C = map(int, f[0].split())  # кол-во клеток, кол-во рядов, кол-во столбцов
d = {k: [0, R+1] for k in range(1, C + 1)}
for i in f[1:]:
    row, col = map(int, i.split())   # ряд, столбец  - координаты занятой клетки
    d[col] += [row]
# обработка данных
res, r = [], []
for col, row in d.items():
    cnt = 0
    row.sort()
    for a, b in zip(row, row[1:]):
        if b - a > cnt:
            cnt = b - a
            r = [cnt, b - 1, col]
    if r:
        res.append(r)
res.sort(key=lambda x: (-x[0], x[1], x[2]))
print(*res[0][1:])  # 3974 1457  (ряд, столбец)


# 27
from math import dist
def centr(ls:list):
    res = []
    for i in ls:
        sm = sum(dist(i, k) for k in ls)
        res += [(sm, i)]
    return min(res)[1]

f_a = open('27var07A.txt').readlines()
cl_a = [[], []]
for i in f_a:
    x, y = map(float, i.replace(',', '.').split())
    if x > 0 and y > 0:
        if y > 16:
            cl_a[0].append((x, y))
        else:
            cl_a[1].append((x, y))
center_a = [centr(i) for i in cl_a]
px_a = int(max(i[0] for i in center_a) * 10_000)
py_a = int(max(i[1] for i in center_a) * 10_000)
print(px_a, py_a)  # 50844 222522

f_b = open('27var07B.txt').readlines()
cl_b = [[], [], []]
for i in f_b:
    x, y = map(float, i.replace(',', '.').split())
    if x > 10 and 0 < y < 20:
        if x > 22:
            cl_b[2].append((x, y))
        elif y > 13:
            cl_b[0].append((x, y))
        else:
            cl_b[1].append((x, y))

px_b = len(min(cl_b, key=len))
py_b = len(max(cl_b, key=len))
print(px_b, py_b)  # 90 413
"""
50844 222522
90 413
"""
