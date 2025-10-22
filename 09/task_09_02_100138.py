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


# https://stepik.org/lesson/752235/step/8?unit=754082
mx = cnt = avr = 0
with open('add/course_100138/task_05.txt') as fl:
    for f in fl:
        f = [*map(float, f.replace(',', '.').split())]
        cnt += 1
        mx = max(mx, max(f))
        avr += sum(f) / len(f)
print(int(mx - avr/cnt))  # 11


# https://stepik.org/lesson/752235/step/9?unit=754082
mx = -100
mn = 100
with open('01_Demo/add/task_06.txt') as fl:
    for f in fl:
        f = [*map(float, f.replace(',', '.').split())]
        mx = max(mx, max(f))
        mn = min(mn, min(f))
print(int(mx - mn))  # 17


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


# https://stepik.org/lesson/752235/step/13?unit=754082
cnt = 0
with open('add/course_100138/task_11.txt') as fl:
    for f in fl:
        f = [*map(float, f.replace(',', '.').split())]
        cnt += len([i for i in f if i > 10])
print(cnt)  # 2170


# https://stepik.org/lesson/752235/step/14?unit=754082
c = 0
with open('add/course_100138/task_10.txt') as fl:
    for f in fl:
        d = map(float, f.replace(',', '.').split())
        c += sum(1 for i in d if i > 20)
print(c)  # 515


# https://stepik.org/lesson/752235/step/15?unit=754082
c = 0
with open('add/course_100138/task_11_2.txt') as fl:
    for f in fl:
        d = map(float, f.replace(',', '.').split())
        c += sum(1 for i in d if i > 20)
print(c)  # 204




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


# https://stepik.org/lesson/752236/step/4?unit=754083
cnt = 0
with open('add/course_100138/task_num_03.txt') as fl:
    for f in fl:
        f = [*map(int, f.split())]
        cnt += sum(f)**2 > f[0] * f[1] * f[2]
print(cnt)  # 725


# https://stepik.org/lesson/752236/step/5?unit=754083
cnt = 0
with open('add/course_100138/task_num_04.txt') as fl:
    for f in fl:
        f = sorted(map(int, f.split()))
        cnt += f[1] == (f[0] + f[2]) / 2
print(cnt)  # 88


# https://stepik.org/lesson/752236/step/6?unit=754083
cnt = 0
with open('add/course_100138/task_num_05.txt') as fl:
    for f in fl:
        f = sorted(map(int, f.split()))
        cnt += f[2]**2 == f[0]**2 + f[1]**2
print(cnt)  # 2



