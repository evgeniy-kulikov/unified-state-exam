""""""
"""
Task 17
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 17.1 Решение задания 17 КЕГЭ """

# https://stepik.org/lesson/559879/step/5?unit=553924
cnt = 0
mx = 0
for n in range(1216, 8938):
    if all([not n % 2, n % 7, n % 11, n % 13, n % 23]):
        cnt += 1
        mx = max(mx, n)
print(cnt, mx)  # 2656 8936


# https://stepik.org/lesson/559879/step/7?unit=553924
cnt = 0
mx = 0
for n in range(2345, 6790):
    if str(n % 2) == str(n % 5):
        cnt += 1
        mx = max(mx, n)
print(cnt, mx)  # 888 6781


# https://stepik.org/lesson/559879/step/10?unit=553924
def n_6(n):
    r = ''
    while n:
        r = str(n % 6) + r
        n //= 6
    return all([2 <= len(r) <= 5, r[-2:] in ('11', '15')])

sm = 0
mx = 0
for i in range(1234, 5679):
    if n_6(i):
        sm += i
        mx = max(mx, i)
print(sm, mx)  # 853625 5663


# https://stepik.org/lesson/559879/step/13?unit=553924
cnt = 0
mx = 0
for i in range(1234, 5679):
    if len(hex(i)[2:]) != len(str(i)):
        cnt += 1
        mx = max(mx, i)
print(cnt, mx)  # 2862 4095


""" 17.2 17 КЕГЭ. Файлы """

# https://stepik.org/lesson/891282/step/3?unit=896100
def fn(n):
    return all([not n % 2, n % 7, n % 11, n % 13, n % 23])

with open('2.txt') as fl:
    ls = [int(i) for i in fl if fn(int(i))]
print(sum(ls), min(ls))  # -441368 -10000


# https://stepik.org/lesson/891282/step/4?unit=896100
# Есть отрицательные числа - при определении, остатка от деления на более чем 2, нужно применять модуль
def fn(n):
    return abs(n) % 5 == n % 2

with open('2.txt') as fl:
    ls = [int(i) for i in fl if fn(int(i))]
print(len(ls), max(ls))  # 957 9951

# https://stepik.org/lesson/891282/step/6?unit=896100
# Есть отрицательные числа - при определении, на какую цифру оканчивается произведение, нужно применять модуль
def fn(a, b):
    return all([not (a + b) % 4, (a + b) % 8, abs(a * b) % 10 == 6])

with open('2.txt') as fl:
    ls = [*map(int, fl)]
    res = []
    for i in range(len(ls) - 1):
        a, b = ls[i], ls[i + 1]
        if fn(a, b):
            res.append((a + b))
print(len(res), max(res))  # 67 19332


# https://stepik.org/lesson/891282/step/7?unit=896100
def fn(a, b):
    return all([(a * b) > 0, not (a + b) % 5])

with open('2.txt') as fl:
    ls = [*map(int, fl)]
    res = []
    for i in range(len(ls) - 1):
        a, b = ls[i], ls[i + 1]
        if fn(a, b):
            res.append((a * b))
print(len(res), min(res))  # 478 27816



# https://stepik.org/lesson/891282/step/11?unit=896100
from statistics import mean
def fn(n):
    return all([not n % 4, n % 16, n % 10 >= 5])

with open('3.txt') as fl:
    ls = [*map(int, fl)]
    res = [i for i in ls if fn(i)]
print(len(res), int(mean(res)))  # 151 5456


# https://stepik.org/lesson/891282/step/15?unit=896100
def fn(n):
    return all([10 <= n <= 99, n % 2])

with open('4.txt') as fl:
    ls = [*map(int, fl)]
    res = []
    for i in range(len(ls) - 2):
        if all([not fn(ls[i]), fn(ls[i + 1]), not fn(ls[i + 2])]):
            res.append(sum(ls[i: i + 3]))
print(len(res), max(res))  # 11 14934



""" 17.3 17 КЕГЭ. Решение задач """

# https://stepik.org/lesson/1034171/step/2?unit=1042537
def fn(a, b):
    return any([a < 0, b < 0]) and a + b >= num_3

with open('6.txt') as fl:
    ls = [*map(int, fl)]
    num_3 = len([i for i in ls if not i % 3])
    res = []
    for i in range(len(ls) - 1):
        if fn(ls[i], ls[i + 1]):
            res.append(sum(ls[i: i + 2]))
print(len(res), max(res))  # 2375 97452


# https://stepik.org/lesson/1034171/step/3?unit=1042537
def fn(a, b):
    return any([99 < a < 1000, 99 < b < 1000]) and not (a + b) % num_5

with open('7.txt') as fl:
    ls = [*map(int, fl)]
    num_5 = min([i for i in ls if all([99 < i < 1000, i % 10 == 5])])
    res = []
    for i in range(len(ls) - 1):
        if fn(ls[i], ls[i + 1]):
            res.append(sum(ls[i: i + 2]))
print(len(res), max(res))  # 13 9500


# https://stepik.org/lesson/1034171/step/4?unit=1042537
def fn(a, b):
    return all([any([99 < a < 1000, 99 < b < 1000]), len(str(a)) != len(str(b)), not (a + b) % num_3])

with open('8.txt') as fl:
    ls = [*map(int, fl)]
    num_3 = min([i for i in ls if all([99 < i < 1000, i % 10 == 5])])
    res = []
    for i in range(len(ls) - 1):
        if fn(ls[i], ls[i + 1]):
            res.append(sum(ls[i: i + 2]))
print(len(res), min(res))  # 2 33120


# https://stepik.org/lesson/1034171/step/8?unit=1042537
def fn(nums:list):
    if [len(str(abs(i))) for i in nums].count(4) == 1:
        return sum(nums) ** 2 <= num_39

with open('12.txt') as fl:
    ls = [*map(int, fl)]
    num_39 = max([i for i in ls if all([999 < abs(i) < 10000, abs(i) % 100 == 39])]) ** 2
    res = []
    for i in range(len(ls) - 1):
        if fn(ls[i: i + 2]):
            res.append(sum(ls[i: i + 2]))
print(len(res), max(res))  # 1591 9233


# https://stepik.org/lesson/1034171/step/11?unit=1042537
def fn(nums:list):
    return all([any(len(str(abs(i))) == 3 and str(i)[-1] == '3' for i in nums), sum(nums) < num_3])

with open('15.txt') as fl:
    ls = [*map(int, fl)]
    num_3 = max([i for i in ls if all([99 < abs(i) < 1000, abs(i) % 10 == 3])])
    res = []
    for i in range(len(ls) - 2):
        if fn(ls[i: i + 3]):
            res.append(sum(ls[i: i + 3]))
print(len(res), max(res))  # 147 944

