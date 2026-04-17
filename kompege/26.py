""" https://kompege.ru/task """
"""
225 507 788 889 954 
1304 1395 1868
2149 2612 2613 2614 3664
4604(=4712) 4629 4660 4712 7096
10107 11681 12256 13394 15341 17537 17881
21598 21719 21910(=21424) 23765 27779
"""


# 225 Джобс 14.09.2020 (Уровень: Базовый)
f = open('add/26/26_225.txt').readlines()
M, N = map(int, f[0].split())
d = [*map(int, f[1:])]
d.sort(reverse=True)
sm = d[0]
c = 1
mn = None
for i in range(1, N):
    if d[i] + sm <= M:
        sm += d[i]
        c += 1
        mn = d[i]
    else:
        continue
print(c, mn)  # 1054 732
# print(sm)  # 1000000


# 507 Джобс 19.10.2020 (Уровень: Средний)
f = open('add/26/26_507.txt').readlines()
n = int(f[0])  # количество товаров кратное 20
d = [*map(int, f[1:])]
d.sort()
# Первая акция
one = int(n * 0.7)
a = sum(i * 0.7 for i in d[:one]) + sum(i * 0.6 for i in d[one:])
# Вторая акция
two = int(n * 0.5)
b = sum(i * 0.6 for i in d[:two]) + sum(i * 0.65 for i in d[two:])
# Итог
res1 = int(abs(a - b))
res2 = d[-1] * (0.6, 0.65)[b > a]
print(res1, int(res2))  # 63792 600


# 788 Джобс 30.11.2020 (Уровень: Средний)
f = open('add/26/26_788.txt').readlines()
D, E, N = map(int, f[0].split())
data = [*map(int, f[1:])]
dn = sorted([i for i in data if i > 500])
en = sorted([i for i in data if i <= 500])

def fn(ls: list, n: int):
    sm = c = 0
    for i in range(len(ls)):
        if sm + ls[i] <= n:
            sm += ls[i]
            c += 1
        else:
            sm -= ls[i-1]
            break
    for i in range(len(ls)-1, 0, -1):
        if sm + ls[i] <= n:
            return c, ls[i]

d1, d2 = fn(dn, D)
e1, e2 = fn(en, E)
print(d1 + e1, d2 + e2)  # 13 1381


# 889 Джобс 25.12.2020 (Уровень: Сложный)
data = open('26.txt')
N, M = map(int, next(data).split())  # количество грузов / грузоподъёмность грузовика (10_000)
d = [*map(int, data)]
d1 = [i for i in d if 310 <= i <= 320]
d2 = []
[d.remove(i) for i in d1]
d.sort()
sm = sum(d1)
for i in range(len(d)):
    if sm + d[i] <= M:
        sm += d[i]
        d2.append(d[i])
    else:
        sm -= d[i-1]
        d2.pop()
        break
# ищем максимальный по величине груз для последнего места
d.sort(reverse=1)
for i in range(len(d)):
    if sm + d[i] <= M:
        sm += d[i]
        d2.append(d[i])
        break
# для второго по величине груза, и т.д. смотрим глазами
print(len(d1) + len(d2), sm)  # 113 9999


# 954 (Уровень: Базовый)
f = open('add/26/26_954.txt').readlines()
N, K, M = map(int, f[0].split())
data = sorted([*map(int, f[1:])], reverse=True)
dk = sum(0.2 * i for i in data[:K])
dm = sum(0.1 * i for i in data[K:K + M])
a = data[K + M]
b = int(dk + dm)
print(a, b)  # 7500 314590




# 1304 Открытый вариант КЕГЭ (Уровень: Базовый)
f = open('add/26/26_1304.txt').readlines()
s, n = map(int, f[0].split())  # грузоподъёмность, количество груза
d = [*map(int, f[1:])]
d.sort()
sm = cnt = 0
for i in range(n):
    if sm + d[i] <= s:
        cnt += 1
        sm += d[i]
    else:
        sm -= d[i-1]  # убираем последний добавленный груз (будем искать более тяжелый)
        break
for i in range(n-1, 0, -1):
    if sm + d[i] <= s:  # самый тяжелый груз при последней загрузке
        print(cnt, d[i])  # 1612 90
        break


# 1395 (Уровень: Базовый)
f = open('add/26/26_1395.txt').readlines()
s, n = map(int, f[0].split())
d = [*map(int, f[1:])]
d.sort()
idx = sm = 0
for i in range(n):
    if sm + d[i] <= s:
        sm += d[i]
        idx = i
    else:
        break
a = n - idx - 1
b = sum(d[idx+1:])
print(a, b)  # 7655 542450


# 1868 Основная волна 2021 (Уровень: Базовый)
f = open('add/26/26_1868.txt').readlines()
data = [[*map(int, i.split())] for i in f[1:]]  # ряд и место выкупленного билета
d = dict()
for k, v in data:
    d.setdefault(k, [])
    d[k] += [v]
