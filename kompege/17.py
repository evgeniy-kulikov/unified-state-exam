""" https://kompege.ru/task """
"""
5491 7718 8475 9748
11236 11949 13088
23276 27629
"""



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


# 9748 Основная волна 19.06.23 (Уровень: Средний)
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

