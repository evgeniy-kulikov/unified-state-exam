""""""
"""
Task 25
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 25.1 Задание 25 ЕГЭ | Урок 1 """
# https://stepik.org/lesson/1720858/step/2?unit=1744394
# https://kompege.ru/task   № 22 Демоверсия 2021 (Уровень: Базовый)
def f(n: int):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

res = []
for n in range(174457, 174506):
    d = f(n)
    if len(d) == 2:
        res += [(d[0]*d[1], d)]

res.sort()
for i in res:
    print(*i[1])
"""
3 58153
7 24923
59 2957
13 13421
149 1171
5 34897
211 827
2 87251
"""


# https://stepik.org/lesson/1720858/step/3?unit=1744394
# https://kompege.ru/task   № 67 Джобс 31.08.2020 (Уровень: Базовый)
def f(n: int):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

res = []
for n in range(81234, 134690):
    d = f(n)
    if len(d) == 3:
        res += [d]

res.sort()
for i in res:
    print(*i)
"""
17 289 4913
19 361 6859
"""

# https://stepik.org/lesson/1720858/step/4?unit=1744394
# https://kompege.ru/task   № 892 (Уровень: Базовый)
def f(n: int):
    dv = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

for n in range(154026, 154044):
    d = f(n)
    if len(d) == 4:
        print(*d[2:])
"""
51343 154029
77017 154034
4969 154039
51347 154041
"""


# https://stepik.org/lesson/1720858/step/5?unit=1744394
# https://kompege.ru/task   № 1388 (Уровень: Средний)
def f(n: int):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

cnt = 7
for n in range(150000, 15000000):
    d = f(n)
    if sum(d) % 13 == 10:
        print(n, sum(d))
        cnt -= 1
    if not cnt:
        break
"""
150016 150745
150024 310775
150048 277469
150108 250403
150139 13660
150144 290495
150146 81273
"""


# https://stepik.org/lesson/1720858/step/6?unit=1744394
# https://kompege.ru/task   № 1231 Апробация 27.04 (Уровень: Базовый)
def f(n: int):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

cnt = 5
for n in range(250200, 25020000):
    d = f(n)
    if len(d) >= 2:
        sm = d[0] + d[-1]
        if sm % 123 == 17:
            print(n, sm)
            cnt -= 1
    if not cnt:
        break
"""
250212 125108
250458 125231
250593 83534
250621 35810
250704 125354
"""


# https://stepik.org/lesson/1720858/step/7?unit=1744394
# https://kompege.ru/task   № 1392 (Уровень: Средний)
from statistics import mean
def f(n: int):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

cnt = 5
for n in range(550000, 5500000):
    d = f(n)
    if d:
        r = int(mean(d))
        if r % 31 == 13:
            print(n, r)
            cnt -= 1
    if not cnt:
        break
"""
550032 28285
550040 49117
550046 28905
550050 19419
550066 35725
"""


# https://stepik.org/lesson/1720858/step/8?unit=1744394
# https://kompege.ru/task   № 2595 (Уровень: Средний)
from math import prod
def f(n):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

cnt = 5
for n in range(4*10**8+1, 4*10**9):
    d = f(n)
    if len(d) >= 5:
        p = prod(d[:5])
        if p % 100 == 17 and p <= n:
            print(p, d[4])
            cnt -= 1
    if not cnt:
        break
"""
782217 37
166617 33
2880117 93
74874717 111
725517 53
"""


# https://stepik.org/lesson/1720858/step/9?unit=1744394
# https://kompege.ru/task   № 2588 (Уровень: Базовый)
def f(n):
    dv = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv, reverse=True)

for n in range(190201, 190261):
    res = [i for i in f(n) if not i % 2]
    if len(res) == 4:
        print(*res[:2])
"""
190226 838
190234 17294
190238 2606
190252 95126
190258 758
"""


# https://stepik.org/lesson/1720858/step/10?unit=1744394
# https://kompege.ru/task  № 1078 (Уровень: Базовый)
def f(n):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return dv