d = [[k, v] for k, v in d.items()]
d.sort(reverse=True)
for r, s in d:
    if len(s) > 1:
        s.sort()
        for i in range(len(s) - 1):
            if s[i + 1] - s[i] == 3:
                print(r, s[i] + 1)  # 8631 7311
                exit()




# 2149 (Уровень: Базовый)
f = open('add/26/26_2149.txt').readlines()
n, m = map(int, f[0].split())
p, v = [], []
for i in map(int, f[1:]):
    if i > 100:
        v.append(i)
    else:
        p.append(i)
p.sort()
v.sort()
sm = cnt = 0
for i in v:
    if sm < m / 2:
        sm += i
        cnt += 1
    else:
        break  # собрали видео
for i in range(len(p)):  # начинаем собирать картинки
    if p[i] + sm <= m:
        cnt += 1
        sm += p[i]
    else:
        sm -= p[i]
        break
for i in range(len(p) - 1, 0, -1):  # ищем макс. большую последнюю картинку
    if p[i] + sm <= m:
        sm += p[i]
        print(m - sm, cnt)  # 0 7347
        break


# 2612 (Уровень: Базовый)
from statistics import mean
f = open('add/26/26_2612.txt').readlines()
n, m = map(int, f[0].split())
d = [*map(int, f[1:])]
d.sort(reverse=True)
top = d[:m]
tail = d[m:]
half = 0  # отсутствие полупроходного балла
if top[-1] == tail[0]:  # наличие полупроходного балла
    half = top[-1]
a = top[-top.count(half) - 1]  # минимальный балл гарантируемого прохода
b = mean(tail[tail.count(half):])  # средний балл тех, кто не проходит
print(a, int(b))  # 276 246


# 2613 (Уровень: Базовый)
f = open('add/26/26_2613.txt').readlines()
d = dict()
for i in f[1:]:
    k, v = map(int, i.split())  # ряд, место
    d.setdefault(k, [])
    d[k] += [v]
d = [[k, v] for k, v in d.items()]
d.sort(reverse=True)
res = []
for r, s in d:
    s.sort()
    mx = 0
    c = 1
    for i in range(len(s) - 1):
        if s[i+1] - s[i] == 1:
            c += 1
            mx = max(mx, c)
        else:
            c = 1
    res.append([mx, r])
res.sort(reverse=True)
print(res[0][1], res[0][0])  # 99 14


# 2614 (Уровень: Базовый)
f = open('add/26/26_2614.txt').readlines()
s, n = map(int, f[0].split())  # выделенная сумма, значения стоимости
book, rare, enc = [], [], []
for i in map(int, f[1:]):
    if i > 3000:
        rare.append(i)
    elif i < 2000:
        book.append(i)
    else:
        enc.append(i)
sm = sum(enc) + min(rare) + max(rare)
c = len(enc) + 2
book.sort()
for i in range(len(book)):
    if sm + book[i] <= s:
        sm += book[i]
        c += 1
    else:
        sm -= book[i - 1]
        break
for i in range(len(book) - 1, 0, -1):
    if sm + book[i] <= s:
        print(c, book[i])  # 398 273
        break


# 3664 (Уровень: Базовый)
f = open('add/26/26_3664.txt').readlines()
# f = open('txt.txt').readlines()
D = dict()
res = []
for i in f[1:]:
    k, v = map(int, i.split())  # ряд, место
    D.setdefault(k, [])
    D[k] += [v]
for k, v in D.items():
    v.sort()
    mx = 0
    for i in range(len(v) - 1):
        mx = max(mx, v[i+1] - v[i] - 1)
    res.append([mx, k])
res.sort(reverse=True)
print(res[0][1], res[0][0])  # 9570 9743




# 4604 Основная волна 2022 (Уровень: Базовый)
f = open('add/26/26_4604.txt').readlines()
# f = open('txt.txt').readlines()
n = int(f[0])  # количество коробок
d = [*map(int, f[1:])]   # значения длин сторон коробок
d.sort(reverse=True)
cur = d[0]
cnt = 1
for i in d:
    if cur - i >= 3:
        cnt += 1
        cur = i
print(cnt, cur)  # 2767 51


