""" https://kompege.ru/task """
"""
926 5240 5632
8002 8370 8425 8675 8951 9918
11663 12468 12923 17527 17555 17633 18168 19246
24629 25353 27298
"""



# 926 Джобс 08.02.2021 (Уровень: Сложный) 🌶️
n = 7**500 + 7**200 - 7**50
for i in range(1000, 0, -1):
    if int('6' * i, 7) < n:
        print(6 * i) # 3000   сумма разрядов
        # print(i)   # 500   число разрядов
        break


# 5240 (Уровень: Средний)
# from string import printable as alf
# [print(alf.index(i)) for i in 'xyz']   # 33 34 35
res = []
for a in range(55):
    n1 = 35*55**3 + a*55**2 + 34*55**1 + 33*55**0
    n2 = 2*55**3 + 33*55**2 + a*55**1 + 34*55**0
    if not (n1 - n2) % 29:
        res.append((a, n1 - n2))
print(abs(max(res)[1] - min(res)[1]))  # 86130


# 5632 (Уровень: Средний)
from string import printable as alf
def f(x, y):
    a = int(f'32{y}{x}a', 21)
    b = int(f'16{y}18', 21)
    return a + b

for x in alf[:21]:
    if all(not f(x,y) % 12 for y in alf[1:21:2]):
        # print(x)  # 3
        print(f(x, 7) // 12)  # 71524
        break

# variant
def f(x, y):
    a = 3*21**4 + 2*21**3 + y*21**2 + x*21**1 + 10*21**0
    b = 1*21**4 + 6*21**3 + y*21**2 + 1*21**1 + 8*21**0
    return a + b

for x in range(21):
    if all(not f(x,y) % 12 for y in range(1, 21, 2)):
        # print(x) # 3
        print(f(x, 7) // 12)  # 71524
        break



# 8002 (Уровень: Базовый)
a = '0123456789abcdefgh'
for i in a[::-1]:
    n = int(f'77968{i}11', 18) + int(f'4{i}213', 18)
    if not n % 7:
        print(n // 7)  # 648833380
        break


# 8370 Danov2305 (Уровень: Средний)
for p in range(5, 100):
    for q in range(6, 100):
        left = 2*p**2 + 3*p + 4
        right = 3*q**2 + 4*q + 5
        if left == right:
            print(left)  # 564
            # print(p, q)  # 16 13
            exit()



# 8425 (Уровень: Средний)
for p in range(5, 1000):
    for y in range(p):
        for x in range(p):
            if (3*p + 2) * (p + 4) == x*p**2 + y*p + 2:
                print(y*p + x)  # 23


# 8675 (Уровень: Базовый)
for x in '0123456789abcdef'[::-1]:
    n = int(f'1f3b{x}75', 16) +  int(f'5d{x}3b', 16)
    if not n % 11:
        print(n // 11)  # 3012112
        break


# 8951 Джобс 02.06.2023 (Уровень: Базовый)
for n in range(6, 36):
    # r = 7**500 - int('53', n)
    r = 7**500 - 5*n + 3
    if not r % 6:
        print(n)
        break


# 9918 (Уровень: Сложный)
# Арифметика и Комбинаторика
print((10 + 66) // 2 * 57)  # 2166

c = 0
for x in range(10, 67):
    for y in range(x):
        c += 1
print(c)  # 2166

R = set()
for x in range(10, 67):
    for y in range(x):
        R.add((y + 1*67**1 + x*67**2 + 3*67**3 + 7*67**4) + (6 + y*x + 9*x**2 + 4*x**3))
print(len(set(R)))  # 2166




# 11663 (Уровень: Базовый)
from string import ascii_lowercase as alf
alf = '0123456789' + alf[:17]
for x in alf[::-1]:
    res = int(f'17{x}35', 27) + int(f'{x}742m', 27) + int(f'{x}', 27)**3
    if not res % 23:
        print(res // 23)  # 127775
        break


# 12468 (Уровень: Базовый)
alf = '0123456789abcdefghi'
for x in alf:
    n = int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)
    if not n % 18:
        print(n // 18)  # 368599039
        break


# 12923 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
n = 3*3125**9 + 2*625**8 - 4*625**7 + 3*125**6 - 2*25**5 - 2024
c = 0
while n:
    c += not n % 25
    n //= 25
print(c)  # 9


# 17527 Основная волна 07.06.24 (Уровень: Базовый)
for x in range(2030, 0, -1):
    n = 3**100 - x
    c = 0
    while n:
        c += not n % 3
        n //= 3
    if c == 5:
        print(x)  # 2024
        break


# 17555 Основная волна 08.06.24 (Уровень: Базовый)
for x in range(2030, 0, -1):
    n = 7**91 + 7**160 - x
    c = 0
    while n:
        c += not n % 7
        n //= 7
    if c == 70:
        print(x)  # 2029
        break


# 17633 Основная волна 19.06.24 (Уровень: Базовый)
for x in range(1000):
    n = 6**260 + 6**160 + 6**60 - x
    c = 0
    while n:
        c += not n % 6
        n //= 6
    if c == 202:
        print(x)  # 216
        break


# 18168 (Уровень: Сложный) 🌶️
# очень долго
res = []
d = 5**2025 + 5**400
# len(str(d)) # 1416
for x in range(70000, 60000, -1):
    c = 0
    n = d - x
    while n:
        c += n % 5 == 4
        n //= 5
    res.append((c, x))
print(max(res)[1]) # (399, 62501) (398, 59376) (399, 46876)
# 62501


# 19246 ЕГКР 21.12.24 (Уровень: Базовый)
from string import printable as alf
for x in alf[:25][::-1]:
    num = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if not num % 24:
        print(num // 24)  # 266249847
        break




# 24629 (Уровень: Базовый)
n = 14**1402 + 28**501 - 14**51 - 1400
c = 0
while n:
    c += n % 14 == 13  # D
    n //= 14
print(c)  # 511


# 25353 ЕГКР 13.12.25 (Уровень: Базовый)
for x in range(1, 27_000):
    c = 0
    n = 3 * 27**9 + 2 * 27**6 + 27**3 - x
    while n:
        c += not n % 27
        n //= 27
    if c == 6:
        print(x)  # 27
        break


# 27298 (Уровень: Средний)
for x in range(40):
    a = 8*40**6 + 7*40**5 + 1*40**4 + x*40**3 + 2*40**2 + 9*40**1 + 1*40**0
    b = 3*40**6 + 6*40**5 + 6*40**4 + x*40**3 + 6*40**2 + 3*40**1 + 1*40**0
    c = 9*40**6 + 7*40**5 + 3*40**4 + x*40**3 + 6*40**2 + 1*40**1 + 8*40**0
    res = a + b + c
    if not res % 39:
        # print(x)  # 10
        print(res // 13)  # 6461195610
        break

# перевод в десятичную СС из другой СС (если ее база больше 36)
def cnv(ls:list, b):
    r = sum(int(n) * b**i for i, n in enumerate(ls[::-1]))
    return r

for x in range(40):
    a = f'8 7 1 {x} 2 9 1'.split()
    b = f'3 6 6 {x} 6 3 1'.split()
    c = f'9 7 3 {x} 6 1 8'.split()
    res = cnv(a, 40) + cnv(b, 40) + cnv(c, 40)
    if not res % 39:
        print(res // 13)  # 6461195610
        break