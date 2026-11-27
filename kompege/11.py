""" https://kompege.ru/task """
"""
136 303 494 6264  825
1342 2119 2571 2857 3100 3169 4462 4616 5061 5914 6083 6746 7032 7261 7813 8469 8556 9742
10713 11230 11660 12243 16322 16377 17524 17552 17630 17865 19243
20805 20972 21594 23195 23370 29071 29073 29343 
31118
"""



# 136 (Уровень: Средний)
from math import ceil, log2
i_cod = ceil(log2(52 + 10)) # 6
cod = ceil(11 * 6 / 8)
num = ceil(7 / 8)
add = 28 - (cod + num)
print(add)  # 18


""" Взято на мой курс """
# 303 Джобс 28.09.2020 (Уровень: Средний)
from math import ceil, log2
# cod_user = ceil(11 * ceil(log2(15 + 10)) / 8)
# cod_1 = 5 * ceil(log2(26))
# cod_2 = 3 * ceil(log2(10))
cod_user = ceil(11 * 5 / 8)
cod_1 = 5 * 5
cod_2 = 3 * 4
cod = ceil((cod_1 + cod_2) / 8)
print(30 - cod_user - cod)  # 18


# 494 Джобс 19.10.2020 (Уровень: Средний)
from math import ceil, log2
n = 6 + 100  # мощность алфавита: команды для коммуникации и указания квадрата
i = ceil(log2(n))  # минимальное число бит на команду
res = ceil(250 * i / 8)
print(res)  # 219



# 6264 Danov2302(Уровень: Сложный) 🌶️
# месяц и день как разные поля
from math import ceil
id_1 = ceil(4 / 8)  # class
id_2 = ceil(3 / 8)  # letter
id_3 = ceil(1 / 8)  # sex
id_4 = ceil(5 / 8)  # day
id_5 = ceil(4 / 8)  # month
id_6 = ceil(7 / 8)  # name
id_7 = ceil(10 / 8)  # surname
I_byte = (id_1 + id_2 + id_3 + id_4 + id_5 + id_6 + id_7)  # 8 byte
I_bit = ceil((4 + 3 + 1 + 5 + 4 + 7 + 10) / 8)  # 5 byte
print((I_byte - I_bit) * 1347)  # 4041

# месяц и день как одно поле
from math import ceil
id_1 = ceil(4 / 8)  # class
id_2 = ceil(3 / 8)  # letter
id_3 = ceil(1 / 8)  # sex
id_4 = ceil(4 * 4 / 8)  #   # day+month  -> 4 десятичные цифры
id_5 = ceil(7 / 8)  # name
id_6 = ceil(10 / 8)  # surname
I_byte = (id_1 + id_2 + id_3 + id_4 + id_5 + id_6) # 8 byte
# день и месяц  ->  31 * 12 = 372 варианта  ->  2**8
I_bit = ceil((4 + 3 + 1 + 8 + 7 + 10) / 8)  # 5 byte
print((I_byte - I_bit) * 1347)  # 4041


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


""" Взято на мой курс """
# 2857 Статград 08.02.2022(Уровень: Средний)
from math import ceil, log2
cod_1 = 1 * 3
cod_2 = 11 * 5
cod_3 = 1 * 11
cod = ceil((cod_1 + cod_2 + cod_3) / 8)
# (cod + add) * 36 = 1188
add = 1188 / 36 - cod
print(add)  # 24


# 3100 (Уровень: Базовый)
from math import ceil, log2
# (ceil(11 * 4 / 8) + add) * 50 = 700
add = 700 / 50 - ceil(11 * 4 / 8)
print(add)  # 8


