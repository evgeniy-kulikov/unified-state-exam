""""""
"""
Task 17
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 17.1 Задание 17 | Урок 1 """
# https://stepik.org/lesson/1698037/step/3?unit=1721419
# https://kompege.ru/task   № 2003 (Уровень: Базовый)
cnt = MX = 0
for n in map(int, open('add/course_233165/17_1_01.txt')):
    if not n % 3 and all(n % i for i in [7,17,19,27]):
        cnt += 1
        MX = max(MX, n)
print(cnt, MX)  # 445 9738


# https://stepik.org/lesson/1698037/step/4?unit=1721419
# https://kompege.ru/task   № 2013 (Уровень: Базовый)
cnt = 0
MN = 10000
for n in map(int, open('add/course_233165/17_1_02.txt')):
    if n % 10 in [2,7] and all(not n % i for i in [3, 11]):
        cnt += 1
        MN = min(MN, n)
print(cnt, MN)  # 13 1287


# https://stepik.org/lesson/1698037/step/5?unit=1721419
# https://kompege.ru/task   № 2015 (Уровень: Базовый)
ls = [*map(int, open('add/course_233165/17_1_05.txt'))]
res = [i for i in ls if all([i % 10 in (5, 7), i % 9, i % 11])]
print(len(res), min(res) + max(res))  # 337 10802


# https://stepik.org/lesson/1698037/step/6?unit=1721419
# https://kompege.ru/task   № 2016 (Уровень: Базовый)
ls = [*map(int, open('add/course_233165/17_1_06.txt'))]
res = [i for i in ls if all([i % 13 == 7, i % 7, i % 11])]
print(max(res) - min(res), len(res))  # 8515 126


# https://stepik.org/lesson/1698037/step/7?unit=1721419
# https://kompege.ru/task   № 2017 (Уровень: Базовый)
cnt = ms = 0
ls = [*map(int, open('add/course_233165/17_1_07.txt'))]
for i in ls:
    if all([i % 16 == 11, not i % 7, i % 6, i % 13, i % 19]):
        cnt += 1
        ms += i
print(ms, cnt)  # 74452 12


# https://stepik.org/lesson/1698037/step/8?unit=1721419
# https://kompege.ru/task   № 1993 (Уровень: Базовый)
cnt = ms = 0
ls = [*map(int, open('add/course_233165/17_1_08.txt'))]
for i in range(len(ls) - 1):
    a, b = ls[i:i+2]
    if all([not ((a+b) % 3), (a+b) % 6, abs(a * b) % 10 == 8]):
        cnt += 1
        ms = max(ms, a+b)
print(cnt, ms)  # 140 17031


# https://stepik.org/lesson/1698037/step/9?unit=1721419
# https://kompege.ru/task  № 1994 (Уровень: Базовый)
dt = [*map(int, open('17_1_09.txt'))]
mn = 10**10
c = 0
for i in range(len(dt) - 1):
    a, b = dt[i:i + 2]
    if a * b > 0 and not (a + b) % 7:
        c += 1
        mn = min(mn, a*b)
print(c, mn)  # 359 115022


# https://stepik.org/lesson/1698037/step/10?unit=1721419
# https://kompege.ru/task  № 1998 (Уровень: Базовый)
from math import prod
dt = [*map(int, open('17_1_10.txt'))]
mx = -10**11
c = 0
for i in range(len(dt) - 2):
    d = dt[i:i + 3]
    if not prod(d) % 7 and abs(sum(d)) % 10 == 5:
        c += 1
        mx = max(mx, sum(d))
print(c, mx)  # 153 19285


# https://stepik.org/lesson/1698037/step/11?unit=1721419
# https://kompege.ru/task  № 1999 (Уровень: Базовый)
from statistics import mean
dt = [*map(int, open('17_1_11.txt'))]
mn = 10**10
c = 0
for i in range(len(dt) - 2):
    d = dt[i:i + 3]
    if any(not i % 12 for i in d) and all(not i % 3 for i in d):
        c += 1
        mn = min(mn, mean(d))
print(c, mn)  # 119 -7213


# https://stepik.org/lesson/1698037/step/12?unit=1721419
# https://kompege.ru/task  № 2402 (Уровень: Средний
from statistics import mean
dt = [*map(int, open('17_1_12.txt'))]
mn = c = 0
for i in range(len(dt) - 2):
    d = dt[i:i + 3]
    if any(i % 3 == 2 for i in d):
        c += 1
        mn += min(d)
print(c, mn)  # 91 2627