for n in range(1204300, 1204381):
    dv = f(n)
    sd = sum(i for i in dv if not i % 2)
    if sd and not sd % 10:
        print(n, sd)
"""
1204328 948760
1204354 27530
1204356 1204380
1204360 1324880
1204366 4850
1204370 291070
1204378 172070
"""


# https://stepik.org/lesson/1720858/step/11?unit=1744394
# https://kompege.ru/task  № 1867 Основная волна 2021 (Уровень: Базовый)
def f(n):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return dv

c = 5
for n in range(500_000, 10**10):
    dv = f(n)
    n8 = [i for i in dv if i % 10 == 8 and i != 8]
    if n8:
        print(n, min(n8))
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



""" 25.2 Задание 25 ЕГЭ | Урок 2 """
# https://stepik.org/lesson/1720859/step/1?unit=1744395
# https://kompege.ru/task   № 2589 (Уровень: Средний)
def f(n):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

cnt = 4
for n in range(300000, 30000000):
    d = [i for i in f(n) if not i % 3]
    if len(d) == 5:
        print(n, d[-1])
        cnt -= 1
        if not cnt:
            break
"""
300051 100017
300075 60015
300156 150078
300159 100053
"""


# https://stepik.org/lesson/1720859/step/2?unit=1744395
# https://kompege.ru/task   № 2361 (Уровень: Средний)
def f(n):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

cnt = 5
for n in range(550000, 5500000):
    d = [i for i in f(n) if i % 10 == 7]
    if len(d) == 3:
        print(n, d[-1])
        cnt -= 1
        if not cnt:
            break
"""
550014 275007
550017 1567
550032 34377
550035 110007
550037 9017
"""


