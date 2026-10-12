""" https://kompege.ru/task """
"""
225 507 788 889 954 
1304 1395 1868
2149 2362 2480 2612 2613 2614 2652 2686 3664
4205(=7274) 4604(=4712) 4629 4660 4712=(4604) 5066 5228 5643 6800 7096
10107 11681 12256 13394 15341 17537 17643 17881 19256 19752 19890
20815 21598 21719 21910(=21424) 22127 23175 23208 23259 23283 23383 23765 24897 25363 27636 27779 28945
30401 31131 31137 31165 31232 31370 31520 
"""


""" Задача взята на мой курс """
# 225 Джобс 14.09.2020 (Уровень: Базовый)
f = open('add/26/26_225.txt').readlines()
M, N = map(int, f[0].split())
d = [*map(int, f[1:])]
d.sort(reverse=True)
sm = d[0]  # сумма файлов
c = idx = 1
for i in range(1, N):
    if d[i] + sm <= M:
        sm += d[i]
        c += 1
    else:
        # print(c, d[i])  # Случай, если меньший файл так и не будет найден.
        idx = i
        break
for i in range(idx, N):  # ищем файл на оставшееся место
    if sm + d[i] <= M:
        print(c + 1, d[i])  # 1054 732  Файл нашелся
        break


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


""" Задача взята на мой курс """
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


# 2362 Сборник ЕГЭ Ушакова 2022(Уровень: Базовый)
f = open('26.txt').readlines()  # получить список строк без \n
N, S = map(int, f[0].split())
d = dict()
for i in f[1:]:
    k, v = map(int, i.split())  # k - тип, v - цена
    d.setdefault(k, [])
    d[k].append(v)
cnt = SM = 0
for k, v in d.items():
    v.sort()
    rub = 0
    for i in v:
        if rub + i <= S:
            rub += i
            cnt += 1
            SM += i  # ❗❗❗ Постоянно добавляем. Возможно что вся партия будет дешевле "S"
        else:
            break
print(cnt, SM)  # 609 31303



# 2480 Сборник ЕГЭ Ушакова 2022(Уровень: Базовый)
f = open('add/26/26_2612.txt').readlines()
d = sorted([*map(int, i.split())] for i in f[1:])
res = [d[0]]
for a1, a2 in d:
    b1, b2 = res[-1]
    if b2 >= a1:
    # if b1 <= a2 and b2 >= a1: # лишние проверки
        # res[-1][0] = min(a1, b1) # лишние проверки
        res[-1][1] = max(a2, b2)
    else:
        res += [[a1, a2]]
sm = sum(b-a for a, b in res)
print(len(res), sm)  # 1226 822094

# Решение через список
f = open("add/26/26_2480.txt")
next(f)
a = [0] * 2_000_000
cnt = 0
for el in f:
    x, y = map(int, el.split())
    for i in range(x, y):
        a[i] = 1  # ставим '1' по длине проблемного участка
for i in range(2_000_000 - 1):
    if a[i] == 1 and a[i + 1] == 0:  # Граница перехода между '1' (конец пробл. уч-ка) и '0'
        cnt += 1  # добавляем участок
print(cnt, sum(a))  # 1226 822094



# 2612 (Уровень: Базовый)
from statistics import mean
f = open('add/26/26_2612.txt').readlines()
n, m = map(int, f[0].split())
d = [*map(int, f[1:])]
d.sort(reverse=True)
top = d[:m]
tail = d[m:]
# print(top[-1], tail[0])  # Визуальное наличие полупроходного балла
if top[-1] == tail[0]:  # наличие полупроходного балла
    half = top[-1]
a = top[-top.count(half) - 1]  # минимальный балл гарантируемого прохода
b = mean(tail[tail.count(half):])  # средний балл тех, кто не проходит
print(a, int(b))  # 276 246


""" Взято на мой курс """
# 2613 (Уровень: Базовый)
f = open('add/26/26_2613.txt').readlines()
d = dict()
for i in f[1:]:
    k, v = map(int, i.split())  # ряд, место
    d.setdefault(k, [])
    d[k] += [v]
