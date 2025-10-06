""""""
"""
Task 05
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 9.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1220674/step/1?unit=1234060
def fn(b):
    # if not sum(int(i) for i in b) % 2:
    if not b.count('1') % 2:
        return '11' + b[2:] + '00'
    else:
        return '10' + b[2:] + '11'
res = 0
for n in range(1,100):
    b = f'{n:b}'
    b = fn(b)
    b = fn(b)
    res = max(res, int(b, 2))
print(res)  # 1584


# https://stepik.org/lesson/1220674/step/2?unit=1234060
res = []
for n in range(1,190):
    nb = f'{n:b}'
    if nb[-1] == '0':
        nb = '1' + nb + '00'
    else:
        nb += f'{nb.count("1"):b}'
    if int(nb, 2) > 190:
        res +=  [[int(nb, 2), n]]
res.sort()
print(res[0][1])  # 16


# https://stepik.org/lesson/1220674/step/3?unit=1234060
for n in range(1, 1000):
    nb = f'{n:b}'
    if not nb.count('1') % 2:
        nb = '101' + nb[3:] + '0'
    else:
        nb = '10' + nb[2:] + '11'
    if int(nb, 2) > 68:
        print(n)  # 19
        break


# https://stepik.org/lesson/1220674/step/4?unit=1234060
cnt = 0
for n in range(100, 201):
    nb = f'{n:b}'
    if not len(nb) % 2:
        nb += '10'
    else:
        nb = '11' + nb
    cnt += nb[-1] == '0'
print(cnt)  # 87


# https://stepik.org/lesson/1220674/step/5?unit=1234060
# число плавает
res = set()
for n in range(1, 1000):
    n -= f'{n:b}'.count('0')
    nb = f'{n:b}'
    nb = nb[-3:] + nb
    if int(nb, 2) > 224:
        res.add(int(nb, 2))
print(min(res))  # 227


# https://stepik.org/lesson/1220674/step/6?unit=1234060
for n in range(1, 10000):
    nb = f'{n:b}'
    nb = nb.replace('0', '_').replace('1', '0').replace('_', '1')
    if n - int(nb, 2) == 979:
        print(n)
        break  # 1001


# https://stepik.org/lesson/1220674/step/7?unit=1234060
for n in range(10000, 0, -1):
    nb = f'{n:b}'[::-1]
    if nb[0] == '0':
        nb = '1' + nb
    nb +=  f'{n:b}'
    if int(nb, 2) < 6000:
        print(n)  # 63
        break


# https://stepik.org/lesson/1220674/step/8?unit=1234060
for n in range(1, 1000):
    b = f'{2*n:b}'
    b += str(sum(int(i) for i in b) % 2)
    b += str(sum(int(i) for i in b) % 2)
    R = int(b, 2)
    if R > 249:
        print(n)  # 31
        break


# https://stepik.org/lesson/1220674/step/9?unit=1234060
for n in range(4, 1000):
    b = f'{n:b}'
    # b += b[-2]
    # b += b[1]
    b += b[-2] + b[1]
    R = int(b, 2)
    if R > 100:
        print(n)  # 25
        break


# https://stepik.org/lesson/1220674/step/10?unit=1234060
def fn(b):
    z, s = b.count('0'), b.count('1')
    if z == s:
        b += b[-1]
    else:
        b += ('0', '1')[z > s]
    return b

for n in range(80, 10000):
    b = f'{n:b}'
    for _ in range(3):
        b = fn(b)
    R = int(b, 2)
    if not R % 2 and R % 4:
        print(n)  # 81
        break


# https://stepik.org/lesson/1220674/step/11?unit=1234060
res = 0
for n in range(1, 10000):
    b = f'{n:b}'
    if not n % 3:
        b = b.replace('0', '11')
    else:
        b = b.replace('1', '10')
    R = int(b, 2)
    if R <= 161:
        res = max(res, R)
print(res)  # 148





""" 9.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1220675/step/1?unit=1234061
for n in range(1, 10000):
    nb = f'{n:b}'
    if not n % 3:
        nb += nb[-3:]
    else:
        nb += f'{(n % 3) * 3:b}'
    if int(nb, 2) > 76:
        print(n)  # 11
        break

# https://stepik.org/lesson/1220675/step/2?unit=1234061
for n in range(1, 10000):
    nb = f'{n:b}'
    if not len(nb) % 2:
        i = len(nb) // 2
        nb = nb[:i] + '000' + nb[i:]
    else:
        nb = '1' + nb + '01'
    if int(nb, 2) > 100:
        print(n) # 16
        break


# https://stepik.org/lesson/1220675/step/3?unit=1234061
res = []
for n in range(1, 1000):
    b = f'{n:b}'
    if b[-1] == '0':
        b = b[:-1] + '1'
    else:
        b = b[:-1] + '0'
    b += f'{b.count("1") % 2:b}'
    r = int(b, 2)
    if r > 78:
        res += [[r, n]]
