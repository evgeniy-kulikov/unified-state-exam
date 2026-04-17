""" https://kompege.ru/task """
"""
5736 8511
17536 17564
21909 23282 23382 23569
"""



# 5736 (Уровень: Средний)
def dv(n):
    r = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return max(r)

c = 5
for n in range(10**9, 10**10):
    if str(n) == str(n)[::-1]:
        r = dv(n)
        if not r % 7:
            c -= 1
            print(n, r)
        if not c:
            break
"""
1001771001 333923667
1002002001 334000667
1003003001 143286143
1004774001 334924667
1005005001 335001667
"""


# 8511 Апробация 17.05 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 10**8+1, 253):
    if fnmatch(str(n), '12??15*6'):
        print(n, n//253)
"""
1278156 5052
12531596 49532
12741586 50362
12951576 51192
"""




# 17536 Основная волна 07.06.24 (Уровень: Средний)
def f(n):
    r = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return sorted(r)

c = 5
for n in range(800_000, 10**10):
    d = f(n)
    if d:
        m = d[0] + d[-1]
        if m % 10 == 4:
            print(n, m)
            c -= 1
    if not c:
        break
"""
800004 400004
800009 114294
800013 266674
800024 400014
800033 61554
"""


# 17564 Основная волна 08.06.24 (Уровень: Средний)
def dv(n):
    r = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

c = 5
for n in range(700_000, 10**10):
    r = dv(n)
    if len(r) > 1:
        m = min(r) + max(r)
        if m % 10 == 4:
            c -= 1
            print(n, m)
    if not c:
        break
"""
700004 350004
700009 41194
700023 233344
700024 350014
700044 350024
"""





# 21909 Открытый вариант 2025 (Уровень: Базовый)
def dv(n):
    r = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return sum(r)

c = 5
for n in range(500_000, 10**10):
    r = dv(n)
    if r % 10 == 6:
        c -= 1
        print(n, r)
    if not c:
        break
"""
500032 1070356
500035 606816
500039 501456
500050 949716
500052 1333696
"""

# 23282 Основная волна 11.06.25 (Уровень: Средний)
def dv(n):
    r = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

def spl(n):
    return all(n % i for i in range(2, int(n**0.5) + 1))

c = 5
for n in range(5_400_000, 10**10):
    r = dv(n)
    res = [i for i in r if smpl(i)]
    if res:
        m = min(res) + max(res)
        if str(m) == str(m)[::-1] and m > 60_000:
            print(n, m)
            c -= 1
    if not c:
        break
"""
5400042 900009
5400420 90009
5400866 158851
5406116 1351531
5406420 90109
"""


# 23382 Резервный день 19.06.25 (Уровень: Средний)
def dv(n):
    r = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

def smpl(n):
    s = [n % i for i in range(2, int(n**0.5 + 1))]
    return all(n % i for i in range(2, int(n**0.5 + 1)))

c = 5
for n in range(6_651_220, 10**10):
    if not c:
        break
    r = dv(n)
    res = [i for i in r if smpl(i) and str(i).count('2')]
    if res:
        if min(res) * max(res) == n:  # ❓ число может быть только из такого варианта 🤔
            c -= 1
            print(n, max(res))

# Вариант
c = 5
for n in range( 6_651_220, 10**10):
    if not c:
        break
    dv_num = dv(n)
    if dv_num:
        d = [i for i in dv_num if smpl(i) and str(i).count('2')]
        if d:
            for p in product(d, repeat=2):
                if p[0] * p[1] == n:  # ✔️ Так точно найдем
                    print(n, max(p))
                    c -= 1
                    break
"""
6651241 2579
6651262 3325631
6651286 3325643
6651314 3325657
6651347 289189
"""


# 23569 Пересдача 03.07.25 (Уровень: Средний)
def dv(n):
    r = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

def smpl(n):
    for i in range(2, int(n**0.5 +1 )):
        if not n % i:
            return False
    return True

c = 5
for n in range(6_086_055, 10**10):
    r = dv(n)
    res = [i for i in r if smpl(i)]
    res = [i for i in res if str(i).count('6') == 1]
    if res:
        m = min(res) * max(res)
        if m == n:
            c -= 1
            print(n, max(res))
    if not c:
        break
"""
6086089 2467
6086161 3673
6087281 9467
6087317 36451
6087727 2683
"""

