""""""
"""
Task 17
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 22.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1227166/step/1?unit=1240685
cnt = 0
ms = -100_000
with open('add/course_195798/22.2_Задание_1.txt') as file:
    d = list(map(int, file))
    m = max(i for i in d if 10 <= abs(i) < 100)
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if any([a > 0 and len(str(a))==3, b > 0 and len(str(b))==3]):
            if not sum([a,b]) % m:
                cnt += 1
                ms = max(ms, sum([a,b]))
print(cnt, ms)  # 11 3430


# https://stepik.org/lesson/1227166/step/2?unit=1240685
cnt = 0
ms = 200_000
with open('add/course_195798/22.2_Задание_2.txt') as file:
    d = list(map(int, file))
    m = min(i for i in d if len(str(i))==3 and i%10==5)
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if sum([len(str(a))==3, len(str(b))==3]) == 1:
            if not sum([a,b]) % m:
                cnt += 1
                ms = min(ms, sum([a,b]))
print(cnt, ms)  # 2 33120


# https://stepik.org/lesson/1227166/step/3?unit=1240685
cnt = ms = 0
with open('add/course_195798/22.2_Задание_3.txt') as file:
    d = list(map(int, file))
    m = min(d)
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if any([a % 117 == m, b % 117 == m]):
            cnt += 1
            ms = max(ms, sum([a,b]))
print(cnt, ms)  # 175 173738


# https://stepik.org/lesson/1227166/step/4?unit=1240685
cnt = 0
ms = -100_000
with open('add/course_195798/22.2_Задание_4.txt') as file:
    d = list(map(int, file))
    m = len([i for i in d if not i % 5])
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if sum([a < 0, b < 0]) == 1 and a+b < m:
            cnt += 1
            ms = max(ms, a+b)
print(cnt, ms)  # 2759 4998


# https://stepik.org/lesson/1227166/step/5?unit=1240685
cnt = 0
ms = -10**6
with open('add/course_195798/22.2_Задание_5.txt') as file:
    d = list(map(int, file))
    for i in range(len(d) - 2):
        a, b, c = d[i:i+3]
        if any([a >= 0, b >= 0, c >= 0]) and not (a+b+c) % 2022:
            cnt += 1
            ms = max(ms, a+b+c)
print(cnt, ms)  # 7 76836


# https://stepik.org/lesson/1227166/step/6?unit=1240685
cnt = 0
ms = 10**9
with open('add/course_195798/22.2_Задание_6.txt') as file:
    d = list(map(int, file))
    mx = max(i for i in d if str(i)[-1] == '9')**2
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if sum([str(a)[-1] == '9', str(b)[-1] == '9']) == 1 and a**2 + b**2 < mx:
            cnt += 1
            ms = min(ms, a**2 + b**2)
print(cnt, ms)  # 1428 356530


# https://stepik.org/lesson/1227166/step/7?unit=1240685
cnt = ms = 0
with open('add/course_195798/22.2_Задание_7.txt') as file:
    d = list(map(int, file))
    ln = max([i for i in d if not i % 73])
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if all([a >= ln, b >= ln]):
            cnt += 1
            ms = max(ms, a + b)
print(cnt, ms)  # 161 19678


# https://stepik.org/lesson/1227166/step/8?unit=1240685
cnt = ms = 0
with open('add/course_195798/22.2_Задание_8.txt') as file:
    d = list(map(int, file))
    mn = min(i for i in d if not i % 123)
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if sum([a % 2023 >= mn, b % 2023 >= mn]) == 1:
            cnt += 1
            ms = max(ms, a + b)
print(cnt, ms)  # 4372 176581


# https://stepik.org/lesson/1227166/step/9?unit=1240685
cnt = 0
ms = 2_000
with open('add/course_195798/22.2_Задание_9.txt') as file:
    d = list(map(int, file))
    mn = min(i for i in d if not i % 37)
    mx = max(i for i in d if not i % 73)
    mn, mx = sorted([mn, mx])  # Скрытая ловушка
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if sum([mn < a < mx, mn < b < mx]) == 1:
            cnt += 1
            ms = min(ms, a + b)
print(cnt, ms)  # 136 574


# https://stepik.org/lesson/1227166/step/10?unit=1240685
cnt = ms = 0
with open('add/course_195798/22.2_Задание_10.txt') as file:
    d = list(map(int, file))
    for i in range(len(d) - 1):
        for k in range(i + 1, len(d)):
            a, b = d[i], d[k]
            if not ((a+b) % 60) and any([not a % 40, not b % 40]):
                cnt += 1
                ms = max(ms, a + b)
print(cnt, ms)  # 29278 19860







""" 22.3 Практика (ур. усложненный) """

# https://stepik.org/lesson/1227167/step/1?unit=1240686
cnt = ms = 0
with open('add/course_195798/22.3_Задание_1.txt') as file:
    d = list(map(int, file))
    num = min(i for i in d if len(str(i)) == 3 and i % 10 == 3)
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if sum(1 for i in d[i:i+2] if len(str(i)) == 4) == 1:
            if not (a**2 + b**2) % num:
                cnt += 1
                ms = max(ms, a**2 + b**2)
print(cnt, ms)  # 74 433966217


"""
отсюда и дальше не решал
https://stepik.org/lesson/1227167/step/2?unit=1240686
"""






""" 24.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1227747/step/7?unit=1241268
cnt = ms = 0
with open('add/course_195798/repeat/24.5_Задание_17.txt') as file:
    d = list(map(int, file))
    mn = min(i for i in d if abs(i) % 10 == 7)
    for i in range(len(d) - 1):
        a, b = d[i:i+2]
        if abs(a) % 10 == abs(b) % 10:
            if sum(1 for i in [a, b] if not i % 7) == 1:
                if a*a + b*b <= mn**2:
                    cnt += 1
                    ms = max(ms, a*a + b*b)
print(cnt, ms)  # 102 97666192


""" 26.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1229246/step/7?unit=1242787
from statistics import  mean
cnt, mx = 0, 0
with open('test.txt') as fl:
    d = list(map(int, fl.readlines()))
    even = mean([k for k in d if not k % 2])
    for i in range(len(d) - 1):
        a, b = d[i], d[i + 1]
        if any([not a % 3, not b % 3]) and any([a < even, b < even]):
            cnt += 1
            mx = max(mx, a+b)
print(cnt, mx)  # 2288 14875


""" 27.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1229629/step/7?unit=1243181
with open('add/course_195798/repeat/27.5_Задание_17.txt') as file:
    d = list(map(int, file))
    res = []
    for i in range(len(d) - 1):
        for k in range(i + 1, len(d)):
            if (d[i] + d[k]) % 2 and not (d[i] * d[k] % 3):
                res.append(d[i] + d[k])
    print(len(res), max(res))  # 13931722 19993


""" 28.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1229674/step/7?unit=1243226
with open('add/course_195798/repeat/28.5_Задание_17.txt') as file:
    d = list(map(int, file))
    cnt, mx_r = 0, 0
    mx = max(i for i in d if str(i)[-2:] == '29')
    for i in range(len(d) - 2):
        row = d[i: i + 3]
        if sum(1 for i in row if len(str(i).strip('-')) == 5) == 2:
            if sum(row) <= mx:
                cnt += 1
                mx_r = max(mx_r, sum(row))
    print(cnt, mx_r)  # 157 973622

