""""""
"""
Task 14
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165
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


# https://stepik.org/lesson/1695816/step/5?unit=1719169
# https://kompege.ru/task  № 234 (Уровень: Базовый)
cnt = 0
n = 2*27**7 + 3**10 - 9
while n:
    cnt += not n % 3
    n //= 3
print(cnt)  # 13


# https://stepik.org/lesson/1695816/step/8?unit=1719169
# https://kompege.ru/task  № 2235 (Уровень: Средний)
res = set()
n = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338
while n:
    res.add(n % 15)
    n //= 15
print(len(res))  # 10


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



""" 14.2 Задание 14 | Урок 2 """
# https://stepik.org/lesson/1695817/step/3?unit=1719170
# https://kompege.ru/task  	№ 243 (Уровень: Средний)
for n in range(4, 36):
    if int('132', n) + int('13', 8) == int('124', n+1):
        print(n)  # 6

# variant
for n in range(4, 100):
    if 1*n**2 + 3*n + 2 + 11 == 1*(n + 1)**2 + 2 * (n + 1) + 4:
        print(n)  # 6


# https://stepik.org/lesson/1695817/step/9?unit=1719170
# https://kompege.ru/task  	№ 4963 (Уровень: Средний) 686
a = '0123456789abcdefg'
for y in a:
    for x in a[:-2]:
        n = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if not n % 131:
            print(n // 131)  # 686
            exit()



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
