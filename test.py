"""
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
#     d = [*map(int, s.split())]
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
# c = 0
# net = ip_network('172.16.168.0/255.255.248.0', 0)
# for i in net:
#     b = f'{i:b}'
#     c += b.count('1') % 5 != 0
# print(c)

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


# https://stepik.org/lesson/1135822/step/5?unit=1147455

# 21  🍒 отрезки
def f(x):
    b = 36 <= x <= 75
    c = 60 <= x <= 110
    a = a1 <= x <= a2
    return (not a) <= (b == c)






