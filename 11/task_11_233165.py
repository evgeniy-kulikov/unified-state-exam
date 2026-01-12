""""""
"""
Task 11
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 11.1 Задание 11 | Урок 1 """
# https://stepik.org/lesson/1688217/step/3?unit=1711506
# https://kompege.ru/task  	№ 126 (Уровень: Базовый)
from math import log2, ceil
psw = ceil(7 * ceil(log2(12)) / 8)
print((15 + psw) * 150)  # 2850


# https://stepik.org/lesson/1688217/step/4?unit=1711506
# https://kompege.ru/task   № 134 (Уровень: Средний)
from math import log2, ceil
psw = ceil(11 * ceil(log2(26 + 26 + 10)) / 8)
print(1024 // (psw + 13))  # 46


# https://stepik.org/lesson/1688217/step/5?unit=1711506
#  https://kompege.ru/task  № 303 Джобс 28.09.2020 (Уровень: Средний)
from math import log2, ceil
psw = ceil(11 * ceil(log2(15 + 10)) / 8)
cod_1 = 5 * ceil(log2(26))
cod_2 = 3 * ceil(log2(10))
cod = ceil((cod_1 + cod_2) / 8)
print(30 - psw - cod)  # 18


# https://stepik.org/lesson/1688217/step/6?unit=1711506
# https://kompege.ru/task   № 1194 Апробация 27.04 (Уровень: Базовый)
from math import log2, ceil
I = ceil(86 * ceil(log2(250)) / 8)
print(I * 256)  # 22016


# https://stepik.org/lesson/1688217/step/7?unit=1711506
# https://kompege.ru/task   № 1412 (Уровень: Базовый)
psw = 20 * 4 // 8
ip = 4
I = 6 * 2**10 / 192
print(I - ip - psw)  # 18


# https://stepik.org/lesson/1688217/step/8?unit=1711506
# https://kompege.ru/task   № 14***
from math import log2, ceil
I = ceil(101 * ceil(log2(10 + 4090)) / 8) / 2**10
print(I * 2048)  # 330


# https://stepik.org/lesson/1688217/step/9?unit=1711506
# https://kompege.ru/task   № 1366 Джобс 16.05.2021 (Уровень: Базовый)
from math import log2, ceil
for i in range(1, 100):
    if ceil(80 * i / 8) * 1200 > 150 * 2**10:
        print(2**(i-1))  # 4096
        break


# https://stepik.org/lesson/1688217/step/11?unit=1711506
# https://kompege.ru/task  № 17934 (Уровень: Средний)
from math import ceil, log2
ind = ceil(99 * ceil(log2((510 + 10))) / 8)
res = ceil(543 * 1024 / 4322) - ind
print(res)  # 5


# https://stepik.org/lesson/1688217/step/12?unit=1711506
# https://kompege.ru/task  № 17935 (Уровень: Средний)
from math import ceil, log2
ind = ceil(745 * ceil(log2((999 + 10))) / 8)
res = int(311 * 1024 / 312) - ind
print(res * 312)  # 27456




""" 11.2 Задание 11 | Задачи прошлых лет """
# https://stepik.org/lesson/1688218/step/1?unit=1711507
#  https://kompege.ru/task  № 9742 Основная волна 19.06.23 (Уровень: Базовый)
from math import log2, ceil
ind = ceil(105 * ceil(log2(1500 + 10)) / 8)
print(ind * 16_384 / 2**10)  # 2320


# https://stepik.org/lesson/1688218/step/2?unit=1711507
# https://kompege.ru/task   № 9780 Основная волна 20.06.23 (Уровень: Базовый)
from math import log2, ceil
I = ceil(25 * ceil(log2(26)) / 8)
print(I * 35)  # 560


# https://stepik.org/lesson/1688218/step/3?unit=1711507
# https://kompege.ru/task   № 9834 Основная волна 27.06.23 (Уровень: Базовый)
from math import log2, ceil
I = ceil(10 * ceil(log2(52)) / 8)
print(I * 65_536 // 1024)  # 512


# https://stepik.org/lesson/1688218/step/4?unit=1711507
#  https://kompege.ru/task  № 17524 Основная волна 07.06.24 (Уровень: Средний)
from math import log2, ceil
for n in range(1, 1000):
    if ceil(n * ceil(log2(52 + 10 + 458)) / 8) * 862 > 276 * 2**10:
        print(n - 1)  # 261
        break


# https://stepik.org/lesson/1688218/step/5?unit=1711507
# https://kompege.ru/task   № 17552 Основная волна 08.06.24 (Уровень: Сложный)
from math import log2, ceil
for i in range(2, 1000):
 if ceil(261 * i / 8) / 2**20 * 252_500 > 31:
     print(2**(i-1) + 1)
     break


# https://stepik.org/lesson/1688218/step/6?unit=1711507
#  https://kompege.ru/task  № 17630 Основная волна 19.06.24 (Уровень: Средний)
from math import log2, ceil
for n in range(1, 1000):
    if ceil(n * ceil(log2(26 + 10 + 450)) / 8) * 708 > 213 * 2**10:
        print(n)  # 274
        break


# https://stepik.org/lesson/1688218/step/7?unit=1711507
#  https://kompege.ru/task  № 23195 Основная волна 10.06.25 (Уровень: Базовый)
from math import log2, ceil
for i in range(1, 1000):
    if ceil(172 * i / 8) * 356_984 > 54 * 2**20:
        print(2**(i - 1) + 1)  # 129
        break


# https://stepik.org/lesson/1688218/step/8?unit=1711507
# https://kompege.ru/task  № 23270 Основная волна 11.06.25 (Уровень: Базовый)
from math import ceil, log2
for n in range(1000):
    user = ceil(n * ceil(log2((27 + 10))) / 8)
    if user * 3548 > 12 * 1024:
        print(n)  # 5
        break


# https://stepik.org/lesson/1688218/step/9?unit=1711507
# https://kompege.ru/task  № 23370 Резервный день 19.06.25 (Уровень: Базовый)
from math import ceil, log2
for n in range(1000):
    num = ceil(n * ceil(log2((17 + 10))) / 8)
    if num * 7_564_230 > 31 * 2**20:
        print(n)  # 7
        break


# https://stepik.org/lesson/1688218/step/10?unit=1711507
# https://kompege.ru/task  № 23749 Демоверсия 2026 (Уровень: Базовый)
from math import ceil
for i in range(10000):
    if ceil(2783 * i / 8) * 3_845_627 > 11 * 2**30:
        print(2**(i-1) + 1)  # 257
        break





""" Варианты """
# 28.1 Вариант 1 | Часть 1
# https://stepik.org/lesson/1729562/step/12?unit=1753391
#  https://kompege.ru/task  № 17865 Демоверсия 2025 (Уровень: Средний)
from math import *
i = ceil(log2(10 + 52 + 963))
for n in range(1, 1000):
    if ceil(i * n / 8) * 2000 > 693 * 1024:
        print(n-1)  # 257
        break


# 29.1 Вариант 2 | Часть 1
# https://stepik.org/lesson/1729865/step/12?unit=1753692
# https://kompege.ru/task  № 19243 ЕГКР 21.12.24 (Уровень: Базовый)
from math import ceil
for i in range(1, 100):
    if ceil(377 * i / 8) * 23155 > 5536 * 1024:
        print(2**(i-1) + 1)  # 33
        break


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730526/step/12?unit=1754355
# https://kompege.ru/task  № 20805 Апробация 05.03.25 (Уровень: Средний)
for i in range(1, 100):
    if 248 * i * 75_600 / 2**23 > 16:
        print(2**(i-1) + 1)  # 129
        break


# 31.1 Вариант 4 | Часть 1
# https://stepik.org/lesson/1736669/step/12?unit=1760675
# https://kompege.ru/task  № 21410 Досрочная волна 2025 (Уровень: Базовый)
from math import *
for i in range(1, 1000):
    if ceil(257 * i / 8) * 295_740 / 2**20 > 33:
        print(2**(i-1))  # 8
        break


# 32.1 Вариант 5 | Часть 1
# https://stepik.org/lesson/1754188/step/12?unit=1778647
# https://kompege.ru/task  № 21706 ЕГКР 19.04.25 (Уровень: Базовый)
from math import ceil
for i in range(1, 100):
    if ceil(119 * i / 8) * 125_300 / 2**20 > 23:
        print(2**(i-1) + 1)  # 4097
        break


# 33.1 Вариант 6 | Часть 1
# https://stepik.org/lesson/1943170/step/12?unit=1969924
# https://kompege.ru/task  № 23195 Основная волна 10.06.25 (Уровень: Базовый)
from math import ceil
for i in range(1, 100):
    if 356_984 * ceil(172 * i / 8) / 2**20 > 54:
        print(2**(i-1) + 1)  # 129
        break


# 34.1 Вариант 7 | Часть 1
# https://stepik.org/lesson/1943172/step/12?unit=1969926
# https://kompege.ru/task  № 23270 Основная волна 11.06.25 (Уровень: Базовый)
from math import ceil, log2
for n in range(1, 1000):
    I = ceil(n * ceil(log2(10 + 27)) / 8) / 1024
    if I * 3548 > 12:
        print(n)  # 5
        break


# 35.1 Вариант 8 | Часть 1
# https://stepik.org/lesson/1943178/step/12?unit=1969932
# https://kompege.ru/task  № 23557 Пересдача 03.07.25 (Уровень: Базовый)
from math import ceil, log2
for n in range(1, 1000):
    if ceil(n * ceil(log2(52 + 500 + 10)) / 8) * 45_877 / 2**20 > 49:
        print(n)  # 896
        break


# 36.1 Вариант 9 | Часть 1
# https://stepik.org/lesson/1943184/step/12?unit=1969938
# https://kompege.ru/task  № 23749 Демоверсия 2026 (Уровень: Базовый)
from math import ceil
for i in range(1, 1000):
    if ceil(2783 * i / 8) * 3_845_627 >= 11 * 2**30:
        print(2**(i - 1) + 1)  # 257
        # print(i)  # 9
        break

