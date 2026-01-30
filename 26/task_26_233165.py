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
# https://kompege.ru/task   № 2614 (Уровень: Базовый) 👍
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
# https://kompege.ru/task   № 2615 Сборник ЕГЭ Ушакова 2022 (Уровень: Базовый)  👍
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
print(sm, res[0][1])  # 391 15230058



# https://stepik.org/lesson/1726035/step/5?unit=1749717
# https://kompege.ru/task   № 732 Джобс 23.11.2020 (Уровень: Базовый)
data = open('add/course_233165/26-2_05.txt').readlines()
n, k = map(int, data[0].split())
D = [tuple(map(int, i.split())) for i in data[1:]]
# Сначала пакеты с самой выгодной ценой, а среди них сначала самые тяжелые
D.sort(key=lambda x: (x[1] / x[0], -x[1]))
res = D[:k]
res.sort()
w = sum(i[0] for i in res)
print(w, res[-1][1])  # 5931 800


# https://stepik.org/lesson/1726035/step/6?unit=1749717
# https://kompege.ru/task   № 2255 (Уровень: Средний) 👍
data = open('add/course_233165/26-2_06.txt').readlines()
n, m = map(int, data[0].split())
D = []
for el in data[1:]:
    a, b = el.split()
    D.append((int(a), b))
D.sort()
N, A = [], []
# Список 'N': макс. возможное кол-во товаров.
# Список 'A': товары группы 'A' не попавшие в список 'N'
sm = 0
for i in range(n):
    if sm + D[i][0] <= m:
        sm += D[i][0]
        N.append(D[i])
    else:
        if D[i][1] == 'A':
            A.append(D[i])
# Заменяем (начиная с дорогих) товары списка 'N' товарами из списка 'A' (начиная с дешёвых)
N.sort(reverse=True)
k = 0
for i in range(len(N)):
    if N[i][1] == 'A':
        continue
    if sm - N[i][0] + A[k][0] <= m:
        sm = sm - N[i][0] + A[k][0]
        N[i] = A[k]
        k += 1
cnt_A = sum(1 for i in N if i[1] == 'A')
print(cnt_A, m - sm)  # 35 44


# https://stepik.org/lesson/1726035/step/7?unit=1749717
# https://kompege.ru/task   № 6056 ФИПИ 04.02.23 (Уровень: Базовый)
data = open('add/course_233165/26-2_07.txt').readlines()
D = [*map(int, data[1:])]
D.sort(reverse=True)
cnt = 1
prev = D[0]
for i in range(1, len(D)):
    if prev - D[i] >= 56:
        prev = D[i]
        cnt += 1
print(cnt, prev)  # 177 78


# https://stepik.org/lesson/1726035/step/8?unit=1749717
# https://kompege.ru/task   № 5446 Джобс 21.12.22 (Уровень: Средний)  👍
data = open('add/course_233165/26-2_08.txt').readlines()
n = int(data[0])
D = [tuple(map(int, i.split())) for i in data[1:]]
# Наибольший пакет получается, если идти от меньшей трубы к большей (от большей к меньшей получается меньше штук)
D.sort()
R = []
for k in range(n):  # пересмотр всех вариантов подбора труб
    cnt = 1
    cur = D[k]
    for i in range(k + 1, n):
        if (D[i][0] - D[i][1] * 2) - cur[0] >= 3:
            cur = D[i]
            cnt += 1
    R.append((cnt, D[k][0]))
R.sort(reverse=True)
print(*R[0])  # 36 106



# https://stepik.org/lesson/1726035/step/9?unit=1749717
# https://kompege.ru/task   № 9756 Основная волна 19.06.23 (Уровень: Средний)
data = open('add/course_233165/26-2_09.txt').readlines()
n = int(data[0])
D = [tuple(map(int, i.split())) for i in data[1:]]
# 1. Максимальное количество мероприятий.
# Сортируем по времени окончания мероприятия
D.sort(key=lambda x: (x[1],))
start, end = 0, 0
res = []
for i in range(n):
    st, en = D[i]
    if st >= end:
        res.append(D[i])
        start, end = st, en
