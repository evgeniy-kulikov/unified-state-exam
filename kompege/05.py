""" https://kompege.ru/task """

"""
49 352 548 551 870
1114 1332 1510 1518 1519 2461 3754 5058 9360 9736 9774 9777 9831
10087 12459 12914 13091 14327 14328 14330 14331 16252 18941 19870 19871 19872 
20278 20883 21473 21474 21782 21974 22269 22270 22271 22272
31143 31213 31351 31502
"""



# 49 Джобс 31.08.2020(Уровень: Базовый)
res = 10**6
for n in range(1, 1000):
    b = f'{n:b}'
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    r = int(b,2)
    if r > 80:
        res = min(res, r)
print(res)


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


# 548 (Уровень: Базовый)
# Бит чётности подбирается так,
# чтобы общее количество единиц в строке (вместе с контрольным битом) всегда было чётным.
res = 10**10
for n in range(1, 1000):
    b = f'{n:b}'
    b += b[-1]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    r = int(b, 2)
    if r > 114:
        res = min(res, r)
print(res)  # 126


# 551 (Уровень: Базовый)
for n in range(1, 1000):
    b = f'{n:b}'
    b += ('01', '10')[n % 2]
    if int(b,2) > 73:
        print(n)  # 19
        break


# 870 Джобс 25.12.2020(Уровень: Базовый)
c = 0
for n in range(2, 1000):
    b = f'{n:b}'
    b += b[-2]
    b += b[1]
    c += 150 <= int(b,2) <= 250
print(c)  # 24


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


# 1510 (Уровень: Базовый)
# Бит чётности подбирается так, чтобы общее количество единиц в строке (вместе с контрольным битом) всегда было чётным.
for n in range(1, 1000):
    b = f'{n:b}'
    b += str(b.count('1') % 2)
    b += '01'[b.count('1') % 2]  # другой вариант
    r = int(b, 2)
    if r > 121:
        print(n)  # 31
        break


# 1518 (Уровень: Базовый)
for n in range(2, 1000):
    b = f'{n:b}'
    b += b[-2]
    b += b[1]
    if int(b,2) > 100:
        print(n)  # 25
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


# 5058 (Уровень: Базовый)
for n in range(1, 2000):
    b = f'{n:b}'
    b = ''.join([('1','0')[i=='1'] for i in b])
    if n - int(b, 2) == 979:
        print(n)  # 1001
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



# 13091 (Уровень: Средний) 👍👍👍 Нестандартный подход!!!
num = set()
for n in range(1, 10_000):
    b = f'{n:b}' + f'{n % 4:b}'
    num.add(int(b, 2))  # На выходе чисел меньше, чем на входе
res = 0
for n in range(1, 10_000):
    c = 0
    for i in range(n, n + 65):
        c += i in num
    res = max(res, c)
print(res)  # 25

# Variant
num = []
for n in range(1, 10_000):
    b = f'{n:b}' + f'{n % 4:b}'
    num.append(int(b, 2))
zero = [0] * (max(num) + 100)
for i in num:
    zero[i] = 1
res = max(sum(zero[i:i+65]) for i in range(len(zero)-65))
print(res)  # 25



# 14327 (Уровень: Средний) 👍 есть ловушка
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    if r:
        return r
    return '0'  # ✔️может передаваться '0'

res = 0
for n in range(1, 1000):
    b = f(n, 8)
    if n % 2:
        add = int(min(b)) * 2
        b += f(add, 8)  # ✔️может передаваться '0'
    else:
        b += max(b)
    r = int(b, 8)
    if r < 313:
        res = n
print(res)  # 38



# 14328 (Уровень: Средний)
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

res = 0
for n in range(1,10_000):
    b = f(n, 12)
    if n % 3:
        b = '2' + b + '0'
    else:
        b = '1' + b + 'b'
    r = int(b, 12)
    if r < 1996:
        res = max(res, r)
print(res)  # 1991


# 14330 (Уровень: Средний)
from math import prod
for n in range(10_000,100_000):
    q = sorted(str(n))
    q = (int(q[0]) + int(q[-1]))**2
    p = prod(map(int, [i for i in str(n) if i in '02468']))
    num = sorted([q, p], reverse=True)
    r = int(str(num[0]) + str(num[1]))
    if r == 12116:
        print(n)  # 22229
        break


