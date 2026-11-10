""" https://kompege.ru/task """
"""
4634 5627 6081 6262 6357 6783 6925 7030 7674 8467 8475 9696 9832 
11228 11946 12795 13824 14249 14661 16256 16375 17550 18258 19878
20070 20189 20282 20488 21592 21976 22547 23193 23747 24344 24345 24346 24347 24359 24360 24889 
27284 27285 27287 28930 29341 29962
31116 31147 31217 31355 31506
"""


""" Взято на мой курс """
# 4634 (Уровень: Базовый)
cnt = 0
with open('add/09/09_4634.txt') as flile:
    for fl in flile:
        a, b, c, d = sorted(map(int, fl.split()))
        if a*d == b*c and c**2 > a*d:
            cnt += 1
print(cnt)  # 13



""" Взято на мой курс """
# 5627 (Уровень: Средний) 🌶️
cnt = 0
for f in open('add/09/09_5627.txt'):
    d = sorted(map(int, f.split()))
    a = [i for i in d if d.count(i) > 1]
    b = all(a - b == d[0] - d[1] for a, b in zip(d, d[1:]))
    if a or b:
        cnt += 1
print(cnt)  # 525


# 6081 /dev/inf 02.2023(Уровень: Сложный) 🌶️🌶️🌶️👍
# две тройки с равными суммами — есть тройка с суммой ровно в половину суммы всей строки
from itertools import combinations, permutations
cnt = 0
with open('add/09/09_6081.txt') as file:
    for fl in file:
        d = list(map(int, fl.split()))
        n1 = [i for i in d if d.count(i) == 1]
        n2 = [i for i in d if d.count(i) == 2]
        if len(n1) == 4 and len(n2) == 2:
            if any(sum(c) * 2 == sum(d) for c in combinations(d, 3)):
                cnt += 1
print(cnt)  # 127



""" Взято на мой курс """
# 6262 Danov2302 (Уровень: Средний)
f = open('add/09/09_6262.txt')
cnt = 0
data = [list(map(int, i.split())) for i in f]
for d in data:
    a = len(set(d)) < 6
    b = sum(i % 2 for i in d) == 3
    cnt += a + b == 1
print(cnt)  # 1852


# 6357 (Уровень: Сложный) 🌶️🌶️
cnt = 0
with open('add/09/09_6357.txt') as file:
    for fl in file:
        d = list(map(int, fl.split()))
        n1 = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) > 1]
        if n1 and rep:
            cnt += sum(n1) / len(n1) < sum(rep) / len(rep)
print(cnt)  # 1770


# 6783 (Уровень: Сложный) 🌶️🌶️
cnt = 0
with open('add/09/09_6783.txt') as file:
    for fl in file:
        d = list(map(int, fl.split()))
        n1 = [i for i in d if d.count(i) == 1]
        n3 = [i for i in d if d.count(i) == 3]
        a = len(n3) == len(n1) == 3
        b = sum(n1) / 3 < sum(n3)
        cnt += a and b
print(cnt)  # 125



# 6925 (Уровень: Сложный) 🌶️🌶️🌶️👍
cnt = 0
with open('add/09/09_6925.txt') as file:
    for fl in file:
        d = list(map(int, fl.split()))
        n1 = [i for i in d if d.count(i) == 1]
        n2 = [i for i in d if d.count(i) == 2]
        even = [i for i in d if not i % 2]
        odd = [i for i in d if i % 2]
        even = (even, [0])[not len(even)]  # sum([0]) / len([0])) == 0
        odd = (odd, [0])[not len(odd)]
        a =  len(n2) == 2 and len(n1) == 4
        b = abs(sum(even) / len(even) - sum(odd) / len(odd)) > 50
        cnt += a + b == 1
print(cnt)  # 862


