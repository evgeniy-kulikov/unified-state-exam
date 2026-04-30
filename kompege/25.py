""" https://kompege.ru/task """
"""
2588 2590 3376 4739 4741 5736 8426 8481 8511
12477 12932 17536 17564 17642
21909 23282 23382 23569
"""


# 2588 (Уровень: Базовый)
def dv(n):
    r = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n //i}
    return sorted([i for i in r if not i % 2], reverse=1)

for n in range(190226, 190261):
    d = dv(n)
    if len(d) == 4:
        print(*d[:2])
"""
190226 838
190234 17294
190238 2606
190252 95126
190258 758
"""


# 2590 (Уровень: Базовый)
for n in range(6080068, 6080177):
    if all(n % i for i in range(2, int(n**0.5 + 1))):
        print(n)
"""
6080069
6080131
6080141
6080147
6080149
6080153
6080161
"""

# 3376 Джобс 22.04.2022 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 14_600_000, 21):
    if fnmatch(str(n), '1*5*9'):
        if all(a < b for a, b in zip(str(n), str(n)[1:])):
            print(n, n//21)
"""
12579 599
123459 5879
134589 6409
1234569 58789
1356789 64609
"""


# 4739 (Уровень: Средний)
def f(n):
    if n > 10_000:
        return n - 10_000
    return f(n + 1) + f(n + 2)

# (f(10) - f(12)) // f(11) == 1
print(f(12_345) + f(10_101))  # 2446



# 4741 (Уровень: Средний)
def f(n):
    if int(n**0.5) == n**0.5:
        return int(n**0.5)
    return f(n + 1) + 1

print(f(4850) + f(5000))  # 232


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


# 8426 (Уровень: Средний)
def f(n):
    if n > 1_000_000:
        return n
    return n + f(2 * n)

c = 0
m = f(2_000) / 2_000
for i in range(1, 10_001):
    if f(i) / i == m:
        c += 1
print(c)  # 1953


#  8481 (Уровень: Базовый)
from fnmatch import fnmatch as f
for n in range(0, 82000000, 237):
    if f(str(n), '81?2*80') and not f(str(n), '*9*'):
        print(n, n // 237)
"""
815280 3440
8162280 34440
81324180 343140
81727080 344840
81821880 345240
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





# 12477 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
from fnmatch import *
for n in range(301111, 4000000):
    if fnmatch(str(n), '3?1111*'):
        if all(n % i for i in range(2, int(n**0.5 + 1))):
            print(n)
"""
311111
361111
3011117
3011119
3311117
3611119
3811117
3911111
"""


# 12932 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 1930000000, 2024):
    if fnmatch(str(n), '1?2*4'):
        if int(n**0.5) == n**0.5:
            print(n, n // 2024)
"""
1024144 506
1327290624 655776
1721586064 850586
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
    if r:
        m = min(r) + max(r)
        if m % 10 == 4:
            print(n, m)
            c -= 1
    if not c:
        break
"""
700004 350004
700009 41194
700023 233344
700024 350014
700044 350024
"""


# 17642 Основная волна 19.06.24 (Уровень: Базовый)
def dv(n):
    r = set()
    for i in range(10, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n //i}
    return [i for i in r if i % 10 == 9]

c = 5
for n in range(800000, 10**10):
    d = dv(n)
    if d:
        print(n, min(d))
        c -= 1
    if not c:
        break
"""
800001 309
800003 47059
800004 409
800006 269
800007 39
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

