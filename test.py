# from itertools import permutations
# print(*'123456')
# s = 'abcdeg'
# g = 'cd de eb bc db bg ga ab'.split()
# t = '24 146 45 12356 34 24'.split()
# for p in permutations(s):
#     if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
#         print(*''.join(p))

# from itertools import product, permutations
# def f(x,y,w,z):
#     return ((x <= y) == (z <= w)) or (x and w)
#
# for a1,a2,a3,a4,a5,a6 in product((0,1), repeat=6):
#     t = [(1,a1,a2,a3), (1,1,a4,a5), (1,1,1,a6)]
#     if len(set(t)) == 3:
#         for p in permutations('xywz'):
#             if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
#                 print(''.join(p))

# https://stepik.org/lesson/1229244/step/6?unit=1242785
# def f(st, en, cnt):
#     cnt += sum([st == 15, st == 21])
#     if st == en:
#         if cnt == 1:
#             return 1
#         return 0
#     if st > en or cnt > 1:
#         return 0
#     return f(st + 1, en, cnt) + f(st + 2, en, cnt) + f(st * 3, en, cnt)
#
# print(f(6, 25, 0))  # 2700

# """ 26.4 Закрепление (ч. 1) """
# # https://stepik.org/lesson/1229245/step/5?unit=1242786
# res = set()
# for n in range(10, 1001):
#     b = f'{n:b}'[1:]
#     if b.count('1'):
#         b = b[b.index('1'):]
#     else:
#         b = '0'
#     res.add(n - int(b, 2))
# print(len(res))  # 7


# from turtle import *
# tracer(0)
# lt(90)
# screensize(2500, 2500)
# k = 50
# for _ in range(4):
#     fd(8*k)
#     rt(90)
# for _ in range(3):
#     fd(12*k)
#     rt(120)
# pu()
# for x in range(-2, k):
#     for y in range(-2, k):
#         goto(x*k, y*k)
#         dot('red') if not x*y else dot()
# done()
"""
A - 30 sec
B = A * 2 / 1.5
"""
# print(30 * 2 / 1.5 / 4)  # 10
# from itertools import permutations
# cnt = 0
# for p in permutations('МАТВЕЙ'):
#     p = ''.join(p)
#     if p[0] != 'Й' and 'АЕ' not in p:
#         cnt += 1
# print(cnt)

# cnt = 0
# with open('test.txt') as fl:
#     d = list(map(float, fl.read().replace(',', '.').split()))
#     for i in range(1, len(d)):
#         cnt += d[i - 1] - d[i] >= 2
# print(cnt)  # 458
# from math import ceil, log2
# user = ceil((2 * ceil(log2(18)) + 8 * ceil(log2(10))) / 8)
# print(user * 25)

# s = '9' * 1000
# while '999' in s or '888' in s:
#     if '888' in s:
#         s = s.replace('888', '9', 1)
#     else:
#         s = s.replace('999', '8', 1)
# print(s)
""" 26.5 Закрепление (ч. 2) """
# Задачка для моего курса
# https://stepik.org/lesson/1229246/step/3?unit=1242787
# from ipaddress import *
# for n in range(32, 0, -1):
#     net1 = ip_network(f'140.37.235.224/{n}', 0)
#     net2 = ip_network(f'140.37.235.192/{n}', 0)
#     if net1 == net2:
#         if ip_address('140.37.235.224') in net1.hosts() \
#                 and ip_address('140.37.235.192') in net2.hosts():
#             print(net1.netmask)  # 255.255.255.128
#             # print(str(net1.netmask).split('.')[-1])  # 128
#             break

# n = 2**2020 + 2**2017 - 15
# print(f'{n:b}'.count('1'))
""" 
( not a  or x**2 <= 100) and (x**2 > 64  or a)
"""
# a = []
# for x in [i * 0.3 for i in range(100_000)]:
#     if not ((1 or x**2 <= 100) and (x**2 <= 64 or 0)):
#         a.append(x)
# print(a[0], a[-1])
""" 26.5 Закрепление (ч. 2) """
# Из интернета. НЕ ПОНЯЛ (((
# https://stepik.org/lesson/1229246/step/5?unit=1242787
# from math import ceil
# def f(x, a1, a2):
#     A = a1 <= x <= a2
#     # return (A <= (x**2 <= 100)) and ((x**2 <= 64) <= A)
#     return (not A or x**2 <= 100) and (x**2 > 64 or A)
#
# M = [i * 0.3 for i in range(-100, 100)]
# R = []
# for a1 in M:
#     for a2 in M:
#         if all(f(x, a1, a2) for x in M):
#             R.append((a2 - a1, (a1, a2)))
# print(max(R))  # (19.8, (-9.9, 9.9))
# print(ceil(max(R)[0]))  # 20

# def f(n):
#     if n == 1: return 1
#     return f(n-1) + n
# print(f(40))
""" 26.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1229246/step/7?unit=1242787
# from statistics import  mean
# cnt, mx = 0, 0
# with open('test.txt') as fl:
#     d = list(map(int, fl.readlines()))
#     even = mean([k for k in d if not k % 2])
#     for i in range(len(d) - 1):
#         a, b = d[i], d[i + 1]
#         if any([not a % 3, not b % 3]) and any([a < even, b < even]):
#             cnt += 1
#             mx = max(mx, a+b)
# print(cnt, mx)

# def f(a,b,mv):
#     if a+b >= 69:
#         return not mv % 2
#     if not mv:
#         return 0
#     g = [f(a+1,b,mv-1), f(a, b+1,mv-1), f(a*2,b,mv-1), f(a, b*3,mv-1)]
#     if not (mv - 1) % 2:
#         return any(g)
#     return all(g)
#     # return any(g)
#
# # print([s for s in range(1, 59) if f(10, s, 2)][0])  # 7  return any(g)
# print(*[s for s in range(1, 59) if f(10, s, 3)][:2])  # 16 19
# print([s for s in range(1, 59) if f(10, s, 4) and not f(10, s, 2)][0])  # 18

# def f(st, en):
#     if st > en: return 0
#     if st == en: return 1
#     return f(st + 1, en) + f(st + 2, en) + f(st * 2, en)
# print(f(3, 10) * f(10, 12))