""" 17.2 Задание 17 | Урок 2 """
# https://stepik.org/lesson/1698038/step/1?unit=1721420
# https://kompege.ru/task   № 2002 (Уровень: Базовый)
cnt = 0
MN = 10**6
l = [*map(int, open('add/course_233165/17_2_01.txt'))]
for i in range(len(l) - 4):
    a, b, c, d = l[i: i + 4]
    if a > b > c > d and a - d > 1000:
        cnt += 1
        MN = min(MN, sum(l[i: i + 4]))
print(cnt, MN)  # 181 -31478


# https://stepik.org/lesson/1698038/step/2?unit=1721420
# https://kompege.ru/task   № 2400 (Уровень: Базовый)
cnt = 0
res = -10**10
ls = [*map(int, open('add/course_233165/17_2_02.txt'))]
for i in range(len(ls) - 1):
    a, b = ls[i: i+2]
    if a+b >= 100 and any([a<0, b<0]):
        cnt += 1
        res = max(res, a*b)
print(cnt, res)  # 1137 -2655


# https://stepik.org/lesson/1698038/step/3?unit=1721420
# https://kompege.ru/task   № 2401 (Уровень: Базовый)
cnt = 0
mn = 10**10
ls = [*map(int, open('add/course_233165/17_2_03.txt'))]
for i in range(len(ls) - 1):
    a, b = ls[i:i+2]
    if 50 <= abs(a) + abs(b) <= 200:
        cnt += 1
        mn = min(mn, min(a, b))
print(cnt, mn)  # 1 -92


# https://stepik.org/lesson/1698038/step/4?unit=1721420
# https://kompege.ru/task  № 2238 (Уровень: Базовый)
dt = [*map(int, open('17_2_04.txt'))]
ms = c = 0
ma = sum(dt) / len(dt)
for i in range(len(dt) - 2):
    d = dt[i:i + 3]
    if sum(i > ma for i in d) >= 2:
        c += 1
        ms = max(ms, sum(d))
print(c, ms)  # 5020 28715


# https://stepik.org/lesson/1698038/step/5?unit=1721420
# https://kompege.ru/task  № 2239 (Уровень: Базовый)
dt = [*map(int, open('17_2_05.txt'))]
ms = 10**10
c = 0
m19 = max(i for i in dt if not i % 19)
for i in range(len(dt) - 1):
    d = dt[i:i + 2]
    if sum(i > m19 for i in d):
        c += 1
        ms = min(ms, sum(d))
print(c, ms)  # 34 11169


# https://stepik.org/lesson/1698038/step/6?unit=1721420
# https://kompege.ru/task  № 2309 (Уровень: Базовый)
dt = [*map(int, open('17_2_06.txt'))]
n11 = [i for i in dt if not i % 11]
n17 = [i for i in dt if not i % 17]
# if len(n11) > len(n17):
#     print(len(n11), min(n11))  # 70 363
# else:
#     print(len(n17), max(n17))
a = ((n11, 'min'), (n17, 'max'))[len(n11) < len(n17)]
print(len(a[0]), eval(a[1])(a[0]))  # 70 363


# https://stepik.org/lesson/1698038/step/7?unit=1721420
# https://kompege.ru/task  № 2310 (Уровень: Базовый)
res = []
dt = [*map(int, open('17_2_07.txt'))]
n4 = [i for i in dt if str(i)[-1] == '4']
s4 = min(n4) + max(n4)
for i in range(len(dt) - 1):
    if dt[i] + dt[i+1] < s4:
        res.append(dt[i] + dt[i+1])
print(len(res),  max(res))  # 503 10094


# https://stepik.org/lesson/1698038/step/8?unit=1721420
# https://kompege.ru/task  № 2403 (Уровень: Средний)
res = []
d = [*map(int, open('17_2_08.txt'))]
for i in range(len(d) - 1):
    if any([not d[i] % 9 and d[i+1] % 9 and abs(d[i+1]) % 8 == 3,
           not d[i+1] % 9 and d[i] % 9 and oct(d[i])[-1] == '3']):
        res.append(max(d[i:i+2]))
print(len(res),  max(res))  # 252 9971


# https://stepik.org/lesson/1698038/step/9?unit=1721420
# https://kompege.ru/task  № 2398 (Уровень: Средний)  👍
res = []
d = [*map(int, open('17_2_09_var.txt'))]
for i in range(len(d) - 2):
    a, b, c = d[i:i+3]
    if all([a <= 0 or a % 10 != 9, c <= 0 or c % 10 != 9, b > 0, abs(b) % 10 == 9]):
        res.append(a + b + c)