# 7030 Danov2303(Уровень: Сложный) 🌶️🌶️🌶️
cnt = 0
with open('add/09/09_7030.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        n2 = [i for i in d if d.count(i) == 2]
        if len(n2) == 6 and len(set(d)) == 3:
            a, b, c = sorted(set(d))
            cnt += c**2 == a**2 + b**2
print(cnt)  # 148



# 7674 (Уровень: Сложный) 🌶️🌶️🌶️
cnt = 0
with open('add/09/09_7674.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        n1 = [i for i in d if d.count(i) == 1]
        n2 = [i for i in d if d.count(i) == 2]
        if len(n1) == 3 and sum(n1) / 3 < sum(n2) / 2:
            cnt += 1
print(cnt)  # 344


""" Взято на мой курс """
#  8467 (Уровень: Средний)
c  = 0
for s in open('9_8467.txt'):
    d = sorted(map(int, s.split()))
    a = len(set(d)) == 5
    b = 2 * (d[0] + d[-1]) < sum(d[1:-1])
    c += a + b == 1
print(c)  # 4720


# 8475 (Уровень: Средний)
from math import prod
f = open('add/09/09_8946.txt')
cnt = 0
data = [sorted(map(int, i.split())) for i in f]
for d in data:
    if d[-1]**2 > prod(d[:-1]):
        cnt += sum(d[-2:]) / sum(d[:-2]) >= 2
print(cnt)  # 10


""" Взято на мой курс """
#  9696 Danov2307 (Уровень: Средний)
c = 0
for s in open('9_9696.txt'):
    d = sorted(map(int, s.split()))
    n2 = [i  for i in d if d.count(i) == 2]
    if len(n2) == 2:
        c += sum(d[2:]) > sum(d[:2]) * 2 and d[-1] % d[0] != 0
print(c)  # 125


""" Взято на мой курс """
# 9832 Основная волна 27.06.13_(23)(Уровень: Средний)
f = open("09.txt").readlines()
for d in f:
    d = [*map(int, d.split())]
    mx = max(d)
    a =  [i for i in d if d.count(i)==2]
    b =  len([i for i in d if d.count(i)==1]) == 3
    if len(a)==4 and b and mx not in a:
        print(sum(d))  # 261
        break


# 11228 (Уровень: Сложный) 🌶️🌶️🌶️
res = 0
with open('add/09/09_11228.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        n2 = [i for i in d if d.count(i) == 2]
        n3 = [i for i in d if d.count(i) == 3]
        if len(n2) == 4 and len(set(n2)) == 2 and len(n3) == 3:
            if sum(i % 2 for i in d[:4]) == 2:
                res += sum(d)
print(res)  # 4675



""" Взято на мой курс """
# 11946 (Уровень: Средний)
c = 0
for n in open('09.txt'):
    d = [*map(int, n.split())]
    n3 = [i for i in d if d.count(i)==3]
    n1 = [i for i in d if d.count(i)==1]
    a = len(n3)==3 and len(n1)==4
    # b = all(a <= b for a,b,in zip(d, d[1:]))
    b = (d == sorted(d))
    if a + b <= 1:
        c += 1
print(c)  # 14018


# 12795 Открытый курс "Слово пацана" (Уровень: Средний)
f = open('add/09/09_12795.txt')
cnt = 0
data = [list(map(int, i.split())) for i in f]
for d in data:
    a = sum(d) // 7
    cnt += a in d
print(cnt)  # 35


# 13824 (Уровень: Сложный) 🌶️🌶️🌶️
from math import prod
cnt = res = 0
with open('add/09/09_13824.txt') as file:
    for fl in file:
        cnt += 1
        d = list(map(int, fl.split()))
        if all(a % 2 != b % 2 for a, b in zip(d, d[1:])):
            n1 = [i for i in d if d.count(i) == 1]
            nm = [i for i in d if d.count(i) > 1]
            if sum(n1) * 3 >= prod(nm):
                res += cnt
print(res)  # 1671305


# 14249 (Уровень: Сложный) 🌶️🌶️🌶️
cnt = res = 0
with open('add/09/09_14249.txt') as file:
    for fl in file:
        cnt += 1
        d = sorted(map(int, fl.split()))
        even = [i for i in d if not i % 2]
        odd = [i for i in d if i % 2]
        if len(even) and len(odd):
            if d[0] + d[-1] == d[1] + d[-2] == sum(d[2:4]):
                res = cnt
print(res)  # 11297


# 14661 Открытый курс "Слово пацана" (Уровень: Сложный) 🌶️🌶️🌶️
cnt = 0
with open('add/09/09_14661.txt') as file:
    for fl in file:
        d = list(map(int, fl.split()))
        even = [i for i in d if not i % 2]
        odd = [i for i in d if i % 2]
        if even and odd:
            if not len(even) % 2 and len(odd) % 2:
                cnt += not max(even) % 4
print(cnt)  # 254



""" Взято на мой курс """
# 16256 Джобс 03.05.24 (Уровень: Сложный) 🌶️🌶️
MX = None
with open('add/09/09_16256.txt') as file:
    for fl in file:
        d = sorted(map(int, fl.split()))
        # if len(set(d)) == 2 and len(set(d[:2])) == len(set(d[-2:])) == 1:  # [1, 1, 4, 4, 4, 4, 4]
        if len(set(d)) == 2 and d[0]==d[1] and d[-2]==d[-1]:  # [1, 1, 4, 4, 4, 4, 4]
            if (d[0] + d[-1]) * 2 < sum(d[2:-2]):
                MX = sum(d)
    print(MX)  # 1700


# 16375 ЕГКР 27.04.24 (Уровень: Базовый)
cnt = 0
for row in [[*map(int, i.split())] for i in open('09.txt')]:
    if len(set(row)) == 6:
        a, b, c = sorted(i for i in row if row.count(i) == 1)[:3]
        d = [i for i in row if row.count(i) == 2][0]
        cnt += a * b * c > d**2
print(cnt)  # 293


# 17550 Основная волна 08.06.24 (Уровень: Базовый)
c = 0
for n in open('09.txt'):
    d = [*map(int, n.split())]
    n3 = [i for i in d if d.count(i)==3]
    n1 = [i for i in d if d.count(i)==1]
    if len(n3)==len(n1)==3:
        c += sum(n3)**2 > sum(n1)**2
print(c)  # 19


""" Взято на мой курс """
# 18258 (Уровень: Сложный) 🌶️🌶️🌶️
cnt = res = 0
with open('add/09/09_18258.txt') as file:
    for fl in file:
        cnt += 1
        d = list(map(int, fl.split()))
        if d == sorted(d):
            rep = [i for i in d if d.count(i) > 1]
            if rep and [i for i in rep if not sum(map(int, str(i))) % 2]:
                res = cnt
    print(res)  # 6937


# 19878 (Уровень: Средний)
res = 0
for f in open('add/09/09_19878.txt'):
    d = list(map(int, f.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n3) == 3 and len(n1) == 4:
        if sum(n1) / 4 <= n3[0]:
            res += 1
print(res)  # 58


""" Взято на мой курс """
# 20070 (Уровень: Средний)
res = 0
for f in open('add/09/09_20070.txt'):
    d = list(map(int, f.split()))
    n2 = [i for i in d if 10 <= i < 100]
    a = len(n2) == 6
    b = all(i % 5 for i in d)
    if a + b == 1:
        res += 1
print(res)  # 1727


# 20189 (Уровень: Средний)
res = 0
for f in open('add/09/09_20189.txt'):
    d = sorted(map(int, f.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) == 2]
    if len(n1) == 3 and len(n2) == 4:
        if d[0] * d[1] > sum(d[2:]):
            res += 1
print(res)  # 113


# 20282 (Уровень: Средний)
res = 0
for f in open('add/09/09_20282.txt'):
    d = sorted(map(int, f.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n1) == len(n3) == 3:
        if d[0]**2 + d[-1]**2 >= sum(d[1:-1])**2:
            res += 1
print(res)  # 6


# 20488 (Уровень: Сложный) 🌶️🌶️🌶️
cnt = 0
for f in open('add/09/09_20488.txt'):
    d = list(map(int, f.split()))
    n1 = [i for i in d if d.count(i) == 1]
    nm = [i for i in d if d.count(i) > 1]
    if nm and max(d) not in nm:
        # cnt += sum(n1) >= sum(nm) * 3
        cnt += sum(n1) / sum(nm) >= 3
print(cnt)  # 1382


""" Взято на мой курс """
# 21592 (Уровень: Средний)
res = c = 0
for f in open('add/09/09_21592.txt'):
    c += 1
    d = [*map(int, f.split())]
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) == 2]
    if len(n2) == 6:
        if (max(n2) - min(n2)) ** 2 > sum(i**2 for i in n1) * 2:
            res = c
print(res)  # 29938


""" Взято на мой курс """
# 21976 (Уровень: Средний)
res = 0
for f in open('add/09/09_21976.txt'):
    d = [*map(int, f.split())]
    if len(set(d)) == 4:
        even = [i for i in d if not i % 2]
        odd = [i for i in d if i % 2]
        if sum(even)**2 > sum(i**3 for i in odd):
            res = sum(d)
print(res)  # 246


""" Взято на мой курс """
# 22547 (Уровень: Средний)
# если числа расположены в порядке возрастания, то среди них отсутствуют одинаковые числа ✔️
res = 0
for f in open('add/09/09_22547.txt'):
    d = [*map(int, f.split())]
    if d == sorted(d) and len(set(d)) == 6 and sum(i % 2 for i in d) == 3:
        res = sum(d)
print(res)  # 335



""" Взято на мой курс """
# 23193 Основная волна 10.06.25(Уровень: Базовый)
cnt = 0
Mx = None
with open('add/09/09_23193.txt') as flile:
    for fl in flile:
        cnt += 1
        d = list(map(int, fl.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 3]
        if len(one) == 3 and len(rep) == 3 and rep[0] > sum(one) / 3:
            Mx = cnt
    print(Mx)  # 10493


""" Взято на мой курс """
# 23747 Демоверсия 2026 (Уровень: Базовый)
f = open('add/09/09_23747.txt')
res = 0
data = [list(map(int, i.split())) for i in f]
for d in data:
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n3) == 3 and len(n1) == 4:
        if sum(n1) / 4 <= n3[0]:
            res = sum(d)
print(res)  # 901


# 24344 (Уровень: Средний) 🌶️
res = c = 0
for i in open('add/09/09_24344.txt'):
    c += 1
    d = sorted(map(int, i.split()))
    if (d[0] + d[-1])**2 > d[1]**3 + d[2]**3:
        if d[0] + d[-1] != d[1] + d[2]:
            res += c
print(res)  # 26033


# 24345 (Уровень: Средний) 🌶️
for i in open('add/09/09_24345.txt'):
    d = sorted(map(int, i.split()))
    if not sum(d) % 2 and d[-2]**2 > d[0] * d[-1]:  # d[-2] квадрат второго БОЛЬШЕГО по величине
        if sum(i for i in d if i < 90) % 10 == 4:
            print(sum(d))  # 1296
            break


# 24346 (Уровень: Средний) 🌶️
res = c = 0
for i in open('add/09/09_24346.txt'):
    c += 1
    d = list(map(int, i.split()))
    n1 = [i for i in d if d.count(i) == 1]
    nm = [i for i in d if d.count(i) > 1]
    if n1 and nm:
        if sum(nm)**2 > sum(n1)**2 and sum(d) % 2:
            res = c
print(res)  # 2671


# 24347 (Уровень: Средний) 🌶️
from math import prod
res = 0
for i in open('add/09/09_24347.txt'):
    d = list(map(int, i.split()))
    mn, mx = min(d), max(d)
    a = d.count(mx) == 1
    b = all(i not in (mn, mx) for i in (d[0], d[-1]))
    c = not prod(sorted(d)[-3:]) % mn
    res += (a + b + c) == 1
print(res)  # 2462


# 24359 (Уровень: Средний)
res = 0
for i in open('add/09/09_24359.txt'):
    d = list(map(int, i.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) == 2]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n3) == 3 and len(n2) == 2:
        if sum(n2 + n3) > sum(n1):
            res = sum(d)
print(res)  # 156


# 24360 (Уровень: Сложный)🌶️🌶️🌶️
res = 10**10
for f in open('add/09/09_24360.txt'):
    d = sorted(map(int, f.split()))
    a = d[0] ** 2 in d
    if sum(d[i] == d[i+1] for i in range(0, 7, 2)) >= 3:
    # cnt = 0
    # for i in range(0, 7, 2):
    #     cnt += d[i] == d[i+1]
    # if cnt >= 3:
        res = min(res, sum(d))
print(res)  # 98



# 24889 (Уровень: Средний) 🌶️
res = 0
for i in open('add/09/09_24889.txt'):
    d = list(map(int, i.split()))
    n1 = sorted(i for i in d if d.count(i) == 1)
    n34 = [i for i in d if 3 <= d.count(i) <= 4]
    if 0 < len(n34) <= 4 and max(d) in n34:
        if len(n1) + len(n34) == 8:
            res += n1[0] + n1[-1] <= sum(n1[1:-1])
print(res)  # 213



# 27284 (Уровень: Средний) 🌶️
res = 0
for i in open('add/09/09_27284.txt'):
    d = list(map(int, i.split()))
    n1 = sorted(i for i in d if d.count(i) == 1)
    n23 = [i for i in d if 2 <= d.count(i) <= 3]
    if 0 < len(n23) <= 3 and min(d) in n23:
        if len(n1) + len(n23) == 7:
            res += n1[0] + n1[-1] > sum(n1[1:-1])
print(res)  # 473


# 27285 (Уровень: Базовый)
res = 0
for i in open('add/09/09_27285.txt'):
    d = list(map(int, i.split()))
    if all(a <= b for a, b in zip(d, d[1:])):
        odd = sum(i % 2 for i in d)
        res += odd <= 3
print(res)  # 130


# 27287 (Уровень: Базовый)
res = 0
for i in open('add/09/09_27287.txt'):
    d = sorted(map(int, i.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n3) == 6 and len(set(n3)) == 2  and n1[0] <= min(n3):
        print(abs(max(n3)))  # 43
        break


# 28930 ЕГКР 18.04.26(Уровень: Базовый)
res = 0
for i in open('add/09/09_28930.txt'):
    d = list(map(int, i.split()))  # не сортируем!
    if all(a < b for a, b in zip(d, d[1:])):
        if (d[0] + d[-1]) <= sum(d[1:-1]):
            res +=1
print(res)  # 138


# 29341 Открытый вариант 2026(Уровень: Базовый)
res = 0
for i in open('add/09/09_29341.txt'):
    d = sorted(map(int, i.split()))
    if d[-1] < sum(d[:-1]):
        if (d[0] + d[-1]) != sum(d[1:-1]):
            res +=1
print(res)  # 2354


# 29962 Апробация 14.05.26(Уровень: Базовый)
res = c = 0
for i in open('add/09/09_29962.txt'):
    c += 1
    d = sorted(map(int, i.split()))
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n1) == 4 and len(n3) == 3:
        if sum(n1) / 4 > n3[0]:
            res = c
print(res)  # 13609



# 31116 Основная волна 18.06.26(Уровень: Базовый)
res = 0
for i in open('add/09/09_31116.txt'):
    d = sorted(map(int, i.split()))
    if len(set(d)) == 5:
        if (d[0] + d[-1]) * 2 > sum(d[1:-1]):
            print(sum(d))  # 1980
            break


# 31147 Основная волна 19.06.26(Уровень: Базовый)
c = res = 0
for i in open('add/09/09_31147.txt'):
    c += 1
    d = sorted(map(int, i.split()))
    if len(set(d)) == 6:
        if sum(d[:3]) * 2 < sum(d[3:]):
            res = c
print(res)  # 27987


# 31217 Резерв 22.06.26(Уровень: Базовый)
res = 0
for i in open('add/09/09_31217.txt'):
    d = [*map(int, i.split())]
    n1 = [i for i in d if d.count(i) == 1]
    n2 = [i for i in d if d.count(i) == 2]
    if len(n1) == 2 and len(n2) == 4:
        res += sum(n2) > sum(n1)
print(res)  # 6322


# 31355 Пересдача 08.07.26(Уровень: Базовый)
from math import prod
res = 0
for i in open('add/09/09_31355.txt'):
    d = [*map(int, i.split())]
    n1 = [i for i in d if d.count(i) == 1]
    n3 = [i for i in d if d.count(i) == 3]
    if len(n1) == len(n3) == 3:
        res += n3[0]**3 < prod(n1)
print(res)  # 179


# 31506 Демоверсия 2027(Уровень: Базовый)
c = 0
for i in open('add/09/09_31506.txt'):
    d = sorted(map(int, i.split()))
    if len(set(d)) == 5:
        c += 2 * (d[0] + d[-1]) > sum(d[1:-1])
print(c)  # 4874