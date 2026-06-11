""" https://kompege.ru/task """
"""
5627 6262 8467 8475 9696
11946 12795 16375 17550
23747
"""


# 5627 (Уровень: Средний)
f = open('add/09/09_5627.txt')
cnt = 0
data = [sorted(map(int, i.split())) for i in f]
for d in data:
    a = [i for i in d if d.count(i) > 1]
    r = d[1] - d[0]
    b = all(b - a == r for b, a in zip(d[1:], d))
    if a or b:
        cnt += 1
print(cnt)  # 525


# 6262 Danov2302 (Уровень: Средний)
f = open('add/09/09_6262.txt')
cnt = 0
data = [list(map(int, i.split())) for i in f]
for d in data:
    a = [i for i in d if d.count(i) > 1]
    b = len([i for i in d if i % 2]) == 3
    if a and not b or b and not a:
        cnt += 1
print(cnt)  # 1852


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


#  9696 Danov2307 (Уровень: Средний)
c = 0
for s in open('9_9696.txt'):
    d = sorted(map(int, s.split()))
    n2 = [i  for i in d if d.count(i) == 2]
    if len(n2) == 2:
        c += sum(d[2:]) > sum(d[:2]) * 2 and d[-1] % d[0] != 0
print(c)  # 125




# 11946 (Уровень: Средний)
c = 0
for n in open('09.txt'):
    d = [*map(int, n.split())]
    n3 = [i for i in d if d.count(i)==3]
    n1 = [i for i in d if d.count(i)==1]
    a = len(n3)==3 and len(n1)==4
    # b = all(a <= b for a,b,in zip(d, d[1:]))
    b = d == sorted(d)
    c += a + b <= 1
print(c)


# 12795 Открытый курс "Слово пацана" (Уровень: Средний)
f = open('add/09/09_12795.txt')
cnt = 0
data = [list(map(int, i.split())) for i in f]
for d in data:
    a = sum(d) // 7
    cnt += a in d
print(cnt)  # 35


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