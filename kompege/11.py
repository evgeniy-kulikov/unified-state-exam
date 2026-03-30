""" https://kompege.ru/task """
"""
494
4462 4616 6746 7813 8469 9742 1342
10713 11230 11660 16377 17524 17552 17630
20805 20972 21594 23195 23370
"""


# 494 Джобс 19.10.2020 (Уровень: Средний)
from math import ceil, log2
n = 6 + 100  # мощность алфавита: команды для коммуникации и указания квадрата
i = ceil(log2(n))  # минимальное число бит на команду
res = ceil(250 * i / 8)
print(res)  # 219

# 4462 Джобс 15.06.2022 (Уровень: Базовый)
res = 0
for n in range(1, 1000):
    b = f'{n:b}'[1:]
    if b.count('1') % 2:
        b = '1' + b + '0'
    else:
        b = '10' + b
    r = int(b, 2)
    if r < 450:
        res = max(res, r)
print(res)  # 444


# 9742 Основная волна 19.06.23 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 1500))
res = ceil(105 * i / 8) * 16_384
print(res // 1024)  # 2320


# 4616 Основная волна 2022 (Уровень: Базовый)
from math import ceil, log2
I = ceil(294 * ceil(log2(10 + 4550)) / 8)
print(I * 131_072 // 2**10)  # 61184


# 6746 Апробация 10.03.23 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 5000))
res = ceil(318 * i / 8) * 8192
print(res // 1024)  # 4136


# 7813 (Уровень: Базовый)
from math import ceil, log2
I = ceil(310 * ceil(log2(10 + 2042)) / 8) + 14
print(I * 65_536 // 2**10)  # 30656


# 8469 (Уровень: Базовый)
from math import ceil
i = 5
for add in range(1, 100):
    if ceil((33 * i) / 8 + add) * 768 > 21 * 2**10:
        print(add - 1)  # 7
        break

# 1342 Danov2101 (Уровень: Сложный) 🌶️
from math import ceil, log2
i1 = ceil(log2(16**3))  # 000-FFF = 4096
I1 = ceil(i1 * 7 / 8)  # i1=12
I2 = ceil(10 * 10 / 8)  # i=10
res = (I1 + I2) * 256 // 1024
print(res)


# 10713 (Уровень: Средний)
from math import ceil
r = ceil((4 * 4 + 3 * 3) / 8) * 500
print(r)  # 2000


# 11230 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(2 + 17))  # 5
I = (ceil(17 * i / 8) + 485) * 4096
print(I // 1024)  # 1984


# 11660 (Уровень: Базовый)
from math import ceil, log2
psw = ceil(35 * ceil(log2(10 + 4090)) / 8)
add = 96000 / 300 - psw
print(int(add))  # 263


# 16377 ЕГКР 27.04.24 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 4080))
res = ceil(79 * i / 8) * 65_536
print(res // 1024)  # 7616


# 17524 Основная волна 07.06.24 (Уровень: Средний)
from math import ceil, log2
for n in range(1, 1000):
    if ceil(n * ceil(log2(10 + 52 + 458)) / 8) * 862 > 276 * 2**10:
        print(n - 1)  # 261
        break


# 17552 Основная волна 08.06.24 (Уровень: Сложный)
from math import ceil, log2
for i in range(1, 100):
    if ceil(261 * i / 8) * 252_500 > 31 * 2**20:
        print(2**(i-1) + 1)  # 9
        break


# 17630 Основная волна 19.06.24 (Уровень: Средний)
from math import log2, ceil
for n in range(1, 1000):
    if ceil(n * ceil(log2(10 + 26 + 450)) / 8) * 708 > 213 * 1024:
        print(n)  # 274
        break



# 20805 Апробация 05.03.25 (Уровень: Средний)
from math import ceil
for i in range(2, 100):
    if ceil(248 * i / 8) * 75_600 > 16 * 2**20:
        print(2**(i - 1) + 1)  # 129
        break


# 20972 (Уровень: Средний) 👍
from math import ceil
for i in range(2, 100):
    if ceil(21 * i / 8) * 1300 > 25 * 1024:
        print(2**(i - 1) - 33 * 2)  # 62 ✔️
        break


# 21594 (Уровень: Средний)
from math import ceil, log2
i = ceil(log2(10 + 32_724))
I = ceil(223 * i / 8) / 2**30
# print(17 // I)  # 43564704.0
print(int(17 / I))  # 43564704


# 23195 Основная волна 10.06.25 (Уровень: Базовый)
from math import ceil
for i in range(1, 100):
    if ceil(172 * i / 8) * 356_984 > 54 * 2**20:
        print(2**(i - 1) + 1)  # 129
        break


# 23370 Резервный день 19.06.25 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 17))  # 5
for n in range(1, 100):
    if ceil((n * i) / 8) * 7_564_230 > 31 * 2**20:
        print(n)  # 7
        break