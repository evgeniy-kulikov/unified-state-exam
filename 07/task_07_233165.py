""""""
"""
Task 07
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 7.1 Задание 7 | Урок 1 """
# https://stepik.org/lesson/1650993/step/3?unit=1673695
from math import log2, ceil
I = ceil(64 * 128 * ceil(log2(128)) / 8) // 2**10
print(I)  # 7


# https://stepik.org/lesson/1650993/step/4?unit=1673695
for i in range(1, 100):
    if ceil(768 * 600 * i / 8) // 2**10 > 420:
        print(2**(i-1))
        break


# https://stepik.org/lesson/1650993/step/5?unit=1673695
"""
600 * 600 * 24  >>  12
300 * 300 * 8  >>  x
"""
res = (12 * 300 * 300 * 8) / (600 * 600 * 24)
print(res)  # 1


# https://stepik.org/lesson/1650993/step/6?unit=1673695
from math import ceil
I = ceil(640 * 480 * 16 / 8) / 2**20
print(I * 128)  # 75


# https://stepik.org/lesson/1650993/step/7?unit=1673695
from math import ceil, log2
I = ceil(1600 * 1200 * ceil(log2(1500)) / 8) / 2**10
print(ceil(I))  # 2579


# https://stepik.org/lesson/1650993/step/8?unit=1673695
from math import ceil, log2
I = ceil(480 * 640 * ceil(log2(1600)) / 8) / 2**10
print(ceil(I))  # 413


# https://stepik.org/lesson/1650993/step/9?unit=1673695
from math import ceil, log2
for i in range(1, 100):
    if ceil(1536 * 2048 * i / 8) / 2**20 > 6:
        print(2**(i-1))  # 65536
        break


# https://stepik.org/lesson/1650993/step/10?unit=1673695
from math import ceil, log2
for i in range(1, 100):
    if ceil(3900 * 2160 * i / 8) / 2**20 > 13:
        print(2**(i-1))  # 4096
        break


# https://stepik.org/lesson/1650993/step/11?unit=1673695
from math import ceil, log2
for i in range(1, 100):
    if ceil(192 * 960 * i / 8) / 2**10 > 90 * 100 / 65:
        print(2**(i-1))  # 64
        break


# https://stepik.org/lesson/1650993/step/12?unit=1673695
from math import ceil
for i in range(1, 100):
    if ceil(640 * 256 * i / 8) / 2**10 > 170 * 135 / 100:
        print(2**(i-1))  # 2048
        break

for i in range(1, 100):
    if 640 * 256 * i / 2**13 > 170 * 135 / 100:
        print(2**(i-1))  # 2048
        break


""" 7.2 Задание 7 | Урок 2 """
# https://stepik.org/lesson/1661195/step/1?unit=1684068
from math import ceil
for i in range(1, 100):
    if ceil(1024 * 120 * (i + 7) / 8) / 2**10 > 210:
        print(2**(i-1))  # 128
        break


# https://stepik.org/lesson/1661195/step/2?unit=1684068
from math import ceil
for i in range(1, 100):
    if ceil(480 * 768 * (i + (i // 2)) / 8) / 2**10 > 405:
        print(2**(i-1))  # 64
        break

# https://stepik.org/lesson/1661195/step/3?unit=1684068
from math import ceil
for i in range(1, 100):
    if ceil(1536 * 1024 * i / 8) * 6 / 2**20 > 9:
        print(2**(i-1))  # 256
        break


# https://stepik.org/lesson/1661195/step/4?unit=1684068
# https://kompege.ru/task   № 158 (Уровень: Базовый)
sec = 48*2**23 / (2 * 64_000 * 16)
print(sec // 60)  # 3


# https://stepik.org/lesson/1661195/step/5?unit=1684068
# https://kompege.ru/task   № 159 (Уровень: Базовый)
t = (5625 * 2**20) / (2 * 48_000 * 24 / 8) / 60
print(int(t) - int(t) % 5)  # 340


# https://stepik.org/lesson/1661195/step/6?unit=1684068
# https://kompege.ru/task   № 162 (Уровень: Средний)
"""
I2 = I1 * 3 / 4  =  I1 * 0.75
A I1 = 100 sec
A I2 = 0.75 * 100  = 75 sec
A / B = 75 / 15 = 5 раз
"""


# https://stepik.org/lesson/1661195/step/7?unit=1684068
# https://kompege.ru/task   № 166 (Уровень: Базовый)
I = 2 * 48_000 * 16 * 90
t = I / 32_000 / 60
print(t)  # 72






""" 7.3 Задание 7 | Задачи прошлых лет """
# https://stepik.org/lesson/1650994/step/1?unit=1673696
# цвет каждого пикселя кодируется 3 байтами
I = 1024 * 768 * 3 * 8
print(I / 65_536)  # 288


# https://stepik.org/lesson/1650994/step/2?unit=1673696
I = 4 * 192_000 * 16
print(967*2**23 / I // 60)  # 11


# https://stepik.org/lesson/1650994/step/3?unit=1673696
I = 2 * 48_000 * 24
print(288*2**23 / I // 60)  # 17


# https://stepik.org/lesson/1650994/step/4?unit=1673696
from math import ceil, log2
I = 1024 * 960 * ceil(log2(8192))
N = 1_474_560 * 280
print(N // I)  # 32




