"""
≥
≤
😉
🙂
🤔
👍
✅
✔️
👎
⛔
❌
❓
❗
🆗
✔
⚡
🌶️
🍓
🍒
⌛
√
"""
""""""
# ЕГЭ Информатика 2026 | Полный Курс
# https://stepik.org/course/233165
# variant
""" Варианты """
# variant  (high speed)
# variant  (slow speed)
# best variant
""""""

# https://stepik.org/lesson/1038609/step/4?unit=1062783
# https://kompege.ru/task  № 1551
""""""
from functools import lru_cache
from itertools import *
from ipaddress import *
from math import ceil, log2
from math import dist

# https://stepik.org/lesson/1368763/step/6?unit=1384856

# 07
# from math import ceil, log2
# for i in range(1, 100):
#     if ceil(640*480 * (i+6) / 8) > 600 * 2**10:
#         print(2**(i-1))
#         break

# 09
# c = 0
# for s in open('09.txt'):
#     d = [*map(int, s.smplit())]
#     n1 = [i for i in d if d.count(i) == 1]
#     n3 = [i for i in d if d.count(i) == 3]
#     if len(n1) == len(n3) == 3:
#         c += sum(n3)**2 > sum(n1)**2
# print(c)

# 11
# i = ceil(log2(10 + 52 + 963))
# for n in range(1, 1000):
#     if ceil(n * i / 8) * 2000 > 693 * 1024:
#         print(n-1)
#         break

# 12
# s = '1' * 81
# while '11111' in s or '888' in s:
#     if '11111' in s:
#         s = s.replace('11111', '88', 1)
#     else:
#         s = s.replace('888', '8', 1)
# print(s)


# 13

# 12947 (Уровень: Базовый)
# from ipaddress import *
# c = 0
# net = ip_network('203.111.195.0/255.255.240.0', 0)
# for i in net:
#     b = f'{i:b}'
#     c += not b.count('0') % 3 and '111' in b and '000' in b
# print(c)  # 1043

# c = 0
# for m in range(1, 33):
#     net = ip_network(f'251.211.38.240/{m}', 0)
#     if str(net.network_address) == '251.211.38.0':
#         c += 1
# print(c)

# from ipaddress import *
# c = 0
# for m in range(1, 33):
#     net1 = ip_network(f'201.44.240.33/{m}', 0)
#     net2 = ip_network(f'201.44.240.107/{m}', 0)
#     if net1 == net2:
#         c += f'{net1.network_address:b}'.count('1') >= 5
# print(c)  # 15




# 14
# n = 7**170 + 7**100
# for x in range(2030, 0, -1):
#     c = 0
#     r = n - x
#     while r:
#         c += not r % 7
#         r //= 7
#     if c == 71:
#         print(x)
#         break


# 15.1
# def f(x, y):
#     return x + y <= 30 or y <= x + 2 or y >= a
# for a in range(1000, -1, -1):
#     if all(f(x, y) for x in range(1000) for y in range(1000)):
#         print(a)
#         break

# 15.2
# 17528 Основная волна 07.06.24 (Уровень: Базовый)
# def f(x):
#     p = 15 <= x <= 40
#     q = 21 <= x <= 63
#     a = a1 <= x <= a2
#     return not p or not q or a
#
# res = 1000
# n = [y for x in (15, 21, 40, 63) for y in (x-0.1, x, x+0.1)] # критические точки: концы P,Q и сдвиги
# for a1 in n:
#     for a2 in n:
#         if a1 < a2 and all(f(x) for x in n):
#             res = min(res, a2-a1)
# print(res)

# 16
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return (n-1) * f(n-1)
# [f(n) for n in range(2025)]
# print((f(2024) + 2*f(2023)) / f(2022))


