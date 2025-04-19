"""
Информатика Подготовка к ЕГЭ 2025
https://stepik.org/course/182932/syllabus
"""


# https://stepik.org/lesson/1084596/step/7?unit=1094956
from math import log2, ceil
code_1 = ceil(ceil(log2(25)) * 11 / 8)  # 7 byte
code_2 = ceil(ceil(log2(26)) * 5 / 8 + ceil(log2(10)) * 3 / 8)  # 5 byte
res = 30 - code_1 - code_2
print(res)  # 18


# https://stepik.org/lesson/1084596/step/2?unit=1094956
from math import log2, ceil
ident = ceil(ceil(log2(8)) * 15 / 8)  # 6 byte
res = (ident + 24) * 20
print(res)  # 600


# https://stepik.org/lesson/1084596/step/3?unit=1094956
from math import log2, ceil
user = ceil(ceil(log2(12)) * 7 / 8)  # 4 byte
res = (user + 15) * 150
print(res)  # 2850


# https://stepik.org/lesson/1084596/step/9?unit=1094956
from math import log2, ceil
indif = 150 * 1024 / 1200   # 128 byte  - один индификатор
for n in range(2, 10_000):
    i = ceil(log2(n))
    if i * 80 / 8 > indif:
        print(n - 1)  # 4096
        break


# https://stepik.org/lesson/1084596/step/10?unit=1094956
from math import log2, ceil
psw = 20 * ceil(log2(9)) / 8 #  10 byte - one passord
ip = 4  # byte - one IP
user = 6 * 1024 / 192  #  32 byte - one user total
user_add = user - psw - ip
print(user_add)  # 18


# https://stepik.org/lesson/1084596/step/11?unit=1094956
from math import log2, ceil
idf = ceil(101 * ceil(log2(4090 + 10)) / 8) #  165 byte - one indif
print(2048 * idf / 1024)  # 330 byte