""""""
"""
course_72713
task_26_72713
task 26
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""

# https://stepik.org/lesson/1461385/step/2?unit=1480760
f = open('26.txt')
S, N = map(int, f.readline().split())
d = sorted(map(int, f))
c = sm = 0
for i in d:
    if sm + i <= S:
        sm += i
        c += 1
    else:
        sm -= i
        break
for k in range(N-1, 0 , -1):
    if sm + d[k] <= S:
        print(c, d[k], sep='')  # 568 50
        break

# variant
f = open('26.txt')
S, N = map(int, f.readline().split())
d = sorted(map(int, f), reverse=True)
U = []
while sum(U) + d[-1] <= S:
    U.append(d.pop())
d = d + [U.pop()]
for i in range(len(d)):
    if sum(U) + d[i] <= S:
        print(len(U)+1, d[i], sep='') # 568 50
        break


# https://stepik.org/lesson/590023/step/2?unit=584984
# 1868 Основная волна 2021(Уровень: Базовый)
f = open('26.txt').readlines()
data = [tuple(map(int, i.split())) for i in f[1:]]  # row, seat
d = dict()
for i in data:
    r, s = i
    d.setdefault(r, [])
    d[r].append(s)
res = [(r, sorted(s))for r, s in d.items() if len(s) > 1]
res.sort(reverse=True)
for i in res:
    for a,b in zip(i[1], i[1][1:]):
        if b - a == 3:
            print(i[0], a+1)  # 8631 7311
            exit()


# https://stepik.org/lesson/590023/step/4?unit=584984
f = open("26.txt")
n = next(f)
d = sorted([[*map(int, i.split())] for i in f], key=lambda x: (-x[0], x[1]))
for t1, t2 in zip(d, d[1:]):
    if t1[0] == t2[0] and t2[1] - t1[1] == 4:
        print(t1[0], t1[1] + 1, sep='')  # 7522 5074
        break


# https://stepik.org/lesson/590023/step/9?unit=584984
# ❗❗❗ Возможны повторные попадания в одну точку
f = open("26.txt")
next(f)
data = [tuple(map(int, i.split())) for i in f]
d = dict()
for r, p in data:
    if not p % 2:
        d.setdefault(r, set())
        d[r].add(p)
res = sorted([(len(p), r) for r, p in d.items()], key=lambda x: (-x[0], x[1]))
print(*res[0], sep='')  # 17 283


# https://stepik.org/lesson/590023/step/10?unit=584984
# решение с ручным анализом ✔️
f = open("26.txt")
next(f)
data = [tuple(map(int, i.split())) for i in f]  # row, seat
d = dict()
for r, p in data:
    d.setdefault(r, set()) # ❗❗❗ Возможны повторные попадания в одну точку
    d[r].add(p)
data = [[r, sorted(p)] for r, p in d.items()]
ls = []
# MX = 0
for el in data:
    c = 1
    for a,b in zip(el[1], el[1][1:]):
        if b - a == 1:
            c += 1
            # MX = max(MX, c)
            if c == 6:  # 6 - значение MX ✔️
                ls.append([el[0], [*range(b-5, b+1)]])
        else:
            c = 1
# print(MX)  # 6  максимальное кол-во точек подряд
res = []
for el in ls:
    row, seat = el  # row, seat
    MN = 10**6
    for s in seat:
        MN = min(MN, min(row-1, 10_000 - row, s-1, 10_000 - s))
    res.append((MN, row))
res.sort()
print(res[0][1], res[0][0]) # 6539 287
"""
[6539, [288, 289, 290, 291, 292, 293]]
"""


# https://stepik.org/lesson/613871/step/1?unit=609338
from math import ceil
f = open("26.txt")
f.readline()
data = sorted(map(int, f))
d_50 = sum(i for i in data if i <= 50)
d_51 = [i for i in data if i > 50]
d_sale = d_51[:len(d_51) // 2]
d_full = sum(d_51[len(d_51) // 2:])
SM = d_50 + d_full + ceil(sum(d_sale) * 0.75)
print(SM, d_sale[-1])  # 469784 511


# https://stepik.org/lesson/613871/step/3?unit=609338
from math import ceil
f = open("26.txt")
next(f)
data = sorted(map(int, f))
g_50, goods = 0, []
for i in data:
    if i <= 50:
        g_50 += i
    else:
        goods.append(i)
idx = len(goods) // 2
g_sale = sum(goods[:idx]) * 0.82
g_fool =  sum(goods[idx:])
print(ceil(g_50 + g_sale + g_fool), goods[idx-1])  # 479364 512


# https://stepik.org/lesson/613871/step/8?unit=609338 🌶️🌶️🌶️🌶️🌶️
f = open("26.txt")
n = int(next(f))
data = sorted(map(int, f))
rub = 100_000
SM = 0
for i in range(1, n+1):
    idx = (i) // 6
    fool = sum(data[:i - idx])
    sale = sum(data[i-idx:i]) * 0.5
    if fool + sale <= rub:
        SM = fool + sale
    else:
        print(i-1, rub - SM)  # 470 20
        break