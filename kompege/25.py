""" https://kompege.ru/task """
"""
315 
1867 2588 2590 2594 3376 4739 4741 5224 5642 5736 8426 8481 8511
11249 12477 12932 17536 17564 17642 19255
21909 23282 23382 23569 23763
"""



# 315 Джобс 28.09.2020 (Уровень: Средний)
def dv(n):
    r = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

for n in range(326496, 649632):
    d = dv(n)
    if len(d) >= 140:
        a = b = 0
        for i in d:
            if i % 2:
                b += 1
            else:
                a += 1
        if a == b:
            print(n, min(i for i in d if i > 1000))
"""
450450 1001
589050 1050
630630 1001
"""





# 1867 Основная волна 2021 (Уровень: Базовый)
def dv(n):
    r = set()
    for i in range(9, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

c = 5
for n in range(500_001, 10**10):
    d = dv(n)
    res = [i for i in d if i % 10 == 8]
    if res:
        print(n, min(res))
        c -= 1
    if not c:
        break
"""
500002 178
500004 18
500016 48
500018 58
500020 4348
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


# 2594 (Уровень: Гроб) 🌶️🌶️🌶️
def dv(n):
    r = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

for n in range(113_000_000, 114_000_001, 2):
    p = n // 2  # эти две строчки очень сильно
    if  int(p**0.5)**2 == p:  # ускоряют код (логику не понял)
        d = dv(n)
        r = sorted(i for i in d if not i % 2)
        if len(r) == 3:
            print(n, r[1])
"""
113010578 15034
113191058 15046
113371682 15058
113612738 15074
113733362 15082
113914418 15094
113974802 15098
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


# 5224 (Уровень: Средний)
from fnmatch import *
for n in range(10**5):  # int((10**10)**0.5) == 10**5
    if fnmatch(str(n**2), '4*1?009'):
        print(n, n**2)
"""
2003 4012009
6497 42211009
63997 4095616009
64997 4224610009
69003 4761414009
"""


# 5642 (Уровень: Средний)
from fnmatch import *
def dv(n):
    r = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

c = 5
for n in range(500_001, 10**10):
    d = dv(n)
    res = [i for i in d if fnmatch(str(i), '*1?3')]
    if len(res) == 3:
        d.remove(n)  # не считая самого числа❗
        print(n, max(d))  # максимальй делитель из ВСЕХ❗ (кроме самого числа)
        c -= 1
    if not c:
        break
"""
500786 250393
501963 167321
503006 251503
503217 167739
506142 253071
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





# 11249 (Уровень: Базовый)
# ✅ Без fnmatch ✅
for n in range(0, 8 * 10**9, 9627):
    s = str(n)
    if s[0] == '7' and '61' in s[1:-3] and s[-3:] == '331':
        print(n, n // 9627)

from fnmatch import *
for n in range(0, 8 * 10**9, 9627):
    if fnmatch(str(n), '7*61*331'):
        print(n, n // 9627)
"""
706169331 73353
7069616331 734353
7406561331 769353
7416188331 770353
7618355331 791353
7676117331 797353
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


# 19255 ЕГКР 21.12.24 (Уровень: Базовый)
from fnmatch import *
# for n in range(0, 10**10, 18579):
for n in range(0, 6*10**9, 18579):
    if fnmatch(str(n), '54?1?3*7'):
        print(n, n // 18579)
"""
545163597 29343
5411932647 291293
5421036357 291783
5451134337 293403
5461538577 293963
5481232317 295023
5491636557 295583
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
    if res:  # if len(res) > 1
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


# 23763 Демоверсия 2026 (Уровень: Базовый)
def dv(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return i + n // i  # ✅ первыми находятся мин. и макс. делители. Другие уже не нужны ❗❗❗
c = 5
for n in range(800_001, 10**10):
    m = dv(n)
    if m and m % 10 == 4:
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