# 2. Самое позднее время окончания последнего мероприятия
# проверяем что есть после окончания предпоследнего мероприятия
finish = [i for i in D if i[0] >= res[-2][1]]
finish.sort(key=lambda x: (-x[1],))
print(len(res), finish[0][1])  # 16 1345



# https://stepik.org/lesson/1726035/step/10?unit=1749717  🤔
# https://kompege.ru/task   № 14595 (Уровень: Средний)
data = open('add/course_233165/26-2_10.txt').readlines()
n = int(data[0])
D = [tuple(map(int, i.split())) for i in data[1:]]
# 1. Максимальное количество мероприятий.
start = end = clean = 0
res = []
D.sort(key=lambda x: (x[1],))
for i in range(n):
    st, en = D[i]
    if st >= end:
        start, end = st, en
        clean += 1
        if clean == 3:
            end += 10
            clean = 0
        res.append((start, end))
mx = len(res)  # 26
# 2. Максимально возможная длительность самой последней по счёту уборки аудитории
t = mx - mx % 3 - 1
en = res[t]  # (1199, 1231)  последняя пара после которой была уборка
# ставшиеся возможные пары (дальше анализируем головой)  🤔
tail = [i for i in D if i[0] >= en[1]]
# [(1246, 1259), (1252, 1260), (1257, 1262), (1237, 1273), (1264, 1273), (1260, 1283), (1231, 1291), (1241, 1294), (1272, 1298)]
# выбранные пары
# [(1257, 1262), (1272, 1298)]
max_clean = 1257 - 1231 + 10
print(mx, max_clean)  # 26 36




""" 26.3 Задание 26 ЕГЭ | Урок 3 """
# https://stepik.org/lesson/1726036/step/2?unit=1749718
# https://kompege.ru/task   № 813 Джобс 07.12.2020 (Уровень: Сложный)
data = open('add/course_233165/26-3_02.txt').readlines()
s, n = map(int, data[0].split())
D = [*map(int, data[1:])]
D.sort()
D_big = D[::-1]
sm = last = cnt = 0
for i in range(n):
    for k in [D_big, D]:
        if k[i] + sm <= s:
            sm += k[i]
            last = k[i]
            cnt += 1
        else:
            print(cnt, last)  # 573 229
            exit()


# https://stepik.org/lesson/1726036/step/3?unit=1749718
# https://kompege.ru/task   № 838 Джобс 14.12.2020 (Уровень: Сложный)
data = open('add/course_233165/26-3_03.txt').readlines()
n = int(data[0])
# s, n = map(int, data[0].split())
D1 = sorted(map(int, data[1:]))  # 1-большие файлы, 2-маленькие файлы
D2 = D1[::-1]
c1 = c2 = 0
sm1 = sm2 = 0
while n:
    sm1 += D1.pop()
    c1 += 1
    n -= 1
    while n and sm2 < sm1:
        sm2 += D2.pop()
        c2 += 1
        n -= 1
print(c1, c2)  # 2054 4612


# https://stepik.org/lesson/1726036/step/4?unit=1749718
# https://kompege.ru/task   № 936 Джобс 08.02.2021 (Уровень: Сложный)
# Грузим в рейс только самые тяжелые грузы из всех
data = open('add/course_233165/26-3_04.txt').readlines()
n, s = map(int, data[0].split())
D = sorted(map(int, data[1:]), reverse=True)
weight = 0
res = []
while D:
    for i in range(len(D)):
        if weight + D[i] <= s:
            weight += D[i]
            D[i] = 0
    res.append(weight)
    weight = 0
    D = [i for i in D if i]
print(len(res), res[-1])  # 423 501


# https://stepik.org/lesson/1726036/step/5?unit=1749718
# https://kompege.ru/task  № 1079 (Уровень: Средний)
data = open('add/course_233165/26-3_05.txt').readlines()
from statistics import mean
from math import ceil
n = int(data[0])
D = sorted(map(int, data[1:]))
a = D[ceil(n * 0.5) - 1]  # 546771
b = D[int(n * 0.75)]  # 778848
even = [i for i in D if not i % 2]
odd = [i for i in D if i % 2]
res = []
for el in [even, odd]:
    for i in range(len(el)):
        for k in range(i + 1, len(el)):
            mn = mean([el[i], el[k]])
            if a < mn < b:
                res.append(mn)
