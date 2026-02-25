""" https://kompege.ru/task """
"""
5627 6262 8475
12795
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


# 8475 (Уровень: Средний)
from math import prod
f = open('add/09/09_8946.txt')
cnt = 0
data = [sorted(map(int, i.split())) for i in f]
for d in data:
    if d[-1]**2 > prod(d[:-1]):
        cnt += sum(d[-2:]) / sum(d[:-2]) >= 2
print(cnt)  # 10




# 12795 Открытый курс "Слово пацана" (Уровень: Средний)
f = open('add/09/09_12795.txt')
cnt = 0
data = [list(map(int, i.split())) for i in f]
for d in data:
    a = sum(d) // 7
    cnt += a in d
print(cnt)  # 35





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