print(len(res),  max(res))  # 206 23427


# https://stepik.org/lesson/1698038/step/10?unit=1721420
# https://kompege.ru/task  № 2399 (Уровень: Средний)
res = []
d = [*map(int, open('17_2_10.txt'))]
d35 = [str(i) for i in d if not i % 35]
s35 = sum(sum(map(int, i)) for i in d35)  # 4641
for i in range(len(d) - 1):
    a, b = d[i:i+2]
    if all([a > s35, b < s35, hex(b)[-2:] == 'ef']) or all([a < s35, b > s35, hex(a)[-2:] == 'ef']):
        res.append(a + b)
print(len(res),  min(res))  # 15 6410




""" 17.3 Задание 17 | Задачи прошлых лет """
# https://stepik.org/lesson/1698039/step/1?unit=1721421
# https://kompege.ru/task   № 9748 Основная волна 19.06.23 (Уровень: Средний)
cnt = res = 0
ls = [*map(int, open('add/course_233165/17_3_01.txt'))]
MX = max(i for i in ls if i % 100 == 15)
for i in range(len(ls) - 3):
    d = ls[i: i + 3]
    if sum(10**4 <= n < 10**5 for n in d) == 1 and sum(d) >= MX:
        cnt += 1
        res = max(res, sum(d))
print(cnt, res)  # 299 196183


# https://stepik.org/lesson/1698039/step/2?unit=1721421
# https://kompege.ru/task   № 23276 Основная волна 11.06.25 (Уровень: Базовый)
cnt = ms = 0
ls = [*map(int, open('add/course_233165/17_3_02.txt'))]
MX = max(i for i in ls if abs(i) % 100 == 25)
for i in range(len(ls) - 2):
    d = ls[i: i+3]
    four = sum(1 for i in d if len(str(abs(i))) == 4) <= 2
    if four and sum(d) <= MX:
        cnt += 1
        ms = max(ms, sum(d))
print(cnt, ms)  # 6315 84523


# https://stepik.org/lesson/1698039/step/3?unit=1721421
# https://kompege.ru/task  № 17530 Основная волна 07.06.24 (Уровень: Базовый)
res = []
d = [*map(int, open('17_3_03.txt'))]
md = min(d)
for i in range(len(d) - 1):
    a, b = d[i:i+2]
    if any([a % 55 == md, b % 55 == md]):
        res.append(a + b)
print(len(res),  min(res))  # 201 2942


# https://stepik.org/lesson/1698039/step/4?unit=1721421
# https://kompege.ru/task  № 17558 Основная волна 08.06.24 (Уровень: Базовый)
res = []
d = [*map(int, open('17_3_04.txt'))]
l32 = len([i for i in d if not i % 32])
for i in range(len(d) - 1):
    a, b = d[i:i+2]
    if any([a < 0, b < 0]) and a+b < l32:
        res.append(a + b)
print(len(res),  max(res))  # 4969 299


# https://stepik.org/lesson/1698039/step/5?unit=1721421
# https://kompege.ru/task  № 17636 Основная волна 19.06.24 (Уровень: Средний)
res = []
d = [*map(int, open('17_3_05.txt'))]
m3 = max(i for i in d if abs(i) % 10 == 3 and len(str(abs(i))) == 3)
for i in range(len(d) - 2):
    a, b, c = d[i:i+3]
    if any([abs(a) % 10 == 3 and len(str(abs(a))) == 3,
            abs(b) % 10 == 3 and len(str(abs(b))) == 3,
            abs(c) % 10 == 3 and len(str(abs(c))) == 3]) \
            and a + b + c < m3:
        res.append(a + b + c)
print(len(res),  max(res))  # 147 944










""""""
""" Варианты """
# 28.1 Вариант 1 | Часть 1
# https://stepik.org/lesson/1729565/step/5?unit=1753394
#  https://kompege.ru/task  № 17873 Демоверсия 2025 (Уровень: Базовый)
d = [*map(int, open('01_17.txt'))]
mn = min(d)
MX = 0
cnt = 0
for i in range(1, len(d)):
    if any([d[i-1] % 16 == mn, d[i] % 16 == mn]):
        cnt += 1
        MX = max(MX, d[i-1] + d[i])
print(cnt, MX)  # 1214 176024


# 29.1 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/5?unit=1753726
# https://kompege.ru/task  № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
cnt = 0
res = 10**10
data = [*map(int, (open('02_17.txt')))]
mx = max(i for i in data if len(str(abs(i))) == 5 and abs(i) % 100 == 43)
for i in range(2, len(data)):
    d = [*data[i-2: i+1]]
    if any(i for i in d if len(str(abs(i))) == 5 and abs(i) % 100 == 43):
        sm = sum(i**2 for i in d)
        if sm <= mx**2:
            cnt += 1
            res = min(res, sm)
