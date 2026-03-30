# https://stepik.org/lesson/1400060/step/12?unit=1417013
# https://kompege.ru/task
# 21424 Досрочная волна 2025 (Уровень: Базовый)
# f = open('add/26/26_21424.txt').readlines()
# f = open('txt.txt').readlines()
# подготовка
# обработка
""""""
# https://stepik.org/lesson/1209382/step/5?unit=1222617  (11)
# https://stepik.org/lesson/1400061/step/10?unit=14170144  (27)
# https://kompege.ru/task

# from math import dist
# def centr(ls:list):
#     pass
# def get_clust(p, p):
#     pass
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
# from string import ascii_lowercase as w
# from itertools import *
# from math  import ceil, log2
# from ipaddress import *
# from functools import lru_cache
# from re import *
# f = open('24var07.txt').readline()
# f = open('txt.txt').readlines()


# https://stepik.org/lesson/1362233/step/3?unit=1378103
# 17537


# f = open('add/26/_1111.txt').readlines()
# c = 0
# for i in f:
#     n = [*map(int, i.split())]
#     n1 = [i for i in n if n.count(i)==1]
#     n2 = [i for i in n if n.count(i)==2]
#     if len(n1)==3 and len(n2)==4:
#         c += sum(n2) / 4 < sum(n) / 7
# print(c)

# i = ceil(log2(10 + 250))
# I = ceil(60 * i / 8) * 65_536 / 1024
# print(int(I))

# for i in range(10_000 - 1, 3, -1):
#     s = '5' + '2' * i
#     while '52' in s or '2222' in s or '1122' in s:
#         s = s.replace('52', '11', 1)
#         s = s.replace('2222', '5', 1)
#         s = s.replace('1122', '25', 1)
#     if sum(map(int, s)) == 64:
#         print(i)
#         break


# net = ip_network('192.168.32.160/255.255.255.240', 0)
# c = 0
# for i in net:
#     c += not f'{i:b}'.count('1') % 2
# print(c)

# alf = '0123456789' + w[:9]
# for i in alf[::-1]:
#     n = int(f'98897{i}21', 19) + int(f'2{i}923', 19)
#     if not n % 18:
#         print(n // 18)
#         break

# def f(x, y, a):
#     return (x + 2*y < a) or (y>x) or (x>60)
#
# for a in range(1000):
#     if all(f(x, y, a) for x in range(1000) for y in range(1000)):
#         print(a)
#         break

# @lru_cache()
# def f(n):
#     if n > 2024:
#         return n
#     return n * f(n+1)
#
# [f(i) for i in range(2025, 0, -1)]
# print(f(2022) / f(2024))

# c = 0
# sm = 0
# d = [*map(int, open('add/26/_1111.txt'))]
# mx = max([i for i in d if str(i)[-2:] == '13'])
# for i in range(len(d) - 2):
#     n =  d[i:i+3]
#     n3 = [i for i in n if 100 <= abs(i) < 1000]
#     if len(n3) == 2 and sum(n) <= mx:
#         c += 1
#         sm = max(sm, sum(n))
# print(c, sm)

# # 26551 (Уровень: Базовый)
# from re import *
# s = open('add/24/24_26551.txt').read()
# reg = r'[1-9A-D][0-9A-D]*[0248AC]'  # четное
# res = findall(reg, s)
# print(len(max(res, key=len)))  # 2598

# f = open('add/KIM_25163454/9_27621.txt').readlines()
# https://kompege.ru/task
# ✅️Better
""""""
# 26078 (Уровень: Базовый) ⛔ ❓  # суперсложная задача
# d = st = open('add/26/24_26078.txt').read()
# st = open('add/26/24_26078.txt').read().replace('W', 'W W').split()
# res = []
# n = 90
# for i in range(len(st) - n):
#     s = st[i:i + n + 1]
#     if ''.join(s).count('2025') >= 110:
#         res.append(s)
#
# https://kompege.ru/task
""""""

# 8510 Апробация 17.05 (Уровень: Средний)
# s = open('add/24/24_8510.txt').read()


# def b5(n):
#     r = ''
#     while n:
#         r = str(n % 5) + r
#         n //= 5
#     return r

# from math import ceil, log2
# for i in range(1, 100):
#     if (ceil(1600 * 1200 * i / 8) / 5 + 100*1024) * 32 > 10 * 2**20:
#         print(2**(i-1))
#         break
# 👍 сложная задача

# https://stepik.org/lesson/1071633/step/6?unit=1081443
# from ipaddress import *
# for n in range(1, 33):
#     net = ip_network(f'115.12.69.38/{n}', 0)
#     if str(net.network_address) == '115.12.64.0':
#         print(n)
#         break

def b7(n):
    r = ''
    while n:
        r = str(n%7) + r
        n //= 7
    return r

# res = 0
# n = 7**500 + 7**200 - 7**50
# for x in range(n, 0, -1):
#     res = max(res, sum(map(int, b7(x))))
#     if res > 1200:
#         print(res)
# print(res)


# 111 (Уровень: Сложный) 🌶️
# from functools import *
# @lru_cache(None)



# https://stepik.org/lesson/564227/step/15?unit=558475
