print(len(res), min(res))  # 2405042 546772


# https://stepik.org/lesson/1726036/step/6?unit=1749718
# https://kompege.ru/task  № 1257 Статград 26.04.2021 (Уровень: Средний)
data = open('add/course_233165/26-3_06.txt').readlines()
D = [*map(int, data[1:])]
cnt = res = 0
even, odd = [], []
for i in D:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)
mx_odd = max(odd)
for i in range(len(even)):
    for k in range(len(odd)):
        a, b = even[i], odd[k]
        if a + b <= mx_odd:  # сокращение вычислений
            if a + b in odd:  # четное + нечетное = нечетное !!!
                cnt += 1
                res = max(res, a + b)
print(cnt, res)  # 15 954387771


# https://stepik.org/lesson/1726036/step/7?unit=1749718
# https://kompege.ru/task  № 2652 Сборник ЕГЭ Ушакова 2022 (Уровень: Базовый)
data = open('add/course_233165/26-3_07.txt').readlines()
data = [*map(int, data[1:])]
D = dict()
for i in data:
    D.setdefault(i, 0)
    D[i] += 1
res = max(v for v in D.values())
print(len(D), res)  # 108 383


# https://stepik.org/lesson/1726036/step/8?unit=1749718
# https://kompege.ru/task  № 2480 Сборник ЕГЭ Ушакова 2022 (Уровень: Базовый)
data = open('add/course_233165/26-3_08.txt').readlines()
data = [tuple(map(int, i.split())) for i in data[1:]]
mx = max(data, key=lambda x: x[1])[1]
d = [0 for i in range(mx + 1)]
for el in data:
    for i in range(*el):
        d[i] = 1
c = 0
for i in range(1, len(d)):
    c += not d[i-1] and d[i]
print(c, sum(d))  # 1226 822094


# https://stepik.org/lesson/1726036/step/9?unit=1749718
# https://kompege.ru/task  № 2650 Сборник ЕГЭ Ушакова 2022 (Уровень: Средний)
data = open('add/course_233165/26-3_09.txt').readlines()
L, M, n = map(int, data[0].split())
dt = [(0,)] + [tuple(map(int, i.split())) for i in data[1:]] + [(L,)]
dt.sort()
cnt = mx = 0
for i in range(1, n + 2):
    p = dt[i][0] - sum(dt[i-1])
    if p >= M:
        cnt += 1
        mx = max(mx, p)
print(cnt, mx)  # 577 24426


# https://stepik.org/lesson/1726036/step/10?unit=1749718
# https://kompege.ru/task  № 2651 Сборник ЕГЭ Ушакова 2022 (Уровень: Средний)
data = open('add/course_233165/26-3_10.txt').readlines()
n = int(data[0])
data = [tuple(map(int, i.split())) for i in data[1:]]
D = dict()
for i in range(n):
    k, v = data[i]
    D.setdefault(k, [0 for _ in range(8)])
    D[k][v-1] += 1
res = []
for k, v in D.items():
    res.append((v.count(0), k))
res.sort(reverse=True)
stamp = sum(i[0] for i in res)
print(stamp, res[0][1])  # 38 1985




""" 26.4 Задание 26 ЕГЭ | Задачи прошлых лет """
# https://stepik.org/lesson/1726037/step/1?unit=1749719
# https://kompege.ru/task  № 9756 Основная волна 19.06.23 (Уровень: Средний)
data = open('add/course_233165/26-4_01.txt').readlines()
n = int(data[0])
data = [tuple(map(int, i.split())) for i in data[1:]]
data.sort(key=lambda x: (x[1],))
res = []
start, end = data[0]
for i in range(1, n):
    st, en = data[i]
    if end <= st:
        res.append((st, en))
        start, end = st, en
last = res[-2][1]
for i in range(1, n):
    if data[-i][0] >= last:
        last = data[-i][1]
        break
print(len(res) + 1, last)  # 16 1345