res = []
for r, s in d.items():
    s.sort()
    mx = 0
    c = 1
    for a, b in zip(s, s[1:]):
        if b - a == 1:
            c += 1
            mx = max(mx, c)
        else:
            c = 1
    res.append([mx, r])
res.sort(reverse=True)
seat, row = res[0]
print(row, seat)  # 99 14


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


# 2652 Сборник ЕГЭ Ушакова 2022(Уровень: Базовый)
# есть штрихкоды типа 00123 и 123 - ведущие нули убрать
f = open('add/26/26_2652.txt').readlines()
f = [*map(int, f[1:])]
d = dict()
for i in f:
    d.setdefault(i, 0)
    d[i] += 1
D = sorted((v, k) for k, v in d.items())
print(len(D), D[-1][0])  # 108 383


# аналог dict()
from collections import Counter
f = open('26.txt').readlines()
d = Counter(map(int, f[1:]))
print(len(d), d.most_common(1)[0][1])  # 108 383


# 2686 Пробный 02.2022 /dev/inf Base level(Уровень: Базовый)
f = open('26.txt').readlines()
d = dict()
for i in f[1:]:
    r, s = map(int, i.split())
    d.setdefault(r, [])
    d[r].append(s)
D = sorted([k, sorted(v, reverse=True)] for k, v in d.items())
for el in D:
    k, v = el
    cnt = 1
    for a, b in zip(v, v[1:]):
        if a - b == 1:
            cnt += 1
            if cnt == 5:
                print(k, a + 3)  # 2022 1239
                exit()
        else:
            cnt = 1


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



""" Взято на мой курс """
# 4205 Открытый вариант 2022 (Уровень: Базовый)
# 7274 OpenFIPI (Уровень: Базовый)
f = open('add/26/26_4205.txt').readlines()  # or  26_7274.txt
d = dict()
for row in f[1:]:
    k, v = map(int, row.split()) # ряд / место
    d.setdefault(k, [])
    d[k] += [v]
