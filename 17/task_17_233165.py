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

