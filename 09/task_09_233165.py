""""""
"""
Task 09
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 9.1 Задание 9 | Урок 1 """
# https://stepik.org/lesson/1679586/step/4?unit=1702700
# https://kompege.ru/task   № 2092 (Уровень: Базовый)
cnt = 0
for f in open('add/course_233165/9-1_04.txt'):
    a, b, c = map(int, f.split())
    cnt += all([a in (1, 3, 5), b <= 36, c <= 43])
print(cnt)  # 1


# https://stepik.org/lesson/1679586/step/5?unit=1702700
# https://kompege.ru/task   № 2093 (Уровень: Средний)
cnt, ln = 0, 0
for f in open('add/course_233165/9-1_05.txt'):
    ln += 1
    g, i = map(int, f.split())
    cnt += g >= 37 and i < 44
print(int(cnt * 100 / ln))  # 13

# https://stepik.org/lesson/1679586/step/6?unit=1702700
# https://kompege.ru/task   № 2094 (Уровень: Средний)
cnt, ln = 0, 0
for f in open('add/course_233165/9-1_06.txt'):
    ln += 1
    g, i = map(int, f.split())
    cnt += g > i and i >= 44

print(int(cnt * 100 / ln))  # 25


# https://stepik.org/lesson/1679586/step/7?unit=1702700
cnt = 0
with open('add/course_233165/9-1_07.txt') as fl:
    for f in fl:
        a, b, c = sorted(map(int, f.split()))
        cnt += (a + c) / 2 == b
    print(cnt)  # 67


# https://stepik.org/lesson/1679586/step/8?unit=1702700
# https://kompege.ru/task   № 2049 (Уровень: Базовый)
cnt = 0
for f in open('add/course_233165/9-1_08.txt'):
    a, b, c = sorted(map(int, f.split()))
    # cnt += b - a == c - b and a < b < c
    cnt += b - a == c - b and a != b
print(cnt)  # 174


# https://stepik.org/lesson/1679586/step/9?unit=1702700
# ПОСЛЕДОВАТЕЛЬНОСТЬ ломаных, то есть стороны идут по порядку
cnt = 0
with open('add/course_233165/9-1_09.txt') as fl:
    for f in fl:
        a, b, c, d = map(int, f.split())
        cnt += a == c and b == d and a != b
    print(cnt)  # 353

# variant
cnt = 0
for f in open('add/course_233165/9-1_09.txt'):
    a, b, c, d = map(int, f.split())
    cnt += all([a == c, b == d, a != b])
print(cnt)  # 353


# https://stepik.org/lesson/1679586/step/10?unit=1702700
# https://kompege.ru/task   № 2095 (Уровень: Базовый)
cnt = 0
for f in open('add/course_233165/9-1_10.txt'):
    cnt += len(set(map(int, f.split()))) == 2
print(cnt)  # 491


# https://stepik.org/lesson/1679586/step/11?unit=1702700
# https://kompege.ru/task   № 2034 (Уровень: Базовый)
cnt = 0
for f in open('add/course_233165/9-1_11.txt'):
    p = sorted(map(int, f.split()))
    cnt += sum(p) == 180
print(cnt)  # 2374


# https://stepik.org/lesson/1679586/step/12?unit=1702700
# https://kompege.ru/task   № 2099 (Уровень: Базовый)
cnt = res = 0
for f in open('add/course_233165/9-1_12.txt'):
    d = sorted(map(int, f.split()))
    if sum(d) == 180:
        cnt += 1
        res += len(set(d)) < 3
