"""
≥
≤
😉
🙂
🤔
😛
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

# Total Many 🍒🍒🍒
# print((545_000 - 288_670 - 110_000 - 43_000) + (18_000 - 85_640))  # 35_690  дебет на 31.05
# print((535_000 + 4_480 - 293_058 - 110_000 - 43_000) - 76_618)  # 16_804  дебет на 19.06
# print((565_000-60_000 + 795 - 291_045 - 110_000 - 43_000) - 76_618)  # -14_868  дебет на 30.06
# print((494_000 + 200 - 288_159 - 110_000 - 43_000) - 81_487)  # -28_446  дебет на 20.07
# print((513_000 + 330 - 297_070 - 110_000 - 43_000) - 81_487)  # -18_227  дебет на 31.07
# print((385_000+150_000 + 580 - 295_745 - 110_000 - 43_000) - 81_487)  # 5_348  дебет на 15.08


""""""
# ЕГЭ Информатика 2026 | Полный Курс
# https://stepik.org/course/233165
# variant
""" Варианты """
# variant  (high speed)
# variant  (slow speed)
# best variant
""""""

""""""
from functools import lru_cache
from itertools import *
from ipaddress import *
from math import ceil, log2
from math import dist

"""
🍒 отрезки
🍒 отрезки + делители
🍓 множества
⌛ конъюнкция
"""

from itertools import *
from turtle import *
from math import ceil, log2
from ipaddress import *
from functools import lru_cache
from fnmatch import *
from math import dist
from re import *




""" 01 """
# from itertools import *
# print(*'12345678')
# s = 'abcdefgh'
# g = 'af fh hc cb bd dg ga gf eb ed eh'.split()
# t = '234 157 147 138 268 58 23 456'.split()
# for p in permutations(s):
#     if all(str(p.index(a) + 1) in t[p.index(b)] for a, b in g):
#         print(*p)
"""