# https://stepik.org/lesson/1720859/step/3?unit=1744395
# https://kompege.ru/task   № 2590 (Уровень: Базовый)
def f(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return False
    return True

for n in range(6080068, 6080177):
    if f(n):
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


# https://stepik.org/lesson/1720859/step/4?unit=1744395
# https://kompege.ru/task   № 506 Джобс 19.10.2020 (Уровень: Базовый)
def fn(n):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return dv

def fs(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return False
    return True

for n in range(25317, 51238):
    dv = fn(n)
    smpl = [i for i in dv if fs(i)]
    if len(smpl) >= 6:
        print(n, max(smpl))

"""
30030 13
39270 17
43890 19
46410 17
"""





""" 25.3 Задание 25 ЕГЭ | Урок 3 """
# https://stepik.org/lesson/1720860/step/1?unit=1744396
# https://kompege.ru/task   № 3229 Досрочный этап 2022 (Уровень: Базовый)
for a in range(10):
    for b in range(10):
        n = int(f'12345{a}6{b}8')
        if not n % 17:
            print(n, n // 17)
"""
123450668 7261804
123451688 7261864
123456618 7262154
123457638 7262214
123458658 7262274
123459678 7262334
"""


# https://stepik.org/lesson/1720860/step/2?unit=1744396
# https://kompege.ru/task   № 4603 Основная волна 2022 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 10**8, 141):
    if fnmatch(str(n), '1234*7'):
        print(n, n // 141)

# variant
from itertools import product
ls = []
for n in range(4):
    ls.extend([''.join(p) for p in product('0123456789', repeat=n)])
for i in ls:
    n = int(f'1234{i}7')
    if not n % 141:
        print(n, n // 141)

"""
1234737 8757
12341307 87527
12342717 87537
12344127 87547
12345537 87557
12346947 87567
12348357 87577
12349767 87587
"""


# https://stepik.org/lesson/1720860/step/3?unit=1744396
# https://kompege.ru/task   № 3692 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 10**9, 169):
    if fnmatch(str(n), '123*567?'):
        print(n, n // 169)

# variant
from itertools import product
w = []
res = []
for i in range(3):
    w += [''.join(p) for p in product('0123456789', repeat=i)]
for a in w:
    for b in w[1:11]:
        n = int(f'123{a}567{b}')
        if not n % 169:
            res.append((n, n // 169))
res.sort()
[print(*i) for i in res]
"""
12325677 72933
12385672 73288
123165679 728791
123225674 729146
123515678 730862
123575673 731217
123865677 732933
123925672 733288
"""


# https://stepik.org/lesson/1720860/step/4?unit=1744396
# https://kompege.ru/task   № 3693 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 10**6+1, 51):
    if fnmatch(str(n), '12*45*'):
        print(n, n // 51)
"""
122145 2395
122451 2401
124542 2442
124593 2443
127245 2495
"""


# https://stepik.org/lesson/1720860/step/5?unit=1744396
# https://kompege.ru/task   № 4711 Демоверсия 2023 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 10**10+1, 2023):
    if fnmatch(str(n), '1?2139*4'):
        print(n, n // 2023)
"""
162139404 80148
1321399324 653188
1421396214 702618
1521393104 752048
"""







""" 25.4 Задание 25 ЕГЭ | Задачи прошлых лет """
# https://stepik.org/lesson/1720861/step/1?unit=1744397
# https://kompege.ru/task   № 9754 Основная волна 19.06.23 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 10**8, 2023):
    if fnmatch(str(n), '3?1*57'):
        print(n, n // 2023)

# variant
from itertools import product
ls = []
for n in range(4):
    ls.extend([''.join(p) for p in product('0123456789', repeat=n)])
for a in '0123456789':
    for b in ls:
        n = int(f'3{a}1{b}57')
        if not n % 2023:
            print(n, n // 2023)
"""
1234737 8757
12341307 87527
12342717 87537
12344127 87547
12345537 87557
12346947 87567
12348357 87577
12349767 87587
"""


# https://stepik.org/lesson/1720861/step/2?unit=1744397
# https://kompege.ru/task   № 9792 Основная волна 20.06.23 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 10**8, 1923):
    if fnmatch(str(n), '1*2??76'):
        print(n, n // 1923)
"""
10022676 5212
12522576 6512
15022476 7812
17522376 9112
19829976 10312
"""


# https://stepik.org/lesson/1720861/step/3?unit=1744397
# https://kompege.ru/task   № 23763 Демоверсия 2026 (Уровень: Базовый)
# https://kompege.ru/task   № 17879 Демоверсия 2025 (Уровень: Базовый)
# https://kompege.ru/task   № 17536 Основная волна 07.06.24 (Уровень: Средний)
def f(n):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    return sorted(dv)

cnt = 5
for n in range(800_000, 10**9):
    d = f(n)
    if d:
        d = d[0] + d[-1]
        if d % 10 == 4:
            print(n, d)
            cnt -= 1
    if not cnt:
        break
"""
800004 400004
800009 114294
800013 266674
800024 400014
800033 61554
"""


# https://stepik.org/lesson/1720861/step/4?unit=1744397
# https://kompege.ru/task   № 17564 Основная волна 08.06.24 (Уровень: Средний)
def f(n):
    dv = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            dv |= {i, n // i}
    if dv:
        return min(dv) + max(dv)

k = 5
for n in range(700_000, 10**10):
    d = f(n)
    if d and d % 10 == 4:
        print(n, d)
        k -= 1
    if not k:
        break
"""
700004 350004
700009 41194
700023 233344
700024 350014
700044 350024
"""






""""""
""" Варианты """

""""""
""" Варианты """
# 28.1 Вариант 1 | Часть 1
# https://stepik.org/lesson/1729565/step/11?unit=1753394
# https://kompege.ru/task  № 17879 Демоверсия 2025 (Уровень: Базовый)
def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
            return sorted(d)

cnt = 5
for n in range(800_000, 10**10):
    d = f(n)
    if d:
        m = d[0] + d[-1]
        if m % 10 == 4:
            print(n, m)
            cnt -= 1
        if not cnt:
            break
"""
800004 400004
800009 114294
800013 266674
800024 400014
800033 61554
"""



# 29.1 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/11?unit=1753726
# https://kompege.ru/task  № 19255 ЕГКР 21.12.24 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 10**10 + 1, 18579):
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


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730528/step/11?unit=1754357
# https://kompege.ru/task  № 20814 Апробация 05.03.25 (Уровень: Базовый)
def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    return sum(d)

c = 5
for n in range(500_001, 10**10):
    r = f(n)
    if r and r % 10 == 9:
        c -= 1
        print(n, r)
    if not c:
        break
"""
500014 250009
500038 495289
500040 1170359
500054 250029
500058 667289
"""


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/11?unit=1760676
# https://kompege.ru/task  № 21422 Досрочная волна 2025 (Уровень: Базовый)
def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    res = sorted(i for i in d if i % 10 == 7 and i != 7)
    return res

c = 5
for n in range(1_125_001, 10**10):
    d = f(n)
    if d:
        print(n, d[0])
        c -= 1
    if not c:
        break
"""
1125003 467
1125006 97
1125009 17
1125011 3187
1125012 177
"""


# 32.2 Вариант 5 | Часть 2
# https://stepik.org/lesson/1754189/step/11?unit=17786487
# https://kompege.ru/task  № 21718 ЕГКР 19.04.25 (Уровень: Базовый)
from fnmatch import *
for n in range(0, 10**10, 7993):
    if fnmatch(str(n), '4*4736*1'):
        print(n, n // 7993)
"""
44736821 5597
4064736241 508537
4303247361 538377
4347368721 543897
4447361151 556407
4473658121 559697
4794736931 599867
"""


# 33.2 Вариант 6 | Часть 2
# https://stepik.org/lesson/1943171/step/11?unit=1969925 👍
# https://kompege.ru/task  № 23207 Основная волна 10.06.25 (Уровень: Средний)
def dv(n):
    d = set()
    for i in range(2, int(n*0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    return d

def smpl(n):
    for i in range(2, int(n * 0.5 + 1)):
        if not n % i:
            return False
    return True

c = 5
for n in range(1_324_728, 10**10):
    d = [i for i in dv(n) if all([smpl(i), str(i).count('5') == 1])]
    if len(d) in (1, 2):
        if d[0] * d[-1] == n:
            c -= 1
            print(n, max(d))
    if not c:
        break
"""
1324795 264959
1324801 1151
1324903 2543
1325015 265003
1325029 5279
"""


# 34.2 Вариант 7 | Часть 2
# https://stepik.org/lesson/1943174/step/11?unit=1969928
# https://kompege.ru/task  № 23282 Основная волна 11.06.25 (Уровень: Средний)
def smp(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return False
    return True

def dv(n):
    res = set()
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i:
            res |= {i, n // i}
    return res

c = 5
for n in range(5_400_001, 10**10):
    res = [i for i in dv(n) if smp(i)]
    if len(res) >= 2:
        m = res[0] + res[-1]
        if m > 60_000 and str(m) == str(m)[::-1]:
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


# 35.2 Вариант 8 | Часть 2
# https://stepik.org/lesson/1943181/step/11?unit=1969936
# https://kompege.ru/task  № 23569 Пересдача 03.07.25 (Уровень: Средний)
def d(n):
    r = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            r |= {i, n // i}
    return r

def s(n):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            return False
    return True

c = 5
for n in range(6_086_055, 10**10):
    dv = [i for i in d(n) if s(i) and str(i).count('6') == 1]
    if len(dv) in (1,2):
        if dv[0] * dv[-1] == n:
            print(n, max(dv))
            c -= 1
    if not c:
        break
"""
6086089 2467
6086161 3673
6087281 9467
6087317 36451
6087727 2683
"""


# 36.2 Вариант 9 | Часть 2
# https://stepik.org/lesson/1943186/step/11?unit=1969940
# https://kompege.ru/task  № 23763 Демоверсия 2026 (Уровень: Базовый)
def f(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    if not d:
        return 0
    return min(d) + max(d)

c = 5
for n in range(800_000, 10**10):
    d = f(n)
    if d and d % 10 == 4:
        print(n, d)
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