print(res * 100 // cnt)  # 3



""" 9.2 Задание 9 | Урок 2 """
# https://stepik.org/lesson/1679588/step/1?unit=1702702
cnt = 0
with open('add/course_233165/9-2_02.txt') as fl:
    for f in fl:
        a, b, c = sorted(map(int, f.split()))
        cnt += c > 90 and a + b + c == 180
    print(cnt)  # 1071


# https://stepik.org/lesson/1679588/step/2?unit=1702702
cnt = 0
with open('add/course_233165/9-2_02.txt') as fl:
    for f in fl:
        a, b, c, d = map(int, f.split())
        cnt += a == c and b == d and a + b + c + d == 360
    print(cnt)  # 984

# variant
cnt = 0
for f in open('add/course_233165/9-2_02.txt'):
    a, b, c, d = map(int, f.split())
    cnt += a == c and b == d and a+b+c+d == 360
print(cnt)  # 984


# https://stepik.org/lesson/1679588/step/3?unit=1702702
cnt = 0
with open('add/course_233165/9-2_03.txt') as fl:
    for f in fl:
        a, b, c, d = sorted(map(int, f.split()))
        cnt += a+b+c > d
    print(cnt)  # 4757


# https://stepik.org/lesson/1679588/step/4?unit=1702702
# https://kompege.ru/task   № 2043 (Уровень: Средний)
cnt = 0
for f in open('add/course_233165/9-2_04.txt'):
    a,b,c,d = list(map(int, f.split()))
    cnt += a == c and b == d
print(cnt)  # 754


# https://stepik.org/lesson/1679588/step/5?unit=1702702
# https://kompege.ru/task   № 2100 (Уровень: Базовый)
MX = 0
for f in open('add/course_233165/9-2_05.txt'):
    a, b, c = sorted(map(int, f.split()))
    if a**2 + b**2 == c**2:
        MX = max(MX, a+b)
print(MX)  # 803


# https://stepik.org/lesson/1679588/step/6?unit=1702702
# https://kompege.ru/task   № 2101 (Уровень: Средний)
cnt = 0
for f in open('add/course_233165/9-2_06.txt'):
    a,b,c = sorted(map(int, f.split()))
    cnt += a**2 + b**2 > c**2
print(cnt)  # 1496


# https://stepik.org/lesson/1679588/step/7?unit=1702702
# https://kompege.ru/task  № 2096 (Уровень: Средний)
cnt = 0
for i in open('9-2_07.txt'):
    x0, y0, x1, y1 = map(int, i.split())
    if all([x0, y0, x1, y1]):
        cnt += (x0 * x1 > 0) and (y0 * y1 > 0)
print(cnt)  # 184


# https://stepik.org/lesson/1679588/step/8?unit=1702702
# https://kompege.ru/task  № 2097 (Уровень: Средний)
cnt = 0
for row in open('9-2_08.txt'):
    x0, y0, x1, y1 = list(map(int, row.split()))
    if (x0 * x1 <= 0 and y0 * y1 > 0) or (y0 * y1 <= 0 and x0 * x1 > 0):
        cnt += 1
print(cnt)  # 531


# https://stepik.org/lesson/1679588/step/9?unit=1702702
# https://kompege.ru/task  № 2098 (Уровень: Базовый)
cnt = 0
for row in open('9-2_09.txt'):
    x0, y0, x1, y1 = list(map(int, row.split()))
    if not x0 * y0 and not x1 * y1:
        cnt += 1
print(cnt)  # 10


# https://stepik.org/lesson/1679588/step/10?unit=1702702
# https://kompege.ru/task  № 2104 (Уровень: Средний)
# Отрезок пересекает одну или две оси
from math import dist
cnt = 0
for row in open('9-2_10.txt'):
    x0, y0, x1, y1 = list(map(int, row.split()))
    if (x0 * x1 <= 0) or (y0 * y1 <= 0):
        cnt += dist((x0, y0), (x1, y1)) <= 5
print(cnt)  # 41





""" 9.3 Задание 9 | Урок 3 """
# https://stepik.org/lesson/1679593/step/1?unit=1702707
cnt = 0
with open('add/course_233165/9-3_01.txt') as fl:
    for f in fl:
        a, b, c = sorted(map(int, f.split()))
        cnt += (a+c) / 2 <= b
    print(cnt)  # 2559


# https://stepik.org/lesson/1679593/step/2?unit=1702707
# https://kompege.ru/task   № 4669 Резервный день 2022 (Уровень: Базовый)
cnt = 0
for f in open('add/course_233165/9-3_02.txt'):
    a,b,c,d = sorted(map(int, f.split()))
    cnt += a+d < b+c
print(cnt)  # 1285


# https://stepik.org/lesson/1679593/step/3?unit=1702707
# https://kompege.ru/task   № 3150 (Уровень: Базовый)
cnt = 0
for f in open('add/course_233165/9-3_03.txt'):
    a, b, c = sorted(map(int, f.split()))
    cnt += c**2 > 2 * a * b
print(cnt)  # 2707


# https://stepik.org/lesson/1679593/step/4?unit=1702707
# https://kompege.ru/task  № 3167 (Уровень: Базовый)
cnt = 0
for row in open('9-3_04.txt'):
    a, b, c, d = sorted(map(int, row.split()))
    cnt += (a + d)**2 > b**2 + c**2
print(cnt)  # 2960


# https://stepik.org/lesson/1679593/step/5?unit=1702707
# https://kompege.ru/task  № 4589 Основная волна 2022 (Уровень: Базовый)
cnt = 0
for row in open('9-3_05.txt'):
    a, b, c, d = sorted(map(int, row.split()))
    cnt += d < a+b+c and a + d == b + c
print(cnt)  # 104


# https://stepik.org/lesson/1679593/step/6?unit=1702707
# https://kompege.ru/task  № 4633 (Уровень: Базовый)
cnt = 0
for row in open('9-3_06.txt'):
    a, b, c, d = sorted(map(int, row.split()))
    cnt += (d - a < (b + c) - d) and a + d == b + c
print(cnt)  # 15


# https://stepik.org/lesson/1679593/step/7?unit=1702707
# https://kompege.ru/task  № 4634 (Уровень: Базовый)
cnt = 0
for row in open('9-3_07.txt'):
    a, b, c, d = sorted(map(int, row.split()))
    cnt += c**2 > a * d and a * d == b * c
print(cnt)  # 13


# https://stepik.org/lesson/1679593/step/8?unit=1702707
# https://kompege.ru/task  № 4636 (Уровень: Базовый)
cnt = 0
for row in open('9-3_08.txt'):
    a, b, c, d = sorted(map(int, row.split()))
    cnt += d - a >= 50 and b * c <= 1000
print(cnt)  # 423


# https://stepik.org/lesson/1679593/step/9?unit=1702707
# https://kompege.ru/task  № 4637 (Уровень: Базовый)
cnt = 0
for row in open('9-3_09.txt'):
    a, b, c, d = sorted(map(int, row.split()))
    cnt += d**3 >= a*b*c*2 and all([a>10, b>10, c>10, d>10])
print(cnt)  # 1820


# https://stepik.org/lesson/1679593/step/10?unit=1702707
# https://kompege.ru/task  № 4614
cnt = 0
with open('add/course_233165/9-3_10.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        cnt += sum(d[:-1]) > d[-1] and len(set(d)) == 3
        # cnt += sum(d[:-1]) > d[-1] and len([i for i in d if d.count(i) == 2]) == 2
    print(cnt)  # 133





""" 9.4 Задание 9 | Урок 4 """
# https://stepik.org/lesson/1679595/step/1?unit=1702709
# https://kompege.ru/task  № 5126 /dev/inf 11.22 (Уровень: Средний)
cnt = 0
with open('add/course_233165/9-4_01.txt') as fl:
    for f in fl:
        d = [*map(int, f.split())]
        d1 = [i for i in d if d.count(i) == 1]
        d3 = [i for i in d if d.count(i) == 3]
        cnt += len(d1) == 3 and len(d3) == 3 and sum(d1)/3 <= sum(d3)
    print(cnt)  # 125

# variant
cnt = 0
for f in open('add/course_233165/9-4_01.txt'):
    d = [*map(int, f.split())]
    d1 = [i for i in d if d.count(i) == 1]
    d3 = [i for i in d if d.count(i) == 3]
    cnt += (len(d1), len(d3)) == (3, 3) and sum(d1) / 3 <= sum(d3)
print(cnt)


# https://stepik.org/lesson/1679595/step/2?unit=1702709
# https://kompege.ru/task   № 5284 /dev/inf 12.2022 (Уровень: Средний)
cnt = 0
for f in open('add/course_233165/9-4_02.txt'):
    d = sorted(map(int, f.split()))
    n1 = sum(1 for n in d if d.count(n) == 1) == 3
    n3 = sum(1 for n in d if d.count(n) == 3) == 3
    cnt += (d[0] + d[-1])**2 > sum(i**2 for i in d[1:-1]) or (n1 and n3)
print(cnt)  # 4209


# https://stepik.org/lesson/1679595/step/3?unit=1702709
# https://kompege.ru/task   № 9740 Основная волна 19.06.23 (Уровень: Средний)
cnt = 0
for f in open('add/course_233165/9-4_03.txt'):
    d = sorted(map(int, f.split()))
    n1 = [n for n in d if d.count(n) == 1]
    n3 = [n for n in d if d.count(n) == 3]
    if len(n1) == 4 and len(n3) == 3:
        cnt += sum(n1) / 4 <= n3[0]
print(cnt)  # 36


# https://stepik.org/lesson/1679595/step/4?unit=1702709
# https://kompege.ru/task  № 9778 Основная волна 20.06.23 (Уровень: Средний)
cnt = 0
with open('add/course_233165/9-4_04.txt') as fl:
    for f in fl:
        cnt += 1
        d = [*map(int, f.split())]
        d1 = [i for i in d if d.count(i) == 1]
        d2 = [i for i in d if d.count(i) == 2]
        if len(set(d)) == 5 and d2[0] >= sum(d1) / 4:
            print(cnt)  # 34
            break


# https://stepik.org/lesson/1679595/step/5?unit=1702709
# https://kompege.ru/task  № 9832 Основная волна 27.06.23 (Уровень: Средний)
with open('add/course_233165/9-4_05.txt') as fl:
    for f in fl:
        d = [*map(int, f.split())]
        d1 = [i for i in d if d.count(i) == 1]
        d2 = [i for i in d if d.count(i) == 2]
        if (len(d1), len(d2)) == (3, 4) and max(d) in d1:
            print(sum(d))  # 261
            break


# https://stepik.org/lesson/1679595/step/6?unit=1702709
# https://kompege.ru/task  № 8609 (Уровень: Базовый)
cnt = 0
for row in open('9-4_06.txt'):
    d = sorted(map(int, row.split()))
    if len(set(d)) == 5:
        cnt += (d[0] + d[-1]) * 2 <= sum(d[1:-1]) * 3
print(cnt)  # 2776


# https://stepik.org/lesson/1679595/step/7?unit=1702709
# https://kompege.ru/task  № 6357 (Уровень: Сложный)
cnt = 0
for row in open('9-4_07.txt'):
    d = list(map(int, row.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) > 1]
    if n1 and n2:
        cnt += sum(n1) / len(n1) < sum(n2) / len(n2)
print(cnt)  # 1770


# https://stepik.org/lesson/1679595/step/8?unit=1702709
# https://kompege.ru/task  № 10910 (Уровень: Средний)
cnt = 0
for row in open('9-4_08.txt'):
    d = sorted(map(int, row.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) > 1]
    if n1 and n2:
        cnt += min(d) not in n2 and (d[0] + d[-1]) < sum(n2)
print(cnt)  # 447


# https://stepik.org/lesson/1679595/step/9?unit=1702709
# https://kompege.ru/task  № 6925 (Уровень: Сложный)  👍👍👍
from statistics import mean
cnt = 0
for row in open('9-4_09.txt'):
    d = list(map(int, row.split()))
    even = [i for i in d if not i % 2]
    odd = [i for i in d if i % 2]
    even = mean(even) if even else 0
    odd = mean(odd) if odd else 0
    a = len(set(d)) == 5
    b = abs(even - odd) > 50
    cnt += a != b
print(cnt)  # 862


# https://stepik.org/lesson/1679595/step/10?unit=1702709
# https://kompege.ru/task  № 6999 (Уровень: Базовый)
cnt = 0
for row in open('9-4_10.txt'):
    d = sorted(map(int, row.split()))
    n3 = [i for i in d if not i % 3]
    if n3:
        cnt += len(n3) == 3 and d[-1] - d[0] <= sum(n3)
print(cnt)  # 1835





""" 9.5 Задание 9 | Задачи прошлых лет """
# https://stepik.org/lesson/1679589/step/2?unit=1702704
# https://kompege.ru/task  № 9740 Основная волна 19.06.23 (Уровень: Средний)
cnt = 0
for row in open('9-5_02.txt'):
    d = sorted(map(int, row.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if n1 and n3:
        cnt += len(n3) == 3 and len(n1) == 4 and sum(n1) / len(n1) <= n3[0]
print(cnt)  # 36


# https://stepik.org/lesson/1679589/step/3?unit=1702704
# https://kompege.ru/task  № 9778 Основная волна 20.06.23 (Уровень: Средний)
cnt = 0
for row in open('9-5_03.txt'):
    cnt += 1
    d = list(map(int, row.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) == 2]
    if n1 and n2:
        if len(n2) == 2 and len(n1) == 4 and n2[0] >= sum(n1) / len(n1):
            print(cnt)  # 34
            break


# https://stepik.org/lesson/1679589/step/4?unit=1702704
# https://kompege.ru/task  № 9832 Основная волна 27.06.23 (Уровень: Средний)
for row in open('9-5_04.txt'):
    d = list(map(int, row.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) == 2]
    if n1 and n2:
        if len(n2) == 4 and len(n1) == 3 and max(d) not in n2:
            print(sum(d))  # 261
            break


# https://stepik.org/lesson/1679589/step/5?unit=1702704
# https://kompege.ru/task № 17522 Основная волна 07.06.24 (Уровень: Базовый)
cnt = 0
with open('add/course_233165/9-5_05.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        cnt += len(set(d)) == 3 and d[-1] < sum(d[:-1])
    print(cnt)  # 147

# variant
cnt = 0
for f in open('add/course_233165/9-5_05.txt'):
    d = sorted(map(int, f.split()))
    cnt += len(set(d)) == 3 and d[-1] < sum(d[:-1])
print(cnt)  # 147


# https://stepik.org/lesson/1679589/step/6?unit=1702704
# https://kompege.ru/task  № 17550 Основная волна 08.06.24 (Уровень: Базовый)
cnt = 0
for row in open('9-5_06.txt'):
    d = list(map(int, row.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if n1 and n3:
        if len(n3) == 3 and len(n1) == 3 and sum(n3) ** 2 > sum(n1) ** 2:
            cnt += 1
print(cnt)  # 19


# https://stepik.org/lesson/1679589/step/7?unit=1702704
# https://kompege.ru/task  № 17628 Основная волна 19.06.24 (Уровень: Базовый)
cnt = 0
for row in open('9-5_07.txt'):
    d = sorted(map(int, row.split()))
    cnt += d[0] + d[-1] <= sum(d[1:-1])
print(cnt)  # 15115


# https://stepik.org/lesson/1679589/step/8?unit=1702704
# https://kompege.ru/task № 23193 Основная волна 10.06.25 (Уровень: Базовый)
cnt = res = 0
for f in open('add/course_233165/9-5_08.txt'):
    cnt += 1
    d = [*map(int, f.split())]
    d1 = [i for i in d if d.count(i) == 1]
    d3 = [i for i in d if d.count(i) == 3]
    # if (len(d1), len(d3)) == (3, 3) and d3[0] > sum(d1) / 3:
    if len(d1) == len(d3) and d3[0] > sum(d1) / 3:
        res = cnt
print(res)  # 10493


# https://stepik.org/lesson/1679589/step/9?unit=1702704
# https://kompege.ru/task  № 23268 Основная волна 11.06.25 (Уровень: Базовый)
cnt = 0
for f in open('add/course_233165/9-5_09.txt'):
    cnt += 1
    d = [*map(int, f.split())]
    d1 = [i for i in d if d.count(i) == 1]
    d2 = [i for i in d if d.count(i) == 2]
    if (len(d1), len(d2)) == (3, 4) and sum(d2) / 4 < max(d1):
        print(cnt)  # 17
        break


# https://stepik.org/lesson/1679589/step/10?unit=1702704
# https://kompege.ru/task  № 23368 Резервный день 19.06.25 (Уровень: Базовый)
cnt = res = 0
for row in open('9-5_10.txt'):
    cnt += 1
    d = sorted(map(int, row.split()))
    if len(set(d)) == 5 and (d[0] + d[-1]) * 2 == sum(d[1:-1]) * 3:
        res = cnt
print(res)  # 13412


# https://stepik.org/lesson/1679589/step/11?unit=1702704
# https://kompege.ru/task  № 23747 Демоверсия 2026 (Уровень: Базовый)
from statistics import mean
res = 0
for row in open('9-5_11.txt'):
    d = list(map(int, row.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n3) == 3 and len(n1) == 4 and mean(n1) <= n3[0]:
        res = sum(d)
print(res)  # 901





""""""
""" Варианты """
# 29.1 Вариант 2 | Часть 1
# https://stepik.org/lesson/1729865/step/10?unit=1753692
# https://kompege.ru/task  № 19241 ЕГКР 21.12.24 (Уровень: Базовый)
from statistics import mean
d = open('02_09.txt')
cnt = res = 0
for k in d:
    cnt += 1
    l = [*map(int, k.split())]
    n1 = [i for i in l if l.count(i) == 1]
    n3 = [i for i in l if l.count(i) == 3]
    if len(n1) == 1 and len(n3) == 6:
        if mean(n3) < n1[0]:
            res = cnt
print(res)  # 17975

# https://stepik.org/lesson/1730526/step/10?unit=1754355
# https://kompege.ru/task  № 17863 Демоверсия 2025 (Уровень: Средний)
c = 0
for i in open('03_09.txt'):
    d = [*map(int, i.split())]
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n3) == 3 and len(n1) == 3:
        c += sum(n3) ** 2 > sum(n1)**2
print(c)  # 273


# 31.1 Вариант 4 | Часть 1
# https://stepik.org/lesson/1736669/step/10?unit=1760675
# https://kompege.ru/task  № 21408 Досрочная волна 2025 (Уровень: Базовый)
c = 0
for i in open('04_09.txt'):
    d = [*map(int, i.split())]
    n1 = [k for k in d if d.count(k) == 1]
    n3 = [k for k in d if d.count(k) == 3]
    # if len(n1) == 1 and len(n3) == 6:
    if len(n3) == 6:
        c += max(n3) > n1[0]
print(c)  # 1


# 32.1 Вариант 5 | Часть 1
# https://stepik.org/lesson/1754188/step/10?unit=1778647
# https://kompege.ru/task  № 21704 ЕГКР 19.04.25 (Уровень: Базовый)
for i in open('05_09.txt'):
    d = [*map(int, i.split())]
    if d == sorted(d, reverse=True):
        if (d[0] + d[-1]) / 2 > sum(d[1:-1]) / 5:
            print(sum(d))  # 652
            break


# 33.1 Вариант 6 | Часть 1
# https://stepik.org/lesson/1943170/step/10?unit=1969924
# https://kompege.ru/task  № 23193 Основная волна 10.06.25 (Уровень: Базовый)
row = res = 0
for i in open('06_09.txt'):
    row += 1
    d = [*map(int, i.split())]
    n3 = [i for i in d if d.count(i) == 3]
    n1 = [i for i in d if d.count(i) == 1]
    if len(n3) == 3 and len(n1) == 3:
        if n3[0] > sum(n1) / 3:
            res = row
print(res)  # 10493


# 34.1 Вариант 7 | Часть 1
# https://stepik.org/lesson/1943172/step/10?unit=1969926
# https://kompege.ru/task  № 23268 Основная волна 11.06.25 (Уровень: Базовый)
c = 0
for i in open('07_09.txt'):
    c += 1
    d = [*map(int, i.split())]
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) == 2]
    if len(n1) == 3 and len(n2) == 4:
        if sum(n2) / 4 < max(n1):
            print(c)  # 17
            break


# 35.1 Вариант 8 | Часть 1
# https://stepik.org/lesson/1943178/step/8?unit=1969932
# https://kompege.ru/task  № 23555 Пересдача 03.07.25 (Уровень: Базовый)
c = 0
for i in open('08_09.txt'):
    d = [*map(int, i.split())]
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) == 2]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n3) == 3 and len(n2) == 2:
        if max(n2 + n3) > max(n1):
            c += 1
print(c)  # 1047




