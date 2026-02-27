# https://stepik.org/lesson/1400060/step/12?unit=1417013
# 21424 Досрочная волна 2025 (Уровень: Базовый)
# f = open('add/26/26_21424.txt').readlines()
# f = open('txt.txt').readlines()
# подготовка
# обработка

# from math import dist
# def centr(ls:list):
#     pass
# def get_clust(p, p):
#     pass
# f = open(f'add/27/20294_27_A.txt')
# https://stepik.org/lesson/1400061/step/5?unit=1417014

# 7718 (Уровень: Средний)

""""""
# https://stepik.org/lesson/1209382/step/5?unit=1222617  (11)
# https://stepik.org/lesson/1400061/step/10?unit=14170144  (27)
# https://kompege.ru/task

# def g_clust(p, k=5):
#     clust = [i for i in data if dist(p, i) < k]
#     [data.remove(i) for i in clust]
#     next_cl = [g_clust(i) for i in clust]
#     [clust.extend(i) for i in next_cl]
#     return clust
#
#
# for s in 'AB':
#     f = open(f'add/27/21911_27_{s}.txt')
#     data = [[*map(float, i.replace(',', '.').split())] for i in f]
#     print(len(data))
#     clust = []
#     while data:
#         p = data.pop()
#         clust.append(g_clust(p))
#         pass
#     [print(len(i)) for i in clust]
#     print(sum(len(i) for i in clust), '\n')

# def g_clust(p, k=1.9):
#     clust = [i for i in data if dist(p, i) < k]
#     [data.remove(i) for i in clust]
#     next_cl = [g_clust(i) for i in clust]
#     [clust.extend(i) for i in next_cl]
#     return clust



# https://stepik.org/lesson/1400061/step/12?unit=1417014
# 21425 Досрочная волна 2025 (Уровень: Базовый)

from itertools import *
from math  import ceil, log2
from ipaddress import *
from functools import lru_cache
from re import *
f = open('24var07.txt').readline()
n = r'(?:0|[1-9]\d*)'
reg = rf'{n}(?:[*-]{n})+'
res = findall(reg, f)
print(len(max(res, key=len)))  # 356

