""""""
"""
Task 26
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 26.1 Задание 26 ЕГЭ | Урок 1 """
# https://stepik.org/lesson/1726034/step/2?unit=1749716
# https://kompege.ru/task   № 936 Джобс 08.02.2021 (Уровень: Сложный)
# made it myself
with open('add/course_233165/26-1_02.txt') as file:
    N, S = map(int, next(file).split())
    m = sorted(map(int, file), reverse=True)
    res = []
    while len(m):
        ship = []
        for i in range(len(m)):
            if sum(ship) + m[i] <= S:
                ship.append(m[i])
                m[i] = 0
        res.append(ship)
        m = [i for i in m if i]
    print(len(res), sum(res[-1]))  # 423 501


# https://stepik.org/lesson/1726034/step/3?unit=1749716
# https://kompege.ru/task   № 225 Джобс 14.09.2020 (Уровень: Базовый)
# made it myself
with open('add/course_233165/26-1_03.txt') as file:
    S, N = map(int, next(file).split())
    m = sorted(map(int, file), reverse=True)
    res = []
    for i in range(len(m)):
        if sum(res) + m[i] <= S:
            res.append(m[i])
            m[i] = 0
    m = [i for i in m if i]
    for i in range(len(m)):
        if sum(res) + m[i] <= S:
            res.append(m[i])
    print(len(res), res[-1])  # 1054 732


# https://stepik.org/lesson/1726034/step/4?unit=1749716
# https://kompege.ru/task   № 788 Джобс 30.11.2020 (Уровень: Средний)
with open('add/course_233165/26-1_04.txt') as file:
    D, E, N = map(int, next(file).split())  # 5000 1500
    m = sorted(map(int, file))

    ls_d = [i for i in m if i > 500]
    ls_d_end = []
    while sum(ls_d) > D:
        ls_d_end.append(ls_d.pop())
    ls_d_end.sort()
    d = D - sum(ls_d[:-1])
    for i in range(len(ls_d_end)):
        if ls_d_end[i] <= d:
            ls_d[-1] = ls_d_end[i]

    ls_e = [i for i in m if i <= 500]
    ls_e_end = []
    while sum(ls_e) > E:
        ls_e_end.append(ls_e.pop())
    ls_e_end.sort()
    e = E - sum(ls_e[:-1])
    for i in range(len(ls_e_end)):
        if ls_e_end[i] <= e:
            ls_e[-1] = ls_e_end[i]
print(len(ls_d) + len(ls_e), max(ls_d) + max(ls_e))  # 13 1381


# https://stepik.org/lesson/1726034/step/5?unit=1749716
# https://kompege.ru/task   № 2149 (Уровень: Базовый)
with open('add/course_233165/26-1_05.txt') as file:
    _, M = map(int, next(file).split())
    d = sorted(map(int, file))
    pic = [i for i in d if i <= 100]
    vid = [i for i in d if i > 100]
    usb = []
    for i in vid:
        if sum(usb) < M / 2:
            usb.append(i)
    for i in pic:
        if sum(usb) + i <= M:
            usb.append(i)
    if M - sum(usb):
        usb.pop()
    for i in pic[::-1]:
        if sum(usb) + i <= M:
            usb.append(i)
            break
    print(M - sum(usb), len(usb))  # 0 7347


# https://stepik.org/lesson/1726034/step/6?unit=1749716
# https://kompege.ru/task   № 1395 (Уровень: Базовый)
with open('add/course_233165/26-1_06.txt') as file:
    S, N = map(int, next(file).split())
    d = sorted(map(int, file))
    p = m = 0
    for i in range(N):
        if m + d[i] <= S:
            m += d[i]
            p = i
        else:
            break
    print(len(d[p+1:]), sum(d[p+1:]))  # 7655 542450


# https://stepik.org/lesson/1726034/step/7?unit=1749716
# https://kompege.ru/task   № 2612 (Уровень: Базовый)
from statistics import mean
idx = 0
data = open('add/course_233165/26-1_07.txt').readlines()
n, m = map(int, data[0].split())
d = sorted(map(int, data[1:]), reverse=True)
for i in range(n):
    if d[i] > d[m]:
        idx = i
    else:
        break
# убираем из списка гарантировано не проходящих последний элемент из списка проходящих студентов (при наличии)
print(d[idx], int(mean(set(d[m:]) - {d[m-1]})))  # 276 246


# https://stepik.org/lesson/1726034/step/8?unit=1749716
# https://kompege.ru/task   № 2614 (Уровень: Базовый)
data = open('add/course_233165/26-1_08.txt').readlines()
s, n = map(int, data[0].split())
d = [*map(int, data[1:])]
rare, book, res = [], [], []
for i in d:
    if i > 3000:
        rare.append(i)
    elif i < 2000:
        book.append(i)
    else:
        res.append(i)
rare.sort()
book.sort()
res.extend([rare[0], rare[-1]])

for i in book:
    if sum(res) + i <= s:
        res.append(i)

res.pop()
for i in book[::-1]:
    if sum(res) + i <= s:  # для максимального использования денег ищем самую дорогую простую книгу
        res.append(i)
        print(len(res), res[-1])  # 398 273
        break


# https://stepik.org/lesson/1726034/step/9?unit=1749716
# https://kompege.ru/task   № 954 (Уровень: Базовый)
data = open('add/course_233165/26-1_09.txt').readlines()
sale = 0
n, k, m = map(int, data[0].split())
d = sorted(map(int, data[1:]), reverse=True)
for i in range(k + m):
    if i < k:
        sale += d[i] * 0.2
    else:
        sale += d[i] * 0.1
print(d[k + m], int(sale))  # 7500 314590