# https://stepik.org/lesson/1726037/step/2?unit=1749719
# https://kompege.ru/task  № 9793 Основная волна 20.06.23 (Уровень: Средний)
# Описание условия мутное!!!
# Другими словами: сортируем детали по минимальному времени (t шлиф. или t окрас.).
data = open('add/course_233165/26-4_02.txt').readlines()
data = [[*map(int, k.split())] + [i] for i, k in enumerate(data[1:], start=1)]
data = [[min(i[:2])] + [i.index(min(i[:2]))] + i for i in data]  # 0-шлифовка 1-окрашивание
data.sort()
ans = sum(not i[1] for i in data[:-1])  # количество деталей, которые будут отшлифованы (считаем нули)
print(data[-1][-1], ans)  # 895 488


# https://stepik.org/lesson/1726037/step/3?unit=1749719
# https://kompege.ru/task  № 17537 Основная волна 07.06.24 (Уровень: Средний)
data = open('add/course_233165/26-4_03.txt').readlines()
N, R, S = map(int, data[0].split())  # кол-во: занятых мест в зале, рядов в зале, мест в каждом ряду
data = [tuple(map(int, i.split())) for i in data[1:]]  # номер ряда, номер места занятого кресла
DS = {k: [R + 1] for k in range(1, S + 1)}  # k - номер места
for el in data:
    row, seat = el
    DS[seat] += [row]

res = []
for i in range(2, S + 1):  # нумерация мест с 1-цы
    s1, s2 = min(DS[i - 1]), min(DS[i])
    res += [(min([s1, s2]) - 1, i)]
res.sort(reverse=True)
print(*res[0])  # 9991 5643

# долгое решение (~21 сек) но можно использовать если нужно искать произвольные промежутки (в рядах)
data = open('add/course_233165/26-4_03.txt').readlines()
N, R, S = map(int, data[0].split())  # кол-во: занятых мест в зале, рядов в зале, мест в каждом ряду
data = [tuple(map(int, i.split())) for i in data[1:]]  # номер ряда, номер места занятого кресла
DS = {k: [0 for _ in range(R + 1)] for k in range(1, S + 1)}  # k - номер места
for el in data:
    row, seat = el
    DS[seat][row] = 1

res = []
for i in range(2, S + 1):
    s1, s2 = DS[i - 1], DS[i]
    for r in range(1, R + 1):
        if s1[r] + s2[r]:
            res.append((r - 1, i))  # r-1 от занятых кресел, к свободным перед ними
            break
res.sort(reverse=True)
print(*res[0])  # 9991 5643


# https://stepik.org/lesson/1726037/step/4?unit=1749719
# https://kompege.ru/task  № 17565 Основная волна 08.06.24 (Уровень: Базовый)
data = open('add/course_233165/26-4_04.txt').readlines()
N, S = map(int, data[0].split())  # кол-во кандидатов, кол-во мест
data = [tuple(map(int, i.split())) for i in data[1:]]  # ID, оценка 1, оценка 2, оценка 3, собеседование
data = [tuple([i[0], sum(i[1:4]), i[4]]) for i in data]  # ID, сумма 3-х оценок, собеседование
data.sort(key=lambda x:(-x[1], -x[2], x[0]))

if data[S - 1][1] == data[S][1]:
    half_score = data[S][1]
    score_ls = [i for i in data if i[1] > half_score]
    half_score_ls = [i for i in data if i[1] == half_score]
else:
    score_ls = data[:S]
    half_score_ls = []
print(score_ls[-1][0], len(half_score_ls))  # 7600410 14



# https://stepik.org/lesson/1726037/step/5?unit=1749719
# https://kompege.ru/task  № 17643 Основная волна 19.06.24 (Уровень: Базовый)
from statistics import mean
data = open('add/course_233165/26-4_05.txt').readlines()
data = [tuple(map(int, i.split())) for i in data[1:]]  # артикул, цена, статус (0=продан, 1=не продан)
avr = mean(i[1] for i in data)
expensive = [i for i in data if i[1] > avr]
dt = dict()  # key=артикул   val=продано, цена, осталось
for i in expensive:
    k = i[0]
    dt.setdefault(k, [0, i[1], 0])
    if i[2]:
        dt[k][2] += 1
    else:
        dt[k][0] += 1

res = [[*v] for v in dt.values()]
res.sort(key=lambda x: (-x[0], -x[1], x[2]))  # артикул для ответа не нужен
a, b, c = res[0]
print(a * b, c)  # 43656 36


