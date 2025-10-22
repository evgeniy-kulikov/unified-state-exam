""""""
"""
Task 24
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 28.2 Практика (ур. базовый) """

# https://stepik.org/lesson/1229671/step/1?unit=1243223
from fnmatch import fnmatch
for n in range((2054431 // 23) * 23, 10**8 + 1, 23):
    if fnmatch(str(n), '2*5443?1'):
        print(n, n // 23)
# 22544301 980187
# 23544341 1023667
# 24544381 1067147
# 28544311 1241057
# 29544351 1284537


# https://stepik.org/lesson/1229671/step/2?unit=1243223
from fnmatch import fnmatch
def f(n):
    dv = [*range(12, 93, 10)]
    res = [i for i in dv if not n % i]
    if len(res) > 4:
        return min(res)

for n in range(103050608, 193959698 + 1, 10):
    if fnmatch(str(n), '1?3?5?6?8'):
        d = f(n)
        if d:
            print(n, n // d)
# 103154688 8596224
# 173457648 14454804


# https://stepik.org/lesson/1229671/step/3?unit=1243223
def f(n):
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return i + n // i

cnt = 5
for n in range(220_001, 10**6):
    d = f(n)
    if d and d % 10 == 4:
        print(n, d)
        cnt -= 1
    if not cnt:
        break
# 220004 110004
# 220023 73344
# 220024 110014
# 220033 20014
# 220043 1044


# https://stepik.org/lesson/1229671/step/4?unit=1243223
def f(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if not n % i:
            d |= {i, n // i}
    res = [i for i in d if not i % 2]
    if len(res) == 4:
        res.sort()
        return res[-1], res[-2]

for n in range(190201, 190261):
    d = f(n)
    if d:
        print(*d)
# 190226 838
# 190234 17294
# 190238 2606
# 190252 95126
# 190258 758


# https://stepik.org/lesson/1229671/step/5?unit=1243223
def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d |= {i, n // i}
    res = [i for i in d if i % 10 == 8 and i != 8]
    if res:
        return min(res)

c = 5
for n in range(500_000, 10**7):
    d = f(n)
    if d:
        print(n, d)
        c -= 1
    if not c:
        break
# 500002 178
# 500004 18
# 500016 48
# 500018 58
# 500020 4348


# https://stepik.org/lesson/1229671/step/6?unit=1243223
def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d |= {i, n // i}
    if d:
        return sum(d)

c = 4
for n in range(136180, 10**7):
    d = f(n)
    if d and d % 385 == 91:
        print(n, d)
        c -= 1
    if not c:
        break
# 136968 232631
# 137126 97881
# 137255 29736
# 138778 69391


# https://stepik.org/lesson/1229671/step/7?unit=1243223
def smpl(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d |= {i, n // i}
    if d:
        res = [i for i in d if smpl(i)]
        return sum(res)

c = 7
for n in range(499_999, 0, -1):
    d = f(n)
    if d and not d % 10:
        print(n, d)
        c -= 1
    if not c:
        break
# 499996 2560
# 499995 320
# 499994 22740
# 499989 860
# 499981 13550
# 499971 166660
# 499959 18520


# https://stepik.org/lesson/1229671/step/8?unit=1243223
def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d |= {i, n // i}
    return [i for i in d if i**2 == n]

for n in range(248015, 251576, 2):
    if n**0.5 == int(n**0.5):
        print(n, *f(n))
# 249001 499
# 251001 501

# short !!!
for n in range(248015, 251576, 2):
    if int(n**0.5) == n**0.5:
        print(n, int(n**0.5))


# https://stepik.org/lesson/1229671/step/9?unit=1243223
def f(n):
    d = set()
    for i in range(3, int(n**0.5) + 1):
        if not n % i:
            d |= {i, n // i}
    if len(d) > 70:
        return max(d)

# Все делители нечетного числа также будут нечетными
for n in range(321655, 654322, 2):
    d = f(n)
    if d:
        print(n, d)
# 405405 135135
# 530145 176715
# 592515 197505
# 626535 208845


# https://stepik.org/lesson/1229671/step/10?unit=1243223
def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d |= {i, n // i}
    res = [i for i in d if 10 <= i < 100]
    if len(res) == 35:
        return min(res), max(res)


for n in range(333555, 778_000):
    d = f(n)
    if d:
        print(*d)
# 10 96
# 10 99
# 10 99
# 10 91
# 10 99




""" 28.3 Практика (ур. усложненный) """

# https://stepik.org/lesson/1229672/step/1?unit=1243224
from fnmatch import *
def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d |= {i, n // i}
    if len(d) == 18:
        return max(d)

for n in range(12045, 1299946, 5):
    if fnmatch(str(n), '12?*45'):
        d = f(n)
        if d:
            print(n, d)
# 1202445 400815
# 1234845 411615
# 1251045 417015
# 1259145 419715
# 1283445 427815
# 1299645 433215


# https://stepik.org/lesson/1229672/step/2?unit=1243224
def f(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return False
    return True

c = 6
for n in range(600_000, 10**7, 6):
    if f(n-1) and f(n+1):
        print(n-1, n+1)
        c -= 1
        if not c:
            break
# 600071 600073
# 600167 600169
# 600239 600241
# 600317 600319
# 600359 600361
# 600401 600403


# https://stepik.org/lesson/1229672/step/3?unit=1243224
from fnmatch import *
def f(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    return sum(i for i in d if i % 2)

c = 7
ls = []
for n in range(10**7-(10**7 % 217), 216, -217):
    if fnmatch(str(n), '14?4*'):
        d = f(n)
        if d:
            ls += [(n, d)]
            c -= 1
            if not c:
                break
ls.sort()
[print(*i) for i in ls]
# 1484714 958464
# 1484931 2336768
# 1494045 3345408
# 1494262 964608
# 1494479 1806336
# 1494696 306432
# 1494913 1785088


# https://stepik.org/lesson/1229672/step/4?unit=1243224
from fnmatch import *
def f(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    res = [i for i in d if not i % 2]
    if len(res) >= 4:
        return sum(res)

c = 7
for n in range(65_000, 10**6):
    if fnmatch(str(n), '6*97*5?'):
        d = f(n)
        if d:
            print(n, d)
            c -= 1
            if not c:
                break
# 69750 129792
# 69752 122080
# 69756 139536
# 69758 75152
# 609750 1103232
# 609752 1291248
# 609754 630840


# https://stepik.org/lesson/1229672/step/5?unit=1243224
def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    res = [i for i in d if i % 2]
    if len(res) >= 6:
        return sorted(res)[-6]

c = 5
for n in range(2*10**8 + 1, 2*10**10):
    d = f(n)
    if d:
        print(n, d)
        c -= 1
        if not c:
            break
# 200000003 48391
# 200000004 42123
# 200000005 5
# 200000008 5101
# 200000009 113443


# https://stepik.org/lesson/1229672/step/6?unit=1243224
def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    if len(d) >= 3:
        res = sorted(d)
        r = sum(res[-3:])
        if not r % 2022:
            return r

ls = []
c = 5
for n in range(1_200_000, 0, -1):
    d = f(n)
    if d and (d != n):
        ls.append((n, d))
        c -= 1
        if not c:
            break
ls.sort()
[print(*i) for i in ls]
# 1091880 1182870
# 1116144 1209156
# 1140408 1235442
# 1164672 1261728
# 1188936 1288014


# https://stepik.org/lesson/1229672/step/7?unit=1243224
from math import prod
def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    if len(d) >= 5:
        res = sorted(d)
        r = prod(res[:5])
        if r % 100 == 17 and r <= n:
            return r, res[4]

c = 5
for n in range(4*10**8 + 1, 5*10**8):
    d = f(n)
    if d:
        print(*d)
        c -= 1
    if not c:
        break
# 782217 37
# 166617 33
# 2880117 93
# 74874717 111
# 725517 53


# https://stepik.org/lesson/1229672/step/8?unit=1243224
def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    if d:
        res = [i for i in d if i % 10 == 7]
        if len(res) == 3:
            return max(res)

c = 5
for n in range(550_000 + 1, 900_000):
    d = f(n)
    if d:
        print(n, d)
        c -= 1
    if not c:
        break
# 550014 275007
# 550017 1567
# 550032 34377
# 550035 110007
# 550037 9017


# https://stepik.org/lesson/1229672/step/9?unit=1243224
from statistics import mean
def smpl(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return False
    return True

def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    res = [k for k in d if smpl(k)]
    if res:
        return int(mean(res))

c = 6
for n in range(310_001, 500_000):
    d = f(n)
    if d and not d % 6 and d % 10 != 4:
        print(n, d)
        c -= 1
    if not c:
        break
# 310005 30
# 310006 77502
# 310010 276
# 310016 60
# 310017 1506
# 310038 17226


# https://stepik.org/lesson/1229672/step/10?unit=1243224
def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    if d:
        return max(d) - min(d)

c = 6
for n in range(350_001, 500_000):
    d = f(n)
    if d and d % 23 == 9:
        print(n, d)
        c -= 1
    if not c:
        break
# 350015 69998
# 350017 8496
# 350036 175016
# 350073 116688
# 350082 175039
# 350128 175062


# https://stepik.org/lesson/1229672/step/11?unit=1243224
from fnmatch import *
def f(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return n // i

for n in range(3520, 10**7):
    if int(n**0.5) == n**0.5:
        if fnmatch(str(n), '3*52?'):
            print(n, f(n))
# 3143529 1047843
# 3175524 1587762
# 3200521 1789
# 3845521 103933
# 3908529 1302843


# https://stepik.org/lesson/1229672/step/12?unit=1243224
def smpl(n):
    if n == 1: return False
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return False
    return True

def f(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    if d:
        simple = [i for i in d if smpl(i)]
        even = [i for i in d if not i % 2]
        if len(simple) == len(even):
            return abs(sum(simple) - sum(even))

c = 5
for n in range(10**8 + 1, 10**9):
    d = f(n)
    if d:
        print(n, d)
        c -= 1
        if not c:
            break
# 100000034 50000017
# 100000042 50000021
# 100000094 50000047
# 100000118 50000059
# 100000126 50000063



# https://stepik.org/lesson/1229672/step/13?unit=1243224
def f(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    if d:
        n3 = [i for i in d if i % 10 == 3 and len(str(i)) == 3]
        if len(n3) == 3:
            return min(n3)

c = 5
for n in range(97**3 + 1, 10**6):
    d = f(n)
    if d:
        print(n, d)
        c -= 1
        if not c:
            break
# 912912 133
# 912951 153
# 913198 103
# 913353 183
# 913767 123


# https://stepik.org/lesson/1229672/step/14?unit=1243224
def f(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d |= {(n // i, i)}
    return d

for n in range(1000000, 1500001):
    d = f(n)
    if d:
        mn = [(max(i), i[0] - i[1]) for i in d]
        mn = sorted([i for i in mn if i[1] <= 110])
        if len(mn) >= 3:
            print(n, mn[-1][0])
# 1113840 1105
# 1179360 1134
# 1208844 1148
# 1422720 1248
# 1499400 1275



""" 28.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1229674/step/15?unit=1243226
from fnmatch import *
st = 1069615 + 1069615 % 3013
for n in range(st, 2 * 10**9, 3013):
    if fnmatch(str(n), '1?6961*5'):
        print(n)
"""
1069615
1769610225
1869611695
1969613165
"""