# 14331 (Уровень: Средний)
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

res = 10**10
for n in range(1,10_000):
    b = f(n, 3)
    tr = sum(map(int, b))
    if tr % 3:
        b += f(tr * 2, 3)
    else:
        b += '212'
    r = int(b, 3)
    if r > 490:
        res = min(res, r)
print(res)  # 512



# 16252 Джобс 03.05.24(Уровень: Средний)
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

res = 10**10
for n in range(1,10_000):
    b = f(n, 3)
    if n % 2:
        b += '2'
        l = int(b[0], 3) * 2
        b = f(l, 3) + b
    else:
        b = '2' + b
        # l = int(b[-1], 3) * 2
        l = (n % 3) * 2  # ✔️значение младшего разряда
        b += f(l, 3)
    r = int(b, 3)
    if r > 100:
        res = min(res, r)
print(res)


# 18941 (Уровень: Средний) ✅
for n in range(1000,10_000):
    a,b,c,d = map(int, str(n))
    p1 = a * b
    p2 = a * c
    p3 = a * d
    p = sorted([p1, p2, p3])[1:]
    res = int(str(p[0]) + str(p[1]))
    if res == 5472:
        print(n)  # 9068
        break



# 19870 (Уровень: Средний)
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    if r:
        return r
    return '0'

res = 10**10
for n in range(0,10_000):
    b = f(n, 4)
    if n % 2:
        b = '13' + b + '21'
    else:
        b = '12' + b
        l = int(b[-1], 4) * 3
        b += f(l, 4)
    r = int(b, 4)
    if r > 50:
        res = min(res, r)
print(res)  # 96



# 19871 (Уровень: Средний) 🌶️ есть ловушка
def f(n, b):
    if n == 0:
        return '0'  # 🌶️ Ловушка, иначе при '0'  вернет  ''
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

for n in range(1,10_000):
    r = f(n, 5)
    if n % 2:
        r = r[-1] + r[1:-1] + r[0]
        r += '1'
        r = r.lstrip('0')  # удаляются незначащие нули
    else:
        l = int(r[-1], 5) * 3
        r += f(l, 5)
    if r.count('0') == 4:
        print(n)  # 250
        break



# 19872 (Уровень: Средний)
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

for n in range(1000,0, -1):
    r = f(n, 7)
    if n % 2:
        r = r[-1] + r[1:-1] + r[0]
        r += '15'
        r = r.lstrip('0')  # удаляются незначащие нули
    else:
        r = '52' + r + '1'
    if len(r) == 4:
        print(n)  # 721
        break



# 20278 (Уровень: Средний)
for n in range(10000,1, -1):
    b = f'{n:b}'
    if b.count('1') % 2:
        b += '10'
        b = '111' + b[3:]
    else:
        b += '01'
        b = '101' + b[3:]
    r = int(b, 2)
    if r < 385:
        print(n)  # 126
        break



# 20883 (Уровень: Средний)
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

for n in range(1, 1000):
    b = f(n, 5)
    if len(b) % 2:
        b += str(n % 5)
        i = len(b) // 2
        b = b[i:] + b[:i]
    else:
        i = len(b) // 2
        b = b[i:] + b[:i]
    r = int(b, 5)
    if r > 50:
        print(n)  # 26
        break



# 21473 (Уровень: Средний)
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

res = []
for n in range(1, 1000):
    b = f(n, 3)
    if not sum(map(int, b)) % 4:
        b = b.replace('1', '*').replace('2', '1').replace('*', '2')
        b = '10' + b
    else:
        b += '20'
        b = b[0] + '02' + b[3:]
    r = int(b, 3)
    if r > 302:
        res.append((r, n))
res.sort(key=lambda x: (x[0], -x[1]))
print(res[0][1])  # 51



# 21474 (Уровень: Средний)
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

res = []
for n in range(1, 1000):
    b = f(n, 6)
    if not sum(map(int, b)) % 5:
        b = b.replace('0', '*').replace('3', '0').replace('*', '3')
        b = '11' + b
    else:
        b += '44'
        b = b[0] + '05' + b[3:]
    r = int(b, 6)
    if r > 1500:
        res.append((r, n))
res.sort(key=lambda x: (x[0], -x[1]))
print(res[0][1])  # 71


