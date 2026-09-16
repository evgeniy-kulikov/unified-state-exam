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


# https://stepik.org/lesson/614865/step/1?unit=610428
f = open('26.txt')
N, M = map(int, next(f).split())  # общее кол-во партий изделий, сумма денег на закупку
d = []
for i in f:
    a, b, c = i.split()  # цена одного изделия, кол-во изделий в партии, тип изделия
    d.append([int(a), int(b), c])
d.sort(key=lambda x: (x[2], x[0]))
sm = cnt = 0
for i in range(N):
    a, b, c = d[i]
    for k in range(b):
        if sm + a <= M:
            sm += a
            cnt += c == 'B'
        else:
            print(cnt, M - sm, sep='') # 5895 227
            exit()


# https://stepik.org/lesson/614865/step/2?unit=610428
f = open('26.txt')
N, M = map(int, next(f).split())  # общее кол-во партий изделий, сумма денег на закупку
d = []
for i in f:
    a, b, c = i.split()  # цена одного изделия, кол-во изделий в партии, тип изделия
    d.append([int(a), int(b), c])
d.sort(key=lambda x: (-ord(x[2]), x[0]))  # ord(c) - ✅ привести к одному типу данных
sm = cnt = 0
for i in range(N):
    a, b, c = d[i]
    for k in range(b):
        if sm + a <= M:
            sm += a
            cnt += c == 'A'
        else:
            print(cnt, M - sm, sep=' ') # 7165 245
            exit()


# https://stepik.org/lesson/614865/step/3?unit=610428
"""
1. Сортируем по возрастанию цены и отсекаем список по "М"
2. Заменяем все товары категории "В" на "А"
"""
f = open('26.txt')
N, M = map(int, next(f).split())  # кол-во изделий, сумма денег на закупку
d = list(map(lambda x: x.split(), f))
d = [(int(i[0]), i[1]) for i in d]  # цена, тип
# d = []
# for i in f:
#     p, w = i.split()  # цена, тип
#     d.append([int(p), w])
d.sort()
sm = 0
for i in range(N):
    p, w = d[i]
    if sm + p <= M:
        sm += p
    else:
        AB = d[:i]
        AB.sort(key=lambda x: x[1])  # конец списка состоит из категорий "В" (цена возрастает)
        A = [i for i in d[i:] if i[1]=='A']
        break
for i in range(1, len(A)+1):
    if AB[-i][1]=='B' and sum(i[0] for i in AB) - AB[-i][0] + A[i-1][0] <= M:
        AB[-i] = A[i-1]  # Заменяем все товары категории "В" на "А"
    else:
        break
res1 = sum(i[1]=='A' for i in AB)
res2 = M - sum(i[0] for i in AB)
print(res1, res2)  # 157 267


# https://stepik.org/lesson/614865/step/4?unit=610428
"""
1. Сортируем по возрастанию цены и отсекаем список по "М"
2. Заменяем все товары категории "A" на "B"
"""
f = open('26.txt')
N, M = map(int, next(f).split())  # кол-во изделий, сумма денег на закупку
d = list(map(lambda x: x.split(), f))
d = sorted((int(i[0]), i[1]) for i in d)
sm = b = 0  # расход денег, кол-во "В"
for i in range(N):
    p, w = d[i]  # цена, тип
    if sm + p <= M:
        sm += p
        b += w=="B"
    else:
        AB = d[:i]
        AB.sort(key=lambda x: -ord(x[1]))  # в конце списка категории "A" (цена возрастает)
        B = [i for i in d[i:] if i[1]=='B']
        break
for i in range(1, len(B)+1):
    if AB[-i][1]=='A' and sum(i[0] for i in AB) - AB[-i][0] + B[i-1][0] <= M:
        AB[-i] = B[i-1]  # Заменяем товары категории "A" на "B"
        b += 1
    else:
        break
rub = M - sum(i[0] for i in AB)
print(b, rub)  # 154 87


# https://stepik.org/lesson/693631/step/3?unit=693279
d = sorted([*map(int, input().split())] for _ in range(int(input())))
res = [d[0]]
for a1, a2 in d:
    b1, b2 = res[-1]
    if b2 >= a1:
    # if b1 <= a2 and b2 >= a1: # лишние проверки
    #     res[-1][0] = min(a1, b1)  # лишние проверки
        res[-1][1] = max(a2, b2)
    else:
        res += [[a1, a2]]
sm = sum(b-a for a, b in res)
print(len(res), sm, sep='')



# https://stepik.org/lesson/693631/step/5?unit=693279
d = sorted([int(int(input())) for _ in range(int(input()))], reverse=True)
res = []
while d:
    cnt = 1
    # cur = d[0]
    # d[0] = 0
    cur, d[0] = d[0], 0
    for i in range(1, len(d)):
        if cur - d[i] >= 5:
            cnt += 1
            # cur = d[i]
            # d[i] = 0
            cur, d[i] = d[i], 0
    res.append(cnt)
    d = [i for i in d if i]
print(len(res), max(res))



# https://stepik.org/lesson/1272875/step/1?unit=1287804
# 5228 (Уровень: Базовый)
f = open('26.txt').readlines()
d = sorted(map(int, f[1:]), reverse=True)
res = [d[0]]
for i in d[1:]:
    if res[-1] - i >= 6:
        res.append(i)
print(len(res), res[-1])  # 489 123



# https://stepik.org/lesson/1272875/step/2?unit=1287804
f = open('26.txt').readlines()
N, M = map(int, f[0].split()) # кол-во коробок, кол-во замочков
box = []  # коробки
lock = set()  # замки
idx, cnt = 0, 1
for el in f[1:]:
    if len(el.split()) == 2:
        b, l = map(int, el.split())
        box.append(b)
        lock.add(l)
    else:
        box.append(int(el))
box.sort(reverse=True)
for i in range(N):  # находим индекс большей стартовой коробки
    if box[i] in lock:
        idx = i
        break
cur = box[idx]
for b in box[idx+1:]:  # находим кол-во подходящих коробкок и последнюю меньшую
    if cur - b >= 6 and b in lock:
        cur = b
        cnt += 1
print(cnt, cur)  # 585 227



# https://stepik.org/lesson/1272875/step/3?unit=1287804
f = open('26.txt').readlines()
d = []
for el in f[1:]:
    if len(el.split()) == 2:
        a, b = map(int, el.split())
        d.extend([(a, 0), (b, 1)])
    else:
        d.append((int(el), 0))
d.sort(reverse=True)
cur, cnt = d[0], 1
for el in d[1:]:
    if cur[0] - el[0] >= 5 and cur[1] != el[1]:
        cur = el
        cnt += 1
print(cnt, cur[0])  # 536 306


# https://stepik.org/lesson/1272875/step/3?unit=1287804
# Krylov_2026     11 var
# https://wiki.pruefungshefte.de/ru/matematika/funkcii/sistema-koordinat-i-chetverti
# Наименование частей происходит против часовой стрелки
f = open('26.txt').readlines()[1:]
d = [[*map(int, i.split())] for i in f]
# сортировка по координате правого верхнего угла квадрата по оси абцисс (Х)
d.sort(key = lambda x: sum(x))

res = [d[0]]  # сбор квадратов
for i in d:
    if i[0] >= sum(res[-1]):
        res.append(i)

d.sort(key=lambda x: -x[0])  # поиск самого удаленного квадрата
for i in d:
    if i[0] >= res[-1][0]:
        res[-1] = i
        break
print(len(res), abs(res[-1][0] - res[-2][0]))