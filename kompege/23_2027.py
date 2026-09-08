""" https://kompege.ru/task """
"""
31518 31523
"""


# 31518 Демоверсия 2027(Уровень: Базовый)
data = []
for i in open('add/23_2027/23_31518.txt'):
    a, b, w = i.split()
    data.append((int(a), int(b), float(w)))

res = [10**10] * 10_001  # кол-во вершин (по заданию) + 1 (страховка)
res[1] = 0  # 1 это откуда идти (по заданию), путь (вес) из 1 в 1 равен 0
for _ in range(201):  # Кол-во строк(ребер) в файле + 1
    for a, b, w in data:
        res[b] = min(res[b], res[a] + w)
print(int(res[100]))  # 10971


# 31523 (Уровень: Базовый)
data = []
for i in open('add/23_2027/23_31523.txt'):
    a, b, w = i.split()
    data.append((int(a), int(b), float(w)))

res = [10**10] * 10_001  # кол-во вершин (по заданию) + 1 (страховка)
res[3] = 0  # 3 это откуда идти (по заданию), путь (вес) из 3 в 3 равен 0
for _ in range(201):  # Кол-во строк(ребер) в файле + 1
    for a, b, w in data:
        res[b] = min(res[b], res[a] + w)
print(int(res[97]))  # 315