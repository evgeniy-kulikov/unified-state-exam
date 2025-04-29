""""""
"""
Task 09
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 28.1 Задание 9 КЕГЭ. Часть 1 """

# https://stepik.org/lesson/752235/step/6?unit=754082
from statistics import mean
ls = []
# Копируем фрагмент таблицы с данными в текстовый файл.
with open('add/course_100138/task_03.txt') as fl:
    for i in fl:
        ls += list(map(float, i.replace(',', '.').split()))
print(int(max(ls) - mean(ls)))  # 14

# https://stepik.org/lesson/752235/step/11?unit=754082
# Копируем фрагмент таблицы с данными в текстовый файл.
from statistics import mean
ls = []
with open('add/course_100138/task_07.txt') as fl:
    for i in fl:
        d = list(map(float, i.replace(',', '.').split()))
        ls += [j for j in d if j > 10]
print(int(mean(ls)))


# https://stepik.org/lesson/752235/step/12?unit=754082
# Копируем фрагмент таблицы с данными в текстовый файл.
cnt = 0
with open('add/course_100138/task_08.txt') as fl:
    for i in fl:
        d = list(map(float, i.replace(',', '.').split()))
        cnt += sum(j <= 10 for j in d)
print(cnt)  # 14


""" 28.2 Задание 9 КЕГЭ. Часть 2 """
# https://stepik.org/lesson/752236/step/2?unit=754083
# Копируем фрагмент таблицы с данными в текстовый файл.
cnt = 0
with open('add/course_100138/task_num_01.txt') as fl:
    for i in fl:
        d = sorted(map(int, i.split()))
        cnt += d[-1] == sum(d[:2])
print(cnt)  # 64


# https://stepik.org/lesson/752236/step/3?unit=754083
# Копируем фрагмент таблицы с данными в текстовый файл.
cnt = 0
with open('add/course_100138/task_num_02.txt') as fl:
    for i in fl:
        d = sorted(map(int, i.split()))
        cnt += d[-1] ** 2 > sum(i ** 2 for i in d[:2])
print(cnt)  # 3921

# https://stepik.org/lesson/752236/step/8?unit=754083
# Копируем фрагмент таблицы с данными в текстовый файл.
cnt = 0
with open('add/course_100138/task_num_06.txt') as fl:
    for i in fl:
        d = set(map(int, i.split()))
        cnt += len(d) == 1
print(cnt)  # 3


# https://stepik.org/lesson/752236/step/12?unit=754083
# Копируем фрагмент таблицы с данными в текстовый файл.
from math import dist
md = 0
with open('add/course_100138/task_num_11.txt') as fl:
    for i in fl:
        d = tuple(map(int, i.split()))
        md = max((md, dist(d, (0, 0))))
print(int(md))  # 70


# https://stepik.org/lesson/752236/step/16?unit=754083
# Копируем фрагмент таблицы с данными в текстовый файл.
cnt = 0
with open('add/course_100138/9_z12.txt') as fl:
    for i in fl:
        d = sorted(map(int, i.split()))
        cnt += sum(d[::3]) <= sum(d[1:3])
print(cnt)  # 15115


""" 28.3 Задание 9 КЕГЭ. Часть 3 """

# https://stepik.org/lesson/1039432/step/2?unit=1047905
# Копируем фрагмент таблицы с данными в текстовый файл.
cnt = 0
with open('add/course_100138/9_z4.txt') as fl:
    for i in fl:
        d = set(map(int, i.split()))
        cnt += len(d) == 5
print(cnt)  # 2859


# https://stepik.org/lesson/1039432/step/2?unit=1047905
# Копируем фрагмент таблицы с данными в текстовый файл.
cnt = 0
with open('add/course_100138/9_z7.txt') as fl:
    for i in fl:
        d = list(map(int, i.split()))
        d1 = [i for i in d if d.count(i) == 1]
        d3 = [i for i in d if d.count(i) == 3]
        cnt += len(d1) == 4 and len(d3) == 3
print(cnt) # 69


# https://stepik.org/lesson/1039432/step/6?unit=1047905
cnt = 0
with open('add/course_100138/9_z1.txt') as fl:
    for i in fl:
        d = sorted(map(int, i.split()))
        d2 = [i for i in d if d.count(i) == 2]
        cnt += len(d2) and d[-1] > sum(d[:-1])
print(cnt)  # 40


# https://stepik.org/lesson/1039432/step/10?unit=1047905
# ответ не принимается !!!
with open('add/course_100138/9_z9.txt') as fl:
    for i in fl:
        d = list(map(int, i.split()))
        d1 = [i for i in d if d.count(i) == 1]
        dn = [i for i in d if d.count(i) == 2]
        if len(d1) == 3 and len(set(dn)) == 2 and max(d) in d1:
            print(sum(d))  # 261
            break


# https://stepik.org/lesson/1039432/step/10?unit=1047905
from statistics import mean
cnt = 0
with open('add/course_100138/9_z8.txt') as fl:
    for i in fl:
        cnt += 1
        d = list(map(int, i.split()))
        d1 = [i for i in d if d.count(i) == 1]
        d2 = [i for i in d if d.count(i) == 2]
        if len (d1) == 4 and d2[0] >= mean(d1):
            print(cnt)  # 34
            break


""" 28.4 9 КЕГЭ через Python """

# https://stepik.org/lesson/1406852/step/2?unit=1424301
cnt = 0
with open('add/course_100138/9_z1.txt') as fl:
    for i in fl:
        d = sorted(map(int, i.split()))
        d1 = [i for i in d if d.count(i) == 1]
        if len(d1) == 2 and d[-1] < sum(d[:-1]):
            cnt += 1
print(cnt)  # 133



