""" https://kompege.ru/task """
"""
1997 2491 4414 4417 4677 5491 6605 6696 6954 7718 8475 8611 9748
11236 11949 13088 16328 16383 17530 17636 19249
23276 27629 31363
"""

"""
ЕГЭ Информатика 2026 | Полный Курс  https://stepik.org/course/233165

17873 1993 1994 1998 1999 2002 2003 2013 2015 2016 2017 2238 2239 2309 2310 2398 2399 2400 2401 2402 2403 
9748 17530 17558 17636 17873 19249 21416 21712 23201 23276 23376 23563 23757
"""


# 1997 (Уровень: Средний)
from math import inf
f = [*map(int, open('17/17_08.txt'))]
mx = -inf
cnt = 0
for a, b in zip(f, f[1:]):
    if a % 2 != b % 2:
        if a % 2:
            a, b = b, a  # even, odd
        if not a % 4 and not b % 11:
            cnt += 1
            mx = max(mx, a + b)
print(cnt, mx)  # 126 15701


# 2491 (Уровень: Базовый)
from statistics import mean
f = [*map(int, open('add/17/17_2491.txt'))]
m = mean(f)
res = []
for i in range(len(f) - 2):
    d = f[i:i+3]
    if any(i < m for i in d):
        if all('9' in str(i) for i in d):
            res.append(sum(d))
print(len(res), max(res))  # 345 17460


# 4414 (Уровень: Базовый)
f = [*map(int, open('add/17/17_4414.txt'))]
c = mx = 0
for i in range(len(f)):
    for k in range(i+1, len(f)):
        a, b = f[i], f[k]
        if not abs(a - b) % 36 and any(not i % 13 for i in (a, b)):
            c += 1
            mx = max(mx, abs(a - b))
print(c, mx)  # 212587 9972


# 4417 (Уровень: Базовый)
f = [*map(int, open('add/17/17_4417.txt'))]
res = []
for i in range(len(f)):
    for k in range(i + 1, len(f)):
        a, b = f[i], f[k]
        if not (a + b) % 120:
            res.append(a + b)
print(len(res), max(res))  # 414830 19920



# 4677 Резервный день 2022(Уровень: Базовый)
cnt, res = 0, -200_000
f = [*map(int, open('add/17/17_4677.txt'))]
n_100 = sum(not i % 100 for i in f)
for a, b in zip(f, f[1:]):
    if (a<0 or b<0) and a+b < n_100:
        cnt += 1
        res = max(res, a + b)
print(cnt, abs(res))  # 4963 93


# 5491 (Уровень: Средний)
f = open('add/17/17_5491.txt')
d = [*map(int, f)]
mn = min(i for i in d if abs(i) % 10 == 3) ** 2
c = res = 0
for a, b in zip(d, d[1:]):
    if abs(min((a, b))) % 10 == 3:  # ✔️
        sm = a**2 + b**2
        if sm < mn:
            c += 1
            res = max(res, sm)
print(c, res)  # 355 99033293


# 6605 Пробник ИМЦ СПб (Уровень: Средний)
f = [*map(int, open('17.txt'))]
M = max(i for i in f if abs(i)%10==5)**2
c = S = 0
for a, b in zip(f, f[1:]):
    if sum(abs(i)%10==5 for i in [a, b]) == 1:
        if abs(a**2 - b**2) <= M:
            c += 1
            S = max(S, abs(a**2 - b**2))
print(c, S)  # 938 98327944


# 6696 (Уровень: Базовый)
# https://stepik.org/lesson/1038775/step/4?unit=1062778
f = [*map(int, open('add/17/17_6696.txt'))]
res = []
for i in range(len(f)):
    d = f[i:i+3]
    if not sum(d) % 2022 and sum(i > 0 for i in d):
        res.append(sum(d))
print(len(res), max(res))  # 7 76836


