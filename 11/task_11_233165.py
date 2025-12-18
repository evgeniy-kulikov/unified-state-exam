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


