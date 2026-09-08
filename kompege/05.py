""" https://kompege.ru/task """

"""
352
1114 1332 1519 2461 3754 
9360 9736 9774 9777 9831 10087 12459 12914
"""



# 352 (Уровень: Базовый)
for n in range(1, 1000):
    b = f'{n:b}'
    if n % 2:
        b += '0'
    else:
        b = '1' + b
    b += '10'[b.count('1') % 2]
    if int(b, 2) > 228:
        print(n)
        break


# 1114 (Уровень: Базовый)
for n in range(96, 1000):
    b = f'{n:b}'
    for _ in range(3):
        one = b.count('1')
        zero = b.count('0')
        if one == zero:
            b += b[-1]
        else:
            b += ('0', '1')[one < zero]
    # В двоичной системе, чтобы число делилось на 4, его последние два бита должны быть '00'
    if b[-2:] == '00':
    # if not int(b, 2) % 4:
        print(n)  # 103
        break


# 1332 Danov2101 (Уровень: Средний)
for n in range(3, 1000, 2):
    b = f'{n:b}'
    b = b[0] + ''.join(['01'[i=='0'] for i in b[1:]])
    if int(b, 2) + n > 99:
        print(n)  # 65
        break


# 1519 (Уровень: Базовый)
for n in range(66, 1000):
    b = f'{n:b}'
    for _ in range(3):
        b0 = b.count('0')
        b1 = b.count('1')
        if b0 == b1:
            b += b[-1]
        else:
            b += ('0', '1')[b1 < b0]
    # В двоичной системе, чтобы число делилось на 4, его последние два бита должны быть '00'
    if b[-2:] == '00':
    # if not int(b, 2) % 4:
        print(n)  # 79
        break


# 2461 (Уровень: Средний)
for n in range(100, 1000):
    a,b,c = map(int, str(n))
    ls = sorted([a**2 + b**2, b**2 + c**2])
    if str(ls[1]) + str(ls[0]) == '9010':
        print(n)  # 139
        break


# 3754 (Уровень: Сложный)
for n in range(398, 1000):
    d = [int(a+b) for a, b in zip(str(n), str(n)[1:])]
    if max(d) + min(d) == 137:
        print(n)  # 398
        break


# 9360 Джобс 10.06.13_(23) (Уровень: Базовый)
res = []
for n in range(1, 1000):
    b = f'{n:b}'
    if n % 3:
        b += f'{n % 3 * 5:b}'
    else:
        b += '010'
    r = int(b, 2)
    if r > 300 and not r % 2:
        res.append((r, n))
res.sort()
print(res[0][1])  # 39


# 9736 Основная волна 19.06.13_(23)(Уровень: Базовый)
res = 0
for n in range(4, 1000):
    b = f'{n:b}'
    if n % 3:
        b += f'{n%3 * 3:b}'
    else:
        b += b[-3:]
    r = int(b, 2)
    if r <= 170:
        res = max(res, r)
print(res)  # 166


# 9774 Основная волна 20.06.13_(23) (Уровень: Средний)
def f(n, b=3):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

res = 10**10
for n in range(1, 10000):
    b = f(n)
    if n % 3:
        b += f(n % 3 * 5)
    else:
        b += b[-2:]
    r = int(b, 3)
    if r > 133:
        res = min(res, r)
print(res)  # 141


# 9777 Основная волна 20.06.13_(23)(Уровень: Базовый)
from itertools import *
res = k = 0
for x in sorted(product(range(1,10), repeat=5)):
    k += 1
    if k % 2 and x[0] != 8 and x.count(2) == 2:
        res = k
print(res)  # 58979


# 9831 Основная волна 27.06.13_(23)(Уровень: Базовый)
from itertools import *
res = 0
for p in sorted(product(range(16), repeat=3)):
    if p[0] and len(set(p)) == 3:
        # res += p[0] % 2 != p[1] % 2 and p[1] % 2 != p[2] % 2
        res += all(a % 2 != b % 2 for a, b in zip(p, p[1:]))
print(res)  # 840


# 10087 Демоверсия 2024 (Уровень: Базовый)
res = 1000
for n in range(4, 1000):
    b = f'{n:b}'
    if n % 3:
        b += f'{n%3 * 3:b}'
    else:
        b += b[-3:]
    r = int(b,2)
    if r > 151:
        res = min(res, r)
print(res)  # 163


# 12459 PRO100 ЕГЭ 29.12.13_(23) (Уровень: Базовый)
def cnv(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

for n in range(1000, 1, -1):
    r = cnv(n, 4)
    if not len(r) % 2:
        i = len(r) // 2
        r = r[:i] + '0' + r[i:]
    if int(r) <= 180:  # строку 'r' принимаем как десятичное число ✅
        print(n)  # 31
        break


# 12914 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
res = 0
for n in range(1000):
    r = f'{n:b}'
    if not n % 3:
        r = r.replace('0', '11')
    else:
        r = r.replace('1', '10')
    r = int(r, 2)
    if r <= 161:
        res = max(res, r)  # 148
print(res)