# 4629 Основная волна 2022 (Уровень: Базовый)
f = open('add/26/26_4629.txt').readlines()
n = int(f[0])  # количество товаров
d = [*map(int, f[1:])]   # цены товаров
d.sort(reverse=True)
user = sum(i / 2 for i in d[:n//4]) + sum(i for i in d[n//4:])
d.sort()
store = sum(i / 2 for i in d[:n//4]) + sum(i for i in d[n//4:])
print(int(user), int(store))  # 39434611 48825239


# 4660 Основная волна 2022 (Уровень: Базовый)
f = open('add/26/26_4660.txt').readlines()
n = int(f[0])  # N товаров для закупки
d = [*map(int, f[1:])]   # стоимость товаров
d.sort(reverse=True)
user = 0
for i in range(0, n, 4):
    user += sum(d[i:i+3]) + d[i+3] / 2
store = sum(i for i in d[:-n//4]) + sum(i / 2 for i in d[-n//4:])
print(int(user), int(store))  # 44101521 48825239


# 7096 OpenFIPI (Уровень: Базовый)
f = open('add/26/26_7096.txt').readlines()
D = [*map(int, f[1:])]
D.sort(reverse=True)
cur = D[0]
cnt = 1
for i in D[1:]:
    if cur - i >= 11:
        cnt += 1
        cur = i
print(cnt, cur)  # 854 54





# 10107 Демоверсия 2024 (Уровень: Средний)
fl = open('26_10107.txt').readlines()
d = [[*map(int, i.split())] for i in fl[1:]]
# сортируем по возрастанию времени окончания.
d.sort(key=lambda x: x[1])
res = []
end = 0
for i in d:
    st, en = i
    if st >= end:
        res.append(i)
        end = en
# ищем самое позднее время начала последнего мероприятия от окончания предпоследнего отобранного мероприятия
mx = 0
for i in d:
    if res[-2][1] <= i[0]:
        mx = max(mx, i[0])
print(len(res), mx - res[-2][1])  # 32 15


# 11681 (Уровень: Базовый) ❓
f = open('add/26/26_11681.txt').readlines()
n, k = map(int, f[0].split())  # N товаров для закупки,  K товаров для скидки
d = [[*map(int, i.split())] for i in f[1:]]  # стоимость товара,  процент скидки
for i in d:
    i += [i[0] * i[1] / 100]  # выгода при скидке
d.sort(key=lambda x: (-x[2], x[0]))
a = sum(i[0] - i[2] for i in d[:k]) + sum(i[0] for i in d[k:])
b = d[k-1][2]  # расхождение между условием, примером и принимаемым ответом.
# Принимается выгода товара купленного со скидкой, с минимально возможной стоимостью.
# А требовали минимальную возможную стоимость товара, купленного со скидкой.
print(int(a), int(b))  # 2903432767 194784 ❓


# 12256 ЕГКР 16.12.23 (Уровень: Базовый)
f = open('add/26/26_12256.txt').readlines()
S, N = map(int, f[0].split())
d = sorted(map(int, f[1:]))
sm = cnt = 0
for i in range(N):
    if sm + d[i] <= S:
        sm += d[i]
    else:
        sm -= d[i-1]
        cnt = i
        break
# ищем самую тяжёлую посылку
for i in range(-1, -N, -1):
    if sm + d[i] <= S:
        print(cnt, d[i])  # 629 50
        break


# 13394 Открытый курс "Слово пацана" (Уровень: Базовый) 👍
from math import ceil
f = open('add/26/26_13394.txt').readlines()
D = [*map(int, f[1:])]
sale = [i for i in D if i > 350]
not_sale = sum(i for i in D if i <= 350)
sale.sort(reverse=True)
# Тактика покупателя
# Только если len(sale) делится на 3 ровно, иначе остаток от деления (самые дешевые товары) продавать без скидки
sm_user = 0
for i in range(0, len(sale), 3):
    a, b, c = sale[i:i + 3]
    sm_user += ceil(a + b + c * 0.25)
print(not_sale + sm_user, end=' ')
# Тактика продавца
# Только если len(sale) делится на 3 ровно, иначе остаток от деления (самые дорогие товары) продавать без скидки
idx = len(sale) // 3
sm_store = sum(sale[:-idx]) + ceil(sum(i * 0.25 for i in sale[-idx:]))
print(not_sale + sm_store)  # 3924309 4275729


# 15341 Досрочная волна 2024 (Уровень: Базовый)
f = open('add/26/26_15341.txt').readlines()
n = int(f[0])
d = [*map(int, f[1:])]
d.sort(reverse=True)
cur = d[0]
c = 1
for i in d[1:]:
    if cur - i >= 8:
        c += 1
        cur = i
print(c, cur)  # 1198 54


# 17537 Основная волна 07.06.24 (Уровень: Средний)
""" ряды - столбцы """
f = open('add/26/26_17537.txt').readlines()
N, R, C = map(int, f[0].split())  # ticket, row, col
data = [[*map(int, i.split())] for i in f[1:]]  # row, col
dc = {i: R+1 for i in range(1, C+1)}  # R+1 если в столбце нет занятых мест (виртуальный ряд после последнего)
for i in data:
    row, col = i
    dc[col] = min(dc[col], row)  # первый занятый ряд для данного вертикального значения места
res = []
for i in range(2, C + 1):
    m = min(dc[i-1], dc[i]) - 1  # -1 переходим на ряд ниже занятого места
    res.append([m, i])
res.sort()
print(*res[-1])  # 9991 5643


# 17881 Демоверсия 2025 (Уровень: Базовый)
from statistics import mean
f = open('26.txt').readlines()
n = int(f[0])
d = [[*map(int, i.split())] for i in f[1:]]
d222 = [i for i in d if i.count(2) == 3]  # получили по 3 двойки
d222.sort()

d = [i + [mean(i[1:])] for i in d if not i.count(2)]  # без двоек
d.sort(key=lambda x: (-x[-1], x[0]))
a = d[n // 4 - 1][0]  # n // 4 - 1  ✅ т.к индекс начинается с нуля
b = d222[0][0]
print(a, b)  # 52326 635




# 20910 Апробация 05.03.25 (Уровень: Средний)
# получение данных
f = open('add/26/26_20910.txt').readlines()
_, R, S = map(int, f[0].split())  # кол-во занятых мест, кол-во рядов, кол-во мест в ряду
res = []
d = {k: [] for k in range(1, S + 1)}  # {место: [ряды], ...}
for n in f[1:]:
    r, s = map(int, n.split())  # номер ряда, номер места
    d[s] += [r]
# анализ данных
for i in range(1, S):  # ⛔ для занятого 1-го ряда алгоритм не подходит
    a = min(d[i]) if d[i] else R+1
    b = min(d[i+1]) if d[i+1] else R+1
    res.append((min([a, b]) - 1, i))
res.sort(key=lambda x: (-x[0], x[1]))
print(*res[0])  # 21028 6660


# 21598 (Уровень: Средний) 👍
f = open('add/26/26_21598.txt').readlines()
n = int(f[0])  # количество сотрудников
data = [[*map(int, i.split())] for i in f[1:]]   # время входа, время выхода
time = [0] * 1441  # ноль будет означать те моменты, когда кол-во сотрудников не меняется
for el in data:
    st, en = el
    time[st] = 1  # фиксируем моменты прихода и ухода сотрудников
    time[en] = 1
change = [i for i in range(1441) if time[i] != 0]  # индекс списка - минута в которую изменялось кол-во сотрудников
# res - временные интервалы между событиями изменения кол-ва сотрудников.
# Начальный и конечный добавляем вручную.
res = [change[0] - 0, 1440 - change[-1]]
# for i in range(len(change) - 1):
#     res.append(change[i + 1] - change[i])
for a, b in zip(change, change[1:]):  # zip место индексов
    res.append(b - a)
print(change[-2], max(res))  # 1431 13


# 21719 ЕГКР 19.04.25 (Уровень: Базовый)
f = open('add/26/26_21719.txt').readlines()
n = int(f[0])  # количество решений
data = set(tuple(map(int, i.split())) for i in f[1:])   # идентификатор студента, номер задачи (+ удалены дубли)
d = dict()  # подготовка
for i in data:
    k, v = i
    d.setdefault(k, [])
    d[k] += [v]

res = []  # обработка
for k, v in d.items():
    sm = 0
    c = 1
    v.sort()
    for i in range(len(v) - 1):
        if v[i+1] - v[i] == 2:
            c += 1
            sm = max(sm, c)
        else:
            c = 1
    res.append((k, sm))
res.sort(key=lambda x: (-x[1], x[0]))
print(*res[0])  # 10135 42


# 21910 Открытый вариант 2025 (Уровень: Базовый)
f = open('add/26/26_21910.txt').readlines()
n = int(f[0])  # количество коробок
d = [*map(int, f[1:])]   # значения длин сторон коробок
d.sort(reverse=True)
cur = d[0]
cnt = 1
for i in d:
    if cur - i >= 9:
        cnt += 1
        cur = i
print(cnt, cur)  # 1040 57


# 23765 Демоверсия 2026 (Уровень: Базовый)
# ✔️ Получается что работаем только со 'сроком годности после вскрытия'
d = open('26.txt').readlines()
dt = [[k, *map(int, i.split())] for k, i in enumerate(d[1:], 1)]
b = [i for i in dt if i[1] > i[2]]
b.sort(key=lambda x: -x[2])  # по значению срока годности (убывание)
print(b[0][0], len(b) - 1)  # 564 444  (len(b)-1  сколько позиций осталось после первого в списке 'b')


# 27779 Апробация 04.03.26 (Уровень: Базовый)
f = open('add/KIM_25164989/26_27779.txt').readlines()
# f = open('add/KIM_25164989/test.txt').readlines()
N = int(f[0])
d = sorted(map(int, f[1:]), reverse=True)
c = 1
cur = d[0]
for i in range(N-1):
    if cur - d[i] >= 8:
        c += 1
        cur = d[i]
print(c, cur)  # 1159 57