"""

""" 02 """
from itertools import *
# def f(x,y,w,z):
#     return not (((not x) or y) and (not w)) or (not (z and (not (y and w))))
#
# for m1,m2,m3,m4,m5,m6,m7 in product((0,1), repeat=7):
#     t = [(0,m1,m2,1), (m3,1,m4,m5), (1,0,m6,m7)]
#     if len(set(t)) == 3:
#         for p in permutations('xywz'):
#             if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
#                 print(''.join(p))

""" 05 """
# 9774 Основная волна 20.06.23 (Уровень: Средний)
# def f(n, b=9):
#     r = ''
#     while n:
#         r = str(n % b) + r
#         n //= b
#     return r

# def f(n, b=12):
#     alf = '0123456789ab'
#     r = ''
#     while n:
#         r = alf[n % b] + r
#         n //= b
#     return r

# res = 10**10
# for n in range(1, 1000):
#     b = f(n)
#     if n % 12:
#         b += f(n % 12 * 9)
#     else:
#         b += b[-2:]
#     r = int(b, 12)
#     if r > 300:
#         res = min(res, r)
# print(res)  # 309

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

""" 07 """
# from math import ceil, log2
# for add in range(10000):
#     if (ceil(9 * 4 / 8) + add) * 23 == 713:
#         print(add)
#         break

""" 08 """
# from itertools import permutations
# c = 0
# for p in permutations('0011111', 5):
#     c += p.count('0') <= 1
# print(c)  # 72

# for p in permutations(alf, 12):
#     if all(a>b for a, b in zip(p, p[1:])):
#         c += all(a%2 != b%2 for a, b in zip(p, p[1:]))
# print(c)  #



""" 09 """
#  9696 Danov2307 (Уровень: Средний)
# c = 0
# for s in open('6tU4Wdefq.txt'):
#     d = sorted(map(int, s.split()))
#     n2 = [i  for i in d if d.count(i) == 2]
#     if len(n2) == 2:
#         c += sum(d[2:]) > sum(d[:2]) * 2 and d[-1] % d[0] != 0
# print(c)  # 125


# https://stepik.org/lesson/564220/step/7?unit=558468 🌶️🌶️🌶️ НУЖНО РЕШИТЬ
# c = 0
# d = [[*map(int, i.split())] for i in open('9-228.txt')]
# d_col = [list(i) for i in zip(*d)]
# for row in d:
#     k = 0
#     n = [(0, i)[row.count(i) == 1] for i in row]    # хотя бы одно число в строке
#     for i in range(6):
#         if n[i] and d_col[i].count(n[i]) < 180:
#             k += 1
#     if k :
#         c += 1
# print(c)  # 1624 5089 9908 13854 15631

# https://stepik.org/lesson/564220/step/7?unit=558468 🌶️🌶️🌶️ НУЖНО РЕШИТЬ
# c = 0
# d = [[*map(int, i.split())] for i in open('9-228.txt')]
# d_col = [list(i) for i in zip(*d)]
# for row in d:
#     if len(set(row)) == 6:  # каждое число в строке
#         if all(d_col[i].count(row[i]) >= 180 for i in range(6)):
#             c += 1
# print(c)  # 312

""" 11 """
# from math import ceil, log2
# i = ceil(log2(10 + 26 + 450))
# for n in range(1, 1000):
#     if ceil(n * i / 8) * 708 > 213 * 2**10:
#         print(n)
#         break

# i = ceil(log2(10 + 52 + 458))
# for n in range(1, 1000):
#     if ceil(n * i / 8) * 862 > 276 * 2**10:
#         print(n - 1)
#         break

""" 12 """

""" 13 """

# from ipaddress import *
# net = ip_network(f'218.194.82.148/255.255.255.192', 0)
# print(net[-2])


# from ipaddress import *
# for x in range(256):
#     net = ip_network(f'192.214.{x}.184/255.255.255.224', 0)
#     if all(f'{i:b}'.count('1') > 15 for i in net) :
#         print(x)  # 127
#         break

# from ipaddress import *
# c = 0
# for m in range(1, 33):
#     net = ip_network(f'115.53.128.88/{m}', 0)
#     if net.network_address == ip_address('115.53.128.0'):
#         if net.num_addresses - 2 >= 1000:
#             c += 1
# print(c)

# from ipaddress import *
# for m in range(32, -1, -1):
#     net1 = ip_network(f'154.63.206.129/{m}', 0)
#     net2 = ip_network(f'154.63.100.75/{m}', 0)
#     if net1 == net2:
#         print(sum(not f'{i:b}'.count('1') % 2 for i in net1))
#         break



""" 14 """

# def cnv(n, b):
#     r = ''
#     while n:
#         r = str(n % b) + r
#         n //= b
#     return r

# def cnv(n, b):
#     r = 0
#     while n:
#         r += n % b == число
#         n //= b
#     return r

# def cnv(n, b):
#     r = ''
#     while n:
#         d = n % b
#         if d < 10:
#             r = str(d) + r  # 0 - 9
#         else:
#             r = '*' + r # 10 - и больше
#         n //= b
#     return r


# for x in range(40):
#     a = 8*40**6 + 7*40**5 + 1*40**4 + x*40**3 + 2*40**2 + 9*40**1 + 1*40**0
#     if not a % 39:
#         # print(x)  # 10
#         print(res // 13)  # 6461195610
#         break
#
# # variant
# def cnv(ls:list, b):
#     r = sum(int(n) * b**i for i, n in enumerate(ls[::-1]))
#     return r
#
# for x in range(40):
#     a = f'8 7 1 {x} 2 9 1'.split()
#     res = cnv(a, 40)
#     if not res % 39:
#         print(res // 13)  # 6461195610
#         break


# from string import printable as alf
# for x in alf[:24][::-1]:
#     n = int(f'4m{x}f', 24) + int(f'265afdn{x}', 24)
#     if not n % 23:
#         print(n // 23)
#         break

# from string import printable as alf
# [print(alf.index(i)) for i in 'xyz']   # 33 34 35
# res = []
# for a in range(55):
#     n1 = 35*55**3 + a*55**2 + 34*55**1 + 33*55**0
#     n2 = 2*55**3 + 33*55**2 + a*55**1 + 34*55**0
#     if not (n1 - n2) % 29:
#         res.append((a, n1 - n2))
# print(abs(max(res)[1] - min(res)[1]))



# def cnv(n, b=5):
#     r = ''
#     while n:
#         r = str(n % b) + r
#         n //= b
#     return r

# for x in range(100000):
#     n = 125**7 - 25**4 + x
#     s = cnv(n)
#     if s.count('4') == 15 and s.count('3') == 1 and s.count('1') == 2:
#         print(x)
#         break



""" 15 """
# https://stepik.org/lesson/564224/step/11?unit=558472






""" 16 """
# https://stepik.org/lesson/1576458/step/8?unit=1597732
# from functools import lru_caeve
# @lru_caeve()
# def f(n):
#     if n < 5:
#         return n
#     return 2*n * f(n-4)
#
# [f(i) for i in range(4, 13767)]
# print((f(13766) - 9 * f(13762)) / f(13758))

""" 17 """
# https://stepik.org/lesson/1576458/step/9?unit=1597732

# # 19249 ЕГКР 21.12.24 (Уровень: Базовый)
# d = [*map(int, open('17_19249.txt'))]
# cnt = 0
# M = 10**10
# mx = max(i for i in d if str(i)[-2:]=='43')
# for a,b,c in (zip(d, d[1:], d[2:])):
#     ls = [a,b,c]
#     if any(len(str(abs(i)))==5 and str(i)[-2:]=='43' for i in ls):
#         abc = a**2 + b**2 + c**2
#         if abc <= mx**2:
#             cnt += 1
#             M  = min(M, abc)
# print(cnt, M)  # 92 838850571

# d = open('17_17530.txt')
# d = [*map(int, d)]
# mn = min(d)
# M = 10**10
# cnt = 0
# for a, b in zip(d, d[1:]):
#     if any([a % 55 == mn, b % 55 == mn]):
#         cnt += 1
#         M = min(M, a + b)
# print(cnt, M)



# https://stepik.org/lesson/1576459/step/1?unit=1597733

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


# def f(a, b, m, w=0):
#     if a + b >= 65:
#         return not m % 2
#     if not m:
#         return 0
#     g = [f(a+1, b, m-1), f(a*3, b, m-1), f(a, b+1, m-1), f(a, b*3, m-1)]
#     if m % 2:
#         return any(g)
#     return any(g) if w else all(g)
#
# print([s for s in range(1, 59) if f(6, s, 2, 1)][0])
# print(*[s for s in range(1, 59) if f(6, s, 3) and not f(6, s, 1)][:2])
# print([s for s in range(1, 59) if f(6, s, 4) and not f(6, s, 2)][0])


# https://stepik.org/lesson/1368764/step/1?unit=1384857
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
# print(*[s for s in range(1, 39) if f(s, 3) and not f(s, 1)])
# print([s for s in range(1, 39) if f(s, 4) and not f(s, 2)][0])

""" 22 """

""" 23 """
# def f(a, b, c=0):
#     c += a == 8
#     if a < b:
#         return 0
#     if a == b and c:
#         return 1
#     return f(a-1, b, c) + f(a//2, b, c)
# print(f(30, 1))  # 115

# def f(a, b, c=0):
#     c += a==10
#     if a > b or a == 20:
#         return 0
#     if a == b and c:
#         return 1
#     return f(a+1, b, c) + f(a+2, b, c) + f(a*3, b, c)
# print(f(4, 22))  # 715


# 13099 (Уровень: Средний)
# def f(a, b, w=0):
#     if a == b:
#         return 1
#     if a > b+1:  #  b+1 >>  8 * 2 = 16 -> 16 - 1 = 15
#         return 0
#     return (f(a-1, b, 1) if not w else 0) + f(a*2, b, 0) + f(a*3, b, 0)
# print(f(3, 15))  # 6
#
# def f(a, b, w=''):
#     if a == b:
#         return 1
#     if a > b+1 or '--' in w:  #  b+1 >>  8 * 2 = 16 -> 16 - 1 = 15
#         return 0
#     return f(a-1, b, w+'-') + f(a*2, b, w+'*') + f(a*3, b, w+'*')
# print(f(3, 15))  # 6



# https://stepik.org/lesson/1228672/step/6?unit=1242205

# def f(a, b):
#     if a >= b:
#         return a == b
#     return f(a+1, b) + f((a+10, a)[a//10==9], b)
# print(f(15, 37))  # 20



""" 24 """
# s = open('24.txt').read().strip()



# from re import *
# s = open('24_1.txt').read().strip()
# n = r'(?:0|[1-9]\d*)'
# reg = rf'{n}(?:[*-]{n})+'
# res = findall(reg, s)
# print(len(max(res, key=len)))  # 128


# s = open('24.txt').read().strip()
# l = c = res = 0
# for r in range(3, len(s)):
#     c += s[r-3:r+1] == 'FSRQ'
#     while c > 80:
#         c -= s[l:l+4] == 'FSRQ'
#         l += 1
#     if c == 80:
#         res = max(res, r-l+1)
# print(res)  # 2379

# Через split()
# s = open('24.txt').read().strip()
# # print(s[:4], s[-4:]) # проверка концов: должны отличаться от 'FSRQ'
# res = 0
# s = s.split('FSRQ')
# n = 80
# for i in range(len(s) - n):
#     # 'k' это прибавка еще от двух 'FSRQ'  >>  'SRQ' + ... + 'FSR'
#     k = 6 if 0 < i < len(s) - n-1 else 3  # учет изменения прибавки для первой и последней выборки
#     r = sum(map(len, s[i:i + n+1])) + 4 * n + k
#     res = max(res, r)
# print(res)  # 2379


""" 25 """
# 23763 Демоверсия 2026 (Уровень: Базовый)
# def dv(n):
#     for i in range(2, int(n**0.5 + 1)):
#         if not n % i:
#             return i + n // i
# c = 5
# for n in range(800_001, 10**10):
#     m = dv(n)
#     if m and m % 10 == 4:
#         print(n, m)
#         c -= 1
#     if not c:
#         break


# def dv(n):
#     r = set()
#     for i in range(2, int(n**0.5 + 1)):
#         if not n % i:
#             r |= {i, n // i}
#     return r

# def spl(n):
#     return all(n % i for i in range(2, int(n**0.5 + 1)))

""" 26 """
from statistics import mean

# # 19256 ЕГКР 21.12.24 (Уровень: Базовый)
# f = open('26_19256.txt').readlines()
# data = [[*map(int, i.split())] for i in f[1:]]  # идентификатор студента / номер правильно решённой задачи
# dt = dict()
# for i in data:
#     dt.setdefault(i[0], set())
#     dt[i[0]] |= {i[1]}
# res = []
# for k, v in dt.items():
#     v = sorted(v)
#     c = cnt = 1
#     for i in range(1, len(v)):
#         if v[i] - v[i-1] == 1:
#             c += 1
#             cnt = max(cnt, c)
#         else:
#             c = 1
#         res += [(k, cnt)]
# res.sort(key=lambda x: (-x[1], x[0]))
# print(*res[0])  # 40031 148





# d = [(k, sorted(v)) for k, v in dt.items()]

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


# from math import dist
# def get_clust(p):
#     clust = [i for i in data if dist(p, i) <= 1]
#     [data.remove(i) for i in clust]
#     next_clust = [get_clust(i) for i in clust]
#     [clust.extend(i) for i in next_clust]
#     return clust
#
# def get_center(ls):
#     r = []
#     for p in ls:
#         sm = sum(dist(p, i) for i in ls)
#         r += [(sm, p)]
#     return min(r)[1]
#
# for w in 'AB':
#     data = [[*map(float, i.replace(',', '.').split())] for i in open(f'27{w}.txt').readlines()]
#     clusters = []
#     while data:
#         p = data.pop()
#         clust = get_clust(p) + [p]
#         clusters.append(clust)
#     center = [get_center(i) for i in clusters]
#     px = int((sum(i[0] for i in center) / len(center)) * 10_000)
#     py = int((sum(i[1] for i in center) / len(center)) * 10_000)
#     print(px, py)
"""

