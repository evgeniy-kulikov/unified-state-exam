"""
Task 07
Информатика Подготовка к ЕГЭ 2025
https://stepik.org/course/182932/syllabus
"""

"""  Измерение графической информации """


# https://stepik.org/lesson/1084599/step/1
from math import log2, ceil
i = ceil(log2(128))
pic = 64 * 128 * i / 8 / 1024
print(pic)  # 7


# https://stepik.org/lesson/1084599/step/2?unit=1094961
for i in range(1, 100):
    if 768 * 600 * i / 8 / 1024 > 420:
        print(2 ** (i - 1))  # 128
        print(i - 1)  # 7
        break


# https://stepik.org/lesson/1084599/step/3?unit=1094961
from math import log2, ceil
size = 0
for n in range(1, 1000):
    if 600 * 600 * n * 24 / 8 / 1024 / 1024 > 12:
        print(n - 1) # 11  (размер документа в inch)
        size = n
        break
pic_new = 300 * 300 * n * log2(256) / 8 / 1024 / 1024
print(pic_new) # 1.02996826171875  =>  1


# https://stepik.org/lesson/1084599/step/4?unit=1094961
pic = 640 * 480 * 16 / 8  #  1 фото
serial = pic * 128 / 1024 / 1024
print(serial)  # 75


# https://stepik.org/lesson/1084599/step/4?unit=1094961
from math import log2, ceil
i = ceil(log2(1500))  # 11
pic = 1600 * 1200 * i / 8 / 1024  #  1 фото
print(ceil(pic))  # 2579


# https://stepik.org/lesson/1084599/step/6?unit=1094961
from math import log2, ceil
i = ceil(log2(1600))
pic = 480 * 640 * i / 8 / 1024
print(ceil(pic))  # 413


# https://stepik.org/lesson/1084599/step/7?unit=1094961
from math import log2, ceil
for n in range(2, 100_000):
    i = ceil(log2(n))
    if 1536 * 2048 * i / 8 / 1024 / 1024 > 6:
        print(n - 1)  # 65536
        break


# https://stepik.org/lesson/1084599/step/8?unit=1094961
from math import log2, ceil
for n in range(2, 100_000):
    i = ceil(log2(n))
    if 3900 * 2160 * i / 8 / 1024 / 1024 > 13:
        print(n - 1)  # 4096
        break


# https://stepik.org/lesson/1084599/step/10?unit=1094961
for n in range(2, 10_000):
    i = ceil(log2(n))
    if (192 * 960 * i / 8 / 1024) * 0.65  > 90:
        print(n - 1)  # 64
        break


# https://stepik.org/lesson/1084599/step/9?unit=1094961
from math import log2, ceil
for n in range(2, 10_000):
    i = ceil(log2(n))
    if (265 * 640 * i / 8 / 1024) * 100/135 > 170:
        print(n - 1)  # 2048
        break


# https://stepik.org/lesson/1084599/step/11?unit=1094961
from math import log2, ceil
for n in range(2, 10_000):
    i = ceil(log2(n)) + 7
    if 1024 * 120 * i / 8 / 1024 > 210:
        print(n - 1)  # 128
        break


# https://stepik.org/lesson/1084599/step/12?unit=1094961
from math import log2, ceil

for n in range(2, 10_000):
    i = ceil(log2(n))
    i += i // 2
    if 480 * 768 * i / 8 / 1024 > 405:
        print(n - 1)  # 64
        break


# https://stepik.org/lesson/1084599/step/13?unit=1094961
from math import log2, ceil

for n in range(2, 10_000):
    i = ceil(log2(n))
    if 1536 * 1024 * i * 6 / 8 / 1024 / 1024 > 9:
        print(n - 1)  # 256
        break

"""
Измерение звуковой информации
"""
#  https://stepik.org/lesson/1084600/step/1?thread=solutions&unit=1094962
t = 48 * 2 ** 20 / (2 * 64_000 * 16 / 8)
print(t / 60)  # 3.2768


#  https://stepik.org/lesson/1084600/step/2?thread=solutions&unit=1094962
t = 5625 * 2 ** 20 / (2 * 48_000 * 24 / 8)
print(t / 60)  # 341.3333333333333


from math import ceil
#  https://stepik.org/lesson/1084600/step/3?thread=solutions&unit=1094962
data = 4 * 40_000 * 16 * 300 / 8 / 2 ** 20
# print(data)  # 91.552734375
print(ceil(data))  # 92


#  https://stepik.org/lesson/1084600/step/4?thread=solutions&unit=1094962
for i in range(1, 100):
    if 2 * 44_000 * i * 325 / 8 / 2 ** 20 > 82:
        print(i - 1)
        break


#  https://stepik.org/lesson/1084600/step/5?thread=solutions&unit=1094962
for i in range(1, 100):
    if 2 * 80_000 * i * 205 / 8 / 2 ** 20 > 80:
        print(i - 1)
        break



#  https://stepik.org/lesson/1084601/step/1?unit=1094963
print(2 * 48_000 * 16 * 90 / 32_000 / 60)



#  https://stepik.org/lesson/1084601/step/2?unit=1094963
# print(2 ** 20 / 8 / 1024)  # 128 KByte/sek  скорость Миши
# print(2 ** 13 / 8 / 1024)  # 1 KByte/sek  скорость Толи
print(1024 * 2 ** 10 * 8 / 2 ** 20)  #  8.0 sek на получение Толей первых 1024 KByte
print(10 * 2 ** 20 * 8 / 2 ** 13)  #  10240.0 sek  передача Толей всего файла Мише
print((10240 + 8) / 60 / 60)  # 10248 sek


# https://stepik.org/lesson/1084601/step/4?unit=1094963
f = 4 * 2 ** 20 * 8
t1 = f / 2 ** 24
t2 = f / 2 ** 20
print(t1 + t2)  # 34


# https://stepik.org/lesson/1084601/step/5?unit=1094963
f = 500 * 2 ** 20 * 8
t_a = 2 * f / (100 * 2 ** 20) + 40
t_b = f / (10 * 2 ** 20)
print(t_a, t_b)  # 120.0 400.0
print(abs(t_a - t_b))  # 280