# 7718 (Уровень: Средний)
f = open('add/17/17_7718.txt')
# d = list(set(map(int, f)))  # лишнее - дубликаты чисел допускаются
d = [*map(int, f)]
c = mx = 0
for i in range(len(d) - 1):  # 👍 перебор всех чисел
    for k in range(i+1, len(d)):  # 👍
        a, b = d[i], d[k]
        if any([not ((a+b) % 18) and a*b % 18, (a + b) % 18 and not a*b % 18]):
            c += 1
            mx = max(mx, a + b)
print(c, mx)  # 120400 19971


# 8475 (Уровень: Средний)
f = open('add/17/17_8475.txt')
d = [*map(int, f)]
mn = min(i for i in d if 100 <= abs(i) < 1000 and abs(i) % 10 == 8) ** 2
cnt = res = 0
for i in range(len(d) - 2):
    if sum(k**2 > mn for k in d[i:i+3]) == 2:
        if len([k for k in d[i:i+3] if 100 <= abs(k) < 1000]):
            cnt += 1
            res = max(res, sum(d[i:i+3]))
print(cnt, res)  # 5312 20235


# 8954 (Уровень: Базовый)
f = [*map(int, open('add/17/17_8954.txt'))]
mx = max(i for i in f if f'{i:x}'[-2:]=='0f')
cnt = res = 0
for a, b in zip(f, f[1:]):
    if sum(not i % 7 for i in (a, b))==1 and not (a + b) % mx:
        cnt += 1
        res = max(res, (a + b))
print(cnt, res)  # 2 9487


# 8611 (Уровень: Базовый)
from math import prod
f = [*map(int, open('add/17/17_8611.txt'))]
mx = max(i for i in f if 100 <= i < 1000)
res = []
for i in range(len(f)):
    d = f[i:i+2]
    if sum(100 <= i < 1000 for i in d) == 1:
        if not prod(d) % mx:
            res.append(prod(d))
print(len(res), min(res))  # 2 2288546


# 9748 Основная волна 19.06.13_(23) (Уровень: Средний)
f = [*map(int, open('17.txt'))]
c = sm = 0
MX = max(i for i in f if i % 100 == 15)
for i in range(len(f) - 2):
    n = f[i:i+3]
    if sum(1 for i in n if 1000 <=i < 10000) == 1:
        if sum(n) >= MX:
            c += 1
            sm = max(sm, sum(n))
print(c, sm)  # 299 196183




# 11236 (Уровень: Средний)
from math import prod
f = open('add/17/17_11236.txt')
d = [*map(int, f)]
mx = max(i for i in d if abs(i) % 10 == 1 and 1000 <= abs(i) < 10000)
mn = min(i for i in d if 10 <= abs(i) < 100) ** 2
cnt = res = 0
for i in range(len(d) - 2):
    num = d[i:i+3]
    a = sum(i > mn for i in num) == 2
    b = not prod(num) % mx
    if a and b:
        cnt += 1
        res = max(res, sum(map(abs, num)))
print(cnt, res)  # 1 118534


# 11949 (Уровень: Средний)
f = open('add/17/17_11949.txt')
d = [*map(int, f)]
mx = max(i for i in d if abs(i) % 100 == 68)
cnt = res = 0
for i in range(len(d) - 3):
    num = d[i:i+4]
    a = [i for i in num if 10 <= abs(i) < 100]
    b = sum(num) >= mx
    if all([len(a) == 1 or len(a) == 4, b]):
        cnt += 1
        res = max(res, sum(num))
print(cnt, res)  # 75 247177


# 13088 (Уровень: Средний)
f = open('add/17/17_13088.txt')
d = [*map(int, f)]
mn = max(i for i in d if i % 100 == 17)
cnt = res = 0
for i in range(len(d) - 2):
    num = d[i:i+3]
    a = [i for i in num if 1000 <= i < 10000]
    b = [i for i in num if not i % 5]
    c = sum(num) > mn
    if all([len(a) == 2, b, c]):
        cnt += 1
        res = max(res, sum(num))
print(cnt, res)  # 21 114132