"""

# https://stepik.org/lesson/1576460/step/4?unit=1597734
# from math import dist
# def get_clust(p, k):
#     clust = [i for i in data if dist(i, p) < k]
#     [data.remove(i) for i in clust]
#     next_clust = [get_clust(i, k) for i in clust]
#     [clust.extend(i) for i in next_clust]
#     return clust
#
# def get_center(ls):
#     r = []
#     for p in ls:
#         sm = sum(dist(p,k) for k in ls)
#         r += [(sm, p)]
#     return min(r)[1]
#
# for w, k in zip('AB', (3, 1)):
#     data = [[*map(float, i.replace(',', '.').split())] for i in open(f'27_{w}.txt').readlines()]
#     # print(len(data))
#     clusters = []
#     while data:
#         p = data.pop()
#         clust = get_clust(p, k) + [p]
#         clusters.append(clust)
#     # [print(len(i)) for i in clusters]
#     # print(sum(len(i) for i in clusters), '\n')
#     center = [get_center(i) for i in clusters]
#     px = int(abs((sum(i[0] for i in center) / len(center)) * 10_000))
#     py = int(abs((sum(i[1] for i in center) / len(center)) * 10_000))
#     print(px, py)


# https://stepik.org/lesson/1201175/step/1?unit=1214384
# from turtle import *
# tracer(0)
# lt(90)
# screensize(2000, 2000)
# k = 50
# for _ in range(4):  # оси
#     fd(50*k)
#     bk(50*k)
#     rt(90)
#
#
# for _ in range(11):
#     fd(4*k)
#     rt(60)
#
#
# pu()
# for x in range(-10, 30):
#     for y in range(-10, 30):
#         goto(x*k, y*k)
#         dot()
# done()

# 19-21
# https://stepik.org/lesson/1221217/step/2?unit=1234627

# 22
# https://stepik.org/lesson/1038797/step/8?unit=1062790




# https://stepik.org/lesson/413775/step/2?unit=584888


# https://stepik.org/lesson/661483/step/13?unit=659105


# s = open('24.txt').read()
# s = input()
# # s = 'CCCBBABAABCC'
# from string import ascii_uppercase as alf
#
# d = {i: 0 for i in alf}
# for a,b,c in zip(s, s[1:], s[2:]):
#     if a == b:
#         d[c] += 1
# d = sorted([(a, b) for a, b in d.items()], key=lambda x: (-x[1], x[0]))
# print(*d[0], sep='') #

# variant
# from re import *

# https://stepik.org/lesson/1254257/step/13?unit=1268462

# s = open('24.txt').read()
# # s = '0.11.2.3.444.5..6666666666'
# A = 2
# res = 0
# s = s.split('.')
# for i in range(len(s) - A):
#     w = '.'.join(s[i:i + A + 1])
#     res = max(res, len(w))
# print(res)  # 403

# s = open('24.txt').read()
# # s = '1.11.11.2222'
# l = c = res = 0
# for r in range(len(s)):
#     c += s[r] == '.'
#     while c > 2:
#         c -= s[l] == '.'
#         l += 1
#     res = max(res, r - l + 1)
# print(res)


# res = 10**10
# l = c = 0
# s = open('24.txt').read().strip()[1:-1]
# for r in range(len(s)):
#     if s[r] == 'Z':
#         c += 1
#     while c >= 270:
#         if s[l] == 'Z':  # в начале и конце строки стоит 'Z' и их ровно 270
#             res = min(res, r - l + 1)
#             c -= 1
#         l += 1
# print(res)  # 1058

# s = open('24.txt').read()
# l = c = 0
# res = 10**6
# for r in range(len(s)):
#     if s[r] == 'A':
#         c += 1
#     while c >= 35:
#         if s[l] == 'A':
#             res = min(res, r - l + 1)
#             c -= 1
#         l += 1
# print(res)  # 40


# s = open('24.txt').read()
# c = l = res = 0
# for r in range(len(s)):
#     c += s[r]=='.'
#     while c > 4:
#         c -= s[l] == '.'
#         l += 1
#     if c <= 4:
#         res = max(res, r-l+1)
# print(res)


# Минимальная длина
# минимальное количество идущих подряд символов, среди которых символ А встречается не менее 500 раз
# s = open('24.txt').read().split('A')[1:-1]
# A = 500
# Min = 10**6
# for i in range(len(s) - (A-2)):
#     w = ''.join(s[i:i + (A-2) + 1])
#     Min = min(Min, len(w) + A)
# print(Min)

# Максимальная длина
# максимальное количество идущих подряд символов, среди которых символ А встречается не более 350 раз.
# s = open('24.txt').read().split('A')
# A = 350
# MX = 0
# for i in range(len(s) - A):
#     w = ''.join(s[i:i + A + 1])
#     MX = max(MX, len(w) + A)
# print(MX)


# variant
# https://stepik.org/lesson/1323132/step/5?unit=1340050

# c = 0
# for n in range(1, 1000):
#     b = f'{n:b}'
#     b += ('00', '10')[n % 2]
#     b += ('0', '1')[b.count('1') % 2]
#     c += 130 <= int(b, 2) <= 350
# print(c)

# res = 0
# for n in range(1, 10000):
#     b = f'{n:b}'
#     for _ in range(2):
#         b += str(b.count('1') % 2)
#     r = int(b, 2)
#     if r <= 71:
#         res = max(res, r)
# print(res)


""""""
"""
course_72713
task_**_72713
task **
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""




# https://stepik.org/lesson/2226020/step/7?unit=2259762

# 5494 (Уровень: Средний) 🌶️🌶️
def f(st, en, w='--'):
    if st > en:
        return 0
    if st == en:
        return 1
    return ((f(st+1, en, w+'+') if w[-2:] != '++' else 0) + 
            (f(st*2, en, w+'*') if w[-2:] != '**' else 0))
print(f(1, 16))  # 101

# variant
def f(st, en, prev='', c=0):
    if st > en: 
        return 0
    if st == en: 
        return 1
    res = 0  # ✅ переменная для хранения количества путей
    if prev != '1' or c < 2:  # если предыдущая команда не 1, или 1 не было уже дважды подряд
        res += f(st+1, en, '1', c+1 if prev=='1' else 1)  # выполняем команду 1
    if prev != '2' or c < 2:  # если предыдущая команда не 2, или 2 не было уже дважды подряд
        res += f(st*2, en, '2', c+1 if prev=='2' else 1)  # выполняем команду 2
    return res  # ✅ возвращаем общее количество путей
print(f(1, 16))  # 101