# https://stepik.org/lesson/1726037/step/6?unit=1749719
# https://kompege.ru/task  № 17881 Демоверсия 2025 (Уровень: Базовый)
from statistics import mean
data = open('add/course_233165/26-4_06.txt').readlines()
n = int(data[0])
data = [tuple(map(int, i.split())) for i in data[1:]]  # id, grades (2-5)
data = [[i[1:].count(2), mean(i[1:]), i[0]] for i in data]  # count(2), mean, id

winner = [i for i in data if not i[0]]
looser = [i for i in data if i[0] > 2]  # студенты, которые имеют более двух «двоек»
winner.sort(key=lambda x: (-x[1], x[2]))
looser.sort(key=lambda x: (x[0], x[2]))
ans_1 = winner[n // 4 - 1][2]  # -1 т.к. индексы идут с нуля (n - от числа ВСЕХ студентов!!! Это гарантируется!!!)
ans_2 = looser[0][2]
print(ans_1, ans_2)  # 52326 635


# https://stepik.org/lesson/1726037/step/7?unit=1749719
# https://kompege.ru/task  № 23208 Основная волна 10.06.25 (Уровень: Базовый)
# Описание условия мутное!!!
# Другими словами: сортируем детали по минимальному времени (t шлиф. или t окрас.).
data = open('add/course_233165/26-4_07.txt').readlines()
data = [[*map(int, k.split())] + [i] for i, k in enumerate(data[1:], start=1)]
data = [[min(i[:2])] + [i.index(min(i[:2]))] + i for i in data]  # 0-шлифовка 1-окрашивание
data.sort()
ans = sum(not i[1] for i in data[:-1])  # количество деталей, которые будут отшлифованы (считаем нули)
print(data[-1][-1], ans)  # 503 478


# https://stepik.org/lesson/1726037/step/8?unit=1749719
# https://kompege.ru/task  № 23283 Основная волна 11.06.25 (Уровень: Базовый)
data = open('add/course_233165/26-4_08.txt').readlines()
K, N = [int(i) for i in data[:2]]   # кол-во: окон, граждан
data = [tuple(map(int, i.split())) for i in data[2:]]  # время: начала / окончания
# data.sort(key=lambda x: x[1])  # если нужно найти максимальное кол-во посетителей
data.sort()
wind = [0 for _ in range(K)]
cnt = fin = 0
for d in data:
    st, en = d
    for i in range(K):
        if wind[i] < st:
            wind[i] = en
            cnt += 1
            fin = i
            break
print(cnt, fin + 1)  # 793 2


# https://stepik.org/lesson/1726037/step/9?unit=1749719
# https://kompege.ru/task  № 23383 Резервный день 19.06.25 (Уровень: Базовый)
data = open('add/course_233165/26-4_09.txt').readlines()
P = int(data[0])    # кол-во: контрольных точек
data = [tuple(map(int, i.split())) for i in data[1:]]  # номер: спортсмена / контрольной точки
Dp = dict()  # key: контрольная точка, val: список спортсменов
for el in data:
    sport, point = el
    Dp.setdefault(point, set())  # set() т.к. спортсмен может посетить одну и ту же контрольную точку несколько раз
    Dp[point] |= {sport}

res = []
for k, v in Dp.items():
    cnt = c = 1
    v = list(v)
    v.sort()
    for i in range(len(v) - 1):
        if v[i+1] - v[i] == 1:
            c += 1
            cnt = max(cnt, c)
        else:
            c = 1
    res.append((cnt, k))
res.sort(key=lambda x: (-x[0], x[1]))
print(*res[0])  # 56 30113


# https://stepik.org/lesson/1726037/step/10?unit=1749719
# https://kompege.ru/task  № 23765 Демоверсия 2026 (Уровень: Базовый)
data = open('add/course_233165/26-4_10.txt').readlines()
n = int(data[0])    # кол-во продуктов
data = [[i, *(map(int, k.split()))] for i, k in enumerate(data[1:], 1)]  # срок: хранения продукта / годности после вскрытия
data = [i + [i[1] < i[2], min(i[1:])] for i in data]  # True-хранения, False-годности
data.sort(key=lambda x: x[4])
last = data[-1]  # [564, 97582, 97257, False, 97257]
print(last[0], sum(not i[3] for i in data) - 1)  # -1  т.к. после last
# 564 444





""""""
""" Варианты """

# 29.2 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/12?unit=1753726
# https://kompege.ru/task  № 19256 ЕГКР 21.12.24 (Уровень: Базовый)
dt = open('02_26.txt').readlines()
n = int(dt[0])
d = [tuple(map(int, i.split())) for i in dt[1:]]  # id, N-task
d = [i for i in set(d)]  # убираем дубликаты
d.sort()
dc = dict()
for i in d:
    dc.setdefault(i[0], [])  # key=id   val=номера задач
    dc[i[0]] += [i[1]]

res = []
for k, v in dc.items():
    c = mx = 1
    if len(v):
        for i in range(1, len(v)):
            if v[i] - v[i-1] == 1:
                c += 1
                mx = max(mx, c)
            else:
                c = 1
    res.append((k, mx))
res.sort(key=lambda x: (-x[1], x[0]))
print(*res[0])  # 40031 148


# 30.2 Вариант 3 | Часть 2
# https://stepik.org/lesson/1730528/step/12?unit=1754357
# https://kompege.ru/task  № 20815 Апробация 05.03.25 (Уровень: Базовый)
s = open('03_26.txt').readlines()
n, k = map(int, s[0].split())  # количество кандидатов / количество мест
dt = [[*map(int, i.split())] for i in s[1:]]
dt = [i + [sum(i[1:])] for i in dt]   #  [id, балл, балл, балл, собeседование, сумма]
dt.sort(key=lambda x: (-x[5], -x[4], x[0]))
half = ans2 = 0
if dt[k-1][5] == dt[k][5]:  # есть полупроходной балл
    half = dt[k][5]
    win = [i for i in dt if i[5] > half]
    ans1 = win[-1][0]
    ans2 = sum(i[5] == half for i in dt)
else:  # полупроходной балл отсутствует
    ans1 = dt[k-1][0]
print(ans1, ans2)  # 45539 127


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/12?unit=1760676
# https://kompege.ru/task  № 21910 Открытый вариант 2025 (Уровень: Базовый)
s = open('04_26.txt').readlines()
n = int(s[0])
d = [*map(int, s[1:])]
d.sort(reverse=True)
cur = d[0]
c = 1
for i in range(1, n):
    if cur - d[i] >= 9:
        c += 1
        cur = d[i]
print(c, cur)  # 1040 57



# 32.2 Вариант 5 | Часть 2
# https://stepik.org/lesson/1754189/step/12?unit=1778648
# https://kompege.ru/task  № 21719 ЕГКР 19.04.25 (Уровень: Базовый)
s = open('05_26.txt').readlines()
n = int(s[0])
dt = [tuple(map(int, i.split())) for i in s[1:]]
dt = [i for i in set(dt)]  # убираем дубликаты
dt.sort()
d = dict()
for i in dt:
    k, v = i
    d.setdefault(k, [])
    d[k] += [v]

res = []
for k in d:
    val = d[k]
    mx = c = 1
    for i in range(1, len(val)):
        if val[i] - val[i-1] == 2:
            c += 1
            mx = max(mx, c)
        else:
            c = 1
    res.append((mx, k))
res.sort(key=lambda x: (-x[0], x[1]))
print(res[0][1], res[0][0])  # 10135 42


# 333.2 Вариант 6 | Часть 2
# https://stepik.org/lesson/1943171/step/12?unit=1969925
# https://kompege.ru/task  № 23208 Основная волна 10.06.25 (Уровень: Базовый)
# Есть вопросы к условию задачи 🤔
s = open('06_26.txt').readlines()
dt = [[i, *map(int, k.split())] for i, k in enumerate(s[1:], 1)]  # номер, Т.шлиф, Т.окр
dt = [i + [i[1] < i[2],  min(i[1:])] for i in dt]  # номер, Т.шлиф, Т.окр, 1/0(шлиф/окр), Т.мин

grind = [i for i in dt if i[3]]
col = [i for i in dt if not i[3]]
grind.sort(key=lambda x: x[4])
col.sort(key=lambda x: x[4])
print(col[-1][0], len(grind))  # 503 478


# 34.2 Вариант 7 | Часть 2
# https://stepik.org/lesson/1943174/step/12?unit=1969928
# https://kompege.ru/task  № 23283 Основная волна 11.06.25 (Уровень: Базовый)
s = open('07_26.txt').readlines()
# s = open('test.txt').readlines()
win, n = map(int, s[:2])
d = [[*map(int, i.split())] for i in s[2:]]
d.sort()
# d.sort(key=lambda x: x[1])  # если нужно найти максимальное кол-во посетителей
mfs = [0 for _ in range(win)]
cnt = cur = 0
for i in d:
    st, en = i
    for w in range(win):
        if st > mfs[w]:
            cnt += 1
            mfs[w] = en
            cur = w + 1
            break
print(cnt, cur)  # 793 2


# 36.2 Вариант 9 | Часть 2
# https://stepik.org/lesson/1943186/step/12?unit=1969940
# https://kompege.ru/task  № 23765 Демоверсия 2026 (Уровень: Базовый)
s = open('09_26.txt').readlines()
d = [[i, *map(int, k.split())] for i, k in enumerate(s[1:], 1)]
d = [i + [i[1]<i[2], min(i[1:])] for i in d]   # id, t1, t2, True-хран/False-годн, min(t)
d.sort(key=lambda x: (-x[3], x[4]))
print(d[-1][0], sum(not i[3] for i in d) - 1)  # -1  т.к. после last
# 564 444


# 35.2 Вариант 8 | Часть 2
# https://stepik.org/lesson/1943181/step/12?unit=1969936  👍
# https://kompege.ru/task  № 23570 Пересдача 03.07.25 (Уровень: Сложный)
# best variant
s = open('08_26.txt')
n, m = map(int, s.readline().split())  # кол-во: участков / моделей снегоуборщиков
power = [int(s.readline()) for _ in range(n)]  # требуемая мощность для каждого участка
data = [[*map(int, s.readline().split())] for _ in range(m)]  # мощность - цена
# Оптимизация. Среди всех моделей с одинаковой мощностью оставляем самую дешевую.
dn = [[10**10, i] for i in range(m)]  # цена, мощность
for pwr, coin in data:  # мощность - цена
    dn[pwr][0] = min(coin, dn[pwr][0])
dn = [i for i in dn if i[0] != 10**10]  # (95384 --> 1000)
dn.sort()
# Получение ответа
sm = mx = 0  # Суммарная стоимость, макс. мощность
for p in power:
    for coin, pwr in dn:  # цена, мощность
        if p <= pwr:
            sm += coin
            mx = max(mx, pwr)
            break
print(sm, mx)  # 1879667450 924



s = open('08_26.txt')
n, m = map(int, s.readline().split())  # кол-во: участков / моделей снегоуборщиков
power = [int(s.readline()) for _ in range(n)]  # требуемая мощность для каждого участка
data = [[*map(int, s.readline().split())] for _ in range(m)]  # 95384   # мощность - цена
# 1 оптимизация. Среди всех моделей с одинаковой ценой оставляем самую мощную.
d = dict()
for v, k in data:
    d.setdefault(k, [])   # цена, мощность
    d[k] += [v]
dn = []
for k, v in d.items():
    dn += [(k, max(v))]  # цена, мощность
dn.sort()  # 61369
# 2 оптимизация. Для каждой текущей мощности модели удаляем все последующие меньшей или равной мощности
for i in range(len(dn)):  # текущая мощность
    if not dn[i]:
        continue
    for k in range(i+1, len(dn)):  # последующие мощности
        if not dn[k]:
            continue
        if dn[k][1] <= dn[i][1]:
            dn[k] = 0  # заменяем лишние мощности для их последующего удаления
dn = [i for i in dn if i]  # 173  (95384 --> 173)
# Получение ответа
sm = mx = 0  # Суммарная стоимость / макс. мощность
for p in power:
    for k, v in dn:  # цена, мощность
        if p <= v:
            sm += k
            mx = max(mx, v)
            break
print(sm, mx)  # 1879667450 924