print(cnt, res)  # 92 838850571


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730528/step/5?unit=1754357
# https://kompege.ru/task  № 17558 Основная волна 08.06.24 (Уровень: Базовый)
d = [*map(int, open('03_17.txt'))]
num = sum(1 for i in d if not abs(i) % 32)
cnt = 0
sm = 0
for i in range(1, len(d)):
    n = d[i - 1:i + 1]
    if any(i < 0 for i in n) and sum(n) < num:
        cnt += 1
        sm = max(sm, sum(n))
print(cnt, sm)  # 4969 299


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/5?unit=1760676
# https://kompege.ru/task  № 21416 Досрочная волна 2025 (Уровень: Базовый)
cnt = 0
sm = - 1 * 10**6
ls = [int(i) for i in open('04_17.txt')]
num = sum(i for i in ls if i < 0)
for i in range(2, len(ls)):
    d = ls[i - 2: i + 1]
    if min(d) * max(d) > num:
        cnt += 1
        sm = max(sm, sum(d))
print(cnt, abs(sm))  # 10007 7953


# 32.2 Вариант 5 | Часть 2
# https://stepik.org/lesson/1754189/step/5?unit=17786487
# https://kompege.ru/task  № 21712 ЕГКР 19.04.25 (Уровень: Базовый)
c = 0
sm = -1 * 10**10
ls = [*map(int, open('05_17.txt'))]
mn = min(i for i in ls if i > 0 and len(str(i)) == 4 and i % 10 == 6)
for i in range(2, len(ls)):
    d = ls[i-2:i+1]
    n4 = [i for i in d if len(str(abs(i))) == 4 and str(i)[-1] == '6']
    if len(n4) == 1 and sum(d) <= mn:
        c += 1
        sm = max(sm, sum(d))
print(c, sm)  # 507 -164893


# 33.2 Вариант 6 | Часть 2
# https://stepik.org/lesson/1943171/step/5?unit=1969925
# https://kompege.ru/task  № 23201 Основная волна 10.06.25 (Уровень: Базовый)
c = 0
M = 10**10
ls = [*map(int, open('06_17.txt'))]
mn = min(i for i in ls if i % 10 == 7 and 99 < i < 1000)
for i in range(1, len(ls)):
    d = ls[i-1:i+1]
    if sum(1 for i in d if 99 < i < 1000) == 1 and not sum(d) % mn:
        c += 1
        M = min(M, sum(d))
print(c, M)  # 9 107


# 34.2 Вариант 7 | Часть 2
# https://stepik.org/lesson/1943174/step/5?unit=1969928
# https://kompege.ru/task  № 23276 Основная волна 11.06.25 (Уровень: Базовый)
c = 0
sm = -1 * 10**10
ls = [*map(int, open('07_17.txt'))]
mx = max(i for i in ls if str(i)[-2:] == '25')
for i in range(2, len(ls)):
    d = ls[i-2:i+1]
    n4 = [i for i in d if len(str(abs(i))) == 4]
    if len(n4) <= 2 and sum(d) <= mx:
        c += 1
        sm = max(sm, sum(d))
print(c, sm)  # 6315 84523


# 35.2 Вариант 8 | Часть 2
# https://stepik.org/lesson/1943181/step/5?unit=1969936
# https://kompege.ru/task  № 23563 Пересдача 03.07.25 (Уровень: Базовый)
c = 0
sm = -10**10
f = [*map(int, open('08_17.txt'))]
mn = min(i for i in f if i > 0 and not i % 35)
for i in range(len(f) - 1):
    a, b = f[i:i+2]
    if a != b and not abs(a - b) % mn:
        c += 1
        sm = max(sm, a + b)
print(c, sm)  # 87 184328


# 36.2 Вариант 9 | Часть 2
# https://stepik.org/lesson/1943186/step/5?unit=1969940
# https://kompege.ru/task  № 23757 Демоверсия 2026 (Уровень: Базовый)

d = [*map(int, open('09_17.txt'))]
res = []
mn = min(i for i in d if 9 < i < 100)
for i in range(len(d) - 1):
    a, b = d[i:i+2]
    if sum([9 < a < 100, 9 < b < 100]) == 1 and not (a + b) % mn:
        res.append(a + b)
print(len(res), max(res))  # 150 9930



