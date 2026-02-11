""" https://kompege.ru/task """
"""
9918
11663 12468 12923 17555 
"""


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