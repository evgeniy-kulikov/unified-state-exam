""" https://kompege.ru/task """
"""
6985
8002 8370 8417 8425 8675 8951 9918
11663 12468 12923 17527 17555 17627 17633
"""



# 6985 (Уровень: Средний)
from itertools import product
c = 0
res = None
for p in product('aklmpc', repeat=6):
    c += 1
    r = ''.join(p)
    if not any(['kc' in r, 'ck' in r]) and len(set(r)) == 4:
        res = c
print(res)  # 46605




# 8002 (Уровень: Базовый)
a = '0123456789abcdefgh'
for i in a[::-1]:
    n = int(f'77968{i}11', 18) + int(f'4{i}213', 18)
    if not n % 7:
        print(n // 7)  # 648833380
        break


# 8370 Danov2305 (Уровень: Средний)
for p in range(5, 1000):
    for q in range(6, 1000):
        if 2*p**2 + 3*p + 4 == 3*q**2 + 4*q + 5:
            print(2*p**2 + 3*p + 4)  # 564
            exit()


# 8417 (Уровень: Базовый)
from itertools import permutations
c = 0
for p in permutations('aaassss', 5):
    c += p.count('s') > p.count('a') and 'aa' not in ''.join(p)
print(c)  # 1224


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


# 17627 Основная волна 19.06.24 (Уровень: Базовый)
from itertools import product
c = 0
for p in product('0123456789aaaaa', repeat=5):
    c += p[0] != '0' and p.count('8') == 1 and p.count('a') >= 2
print(c)  # 83175


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


