""" https://kompege.ru/task """
"""
136 303 494 825
1342 2119 2571 4462 4616 5061 5914 6746 7032 7813 8469 9742
10713 11230 11660 12243 16377 17524 17552 17630 17865 19243
20805 20972 21594 23195 23370
"""



# 136 (Уровень: Средний)
from math import ceil, log2
i_cod = ceil(log2(52 + 10)) # 6
cod = ceil(11 * 6 / 8)
num = ceil(7 / 8)
add = 28 - (cod + num)
print(add)  # 18


# 303 Джобс 28.09.2020 (Уровень: Средний)
from math import ceil
cod = ceil(11 * 5 / 8)
num = ceil((5*5 + 10) / 8)
add = 30 - (cod + num)
print(add)  # 18


# 494 Джобс 19.10.2020 (Уровень: Средний)
from math import ceil, log2
n = 6 + 100  # мощность алфавита: команды для коммуникации и указания квадрата
i = ceil(log2(n))  # минимальное число бит на команду
res = ceil(250 * i / 8)
print(res)  # 219


# 825 Джобс 14.12.2020 (Уровень: Сложный)
from math import ceil
I = ceil(50 * 11 / 8) * (12312 // 50) + ceil(12312 % 50 * 11 / 8)
print(ceil(I / 1024))  # 17





# 1342 Danov2101 (Уровень: Сложный) 🌶️
from math import ceil, log2
i1 = ceil(log2(16**3))  # 000-FFF = 4096
I1 = ceil(i1 * 7 / 8)  # i1=12
I2 = ceil(10 * 10 / 8)  # i=10
res = (I1 + I2) * 256 // 1024
print(res)


# 2119 Danov2201 (Уровень: Сложный) 🌶️
from math import ceil, log2
i = ceil(log2(10 + 52))
for n in range(1, 100):
    if ceil(n * i / 8) * 1000 > 4 * 1024:
        print(62**(n - 1))  # 62**5 ->  916132832  кол-во комбинаций
        break


#  2571 (Уровень: Средний)
from math import ceil, log2
p1 = 10 * 5
p2 = ceil(log2(99999))
I = ceil((p1 + p2) / 8) + 13
print(1800 // I)  # 81


# 3169 (Уровень: Средний)
from math import ceil
p1 = 15 * 5
p2 = 14
p = ceil((p1 + p2) / 8)
res = 1600 // (p + 12)
print(res)  # 66


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


# 4616 Основная волна 2022 (Уровень: Базовый)
from math import ceil, log2
I = ceil(294 * ceil(log2(10 + 4550)) / 8)
print(I * 131_072 // 2**10)  # 61184


# 5061 (Уровень: Сложный)
from math import ceil, log2
i = ceil(log2(52 + 11))
for add in range(1, 1000):
    p1 = (ceil(35 * i / 8) + add) * 4
    p2 = (ceil(27 * i / 8) + add) * 5
    if p1 + p2 > 320:
        print(add)
        break


# 5914 (Уровень: Средний)
from math import ceil
p1 = 26 * 5
p2 = 12
res = ceil(38_776 * (p1 + p2) / 2**13)
print(res)  # 673


# 6746 Апробация 10.03.23 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 5000))
res = ceil(318 * i / 8) * 8192
print(res // 1024)  # 4136


# 7032 Danov2303 (Уровень: Сложный) 🌶️
from math import ceil, log2
num = 4
lertter = 2
sex = 1
day = 5
mouth = 4
name = 7
row = 6  # byte (размер записи без поля фамилии в байтах)
for i in range(1, 2000):
    if (6 + i) * 1279 > 10 * 1024:
        surname = i - 1
        print(2**(surname * 8))  # 65536
        break


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


# 9742 Основная волна 19.06.23 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 1500))
res = ceil(105 * i / 8) * 16_384
print(res // 1024)  # 2320




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


# 12243 ЕГКР 16.12.23 (Уровень: Базовый)
from math import ceil, log2
I = ceil(110 * 11 / 8)
print(int(I * 32_768 / 1024))  # 4864


# 16377 ЕГКР 27.04.24 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 4080))
res = ceil(79 * i / 8) * 65_536
print(res // 1024)  # 7616


# 17524 Основная волна 07.06.24 (Уровень: Средний)
from math import ceil, log2
for n in range(1, 1000):
    if ceil(n * 10 / 8) * 862 > 276 * 1024:  # 10 = ceil(log2(10 + 52 + 458))
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


# 17865 Демоверсия 2025 (Уровень: Средний)
from math import ceil, log2
for n in range(1, 1000):
    if ceil(n * 11 / 8) * 2000 > 693 * 1024:  # 2**i >= 1025  --> i = 11
        print(n-1)  # 257
        break


# 19243 ЕГКР 21.12.24 (Уровень: Базовый)
from math import ceil, log2
for i in range(1, 100):
    if ceil(377 * i / 8) * 23155 > 5536 * 2**10:
        print(2**(i-1) + 1)  # 33
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