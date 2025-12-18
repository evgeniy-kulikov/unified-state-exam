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