# 16328 Открытый вариант 2024 (Уровень: Базовый)
f = [*map(int, open('17_16328.txt'))]
M = min(i for i in f if not i%19)
c = S = 0
for a, b in zip(f, f[1:]):
    if any([not a % M, not b % M]):
        c += 1
        S = max(S, a+b)
print(c, S)  # 142 175430


# 16383 ЕГКР 27.04.24 (Уровень: Базовый)
f = [*map(int, open('17_16383.txt'))]
M = max(i for i in f if len(str(abs(i)))==5 and str(abs(i))[-2:]=='21')**2
cnt = S = 0
for a, b in zip(f, f[1:]):
    if a**2 + b**2 >= M:
        if sum(len(str(abs(i)))==5 and str(abs(i))[-2:]=='21' for i in [a, b]) == 1:
                cnt += 1
                S = max(S, a+b)
print(cnt, S)  # 74 103365


# 17530 Основная волна 07.06.24 (Уровень: Базовый)
f = [*map(int, open('17_17530.txt'))]
M = min(f)
c = 0
S = 10**10
for a, b in zip(f, f[1:]):
    if any([a%55 == M, b%55 == M]):
        c += 1
        S = min(S, a+b)
print(c, S)  # 201 2942


# 17636 Основная волна 19.06.24 (Уровень: Средний)
f = [*map(int, open('17_17636.txt'))]
M = max(i for i in f if len(str(abs(i)))==3 and str(i)[-1]=='3')
cnt = S = 0
for a, b, c in zip(f, f[1:], f[2:]):
    if a + b + c < M:
        if any(i for i in [a, b, c]  if len(str(abs(i)))==3 and str(i)[-1]=='3'):
                cnt += 1
                S = max(S, a+b+c)
print(cnt, S)  # 147 944


# 19249 ЕГКР 21.12.24 (Уровень: Базовый)
d = [*map(int, open('17_19249.txt'))]
cnt = 0
M = 10**10
mx = max(i for i in d if str(i)[-2:]=='43')
for a,b,c in (zip(d, d[1:], d[2:])):
    ls = [a,b,c]
    if any(len(str(abs(i)))==5 and str(i)[-2:]=='43' for i in ls):
        abc = a**2 + b**2 + c**2
        if abc <= mx**2:
            cnt += 1
            M  = min(M, abc)
print(cnt, M)  # 92 838850571



# 23276 Основная волна 11.06.25 (Уровень: Базовый)
f = open('add/17/17_23276.txt')
d = [*map(int, f)]
c = sm = 0
mx = max(i for i in d if abs(i) % 100 == 25)
for i in range(len(d) - 2):
    ls = d[i: i + 3]
    if sum(1000 <= abs(i) < 10000 for i in ls) <= 2:
        if sum(ls) <= mx:
            c += 1
            sm = max(sm, sum(ls))
print(c, sm)  # 6315 84523


# 27629 Апробация 04.03.26 (Уровень: Базовый)
c = 0
res = 0
f = open('add/KIM_25164989/17_27629.txt').readlines()
d = [*map(int, f)]
n_43 = max(i for i in d if len(str(abs(i))) == 4 and str(i)[-2:] == '43')
for i in range(len(d) - 1):
    num = d[i:i+2]
    if any(len(str(abs(k))) == 4 for k in num):
        if sum(num) ** 2 < n_43 ** 2:
            c += 1
            res = max(res, sum(num) ** 2)
print(c, res)  # 1218 98843364


# 31363 Пересдача 08.07.26(Уровень: Средний)
res = []
f = [*map(int, open('add/17/17_31363.txt'))]
mx = max(i for i in f if 1000 <= abs(i) <= 9999 and abs(i) % 10 == 3)
for i in range(len(f) - 2):
    d = f[i:i+3]
    if sum(1000 <= abs(i) <= 9999 and abs(i) % 10 == 3 for i in d) == 2:
        if sum(d) > mx:
            res.append(sum(d))
print(len(res),  max(res))  # 2508 104796