res = sorted([(k, v) for k, v in d.items()], reverse=True)
for r, v in res:
    v.sort()
    if len(v) > 1:
        for a, b in zip(v, v[1:]):
            if b - a == 14:
                print(r, a+1)  # 59966 50449
                exit()


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
D = [*map(int, open('add/26/26_4629.txt').readlines())]
N = D[0]  # количество товаров
d = sorted(D[1:])
sm1 = sum(d[:N*3//4]) + sum(d[N*3//4:]) // 2  # покупатель
sm2 = sum(d[:N//4]) // 2 + sum(d[N//4:])  # магазин
print(sm1, sm2)  # 39434611 48825239


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


# 5066 (Уровень: Базовый)
f = open('add/26/26_5066.txt').readlines()
d = sorted([*map(int, f[1:])], reverse=True)
res = []
while d:
    cnt = 1
    # cur = d[0]
    # d[0] = 0
    cur, d[0] = d[0], 0
    for i in range(1, len(d)):
        if cur - d[i] >= 7:
            cnt += 1
            # cur = d[i]
            # d[i] = 0
            cur, d[i] = d[i], 0
    res.append(cnt)
    d = [i for i in d if i]
print(len(res), max(res))  # 23 1306



# 5228 (Уровень: Базовый)
f = open('add/26/26_5228.txt').readlines()
d = sorted(map(int, f[1:]), reverse=True)
res = [d[0]]
for i in d[1:]:
    if res[-1] - i >= 8:
        res.append(i)
print(len(res), res[-1])  # 369 123



# 5643 (Уровень: Средний) ❓❓❓ словие полный бред! Задачу никому не предлагать!!!
# https://www.youtube.com/watch?v=tzQWZxfOrQY&t=12090s
f = open('26_5643.txt').readlines()
N, M = map(int, f[0].split()) # кол-во коробок, кол-во замочков
box = []  # коробки
lock = set()  # замки
cnt = 1
res = []
for el in f[1:]:
    if len(el.split()) == 2:
        b, l = map(int, el.split())
        box.append(b)
        lock.add(l)
    else:
        box.append(int(el))
box.sort(reverse=True)
box = [i for i in box if i in lock]
for i in box:
    if not i % 2:  # ❓❓❓ находим большую стартовую СИНЮЮ (КРАСНУЮ ???) коробку
        res.append(i)
        break

for b in box:  # находим кол-во подходящих коробкок и последнюю меньшую
    if res[-1] - b >= 9 and b in lock and res[-1] % 2 != b % 2:
        res.append(b)

if not res[-1] % 2:  # последняя коробка должна быть красной ❓❓❓
    print(len(res), res[-1]) # 354 233
else:
    print(len(res)-1, res[-2])  # 353 242 (верно)



# 6800 (Уровень: Средний) 🌶️🌶️🌶️🌶️🌶️
# Логика: суммируем (5/6 начала списка + от 0 до 5 позиций) + (1/6 конца списка (со скидкой))
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





""" Взято на мой курс """
# 10107 Демоверсия 2024 (Уровень: Средний)
f = open('add/26/26_10107.txt')
next(f)
d = [[*map(int, i.split())] for i in f]
d.sort(key=lambda x: x[1])  # сортируем по возрастанию времени окончания.
res = [d[0]]  # проведение мероприятий
for i in d:
    st, en = i
    if st >= res[-1][1]:
        res.append(i)
# ищем самое позднее время начала последнего мероприятия от окончания предпоследнего мероприятия (т.е. макс. перерыв)
for i in d[::-1]:
    if res[-2][1] <= i[0]:
        print(len(res), i[0] - res[-2][1])  # 32 15
        break



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



""" Взято на мой курс """
# 12256 ЕГКР 16.12.13_(23) (Уровень: Базовый)
f = open('add/26/26_12256.txt').readlines()
M, N = map(int, f[0].split())
D = sorted(map(int, f[1:]))
c = m = 0
for i in range(N):
    if m + D[i] <= M:
        c += 1
        m += D[i]
    else:
        m -= D[i-1]
        break
# ищем самую тяжёлую посылку
for i in range(N-1, -1, -1):
    if m + D[i] <= M:
        print(c, D[i])  # 629 50
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



""" Взято на мой курс """
# 17643 Основная волна 19.06.24 (Уровень: Базовый)
from statistics import mean
f = open('add/26/26_17643.txt').readlines()
next(f)
data = [[*map(int, i.split())] for i in f]  # артикул / цена / статус(0-продан/1-не продан)
avr = mean(i[1] for i in data)
expensive = [i for i in data if i[1] > avr]
d_exp = {i[0]: [i[1], 0, 0] for i in expensive}  # артикул: [i[1],0,0] цена /  кол-во не продан/продан
for i in expensive:
    if i[2]:  # если НЕ продан
        d_exp[i[0]][2] += 1
    else:
        d_exp[i[0]][1] += 1
res = [[k] + [*v] for k, v in d_exp.items()] # артикул / цена / кол-во: не продан/продан
res.sort(key=lambda x: (-x[2], -x[1], x[3]))
_, price, cnt, remainder = res[0]
print(price * cnt, remainder)  # 43656 36



""" Взято на мой курс """
# 17881 Демоверсия 2025 (Уровень: Базовый)
from statistics import mean
f = open('26_17881.txt')
N = int(next(f))  # кол-во студентов
data = [[*map(int, i.split())] for i in f]
data = [(i[0], mean(i[1:]), i[1:].count(2)) for i in data]  # id / сред.балл /  наличие двоек
vin = [i for i in data if not i[2]]   # Без двоек
d2 = sorted(i for i in data if i[2]==3)  # получили по 3 двойки (по условию задачи мы ищем только ID, а не место в общем списке)
vin.sort(key=lambda x: (-x[1], x[0]))
idx = N // 4 - 1  # -1 ✅ т.к индекс начинается с нуля
print(vin[idx][0], d2[0][0])  # 52326 635



# 19256 ЕГКР 21.12.24 (Уровень: Базовый)
f = open('26_19256.txt').readlines()
data = [[*map(int, i.split())] for i in f[1:]]  # идентификатор студента / номер правильно решённой задачи
dt = dict()
for i in data:
    dt.setdefault(i[0], set())
    dt[i[0]] |= {i[1]}
res = []
for k, v in dt.items():
    v = sorted(v)
    c = cnt = 1
    for i in range(1, len(v)):
        if v[i] - v[i-1] == 1:
            c += 1
            cnt = max(cnt, c)
        else:
            c = 1
        res += [(k, cnt)]
res.sort(key=lambda x: (-x[1], x[0]))
print(*res[0])  # 40031 148



# 19752 (Уровень: Базовый)
f = open('add/26/26_19752.txt')
N = int(next(f))  # 9566
data = [[*map(int, i.split())] for i in f]  #  ID участника / баллы (за 10 вопросов)
data = [[i[0]] + [sum(i[1:])] + [sum(k for k in i[1:] if k > 0)] + [sum(1 for p in i[1:] if p)] + [i[1:]] for i in data]
data.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
data = [i for i in data if i[1] > 0]  # только положительная сумма баллов
# Победители отборочного тура
idx = len(data) // 3
first = data[:idx]
first_add = [i for i in data[idx:] if i[1:4] == first[-1][1:4]]
# Дополнительный отборочный тур
idx_second = idx + len(first_add)
second =  data[idx_second:]
second_1 = second[:len(second) // 10]
second_2 = [i for i in second[len(second_1):] if i[1:4] == second_1[-1][1:4]]
print(second_1[0][0], len(second_1) + len(second_2))  # 35669 478



# 19890 (Уровень: Базовый)
f = open('add/26/26_19890.txt')
N, K = map(int, next(f).split())  # кол-во ящиков / грузоподъёмность
first, second = [], []
for i in map(int, f):  # массы ящиков
    if 310 <= i <= 320:
        first.append(i)
    else:
        second.append(i)
second.sort()
sm = sum(first)
cnt = len(first)
for i in range(len(second)):  # сборка грузов
    if sm + second[i] <= K:
        sm += second[i]
        cnt += 1
    else:
        sm -= second[i-1]  # убираем последний груз
        break
for i in second[::-1]:  # ищем максимальный по массе последний груз
    if sm + i <= K:
        sm += i
        break
print(cnt, sm)  # 129 10000



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



# 20815 Апробация 05.03.25(Уровень: Базовый)
f = open('add/26/26_20815.txt')
N, K = map(int, next(f).split())  # кол-во кандидатов / кол-во мест
data = [[*map(int, i.split())] for i in f]  # ID кандидата / четыре числа - 3 испытания + собеседование
d = [[i[0]] + [sum(i[1:])] + [i[-1]] for i in data]  # ID кандидата / сумма всех баллов/ собеседование
d.sort(key=lambda x: (-x[1], -x[2], x[0]))
d_vin = d[:K]
d_loser = d[K:]
# print(d_vin[-1][1], d_loser[0][1])  # 279 279  есть полупроходной балл
half = d_vin[-1][1]
ans_1 = [i for i in d_vin if i[1] > half][-1][0]
ans_2 = sum(i[1] == half for i in d)
print(ans_1, ans_2)  # 45539 127



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


# 22127 (Уровень: Базовый)
# 🆗🆗🆗 Новый подход 🆗🆗🆗
# ✅✅✅ вариант БЕЗ создания списка для  всех 86_400_000 миллисекунд. код работает меньше 2-х секунд
f = open('add/26/26_22127.txt')
next(f)
data = [[*map(int, i.split())] for i in f]  # время начала и окончания приёма
data.sort()  # сортировка по возрастанию начал приема
cnt = sm = mx = 0
for client in data + [[86_400_000, 86_400_000]]:  # 60 * 60 * 24 * 1000  (миллисекунд за сутки)
    if client[0] > mx:  # если время начала нового приема больше времени окончания предыдущей общей серии приемов (в т.ч. и при самом начале)
        cnt += 1  # период простоя
        sm += client[0] - mx  # суммарня длительность простоя
    mx = max(mx, client[1] + 1)  # конечная граница текущих совпадающих приемов
print(cnt, sm)  # 36 35834

# ⛔ Долго: код работает 60 секунд  (через создание списка для  всех 86_400_000 миллисекунд)
f = open('add/26/26_22127.txt')
res = [0] * 60*60*24*1000
next(f)
d = [[*map(int, i.split())] for i in f]  # время начала и окончания приёма
d.sort()
for el in d:
    st, en = el
    for i in range(st, en + 1):
        res[i] = 1
res = [1] + res + [1]  # [1] костыли в начало и конец, для верного подсчета "0" (простоя)
zero = cnt = 0
for a, b in zip(res, res[1:]):
    zero += not a
    cnt += a != b
print(cnt // 2, zero)  # 36 35834



# 23175 Основная волна 10.06.25(Уровень: Базовый)
# Нужно проверить два вида сортировки ✅
f = open('add/26/26_23175.txt')
N, M = map(int, next(f).split())  # кол-во грузов(cargo) / контейнеров(container)
d = [*map(int, f)]
cargo = sorted(d[:N])
container = sorted(d[N:])
res = []
idx = 0
for el in container:
    for i in range(idx, N):
        if cargo[i] <= el:
            res += [(cargo[i], el)]
            idx = i + 1
            break
max_container = res[-1][1]
for i in cargo[::-1]:
    if i <= max_container:
        print(len(res), i -res[-2][0])   # 800 48
        break
# ⛔ этот вариант хуже
cargo = sorted(d[:N], reverse=True)
container = sorted(d[N:], reverse=True)
res = []
idx = 0
for el in container:
    for i in range(idx, N):
        if cargo[i] <= el:
            res += [cargo[i]]
            idx = i + 1
            break
print(len(res), res[0] - res[1])  # 800 1



#  23208 Основная волна 10.06.25(Уровень: Базовый)
# https://vkvideo.ru/video-205865487_456240487?t=1h29m31s&ref_domain=kompege.ru
f = open('add/26/26_23208.txt').readlines()
N = int(f[0])
f = [[*map(int, k.split())] + [i] for i, k in enumerate(f[1:], 1)]  # Шлифовка, Окрашивание, Номер
f = [[(1, 0)[i[0] < i[1]]] + i for i in f]  # 0, 1  шлифовка / окрашивание
grind = sorted(i for i in f if not i[0])  # шлифовка
color = sorted([i for i in f if i[0]], key=lambda x: -x[2])  # окрашивание (убывание)
# финишный анализ глазами
print(grind[-1], 'последняя шлифовка')  # [0, 90948, 93066, 568]
print(color[0], 'последняя окраска')  #   [1, 96995, 96881, 503]
print(color[0][-1], len(grind))  # последняя деталь - это окраска
# 503 478



""" Взято на мой курс """
#  23259 Основная волна 11.06.25(Уровень: Базовый)
# Логика: в самые грузоподъемные саноки сажаем первый, из возможной по массе, экипаж.
f = open('add/26/26_23259.txt')
N, M = map(int, next(f).split())  # кол-во экипажей(crew) / санок(sled)
d = [*map(int, f)]  # массы экипажей + грузоподъемность санок
crew = sorted(d[:N], reverse=True)  # массы экипажей (в граммах)
sled = sorted(d[N:], reverse=True)  # максимально допустимая масса экипажа для конкретных санок
idx = 0
res_sled = []
for el in sled:
    for i in range(idx, N):
        if crew[i] <= el:
            res_sled.append(el)
            idx = i + 1
            break
print(len(res_sled), end = ' ')  # 800
max_sled = sled[0]
for i in crew:
    if i <= max_sled:
        print(i)  # 450466
        break
# 800 450466



""" Взято на мой курс """
# 23283 Основная волна 11.06.25 (Уровень: Базовый)
# https://vkvideo.ru/video-205865487_456240488?t=1h26m3s&ref_domain=kompege.ru
with open('add/26/26_23283.txt') as fl:
    windows, user = int(fl.readline()), int(fl.readline())  # кол-во окон / граждан
    time = [tuple(map(int, i.split())) for i in fl]  # время начала / время окончания приёма (в минутах)
    time.sort()
    win = [0] * windows
    cnt = last = 0
    for st, en in time:
        for i in range(windows):  # каждый раз пробегаемся по всем окнам
            if win[i] < st:  #  '<'  со следующей минуты после завершения приёма предыдущего
                win[i] = en
                cnt += 1
                last = i
                break
print(cnt, last + 1)  # 793 2 (+ 1: места (окна) пронумерованы начиная с 1)


# 23383 Резервный день 19.06.25 (Уровень: Базовый)
# https://vkvideo.ru/video-205865487_456240489?t=1h15m52s&ref_domain=kompege.ru
with open('add/26/26_23383.txt') as fl:
    next(fl)  # игнорируем первое число
    num = [tuple(map(int, i.split())) for i in fl]   # [0] номер спортсмена, [1] номер посещённой им точки
    d = dict()  # k: номер точки, v: номер спортсмена
    for el in set(num):
        v, k = el
        d.setdefault(k, [])
        d[k] += [v]
    res = []
    for k, v in d.items():
        c = cnt = 1
        v.sort()
        for a, b in zip(v, v[1:]):
            if b - a == 1:
                c += 1
                cnt = max(cnt, c)
            else:
                c = 0
        res.append((cnt, k))  # (число спортсменов с идущими подряд номерами, номер точки)
    res.sort(key=lambda x: (-x[0], x[1]))
    print(*res[0])  # 56 30113

# variant с костылем ⛔
with open('add/26/26_23383.txt') as fl:
    next(fl)  # игнорируем первое число
    num = [tuple(map(int, i.split())) for i in fl]   # [0] номер спортсмена, [1] номер посещённой им точки
    num = sorted(set(num), key=lambda x: (x[1], x[0])) + [(-1, -1)] # +[(-1, -1)] ⛔ костыль для зачета последнего реального значения
    c = 1
    res = []
    for i in range(len(num) - 1):
        s1, p1 = num[i]  # текущая спортсмен / точка
        s2, p2 = num[i + 1]  # следующая спортсмен / точка
        if p1 == p2 and (s2 - s1) == 1:
            c += 1
        else:
            res += [(c, p1)]
            c = 1
    res.sort(key=lambda x: (-x[0], x[1]))
    print(*res[0])  # 56 30113



# 24897 (Уровень: Средний) 🌶️🌶️🌶️
f = open('add/26/26_24897.txt')
N = int(next(f))  # кол-во заявок
dt = dict()
for el in f:
    z, d, p = map(int, el.split())  # номера:  заявки / дома / подъезда
    dt.setdefault(d, [])
    dt[d].append([p, z])
# результирующий список
res = []  # [925, 2, [84, 599896]]  дом / кол-во подъездов подряд / 1-й повтор. подъезд в серии (с номером заявки)
for k, v in dt.items():  # убираем дубликаты подъездов (оставляем подъезд с минимальным номером заявки)
    v.sort()
    ls = [v[0]]
    for a, b in zip(v, v[1:]):
        if a[0] != b[0]:
            ls += [b]
    v += [[0, 0]]   # костыль для обработки последнего реального значения в списке
    c = 1
    for i in range(1, len(v)):  # считаем кол-во идущих подряд подъездов
        if v[i][0] - v[i-1][0] == 1:
            c += 1
        else:
            if c > 1:
                res += [[k, c, v[i-c]]]
                c = 1
#  финиш
res.sort(key=lambda x: (-x[1], x[2][1]))
ans = res[0]
print(ans[0], ans[2][0])  # 503 805



# 25363 ЕГКР 13.12.25(Уровень: Базовый)
f = open('add/26/26_25363.txt')
next(f)
d = [[*map(int, k.split()), i] for i, k in enumerate(f, 1)]  # режим ожидания / использования
a, b = [], []
for i in d:
    if i[0] < i[1]:
        a.append(i)
    else:
        b.append(i)
a.sort()
b.sort(key=lambda x: -x[1])
print(b[0][2], len(b) - 1)  # 667 517


# 27636 Апробация 04.03.26(Уровень: Базовый)
f = open('add/26/26_27636.txt')
S, N = map(int, next(f).split())  # грузоподъёмность / кол-во контейнеров
d = sorted(map(int, f))
sm = 0
for i in range(N):
    if sm + d[i] <= S:
        sm += d[i]
    else:
        print(N-i, sum(d[i:]))  # 7347 472188
        break



# 23765 Демоверсия 2026 (Уровень: Базовый)
# ✔️ Получается что работаем только со 'сроком годности после вскрытия'
d = open('add/26/26_23765.txt').readlines()
dt = [[k, *map(int, i.split())] for k, i in enumerate(d[1:], 1)]
b = [i for i in dt if i[1] > i[2]]  # срок хранения > годности
b.sort(key=lambda x: -x[2])  # по значению срока годности (убывание)
print(b[0][0], len(b) - 1)  # 564 444  (len(b)-1  сколько позиций осталось после первого в списке 'b')


# 27779 Апробация 04.03.26 (Уровень: Базовый)
f = open('add/26/26_27779.txt')
# f = open('add/KIM_25164989/26_27779.txt')
next(f)
d = sorted(map(int, f), reverse=True)
cnt = 1
cur = d[0]
for n in d[1:]:
    if cur - n >= 8:
        cnt += 1
        cur = n
print(cnt, cur)


# 28945 ЕГКР 18.04.26(Уровень: Базовый)
# Логика: берем из заявки самое дальнее начало учатка и самой большей протяженностью
f = open('add/26/26_28945.txt')
# f = open('add/26/test.txt')
N = int(next(f))  # кол-во заявок
d = [[*map(int, i.split())] for i in f]  # начало участка (в метрах от начала дороги) / протяжённость
# d.sort(key=lambda x: (x[1], x[0]))  # 74 400 плохой вариант
# d.sort()  26 180 плохой вариант
# d.sort(key=lambda x: (-x[0], -x[1]))  # 77 184
d.sort(reverse=True)  # 77 184
res = [0] * 10_000
cnt = 0
for st, ln in d:
    if all(not res[i] for i in range(st, st+ln)):
        cnt += 1
        for i in range(st, st+ln):
            res[i] = 1  # помечаем единицей начало каждого метра участка для уборки
print(cnt, res[::-1].index(1))  # 77 184


# 30401 (Уровень: Средний)
f = open('add/26/26_30401.txt')
K, N = map(int, next(f).split())  # кол-во камер / кол-во заявок
cam, bid = [], []  # тип камеры / заявки
res = [0] * (K)  # камеры
for i in f:
    d = [*map(int, (i.split()))]
    if len(d) == 2:
        cam.append(d)  # тип камеры / объём / + number
    else:
        bid.append(d)  # время начала хранения / время окончания хранения / объём камеры / тип камеры / + number
bid = [k + [i] for i, k in enumerate(bid, 1)] # + исходная нумерация
cam = [k + [i] for i, k in enumerate(cam, 1)] # + исходная нумерация
# заявки упорядочиваются по возрастанию времени начала, а при одинаковом времени начала - по возрастанию времени окончания.
# Если время начала и время окончания у нескольких заявок совпадают, они обрабатываются в том порядке, в котором записаны во входном файле.
bid.sort(key=lambda x: (x[0], x[1], x[-1]))
# свободная подходящую камеря минимального объёма. Если таких камер несколько, выбирается камера с наименьшим порядковым номером.
cam.sort(key=lambda x: (x[1], x[2]))
cnt = num = 0
for b in bid:
    st, en, vb, type_b, n = b
    for i in range(K):
        type_c, vc, nc = cam[i]
        # res[i] + 1  - камера считается свободной только со следующей минуты после окончания предыдущего хранения
        if st >= res[i] + 1 and vb <= vc and type_b == type_c:
            res[i] = en
            cnt += 1
            num = nc
            break
print(cnt, num)  # 1989 40



# 31131 Основная волна 18.06.26(Уровень: Средний)
f = open('add/26/26_31131.txt')
_, K = map(int, next(f).split())  # кол-во строк / вместимость спец. раздела
d = dict()
res = []
for el in f:
    t, i, s = el.split()
    if int(t[:2]) < 12:
        d.setdefault(i, 0)
        d[i] += int(s)
    res.append(int(s))
ans_1 = max([i for i in d.items()], key=lambda x: x[1])
ans_2 = []
SM = 0
for i in range(len(res)):
    if res[i] + SM <= K:
        SM += res[i]
    else:
        ans_2 += [SM]
        SM = res[i]
ans_2.sort()
print(ans_1[0], sum(ans_2[-2:]))  # 9517 46436



# 31137 Основная волна 18.06.26(Уровень: Средний)
f = open('add/26/26_31137.txt')
N, K = map(int, next(f).split()) # кол-во строк / вместимость спец. раздела
d = dict()
res = []
for el in f:
    t, i, s = el.split()
    d.setdefault(i, 0)
    d[i] += int(s)
    if int(t[:2]) < 12:
        res.append(int(s))
ans_1 = sorted(v for k, v in d.items())
ans_2 = None
SM = 0
for i in range(len(res)):
    if res[i] + SM <= K:
        SM += res[i]
    else:
        ans_2 = SM
        SM = res[i]
print(sum(ans_1[-2:]), ans_2)  # 481895 21328



# 31165 Основная волна 19.06.26(Уровень: Средний)
f = open('add/26/26_31165.txt')
K,  _ = map(int, next(f).split())  # приёмщики / сборщики винограда
ls = [0] * (K + 1)
data = []
for el in f:
    st, en, vin = el.split()
    data.append([int(st), int(en), vin == 'A'])  #  "А" == 1
data.sort(key=lambda x: (x[0], x[1], -x[2]))  #-x[2]) - ❗❗❗ для сортировки имеет значение сорт винограда. Сначала "А" (ЗАСАДА в задаче❗❗❗)
# data.sort(key=lambda x: (x[1], x[0], -x[2]))  # 9026 56 - так хуже
cnt = user = 0
for st, en, vin in data:
    for i in range(1, K+1):
        if ls[i] <= st and (i % 2 == vin):
            ls[i] = en+5
            cnt += 1
            user = i
            break
print(cnt, user)  # 9338 52



# 31232 Резерв 22.06.26(Уровень: Средний)
f = open('add/26/26_31232.txt')
_, K = map(int, next(f).split())
d = dict()
backup = []
for el in f:
    t, indf, s = el.split()  # время(часы, минуты, секунды), идентификатор, объём данных
    d.setdefault(indf, 0)
    d[indf] += int(s)
    if int(t[:2]) < 12:
        backup += [int(s)]
answer_1 = max(v for k, v in d.items() if v <= 150_000)  # 149369
answer_2 = []
SM = 0
for i in backup:
    if SM + i <= K:
        SM += i
    else:
        answer_2.append(SM)
        SM = i
print(answer_1, sum(answer_2[-2:]))
# 149369 45828



# 31370 Пересдача 08.07.26(Уровень: Средний)
f = open('add/26/26_31370.txt')
_, K = map(int, next(f).split())  # вместимость раздела
d = dict()  # объём данных переданых по каждому клиенту
backup = []  # для answer_2
for el in f:
    t, i, s = el.split()  # время(часы, минуты, секунды), идентификатор, объём данных
    i, s = map(int, [i, s])
    d.setdefault(i, 0)  # идентификатор, объём данных
    d[i] += s
    if int(t[:2]) < 12:
        backup.append(s)
client = sorted([i for i in d.items()], key = lambda x: x[1])
answer_1 = client[0][0] + client[1][0]  # 17248  сумма идентификаторов 2-х клиентских устройств
answer_2 = []  # резервные копии
SM = 0
for i in backup:
    if SM + i <= K:
        SM += i
    else:
        answer_2.append(SM)
        SM = i
print(answer_1, sum(answer_2[-2:]))  # 17248 43147



# 31520 Демоверсия 2027(Уровень: Базовый)
f = open('add/26/26_31520.txt').readlines()
N, K = map(int, f[0].split())  # кол-во строк, вместимость Кбайт
data = []
for i in f[1:]:
    t, i, s = i.split()
    data.append([int(t[:2]), int(i), int(s)])  # время (час), идентификатор клиента, объём данных Кбайт

d = dict()
for i in data:
    d.setdefault(i[1], 0)
    d[i[1]] += i[2]
res1 = max((s, i) for i, s in d.items())
print(res1[1])  # 7040 - идентификатор клиента

# [K] - Принудительно добавляет последнюю набранную сумму sm в res2. Сам при этом не добавляется
data2 = [i[2] for i in data if i[0] < 12] + [K]
res2 = []
sm = 0
for s in data2:  # s - объём данных Кбайт
    if sm + s <= K:
        sm += s
    else:
        res2.append(sm)
        sm = s
res2.sort(reverse=True)
print(res2[0] + res2[1])  # 52204 сумма объёмов (в Кбайт) двух наибольших резервных копий
# 7040 52204



