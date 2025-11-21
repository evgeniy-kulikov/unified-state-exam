""""""
"""
Task 09
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 9.1 Задание 9 | Урок 1 """
# https://stepik.org/lesson/1679586/step/7?unit=1702700
cnt = 0
with open('add/course_233165/WAH-un7SO.txt') as fl:
    for f in fl:
        a, b, c = sorted(map(int, f.split()))
        cnt += (a + c) / 2 == b
    print(cnt)  # 67


# https://stepik.org/lesson/1679586/step/9?unit=1702700
# ПОСЛЕДОВАТЕЛЬНОСТЬ ломаных, то есть стороны идут по порядку
cnt = 0
with open('add/course_233165/N5aH51mMN.txt') as fl:
    for f in fl:
        a, b, c, d = map(int, f.split())
        cnt += a == c and b == d and a != b
    print(cnt)  # 353

# variant
cnt = 0
for f in open('add/course_233165/N5aH51mMN.txt'):
    a, b, c, d = map(int, f.split())
    cnt += all([a == c, b == d, a != b])
print(cnt)  # 353


# https://stepik.org/lesson/1679586/step/12?unit=1702700
# https://kompege.ru/task   № 2099 (Уровень: Базовый)
cnt = res = 0
for f in open('add/course_233165/1_01.txt'):
    d = sorted(map(int, f.split()))
    if sum(d) == 180:
        cnt += 1
        res += len(set(d)) < 3
print(res * 100 // cnt)  # 3



""" 9.2 Задание 9 | Урок 2 """
# https://stepik.org/lesson/1679588/step/1?unit=1702702
cnt = 0
with open('add/course_233165/aPOjXPNBT.txt') as fl:
    for f in fl:
        a, b, c = sorted(map(int, f.split()))
        cnt += c > 90 and a + b + c == 180
    print(cnt)  # 1071


# https://stepik.org/lesson/1679588/step/2?unit=1702702
cnt = 0
with open('add/course_233165/OZIpBBHnP.txt') as fl:
    for f in fl:
        a, b, c, d = map(int, f.split())
        cnt += a == c and b == d and a + b + c + d == 360
    print(cnt)  # 984

# variant
cnt = 0
for f in open('add/course_233165/OZIpBBHnP.txt'):
    a, b, c, d = map(int, f.split())
    cnt += a == c and b == d and a+b+c+d == 360
print(cnt)  # 984


# https://stepik.org/lesson/1679588/step/3?unit=1702702
cnt = 0
with open('add/course_233165/vUKQEs8H3.txt') as fl:
    for f in fl:
        a, b, c, d = sorted(map(int, f.split()))
        cnt += a+b+c > d
    print(cnt)  # 4757


# https://stepik.org/lesson/1679588/step/4?unit=1702702
# https://kompege.ru/task   № 2043 (Уровень: Средний)
cnt = 0
for f in open('add/course_233165/2_01.txt'):
    a,b,c,d = list(map(int, f.split()))
    cnt += a == c and b == d
print(cnt)  # 754




""" 9.3 Задание 9 | Урок 3 """
# https://stepik.org/lesson/1679593/step/1?unit=1702707
cnt = 0
with open('add/course_233165/3_01.txt') as fl:
    for f in fl:
        a, b, c = sorted(map(int, f.split()))
        cnt += (a+c) / 2 <= b
    print(cnt)  # 2559


# https://stepik.org/lesson/1679593/step/2?unit=1702707
# https://kompege.ru/task   № 4669 Резервный день 2022 (Уровень: Базовый)
cnt = 0
for f in open('add/course_233165/3_02.txt'):
    a,b,c,d = sorted(map(int, f.split()))
    cnt += a+d < b+c
print(cnt)  # 1285


# https://stepik.org/lesson/1679593/step/10?unit=1702707
# https://kompege.ru/task  № 4614
cnt = 0
with open('add/course_233165/3_10.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        cnt += sum(d[:-1]) > d[-1] and len(set(d)) == 3
        # cnt += sum(d[:-1]) > d[-1] and len([i for i in d if d.count(i) == 2]) == 2
    print(cnt)  # 133



""" 9.4 Задание 9 | Урок 4 """
# https://stepik.org/lesson/1679595/step/1?unit=1702709
# https://kompege.ru/task  № 5126 /dev/inf 11.22 (Уровень: Средний)
cnt = 0
with open('add/course_233165/9yLNISRDc.txt') as fl:
    for f in fl:
        d = [*map(int, f.split())]
        d1 = [i for i in d if d.count(i) == 1]
        d3 = [i for i in d if d.count(i) == 3]
        cnt += len(d1) == 3 and len(d3) == 3 and sum(d1)/3 <= sum(d3)
    print(cnt)  # 125

# variant
cnt = 0
for f in open('add/course_233165/9yLNISRDc.txt'):
    d = [*map(int, f.split())]
    d1 = [i for i in d if d.count(i) == 1]
    d3 = [i for i in d if d.count(i) == 3]
    cnt += (len(d1), len(d3)) == (3, 3) and sum(d1) / 3 <= sum(d3)
print(cnt)



# https://stepik.org/lesson/1679595/step/4?unit=1702709
# https://kompege.ru/task  № 9778 Основная волна 20.06.23 (Уровень: Средний)
cnt = 0
with open('add/course_233165/eX154PNow.txt') as fl:
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
with open('add/course_233165/LbhxBxvcF.txt') as fl:
    for f in fl:
        d = [*map(int, f.split())]
        d1 = [i for i in d if d.count(i) == 1]
        d2 = [i for i in d if d.count(i) == 2]
        if (len(d1), len(d2)) == (3, 4) and max(d) in d1:
            print(sum(d))  # 261
            break




""" 9.5 Задание 9 | Задачи прошлых лет """
# https://stepik.org/lesson/1679589/step/5?unit=1702704
# https://kompege.ru/task № 17522 Основная волна 07.06.24 (Уровень: Базовый)
cnt = 0
with open('add/course_233165/AerfLn3ms.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        cnt += len(set(d)) == 3 and d[-1] < sum(d[:-1])
    print(cnt)  # 147

# variant
cnt = 0
for f in open('add/course_233165/AerfLn3ms.txt'):
    d = sorted(map(int, f.split()))
    cnt += len(set(d)) == 3 and d[-1] < sum(d[:-1])
print(cnt)  # 147


# https://stepik.org/lesson/1679589/step/8?unit=1702704
# https://kompege.ru/task № 23193 Основная волна 10.06.25 (Уровень: Базовый)
cnt = res = 0
for f in open('add/course_233165/-kXoRpmha6.txt'):
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
for f in open('add/course_233165/hB4WZuaqC0.txt'):
    cnt += 1
    d = [*map(int, f.split())]
    d1 = [i for i in d if d.count(i) == 1]
    d2 = [i for i in d if d.count(i) == 2]
    if (len(d1), len(d2)) == (3, 4) and sum(d2) / 4 < max(d1):
        print(cnt)  # 17
        break

