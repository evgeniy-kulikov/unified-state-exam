""""""
"""
Task 11
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165
"""


""" 11.1 Задание 11 | Урок 1 """
# https://stepik.org/lesson/1688217/step/3?unit=1711506
# https://kompege.ru/task  	№ 126 (Уровень: Базовый)
from math import log2, ceil
psw = ceil(7 * ceil(log2(12)) / 8)
print((15 + psw) * 150)  # 2850


# https://stepik.org/lesson/1688217/step/5?unit=1711506
#  https://kompege.ru/task  № 303 Джобс 28.09.2020 (Уровень: Средний)
from math import log2, ceil
psw = ceil(11 * ceil(log2(15 + 10)) / 8)
cod_1 = 5 * ceil(log2(26))
cod_2 = 3 * ceil(log2(10))
cod = ceil((cod_1 + cod_2) / 8)
print(30 - psw - cod)  # 18



""" 11.2 Задание 11 | Задачи прошлых лет """
# https://stepik.org/lesson/1688218/step/1?unit=1711507
#  https://kompege.ru/task  № 9742 Основная волна 19.06.23 (Уровень: Базовый)
from math import log2, ceil
ind = ceil(105 * ceil(log2(1500 + 10)) / 8)
print(ind * 16_384 / 2**10)  # 2320


# https://stepik.org/lesson/1688218/step/4?unit=1711507
#  https://kompege.ru/task  № 17524 Основная волна 07.06.24 (Уровень: Средний)
from math import log2, ceil
for n in range(1, 1000):
    if ceil(n * ceil(log2(52 + 10 + 458)) / 8) * 862 > 276 * 2**10:
        print(n - 1)  # 261
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