# 21782 (Уровень: Средний)
def f(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

res = []
for n in range(1, 1000):
    b = f(n, 6)
    # if b[-1] == '3':
    if n % 6 == 3:
        b = b.replace('2', '*').replace('0', '2').replace('*', '0')
        b = '10' + b
    else:
        b += '15'
        b = '3' + b[1:]
    r = int(b, 6)
    if r < 1299:
        res.append((r, n))
res.sort(key=lambda x: (-x[0], x[1]))
print(res[0][1])  # 11


# 21974 (Уровень: Средний)
res = []
for n in range(1, 1000):
    b = f'{n:b}'
    if n % 2:
        b = '1' + b[1:].replace('1', '00')
    else:
        b = b.replace('0', '1')
    r = int(b, 2)
    if r <= 600:
        res.append((r, n))
res.sort(reverse=True)
print(res[0][1])  # 257


# 22269 (Уровень: Средний)
def f(n):
    r = ''
    while n:
        r = str(n % 5) + r
        n //= 5
    return r

res = []
for n in range(1, 1000):
    r = f(n)
    # if r[-1] == '0':
    if not n % 5:
        r = r.replace('1', '*').replace('4', '1').replace('*', '4')
        r = '33' + r
    else:
        r += '42'
        r = '3' + r[1:]
    if int(r,5) < 1922:
        res.append((int(r,5), n))
res.sort(key=lambda x: (-x[0], x[1]))
print(res[0][1])  # 9


# 22270 (Уровень: Средний)
def f(n):
    r = ''
    while n:
        r = str(n % 4) + r
        n //= 4
    return r

res = []
for n in range(1000, 0, -1):
    r = f(n)
    if r[0] == '3':
        r = r.replace('1', '*').replace('3', '1').replace('*', '3')
        r = '21' + r
    else:
        r += '12'
        r = '1' + r[1:]
    if int(r,4) < 598:
        res.append((int(r,4), n))
res.sort(reverse=True)
print(res[0][1])  # 63


# 22271 (Уровень: Средний)
def f(n):
    r = ''
    while n:
        r = str(n % 8) + r
        n //= 8
    return r

res = []
for n in range(1000, 0, -1):
    r = f(n)
    if r[0] == '5':
        r = r.replace('2', '*').replace('1', '2').replace('*', '1')
        r += '11' + r
    else:
        r += '10'
        r = '2' + r[1:]
    if int(r,8) < 1354:
        res.append((int(r,8), n))
res.sort(reverse=True)
print(res[0][1])  # 61


# 22272 (Уровень: Средний)
def f(n):
    r = ''
    while n:
        r = str(n % 9) + r
        n //= 9
    return r

res = []
for n in range(1000, 0, -1):
    r = f(n)
    if r[0] == '7':
        r = r.replace('6', '*').replace('3', '6').replace('*', '3')
        r = '34' + r
    else:
        r += '45'
        r = '3' + r[1:]
    if int(r,9) < 2876:
        res.append((int(r,9), n))
res.sort(reverse=True)
print(res[0][1])  # 79


# 31143 Основная волна 19.06.26(Уровень: Базовый)
res = 0
for n in range(1, 1000):
    b = f'{n:b}'
    if n % 2:
        b = '1' + b + '00'
    else:
        b = '11' + b + '11'
    r = int(b,2)
    if r <= 113:
        res = max(res, r)
print(res)  # 108


# 31213 Резерв 22.06.26(Уровень: Базовый)
res = 10**10
for n in range(17, 10_000):
    b = f'{n:b}'
    if n % 2:
        b = '1' + b + '01'
    else:
        b = '10' + b
    r = int(b, 2)
    res = min(res, r)
print(res)  # 82


# 31351  Пересдача 08.07.26(Уровень: Базовый)
for n in range(1, 100):
    b = f'{n:b}'
    if b.count('1') % 2:
        b += '1'
        b = '11' + b[2:]
    else:
        b += '0'
        b = '10' + b[2:]
    r = int(b, 2)
    if r >= 16:
        print(n)  # 8
        break


# 31502 Демоверсия 2027(Уровень: Базовый)
res = 10**10
for n in range(1, 10_000):
    b = f'{n:b}'
    if n % 2:
        b = '1' + b + '00'
    else:
        b = '11' + b + '11'
    r = int(b, 2)
    if r > 95:
        res = min(res, r)
print(res)  # 100