res.sort()
print(res[0][1]) # 41


# https://stepik.org/lesson/1220675/step/4?unit=1234061
res = []
for n in range(64, 1000):
    b = f'{n:b}'
    if not b.count('1') % 2:
        inv = b[-4:].replace('0', '*').replace('1', '0').replace('*', '1')
        b = b[:-4] + inv
    else:
        inv = b[-5:-1].replace('0', '*').replace('1', '0').replace('*', '1')
        b = b[:-5] + inv + b[-1]
    r = int(b, 2)
    res += [[r, n]]
res.sort()
print(res[0][1])

# вариант без списка
min_r, res = 100**100, 0
for n in range(64, 1000):
    b = f'{n:b}'
    if not b.count('1') % 2:
        inv = b[-4:].replace('0', '*').replace('1', '0').replace('*', '1')
        b = b[:-4] + inv
    else:
        inv = b[-5:-1].replace('0', '*').replace('1', '0').replace('*', '1')
        b = b[:-5] + inv + b[-1]
    r = int(b, 2)
    if r < min_r:
        min_r = r
        res = n
print(res)


# https://stepik.org/lesson/1220675/step/5?unit=1234061
# Есть вопросы к этому заданию
def fn(num):
    if sum(int(i) for i in str(n)) % 2:
        return '1'
    return '0'

res = 100**100

for n in range(1, 10000):
    b = f'{n:b}'
    for _ in range(3):
        b += fn(n)
    r = int(b, 2)
    if r > 2054:
        res = min(res, r)
print(res)  # 2055


# https://stepik.org/lesson/1220675/step/6?unit=1234061
res = 1000
for n in range(6, 1000):
    b = f'{n:b}'
    if not b[:3].count('1') % 2:
        b = '1' + b[:-2] + '01'
    else:
        b = '10' + b[2:] + '1'
    if int(b, 2) > 50:
        res = min(res, n)
print(res)  # 20


# https://stepik.org/lesson/1220675/step/7?unit=1234061
from math import prod
for m in range(1, 1000):
    nm = str(m) + '120'
    p1 = ''.join([i for i in nm if i in '2468'])
    p2 = ''.join([i for i in nm if i in '13579'])
    p1 = prod(map(int, p1))
    p2 = prod(map(int, p2))
    r = abs(p1 - p2)
    if r == 29:
        print(m)  # 238
        break

# короче
for m in range(1, 1000):
    p1, p2 = 2, 1 # взяли из  120
    for i in str(m).replace('0', ''):
        if i in '2468':
            p1 *= int(i)
        else:
            p2 *= int(i)
    if abs(p1 - p2) == 29:
        print(m)  # 238
        break

# https://stepik.org/lesson/1220675/step/8?unit=1234061
for n in range(100, 1000):
    a, b, c = map(int, str(n))
    n1 = str(a*a + b*b)
    n2 = str(b*b + c*c)
    r = ''.join(sorted([n1, n2], reverse=1))
    if r == '9010':
        print(n)  # 139
        break


# https://stepik.org/lesson/1220675/step/9?unit=1234061
from math import prod
for n in range(1, 1000):
    m = prod([int(i) for i in str(n)])
    b = f'{m:b}' + '00'
    r = int(b, 2)
    if r == 864 and len(set(str(n))) == 1:
        print(n)  # 666


# https://stepik.org/lesson/1220675/step/10?unit=1234061
res = 100**100
for n in range(1, 1000):
    b = f'{n:b}'.replace('0', '00').replace('1', '11')
    # b = ''
    # for i in f'{n:b}':
    #     if i == '0':
    #         b += '00'
    #     else:
    #         b += '11'
    if int(b, 2) > 63:
        res = min(res, int(b, 2))
print(res)  # 192


# https://stepik.org/lesson/1220675/step/11?unit=1234061
def f4(n):
    s = ''
    while n:
        s += str(n % 4)
        n //= 4
    return s[::-1]

res = 10
for n in range(1, 1000):
    b = f4(n)
    b = str(n % 2) + b + str(n % 3)
    R = int(b, 4)
    if 10 <= R < 100:
        res = max(res, R)
print(res)  # 96


# https://stepik.org/lesson/1220675/step/12?unit=1234061
def f3(n):
    s = ''
    while n:
        s += str(n % 3)
        n //= 3
    return s[::-1]

res = 1000
num = 0
for n in range(10, 1000):
    b = f3(n)
    if not n % 2:
        b = b + b[-2:]
    else:
        t = sum(int(i) for i in b)
        b = b + f3(t)
    R = int(b, 3)
    if R < res:
        res = R
        num = n
print(num)  # 27


# https://stepik.org/lesson/1220675/step/13?unit=1234061
def f6(n):
    s = ''
    while n:
        s = str(n % 6) + s
        n //= 6
    return s + s[-1]

