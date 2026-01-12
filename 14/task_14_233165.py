""""""
"""
Task 14
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""

""" 14.1 Задание 14 | Урок 1 """
# https://stepik.org/lesson/1695816/step/3?unit=1719169
# https://kompege.ru/task  № 58 Джобс 31.08.2020 (Уровень: Базовый)
cnt = 0
n = 64**30 + 2**300 - 4
while n:
    cnt += n % 8 == 7
    n //= 8
print(cnt)  # 59

# variant
n = 64**30 + 2**300 - 4
print(oct(n).count('7'))  # 59


# https://stepik.org/lesson/1695816/step/4?unit=1719169
# https://kompege.ru/task   № 233 (Уровень: Базовый)
n = 3 * 16**8 - 4**5 + 3
cnt = 0
while n:
    cnt += n % 4 == 3
    n //= 4
print(cnt)  # 12


# https://stepik.org/lesson/1695816/step/5?unit=1719169
# https://kompege.ru/task  № 234 (Уровень: Базовый)
cnt = 0
n = 2*27**7 + 3**10 - 9
while n:
    cnt += not n % 3
    n //= 3
print(cnt)  # 13


# https://stepik.org/lesson/1695816/step/6?unit=1719169
# https://kompege.ru/task   № 387 (Уровень: Базовый)
n = 51 * 7**12 - 7**3 - 22
cnt = 0
while n:
    cnt += n % 7
    n //= 7
print(cnt)  # 70


# https://stepik.org/lesson/1695816/step/7?unit=1719169
# https://kompege.ru/task   № 1071 (Уровень: Средний)

for i in range(1, 1000):
    n = 125**200 - 5**i + 74
    cnt = 0
    while n:
        cnt += (n % 5 == 4)
        n //= 5
    if cnt == 100:
        print(i)  # 502
        break


# https://stepik.org/lesson/1695816/step/8?unit=1719169
# https://kompege.ru/task  № 2235 (Уровень: Средний)
res = set()
n = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338
while n:
    res.add(n % 15)
    n //= 15
print(len(res))  # 10


# https://stepik.org/lesson/1695816/step/9?unit=1719169
# https://kompege.ru/task   № 12923 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
cnt = 0
while n:
    cnt += not n % 25
    n //= 25
print(cnt)  # 9


# https://stepik.org/lesson/1695816/step/10?unit=1719169
# https://kompege.ru/task   № 2033 (Уровень: Базовый)
n = 6*144**26 + 11*12**75 - 48
cnt = 0
while n:
    cnt += n % 12 == 11
    n //= 12
print(cnt)  # 51


# https://stepik.org/lesson/1695816/step/11?unit=1719169
# https://kompege.ru/task  № 1122 (Уровень: Средний)
for x in range(100):
    n = 36**17 - 6**x + 71
    b = ''
    while n:
        b += str(n % 6)
        n //= 6
    if sum(map(int, b)) == 61:
        print(x)  # 24
        break

# variant
for x in range(100):
    n = 36**17 - 6**x + 71
    b = []
    while n:
        b.append(n % 6)
        n //= 6
    if sum(b) == 61:
        print(x)  # 24
        break


# https://stepik.org/lesson/1695816/step/12?unit=1719169
# https://kompege.ru/task   № 1222 Апробация 27.04 (Уровень: Базовый)
n = 5*216**1156 - 4*36**1147 + 6**1153 - 875
cnt = 0
while n:
    cnt += n % 6 == 5
    cnt -= not n % 6
    n //= 6
print(cnt)  # 1182




""" 14.2 Задание 14 | Урок 2 """
# https://stepik.org/lesson/1695817/step/1?unit=1719170
# https://kompege.ru/task   № 241 (Уровень: Базовый)
for x in range(2, 33):
    if int('33', x + 4) - int('33', 4) == 10:
        print(x)  # 11

# https://stepik.org/lesson/1695817/step/2?unit=1719170
# https://kompege.ru/task   № 242 (Уровень: Средний)
for n in range(8, 35):
    if int('103', n) == int('97', n + 2):
        print(n)  # 11


# https://stepik.org/lesson/1695817/step/3?unit=1719170
# https://kompege.ru/task  	№ 243 (Уровень: Средний)
for n in range(4, 36):
    if int('132', n) + int('13', 8) == int('124', n+1):
        print(n)  # 6

# variant
for n in range(4, 100):
    if 1*n**2 + 3*n + 2 + 11 == 1*(n + 1)**2 + 2 * (n + 1) + 4:
        print(n)  # 6


# https://stepik.org/lesson/1695817/step/4?unit=1719170
# https://kompege.ru/task   № 256 (Уровень: Средний)
def conv(n, b):
    r = ''
    while n:
        r = str(n % b) + r
        n //= b
    return r

for n in range(1, 100):
    a = len(conv(n, 6)) == 2
    b = len(conv(n, 5)) == 3
    c = conv(n, 11)[-1] == '1'
    if a and b and c:
        print(n)  # 34


# https://stepik.org/lesson/1695817/step/5?unit=1719170
# https://kompege.ru/task  № 385 (Уровень: Средний)
a = int('10000', 2)
b = int('4444', 5) + 1
c = 0
for n in range(a, b):
    c += hex(n)[-1] == 'c'
print(c)  # 38


# https://stepik.org/lesson/1695817/step/6?unit=1719170
# https://kompege.ru/task  № 4702 Демоверсия 2023 (Уровень: Средний)

for n in '0123456789abcde':
    r = int(f'123{n}5', 15) + int(f'1{n}233', 15)
    if not r % 14:
        print(r // 14)  # 8767
        break


# https://stepik.org/lesson/1695817/step/7?unit=1719170
# https://kompege.ru/task  № 4961 (Уровень: Средний)
for n in '0123456789abcdefg':
    r = int(f'9759{n}', 17) + int(f'3{n}108', 17)
    if not r % 11:
        print(r // 11)  # 95306
        break


# https://stepik.org/lesson/1695817/step/8?unit=1719170
# https://kompege.ru/task  № 4962 (Уровень: Средний)
for n in '0123456789a':
    r = int(f'3364{n}', 11) + int(f'{n}7946', 12) == int(f'55{n}87', 14)
    if r:
        print(int(f'55{n}87', 14))  # 207291
        break


# https://stepik.org/lesson/1695817/step/9?unit=1719170
# https://kompege.ru/task  	№ 4963 (Уровень: Средний) 686
a = '0123456789abcdefg'
for y in a:
    for x in a[:-2]:
        n = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if not n % 131:
            print(n // 131)  # 686
            exit()


# https://stepik.org/lesson/1695817/step/10?unit=1719170
# https://kompege.ru/task  № 4964 (Уровень: Средний)
from string import ascii_lowercase as st
alf = '0123456789' + st[:11]
for x in alf:
    if all(not (int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)) % 18 for y in alf):
        print((int(f'125{x}9', 21) + int(f'36599', 21)) // 18)  # 47594
        break





""" 14.3 Задание 14 | Задачи прошлых лет """
# https://stepik.org/lesson/1695818/step/1?unit=1719171
# https://kompege.ru/task   № 9745 Основная волна 19.06.23 (Уровень: Базовый)
# a = [*'0123456789'] + [*map(chr, range(97, 106))]
a = '0123456789abcdefghi'[::-1]
for x in a:
    n = int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
    if not n % 18:
        print(n // 18)  # 470402599
        break


# https://stepik.org/lesson/1695818/step/2?unit=1719171
# https://kompege.ru/task  № 9783 Основная волна 20.06.23 (Уровень: Базовый)
from string import ascii_lowercase as st
alf = '0123456789' + st[:12]
for x in alf:
    res = int(f'18{x}89957', 22) + int(f'80{x}33', 22) + int(f'521{x}6', 22)
    if not res % 21:
        print(res // 21)  # 162947670
        break


# https://stepik.org/lesson/1695818/step/3?unit=1719171
# https://kompege.ru/task  № 9837 Основная волна 27.06.23 (Уровень: Базовый)
from string import ascii_lowercase as st
alf = '0123456789' + st[:13]
for x in alf:
    res = int(f'7{x}38596', 23) + int(f'14{x}36', 23) + int(f'61{x}7', 23)
    if not res % 22:
        print(res // 22)  # 47163321
        break


# https://stepik.org/lesson/1695818/step/4?unit=1719171
# https://kompege.ru/task  № 17527 Основная волна 07.06.24 (Уровень: Базовый)
for x in range(2030, 0, -1):
    r = 3**10 - x
    c = 0
    while r:
        c += not r % 3
        r //= 3
    if c == 5:
        print(x)  # 2024
        break


# https://stepik.org/lesson/1695818/step/5?unit=1719171
# https://kompege.ru/task  № 17555 Основная волна 08.06.24 (Уровень: Базовый)
for x in range(2030, 0, -1):
    r = 7**91 + 7**160 - x
    c = 0
    while r:
        c += not r % 7
        r //= 7
    if c == 70:
        print(x)  # 2029
        break


# https://stepik.org/lesson/1695818/step/6?unit=1719171
# https://kompege.ru/task  № 17633 Основная волна 19.06.24 (Уровень: Базовый)
for x in range(2031):
    r = 6**260 + 6**160 + 6**60 - x
    c = 0
    while r:
        c += not r % 6
        r //= 6
    if c == 202:
        print(x)  # 216
        break


# https://stepik.org/lesson/1695818/step/7?unit=1719171
# https://kompege.ru/task  № 23198 Основная волна 10.06.25 (Уровень: Базовый)
for x in range(3001):
    r = 9**150 + 9**30 - x
    c = 0
    while r:
        c += not r % 9
        r //= 9
    if c == 122:
        print(x)  # 81
        break


# https://stepik.org/lesson/1695818/step/8?unit=1719171
# https://kompege.ru/task   № 23273 Основная волна 11.06.25 (Уровень: Базовый)
a = [*'0123456789'] + [*map(chr, range(97, 97+19))]
for x in a:
    n = int(f'463{x}7921', 29) + int(f'8241{x}153', 29)
    if not n % 28:
        print(n // 28)  # 7567913105
        break

# variant
# Перевод в СС с основанием больше 36
# a: list - состав конвертируемого числа [2, 9, 0, 1]
# b: int - основание
def conv(a: list, b: int):
    a = a[::-1]
    r = 0
    for i in range(len(a)):
        r += a[i] * b**i
    return r

for x in range(29):
    n = conv([4,6,3,x,7,9,2,1], 29) + conv([8,2,4,1,x,1,5,3], 29)
    if not n % 28:
        print(n // 28)  # 7567913105
        break


# https://stepik.org/lesson/1695818/step/9?unit=1719171
# https://kompege.ru/task   № 23373 Резервный день 19.06.25 (Уровень: Базовый)
n = 2*2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35
cnt = 0
while n:
    cnt += n % 49 <= 9
    n //= 49
print(cnt)  # 267



# https://stepik.org/lesson/1695818/step/10?unit=1719171
# https://kompege.ru/task   № 23753 Демоверсия 2026 (Уровень: Базовый)
def c(ls):
    ls = ls[::-1]
    r = 0
    for i in range(len(ls)):
        r += ls[i] * 29**i
    return r

for x in range(28, 1, -1):
    n = c([9, 2, 3, x, 8, 7, 4]) + c([5, 2, 4, x, 6, 1, 5, 2])
    if not n % 28:
        print(n // 28)  # 3319197720
        break




""""""
""" Варианты """
# 28.1 Вариант 1 | Часть 1
# https://stepik.org/lesson/1729565/step/2?unit=1753394
#  https://kompege.ru/task  № 17868 Демоверсия 2025 (Уровень: Базовый)

for x in '0123456789abcdefghi'[::-1]:
    n = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if not n % 18:
        print(n // 18)  # 469034148
        break

# 29.1 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/2?unit=1753726
# https://kompege.ru/task  № 19246 ЕГКР 21.12.24 (Уровень: Базовый)
from string import ascii_lowercase as s
a = '0123456789' + s[:15]
for i in a[::-1]:
    res = int(f'11353{i}12', 25) + int(f'135{i}21', 25)
    if not res % 24:
        print(res // 24)  # 266249847
        break


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730528/step/2?unit=1754357
# https://kompege.ru/task  № 20808 Апробация 05.03.25 (Уровень: Средний)
def f(n):
    s = 0
    while n:
        s += not n % 7
        n //= 7
    return s

zero = 0
res = 0
for x in range(2030, 0, -1):
    n = 7**170 + 7**100 - x
    tr = f(n)
    if tr > zero:
        zero = tr
        res = x
print(res)  # 1715

#  variant
zero = 0
res = 0
for x in range(1, 2031):
    n = 7**170 + 7**100 - x
    tr = f(n)
    if tr >= zero:  # >=   очень важно!!!
        zero = tr
        res = x
print(res)  # 1715


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/2?unit=1760676
# https://kompege.ru/task  № 21413 Досрочная волна 2025 (Уровень: Базовый)
from string import ascii_lowercase as alf
for x in '0123456789' + alf[:11]:
    n = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
    if not n % 20:
        print(n // 20)  # 72450445
        break


# 32.2 Вариант 5 | Часть 2
# https://stepik.org/lesson/1754189/step/2?unit=17786487
# https://kompege.ru/task  № 21709 ЕГКР 19.04.25 (Уровень: Базовый)
def f(n):
    s = 0
    while(n):
        s += not n % 4
        n //= 4
    return s

res = 0
z = 0
for x in range(1, 3_000):
    n = 4**210 + 4**110 - x
    if f(n) > z:
        z = f(n)
        res = x
print(res)  # 1024


# 33.2 Вариант 6 | Часть 2
# https://stepik.org/lesson/1943171/step/2?unit=1969925
# https://kompege.ru/task  № 23198 Основная волна 10.06.25 (Уровень: Базовый)
def f(n):
    c = 0
    while n:
        c += not n % 9
        n //= 9
    return c

for x in range(1, 3000):
    n = 9**150 + 9**30 - x
    if f(n) == 122:
        print(x)  # 81
        break


# 34.2 Вариант 7 | Часть 2
# https://stepik.org/lesson/1943174/step/2?unit=1969928
# https://kompege.ru/task  № 23273 Основная волна 11.06.25 (Уровень: Базовый)
from string import ascii_lowercase as ascii
alf = '0123456789' + ascii[:19]
for x in alf:
    n = int(f'463{x}7921', 29) + int(f'8241{x}153', 29)
    if not n % 28:
        print(n // 28)
        break


# 35.2 Вариант 8 | Часть 2
# https://stepik.org/lesson/1943181/step/2?unit=1969936
# https://kompege.ru/task  № 23560 Пересдача 03.07.25 (Уровень: Базовый)
def f(n):
    c = 0
    while n:
        c += not n % 9
        n //= 9
    return c

for x in range(2400,0,-1):
    n = 7*9**210 + 6*9**110 - x
    if f(n) == 100:
        print(x)  # 2394
        break


# 36.2 Вариант 9 | Часть 2
# https://stepik.org/lesson/1943186/step/2?unit=1969940
# https://kompege.ru/task  № 23752 Демоверсия 2026 (Уровень: Базовый)
n = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
cnt = 0
while n:
    if n % 27 > 9:
        cnt += 1
    n //= 27
print(cnt)  # 3367

