""""""
"""
Task 17
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
"""

""" 17.1 Обработка массивов данных """
# https://stepik.org/lesson/1188300/step/2?unit=1201233
res = list()
# file = [i for i in open('add/course_182932/17_2003.txt')]
with open('add/course_182932/17_2003.txt') as file:
    for f in file:
        n = int(f)
        if all([not n % 3, n % 7, n % 17, n % 19, n % 27]):
            res.append(n)
print(len(res), max(res))  # 445 9738


# https://stepik.org/lesson/1188300/step/3?unit=1201233
data = [int(i) for i in open('add/course_182932/17_2013.txt')]
res = []
for n in data:
    if all([n % 10 == 2 or n % 10 == 7, not n % 3, not n % 11]):
        res.append(n)
print(len(res), min(res))  # 13 1287


# https://stepik.org/lesson/1188300/step/4?unit=1201233
data = [int(i) for i in open('add/course_182932/17_2015.txt')]
res = []
for n in data:
    if all([n % 10 == 5 or n % 10 == 7, n % 9, n % 11]):
        res.append(n)
print(len(res), min(res) + max(res))  # 337 10802


# https://stepik.org/lesson/1188300/step/5?unit=1201233
data = [int(i) for i in open('add/course_182932/17_2016.txt')]
res = []
for n in data:
    if all([n % 13 == 7, n % 7, n % 11]):
        res.append(n)
print(max(res) - min(res), len(res))  # 8515 126


# https://stepik.org/lesson/1188300/step/6?unit=1201233
data = [int(i) for i in open('add/course_182932/17_2017.txt')]
res = []
for n in data:
    if all([hex(n)[-1] == 'b',not n % 7, n % 6, n % 13, n % 19]):
        res.append(n)
print(sum(res), len(res))  # 74452 12


# https://stepik.org/lesson/1188300/step/7?unit=1201233
data = [int(i) for i in open('add/course_182932/17_1993.txt')]
cnt = 0
MX = -10**6
for i in range(len(data) - 1):
    a, b = map(int, data[i:i+2])
    if all([not (a+b) % 3, (a+b) % 6, abs(a*b) % 10 == 8]):
        cnt += 1
        MX = max(MX, a + b)
print(cnt, MX)  # 140 17031


# https://stepik.org/lesson/1188300/step/8?unit=1201233
data = [int(i) for i in open('add/course_182932/17_1994.txt')]
cnt = 0
M = 10**6
for i in range(len(data) - 1):
    a, b = map(int, data[i:i+2])
    if all([a * b > 0, not (a+b) % 7]):
        cnt += 1
        M = min(M, a * b)
print(cnt, M)  # 359 115022


# https://stepik.org/lesson/1188300/step/9?unit=1201233
data = [int(i) for i in open('add/course_182932/17_1998.txt')]
cnt = 0
M = -10**6
for i in range(len(data) - 2):
    a, b, c = map(int, data[i:i+3])
    if all([not (a * b * c) % 7, abs(a + b + c) % 10 == 5]):
        cnt += 1
        M = max(M, a + b + c)
print(cnt, M)  # 153 19285


# https://stepik.org/lesson/1188300/step/10?unit=1201233
data = [int(i) for i in open('add/course_182932/17_1999.txt')]
cnt = 0
M = 10**6
for i in range(len(data) - 2):
    a, b, c = map(int, data[i:i+3])
    if all([any([not a % 12, not b % 12, not c % 12]),
            not a % 3, not b % 3, not c % 3]):
        cnt += 1
        M = min(M, (a + b + c) // 3)  # если все числа делятся на 3, то и их сумма (произведение) делиться на 3
print(cnt, M)  # 119 -7213


# https://stepik.org/lesson/1188300/step/11?unit=1201233
data = [int(i) for i in open('add/course_182932/17_2402.txt')]
cnt = 0
M = 0
for i in range(len(data) - 2):
    a, b, c = map(int, data[i:i+3])
    if any([a % 3 == 2, b % 3 == 2, c % 3 == 2]):
        cnt += 1
        M += min(a, b, c)
print(cnt, M)  # 91 2627


# https://stepik.org/lesson/1188300/step/12?unit=1201233
data = [int(i) for i in open('add/course_182932/17_2002.txt')]
cnt = 0
M = 10**10
for i in range(len(data) - 3):
    a, b, c, d = map(int, data[i:i+4])
    if a > b > c > d and abs(a - d) > 1000:
        cnt += 1
        M = min(M, a + b + c + d)
print(cnt, M)  # 181 -31478