""" Взято на мой курс """
# 3169 (Уровень: Средний)
from math import ceil, log2
id_1 = 15 * 5
id_2 = 1 * ceil(log2(9999))
I = ceil((id_1 + id_2) / 8) + 12
print(1600 // I)  # 66


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


# 6083 (Уровень: Базовый)
from math import ceil
# (ceil(196 * 11 / 8) + add) * 2048 = 604*1024
add = 604*1024 / 2048 - ceil(196 * 11 / 8)
print(add)  # 32


# 6746 Апробация 10.03.13_(23) (Уровень: Базовый)
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


# 7261 OpenFIPI(Уровень: Базовый)
from math import ceil, log2
# (ceil(25 * 3 / 8) + add) * 200 = 4_800
add = 4_800 / 200 - ceil(25 * 3 / 8)
print(add)  # 14



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


""" Взято на мой курс """
# 9064 Danov2306(Уровень: Базовый)
from math import ceil, log2
# (ceil(29 * 4 / 8) + add) * 279 = 14_508
add = 14_508 / 279 - ceil(29 * 4 / 8)
print(add)  # 37



# 8556 (Уровень: Базовый)
from math import ceil, log2
I = ceil(116 * 7 / 8) * 301_504
print(ceil(I / 2**20))  # 30


# 9742 Основная волна 19.06.13_(23) (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 1500))
res = ceil(105 * i / 8) * 16_384
print(res // 1024)  # 2320




# 10713 (Уровень: Средний)
from math import ceil
r = ceil((4 * 4 + 3 * 3) / 8) * 500
print(r)  # 2000


""" Взято на мой курс """
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


# 12243 ЕГКР 16.12.13_(23) (Уровень: Базовый)
from math import ceil, log2
I = ceil(110 * 11 / 8)
print(int(I * 32_768 / 1024))  # 4864


# 16322 Открытый вариант 2024(Уровень: Базовый)
from math import ceil, log2
I = ceil(317 * ceil(log2(10 + 4090)) / 8) * 262_144
print(I / 2**20)  # 129


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


""" Взято на мой курс """
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


""" Взято на мой курс """
# 20972 (Уровень: Средний) 👍
from math import ceil
for i in range(2, 100):
    if ceil(21 * i / 8) * 1300 > 25 * 1024:
        print(2**(i - 1) - 33 * 2)  # 62 ✔️
        break



""" Взято на мой курс """
# 21594 (Уровень: Средний)
from math import ceil, log2
I = ceil(223 * ceil(log2(10 + 26 + 32_724)) / 8)
n = 17 * 2**30 // I
print(n)  # 43564704



# 23195 Основная волна 10.06.25 (Уровень: Базовый)
from math import ceil
for i in range(1, 100):
    if ceil(172 * i / 8) * 356_984 > 54 * 2**20:
        print(2**(i - 1) + 1)  # 129
        break


""" Взято на мой курс """
# 23370 Резервный день 19.06.25 (Уровень: Базовый)
from math import ceil, log2
i = ceil(log2(10 + 17))  # 5
for n in range(1, 100):
    if ceil((n * i) / 8) * 7_564_230 > 31 * 2**20:
        print(n)  # 7
        break


# 29071 (Уровень: Средний)
from math import ceil, log2
for i in range(1, 100):
    x = ceil(11 * i / 8) * 1024
    y = ceil(13 * i / 8) * 256
    if x + y == 22 * 1024:
        print(2**i)  # 4096
        break


# 29073 (Уровень: Средний)
# Порядковый номер записи (от 0 до 65535) нужно представить в виде двоичного числа.
# Для числа из 65536 вариантов минимально необходимая длина: ceil(log2(65_536)) ->  16 бит ✅
from math import ceil, log2
code = ceil(log2(65_536))  # 16
for l in range(1, 10000):
    if ceil((code + l * 5) / 8) * 65_536 == 60_096 * 1024:
        print(l)  # 1498
        break



# 29343 Открытый вариант 2026(Уровень: Базовый)
from math import ceil, log2
I = ceil(257 * ceil(log2(17 + 4080)) / 8)
print(I * 8_388_608 // 2**20)



# 31118 Основная волна 18.06.26(Уровень: Базовый)
from math import ceil, log2
for i in range(1, 100):
    if ceil(172 * i / 8) * 187_564 > 39 * 2**20:
        print(2**(i-1))  # 1024
        break

