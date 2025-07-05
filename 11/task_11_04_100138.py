""""""
"""
Task 11
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 40.2 Пароли и дополнительные сведения """

# https://stepik.org/lesson/768216/step/2?unit=770575
from math import log2, ceil
i = ceil(log2(17))  # 5 bit
I = ceil(i * 15 / 8)  # 10 byte
print(I * 40)  # 400 byte


# https://stepik.org/lesson/768216/step/8?unit=770575
from math import log2, ceil
i = ceil(log2(260))  # 9 bit
I = ceil(i * 60 / 8)  # 68 byte
print(I * 65_536 / 1024)  # 4352 KByte


# https://stepik.org/lesson/768216/step/10?unit=770575
from math import log2, ceil
i = ceil(log2(8))  # 3 bit
I = ceil(i * 15 / 8) + 24 # 30 byte
print(I * 30)  # 900 Byte


# https://stepik.org/lesson/768216/step/16?unit=770575
from math import log2, ceil
i = ceil(log2(12))  # 4 bit
I = 1000 / 50  # 20  byte
I_add = I - ceil(i * 15 / 8)
print(I_add)  # 12 byte


""" 40.3 Пароли. Обратные задачи """

# https://stepik.org/lesson/1364479/step/2?unit=1380415
from math import log2, ceil
I = ceil(31 * 2**20 / 252_500)  # 129 byte
for i in range(1, 100):
    if 261 * i > I * 8:
        print(2 ** (i - 1) + 1)  # 9  (МИНИМАЛЬНО возможная мощность алфавита)
        break


# https://stepik.org/lesson/1364479/step/3?unit=1380415
from math import log2, ceil
I = ceil((213 * 2**10) / 708)  # 309 byte
i = ceil(log2(10 + 26 + 450))  # 9
for n in range(1, 100_000):
    if n * i > I * 8:
        print(n - 1)  # 274
        break


# https://stepik.org/lesson/1364479/step/4?unit=1380415
from math import log2, ceil
i = ceil(log2(10 + 2030))  # 11 bit
I = ceil((67 * 1024) / 318)  # 216 byte
for n in range(1, 1000):
    if i * n > I * 8:
        print(n - 1)  # 157
        break


""" 40.4 Непосимвольное кодирование """

# https://stepik.org/lesson/768217/step/2?unit=770576
from math import log2, ceil
i_per = ceil(log2(26 + 26 + 10))  # 6 bit
I_per = ceil(i_per * 15 / 8)  # 9 byte
I_add = 14  # byte
I_num = ceil(log2(2000) / 8)  # 1 byte
print(I_per + I_add + I_num)  # 30 byte


# https://stepik.org/lesson/768217/step/5?unit=770576
from math import log2, ceil
i_per = ceil(log2(26 + 26 + 10))  # 6 bit
I_per = ceil(i_per * 15 / 8)  # 12 byte
I_num = ceil(log2(2_000) / 8)  # 2 byte
I_add = 28 - I_per - I_num
print(I_add)  # 14 byte


# https://stepik.org/lesson/768217/step/6?unit=770576
from math import log2, ceil
i_per1 = ceil(log2(32))  # 5 bit
i_per2 = ceil(log2(10))  # 4 bit
I_per = ceil((i_per1 * 15 + i_per2 * 5) / 8)  # 12 byte
I_add = 10
print(I_per + I_add)  # 22 byte


# https://stepik.org/lesson/768217/step/7?unit=770576
from math import log2, ceil
i_per1 = ceil(log2(33))  # 6 bit
i_per2 = ceil(log2(10))  # 4 bit
I_per = ceil((i_per1 * 10 + i_per2 * 3) / 8)  # 9 byte
I_add = 24 - I_per
print(I_add)  # 15 byte
