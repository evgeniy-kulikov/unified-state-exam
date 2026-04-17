# https://stepik.org/lesson/703202/step/1?unit=703535
from itertools import *
print(*'1234567')
g = 'аб бд дж же ев ва га ге гж'.split()
t = '246 136 25 157 34 127 46'.split()
for p in permutations('абвгдеж'):
    if all(str(p.index(a) + 1) in t[p.index(b)]  for a, b in g):
        print(*p)
"""
1 2 3 4 5 6 7
г ж д а б е в
22 + 17 = 39
"""


# https://stepik.org/lesson/703202/step/2?unit=703535
from itertools import *
def f(x,y,w,z):
    return (x and not y) or (y == z) or w

for m1,m2,m3,m4 in product((0,1), repeat=4):
    t = [(m1,m2,1, m3), (0,0,0,1), (1,0,m4,1)]
    if len(set(t)) == 3:
        for p in permutations('xywz'):
            if [f(**dict(zip(p, d))) for d in t] == [0,0,0]:
                print(''.join(p))  # xwzy


# https://stepik.org/lesson/703202/step/5?unit=703535
res = []
for n in range(2, 1000):
    b = f'{n:b}'
    if n % 3:
        b += f'{n%3:b}'
    else:
        b += b[:2]
    r = int(b, 2)
    if r < 105:
        res.append((r, n))
res.sort(key=lambda x: (-x[0], x[1]))
print(res[0][1])


# https://stepik.org/lesson/703202/step/6?unit=703535
print(21*13 + 14*7 - 6*12)  # 299


# https://stepik.org/lesson/703202/step/7?unit=703535
for i in range(1, 100):
    if 800*630 * i * 0.65 > 270 * 2**13:
        print(2**(i-1))  # 64
        break


# https://stepik.org/lesson/703202/step/8?unit=703535
from itertools import *
c = 0
for p in set(permutations('АББАТИСА')):
    s = ''.join(p)
    s = s.replace('И', 'А')
    s = s.replace('Т', 'Б').replace('С', 'Б')
    c += all(not i in s for i in ('АА', 'ББ'))
print(c)  # 96



# https://stepik.org/lesson/703202/step/9?unit=703535
c = 0
for n in open('09.txt'):
    d = [*map(int, n.split())]
    n1 = [i for i in d if d.count(i) == 1 and i % 2]
    n2 = [i for i in d if d.count(i) == 2 and not i % 2]
    if len(n1) == 2 and len(n2) == 2:
        c += 1
print(c)  # 53


# https://stepik.org/lesson/703202/step/11?unit=703535
from math import ceil, log2
i = ceil(log2(10 + 1350))
I = ceil(243 * i / 8)
print(I * 65_536 // 1024)  # 21440

"""
1-11  01:10:00
"""


# https://stepik.org/lesson/703202/step/12?unit=703535
s_in = '01' * 144 + '2' * 712  # 712 = (1000 - 144 * 2)
s_out = '12' * 144 + '0' * (1000-144*2)  # 3 * 144 = 432
# 144


# https://stepik.org/lesson/703202/step/13?unit=703535
from ipaddress import *
for m in range(32, 1, -1):
    net1 = ip_network(f'176.213.225.119/{m}', 0)
    net2 = ip_network(f'176.213.195.58/{m}', 0)
    if net1 == net2:
        c = sum(not f'{i:b}'.count('1') % 2 for i in net1)
        print(c)  # 8192
        break



# https://stepik.org/lesson/703202/step/14?unit=703535
for x in '0123456789abcdef':
    n = int(f'2{x}bad', 16) + int(f'3c{x}fe', 16)
    if not n % 15:
        print(n // 15)  # 26789
        break


# https://stepik.org/lesson/703202/step/15?unit=703535
def f(x):
    b = 40 <= x <= 60
    return x % 13 or not b or (a < x+20)

for a in range(1000, 0, -1):
    if all(f(x) for x in range(10000)):
        print(a)  # 71
        break

"""
1-15  01:37:00
"""


# https://stepik.org/lesson/703201/step/1?unit=703534
from functools import lru_cache
@ lru_cache
def f(n):
    if n == 1:
        return 3
    if n % 2:
        return f(n-1) + 7
    return f(n-1) + 5 * (n-1)

[f(n) for n in range(1, 8766)]
print(f(8765))  # 96040297


# https://stepik.org/lesson/703201/step/2?unit=703534
data = [*map(int, open('17.txt'))]
avr = [i for i in data if i % 2]
avr = sum(avr) / len(avr)
res = mx = 0
for i in range(len(data) - 2):
    a, b, c = data[i:i+3]
    if all([not f'{a+b:o}'.count('7'), not f'{c+b:o}'.count('7'), not f'{a+c:o}'.count('7')]):
        if a+b+c < avr:
            res += 1
            mx = max(mx, a+b+c)
print(res, mx)  # 25 5750


# https://stepik.org/lesson/703201/step/3?unit=703534
def f(a, m):
    if a >= 55:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, m-1), f(a+4, m-1), f(a*3, m-1)]
    if m % 2:
        return any(g)
    return all(g)

print([s for s in range(1, 55) if f(s, 2)][0])  # 18
print(*[s for s in range(1, 55) if f(s, 3) and not f(s, 1)][:2])  # 6 14
print([s for s in range(1, 55) if f(s, 4) and not f(s, 2)][0])  # 13
"""
1-21  02:04:00
"""

# https://stepik.org/lesson/703201/step/5?unit=703534
def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    # return f(a+1, b) + f(int(str(a) + '1', 10), b)
    return f(a+1, b) + f(a*10 + 1, b)

print(f(1, 344))  # 77

"""
1-23  02:33:00
"""


# https://stepik.org/lesson/703201/step/6?unit=703534
from re import *
s = open('24.txt').readline().strip()
reg1 = r'(?:BA)+'
reg2 = r'(?:DA)+'
reg3 = r'(?:BA|DA)+'
res1 = max(len(i) for i in findall(reg1, s))
res2 = max(len(i) for i in findall(reg2, s))
res3 = max(len(i) for i in findall(reg3, s))
print(max([res1, res2, res3])//2)  # 151


# https://stepik.org/lesson/703201/step/8?unit=703534
from fnmatch import *
# for n in range(0, 10**9, 23):  # долго
# for n in range(0, 123459798, 23):
for n in range(12345078 // 23 * 23, 123459798, 23):
    if fnmatch(str(n), '12345?7*8'):
        print(n, n // 23)

for a in '0123456789':
    for b in [''] + [*'0123456789']:
        n = int(f'12345{a}7{b}8')
        if not n % 23:
            print(n, n//23)
"""
123450798 5367426
123451718 5367466
123453788 5367556
123454708 5367596
123456778 5367686
123459768 5367816
"""
"""
1-25  02:45:00
"""