# https://stepik.org/lesson/1726034/step/10?unit=1749716
# https://kompege.ru/task   № 507 Джобс 19.10.2020 (Уровень: Средний)
data = open('add/course_233165/26-1_10.txt').readlines()
sale1, sale2 = [], []
n = int(data[0])
d = sorted(map(int, data[1:]))
for i in range(n):
    if i < n * 0.7:
        sale1.append(d[i] * 0.7)
    else:
        sale1.append(d[i] * 0.6)
    if i < n * 0.5:
        sale2.append(d[i] * 0.6)
    else:
        sale2.append(d[i] * 0.65)
a, b = sum(sale1), sum(sale2)
print(int(a - b), int((sale1[-1], sale2[-1])[a < b]))  # 63792 600



# https://stepik.org/lesson/1726034/step/11?unit=1749716
# https://kompege.ru/task   № 2615 Сборник ЕГЭ Ушакова 2022 (Уровень: Базовый)
"""
Общий принцип (гири только на одной чаше):
Если у вас есть гири с весами (w_1, w_2,... ,w_k), то максимальный вес, который можно получить из первых (k) гирь,
равен их сумме S_k = w_1 + w_2 + ... + w_k
Чтобы можно было взвесить все веса от 1 до S_k, следующая гиря w_k+1 должна быть НЕ БОЛЬШЕ, чем S_k + 1.
Если w_k+1 > S_k + 1, то вес S_k + 1 не удастся взвесить, и это будет МИНИМАЛЬНЫЙ невзвешиваемый вес,
так как все веса до S_k уже можно получить.
Для идеального случая (чтобы взвешивать все веса подряд) веса гирь должны быть степенями двойки: 1, 2, 4, 8...
"""
data = open('add/course_233165/26-1_11.txt').readlines()
n = int(data[0])
d = sorted(map(int, data[1:]))
for i in range(1, n):
    if d[i] > sum(d[:i]) + 1:
        print(sum(d[:i]) + 1, len(d[:i]))  # 32224 126
        break




""" 26.2 Задание 26 ЕГЭ | Урок 2 """
# https://stepik.org/lesson/1726035/step/1?unit=1749717
# https://kompege.ru/task   № 2617 Сборник ЕГЭ Ушакова 2022 (Уровень: Базовый)
from math import ceil
data = open('add/course_233165/26-2_01.txt').readlines()
# data = open('add/course_233165/test.txt').readlines()  #
n = int(data[0])
d = sorted(map(int, data[1:]), reverse=True)
mx = idx = 0
for i in range(ceil(n // 5), n - 1):
    delta = d[i] - d[i + 1]
    if delta > mx:
        mx = delta
        idx = i
print(idx + 1, d[idx])


# https://stepik.org/lesson/1726035/step/2?unit=1749717
# https://kompege.ru/task   № 1868 Основная волна 2021 (Уровень: Базовый)
dt = dict()
data = open('add/course_233165/26-2_02.txt').readlines()
n = int(data[0])
d = [[*map(int, i.split())] for i in data[1:]]
d.sort(key=lambda x: (-x[0],))
for i in d:
    dt.setdefault(i[0], [])
    dt[i[0]].append(i[1])
for k in dt:
    ls = sorted(dt[k])
    if len(ls) >= 2:
        for i in range(len(ls) - 1):
            if ls[i + 1] - ls[i] == 3:
                print(k, ls[i]+1)  # 8631 7311
                exit()


# https://stepik.org/lesson/1726035/step/3?unit=1749717
# https://kompege.ru/task   № 2613 (Уровень: Базовый)
dt = dict()
res = []
data = open('add/course_233165/26-2_03.txt').readlines()
d = [[*map(int, i.split())] for i in data[1:]]
for i in d:
    dt.setdefault(i[0], [])
    dt[i[0]].append(i[1])
for k in dt:
    cnt = mx = 1
    ls = sorted(dt[k])
    for i in range(1, len(ls)):
        if ls[i-1] + 1 == ls[i]:
            cnt += 1
            mx = max(mx, cnt)
        else:
            cnt = 1
    res.append((mx, k))
res.sort(reverse=True)
print(res[0][1], res[0][0])  # 99 14


# https://stepik.org/lesson/1726035/step/4?unit=1749717
# https://kompege.ru/task   № 2616 Сборник ЕГЭ Ушакова 2022 (Уровень: Базовый)
dt = dict()
res = list()
sm = 0
data = open('add/course_233165/26-2_04.txt').readlines()
_, s = map(int, data[0].split())
d = [[*map(int, i.split())] for i in data[1:]]
d.sort()
for k in d:
    dt.setdefault(k[0], [])
    dt[k[0]].append(k[1])
for k in dt:
    goods = len(dt[k])
    m = 0
    for v in dt[k]:
        if m + v <= s:
            m += v
            goods -= 1
    res.append((goods, k))
    sm += goods
res.sort(key=lambda x: (-x[0], x[1]))
print(sm, res[0][1])




""" 26.4 Задание 26 ЕГЭ | Задачи прошлых лет """
# https://stepik.org/lesson/1726037/step/1?unit=1749719
# https://kompege.ru/task   № 9756 Основная волна 19.06.23 (Уровень: Средний)
data = open('add/course_233165/26-3_01.txt').readlines()
N = int(data[0])
ls = [tuple(map(int, i.split())) for i in data[1:]]
ls.sort(key=lambda x: (x[1], x[0]))
res = []
end = 0
for i in ls:
    st, en = i
    if st >= end:
        res.append(i)
        end = en
res.pop()
end = res[-1][1]
for i in ls[::-1]:
    if i[0] >= end:
        res.append(i)
        break
print(len(res), res[-1][1])  # 16 1345