# https://stepik.org/lesson/752236/step/9?unit=754083
c = 0
with open('add/course_100138/task_num_07.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        if d.count(90) == 1:
            c += sum(i for i in d if i != 90) == 90
print(c)  # 1


# https://stepik.org/lesson/752236/step/10?unit=754083
c = 0
with open('add/course_100138/task_num_08.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        c += d.count(60) == 3
        # c += len(set(d)) == 1 and sum(d) == 180
print(c)  # 2


# https://stepik.org/lesson/752236/step/11?unit=754083
c = 0
with open('add/course_100138/task_num_09.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        c += sum(1 for i in d if i > 0)==2
print(c)  # 1180


# https://stepik.org/lesson/752236/step/12?unit=754083
from math import dist
md = 0
with open('add/course_100138/task_num_11.txt') as fl:
    for i in fl:
        d = tuple(map(int, i.split()))
        md = max((md, dist(d, (0, 0))))
print(int(md))  # 70


# https://stepik.org/lesson/752236/step/13?unit=754083
c = 0
with open('add/course_100138/task_num_12.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        if len(set(d)) == 1 or len([i for i in d if d.count(i) == 2]) == 4:
            c += 1
print(c)  # 5


# https://stepik.org/lesson/752236/step/15?unit=754083
c = 0
with open('add/course_100138/9_z2.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        if d[0] + d[3] < d[1] + d[2]:
            c += 1
print(c)  # 1285


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


# https://stepik.org/lesson/1039432/step/3?unit=1047905
# Копируем фрагмент таблицы с данными в текстовый файл.
cnt = 0
with open('add/course_100138/9_z7.txt') as fl:
    for i in fl:
        d = list(map(int, i.split()))
        d1 = [i for i in d if d.count(i) == 1]
        d3 = [i for i in d if d.count(i) == 3]
        cnt += len(d1) == 4 and len(d3) == 3
print(cnt)    # 69


# https://stepik.org/lesson/1039432/step/4?unit=1047905
cnt = 0
with open('add/course_100138/9_z9.txt') as fl:
    for f in fl:
        f = list(map(int, f.split()))
        twins = [i for i in f if f.count(i) == 2]
        single = [i for i in f if i not in twins]
        cnt += len(twins) == 4 and len(single) == 3
print(cnt)  # 183


# https://stepik.org/lesson/1039432/step/6?unit=1047905
cnt = 0
with open('add/course_100138/9_z1.txt') as fl:
    for i in fl:
        d = sorted(map(int, i.split()))
        d2 = [i for i in d if d.count(i) == 2]
        cnt += len(d2) and d[-1] > sum(d[:-1])
print(cnt)  # 40


# https://stepik.org/lesson/1039432/step/7?unit=1047905
cnt = 0
with open('add/course_100138/9_z4.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        if len(set(d)) == 5 and (d[0] + d[-1]) * 3 <= sum(d[1:-1]) * 2:
            cnt += 1
    print(cnt)  # 853


# https://stepik.org/lesson/1039432/step/8?unit=1047905
cnt = 0
with open('add/course_100138/9_z5.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        if len(set(d)) == 5 and 2 * (d[0] + d[-1]) >= sum(d[1:-1]):
            cnt += 1
    print(cnt)  # 15058


# https://stepik.org/lesson/1039432/step/9?unit=1047905
cnt = 0
with open('add/course_100138/9_z10.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        rep = [i for i in d if d.count(i) == 2]
        if len(rep) == 2 and d[-1] < sum(d[:-1]):
            cnt += 1
    print(cnt)  # 147



""" Взято на мой курс """
# https://stepik.org/lesson/1039432/step/10?unit=1047905
# ответ не принимается !!!
with open('add/course_100138/9_z9.txt') as fl:
    for i in fl:
        d = list(map(int, i.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 2]
        if len(one) == 3 and len(rep) == 4 and max(d) in one:
            print(sum(d))  # 261  ВЕРНО!!!
            break


# https://stepik.org/lesson/1039432/step/11?unit=1047905
cnt = 0
with open('add/course_100138/9_z6.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        if len(set(d)) == 5 and (d[0] + d[-1]) * 3 >= sum(d[1:-1]) * 2:
            cnt += 1
    print(cnt)  # 7695


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


# https://stepik.org/lesson/1039432/step/13?unit=1047905
from statistics import mean
cnt = 0
with open('add/course_100138/9_z3.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 2]
        if len(rep) == 2 and len(one) == 4 and mean(one) <= sum(rep):
            cnt += 1
    print(cnt)  # 2241


# https://stepik.org/lesson/1039432/step/14?unit=1047905
from statistics import mean
cnt = 0
with open('add/course_100138/9_z7.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 3]
        if len(rep) == 3 and len(one) == 4 and mean(one) <= rep[0]:
            cnt += 1
    print(cnt)  # 36


# https://stepik.org/lesson/1039432/step/16?unit=1047905
cnt = 0
with open('add/course_100138/09_z11.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 3]
        if len(rep) == 3 and len(one) == 3 and sum(rep)**2 > sum(one)**2:
            cnt += 1
    print(cnt)  # 19





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


# https://stepik.org/lesson/1406852/step/3?unit=1424301
cnt = 0
with open('add/course_100138/9_z2.txt') as fl:
    for f in fl:
        f = sorted(map(int, f.split()))
        cnt += (f[0] + f[-1]) < sum(f[1:-1])
print(cnt)  # 1285


# https://stepik.org/lesson/1406852/step/4?unit=1424301
from statistics import mean
cnt = 0
with open('add/course_100138/9_z3.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 2]
        if len(rep) == 2 and len(one) == 4 and mean(one) <= sum(rep):
            cnt += 1
    print(cnt)  # 2241




# https://stepik.org/lesson/1406852/step/9?unit=1424301
from statistics import mean
cnt = 0
with open('add/course_100138/9_z8.txt') as file:
    for fl in file:
        cnt += 1
        d = sorted(map(int, fl.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 2]
        if len(rep) == 2 and len(one) == 4 and rep[0] >= mean(one):
            print(cnt)  # 34
            break