for n in range(100000, 0, -1):
    b = int(f6(n), 6)
    b = f'{b:b}'
    R = b.count('1')
    if R == 18:
        print(n)  # 87359
        break


# https://stepik.org/lesson/1220675/step/14?unit=1234061
def f7(n):
    s = ''
    while n:
        s = str(n % 7) + s
        n //= 7
    return s

cnt = 0
for n in range(343, 2402):
    b = f7(n)
    if b[-1] in '02468':
        b = '6' + b
    else:
        b = '5' + b
    R = int(b, 7)
    cnt += R > 14500
print(cnt)  # 1177


# https://stepik.org/lesson/1220675/step/15?unit=1234061
cnt = 0
for n in range(1, 10000):
    h = hex(n)[2:].lower()
    if not h.count('b') % 2:
        h = '1' + h
    else:
        h += '1'
    cnt += len(str(int(h, 16))) == 2
print(cnt)  # 14


# https://stepik.org/lesson/1220675/step/16?unit=1234061
def f3(n):
    s = ''
    while n:
        s += str(n % 3)
        n //= 3
    return s[::-1]

res = 100**100
for n in range(16, 10000):
    b = f3(n)
    sm = sum(int(i) for i in b)
    if not sm % 4:
        b = '1' + b[:-2]
    else:
        b += f3(sm % 4 * 3)
    R = int(b, 3)
    if R > 353:
        res = min(res, R)
print(res)  # 354


""" 12.4 Закрепление """
# https://stepik.org/lesson/1221558/step/5?unit=1234968
for n in range(1, 1000):
    b = f'{n:b}'.zfill(8)
    b = b.replace('0', '*').replace('1', '0').replace('*', '1')
    r = int(b, 2) - n
    if r == 133:
        print(n)  # 61
        break


""" 14.4 Закрепление """
# https://stepik.org/lesson/1222740/step/5?unit=1236143
for n in range(10000, 1000000):
    s = str(n)
    a = sum(map(int, [s[i] for i in range(0,5,2)]))
    b = sum(map(int, [s[i] for i in range(1,5,2)]))
    if ''.join(map(str, sorted([a, b]))) == '723':
        print(n)  # 50979
        break

""" 15.3 Закрепление """
# https://stepik.org/lesson/1223041/step/5?unit=1236528
for n in range(1000):
    b = f'{n:b}'
    for _ in range(2):
        b += str(b.count('1') % 2)
    if int(b, 2) > 77:
        print(n)  # 19
        break

""" 16.4 Закрепление """
# https://stepik.org/lesson/1223083/step/5?unit=1236572
for n in range(999, 10_000):
    b = f'{n:b}'
    b = b.replace('0', '*').replace('1', '0').replace('*', '1')
    if n - int(b, 2) == 999:
        print(n)  # 1011
        break


""" 17.4 Закрепление """
# https://stepik.org/lesson/1223105/step/5?unit=1236594
for n in range(1, 10_000):
    b = f'{n:b}'
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    r = int(b, 2)
    if r > 83:
        print(r)  # 86
        break


""" 18.4 Закрепление """
# https://stepik.org/lesson/1224003/step/5?unit=1237500
for n in range(100, 1000):
    a,b,c = list(map(int, str(n)))
    ls = sorted([a*b, b*c])
    if int(str(ls[0]) + str(ls[1])) == 621:
        print(n)  # 237
        break


""" 19.4 Закрепление """
# https://stepik.org/lesson/1225428/step/5?unit=1238919
for n in range(13, 256):
    b = f'{n:b}'.zfill(8)
    b = b.replace('0', '*').replace('1', '0').replace('*', '1')
    if  int(b, 2) - n == 111:
        print(n)  # 72


""" 20.4 Закрепление """
# https://stepik.org/lesson/1226263/step/5?unit=1239750
for n in range(999, 99, -1):
    a,b,c = map(int, str(n))
    d = sorted([a*b, b*c])
    r = int(''.join(map(str, d)))
    if r == 621:
        print(n) # 732
        break


""" 21.4 Закрепление """
# https://stepik.org/lesson/1227125/step/5?unit=1240643
cnt = 0
for n in range(1111, 10000, 2):
    a,b,c,d = map(int, str(n))
    if all(i%2 for i in (a,b,c,d)):
        d = sorted([a+b, c+d])
        cnt += ''.join(map(str, d)) == '414'
print(cnt)  # 12


""" 26.4 Закрепление (ч. 1) """
# https://stepik.org/lesson/1229245/step/5?unit=1242786
res = set()
for n in range(10, 1001):
    b = f'{n:b}'[1:]
    if b.count('1'):
        b = b[b.index('1'):]
    else:
        b = '0'
    res.add(n - int(b, 2))
print(len(res))  # 7