# 17
# res = sm = 0
# d = [*map(int, open('17.txt'))]
# MX = min(d)
# for i in range(len(d) - 1):
#     if any(i % 16 == MX for i in d[i:i+2]):
#         res += 1
#         sm = max(sm, sum(d[i:i+2]))
# print(res, sm)  # 1214 176024

"""
🍒 отрезки
🍒 отрезки + делители
🍓 множества
⌛ конъюнкция
"""

"""❌ Не решено ❌"""

""" 06 """
# from turtle import *
# lt(90)
# screensize(2000, 2000)
# tracer(0)
# k = 20
# for _ in range(9):
#     fd(22 * k)
#     rt(90)
#     fd(6 * k)
#     rt(90)
# pu()
# fd(1 * k)
# rt(90)
# fd(5 * k)
# lt(90)
# pd()
# for _ in range(9):
#     fd(53 * k)
#     rt(90)
#     fd(75 * k)
#     rt(90)
# pu()
# for x in range(-70, 10):
#     for y in range(-40, 30):
#         goto(x*k, y*k)
#         dot()
# done()


from itertools import *
from turtle import *
from math import ceil, log2
from ipaddress import *
from functools import lru_cache
from fnmatch import *
from math import dist

# 🍒 отрезки
# 🍓 множества
# ⌛ конъюнкция
# 🆗 x и y



# def dv(n):
#     r = set()
#     for i in range(2, int(n**0.5 + 1)):
#         if not n % i:
#             r |= {i, n // i}
#     return r

""" 19-21 """
# 17638 Основная волна 19.06.24 (Уровень: Базовый)
# def f(a, m, w=0):
# def f(a, m):
#     if a >= 39:
#         return not m % 2
#     if not m:
#         return 0
#     g = [f(a+1, m-1), f(a+3, m-1), f(a*2, m-1),]
#     # if m % 2:
#     #     return any(g)
#     # return any(g) if w else all(g)
#     return any(g) if m % 2 else all(g)
#
# print([s for s in range(1, 39) if f(s, 2)][0])
# print(*[s for s in range(1, 39) if f(s, 3) and not f(s, 1)][:2])
# print([s for s in range(1, 39) if f(s, 4) and not f(s, 2)][0])



# 175
# def f(a, b, m, w=0):
#     if a + b >= 375:
#         return not m % 2
#     if not m:
#         return 0
#     g = [f(a+3, b, m-1), f(a*2, b, m-1), f(a, b+3, m-1), f(a, b*2, m-1)]
#     if m % 2:
#         return any(g)
#     return any(g) if w else all(g)
#
# print([s for s in range(1, 348) if f(27, s, 2, 1)][0])
# s20 = [s for s in range(1, 348) if f(27, s, 3) and not f(27, s, 1)]
# print(s20[0], s20[-1])
# print([s for s in range(1, 348) if f(27, s, 4) and not f(27, s, 2)][0])


""" 27 """

# from math import dist
# def get_cluster(p):
#     clust = [i for i in data_in if dist(p, i) < 2]
#     [data_in.remove(i) for i in clust]
#     next_clust = [get_cluster(i) for i in clust]
#     [clust.extend(i) for i in next_clust]
#     return clust
#
# def get_center(a: list):
#     res = []
#     for i in a:
#         sm = sum(dist(i, k) for k in a)
#         res.append([sm, i])
#     return min(res)[1]
#
#
# for w in 'AB':
#     f = open(f'27{w}.txt')
#     data_in = [[*map(float, i.replace(',', '.').split())] for i in f]
#     # print(len(data_in))
#     clusters = []
#     while data_in:
#         p = data_in.pop()
#         clusters.append(get_cluster(p) + [p])
#     # [print(len(i)) for i in clusters]
#     # print(sum(len(i) for i in clusters), '\n')
#     center = [get_center(i) for i in clusters]
#     px = int(abs(sum(i[0] for i in center) / len(center)) * 10_000)
#     py = int(abs(sum(i[1] for i in center) / len(center)) * 10_000)
#     print(px, py)


















