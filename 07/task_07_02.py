"""
Task 07
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248/syllabus
"""

"""  Измерение графической информации """

""" 7.11 ЕГЭ Тренировка 7 """
# https://stepik.org/lesson/421031/step/2?auth=login&unit=410641
from math import log2, ceil
# I = (128 * 256 * 8) / 8
I = (128 * 256 * ceil(log2(256))) / 8
print(I * 24 * 60 * 10 / 2 ** 20)


# https://stepik.org/lesson/421031/step/2?auth=login&unit=410641
# !!!  ИНТЕРЕСНАЯ ЗАДАЧА !!!
from math import log2, ceil, floor
for i in range(1, 10000):
    I = 800 * 600 * ceil(log2(i)) / 8 / 1024
    if I > 700:
        # print(i - 1)  # 2048
        print(ceil(log2(i - 1)), 'bit')  # 11
        # Для кодирования цвета каждого пикселя используется одинаковое целое количество байт
        print(floor(log2(i - 1) / 8), 'byte')  # 1
        print(2 ** (floor(log2(i - 1) / 8) * 8), 'color')  # 256
        break


# https://stepik.org/lesson/421031/step/5?auth=login&unit=410641
Ib = 10 * 2 ** 20 * 8  # bit
v = 2 ** 20  # bit/sec
tb = Ib / v  # 80 sec
Ia = 3 * 2 ** 20 * 8  # bit
ta = 12 + 2 + Ia /v  # 38 sec
print(tb - ta)  # 42 sec
# А42


# https://stepik.org/lesson/421031/step/7?auth=login&unit=410641
# Ia = ppi * 300 ** 2 * 24 == 3 * 2**20 * 8
# Ib = ppi * 100 ** 2 * i == 128 * 2**10 * 8
for i in range(1, 100):
    # if (100**2 * i * 3 * 2**20 * 8) / (300 ** 2 * 24) == 128 * 2**10 * 8:
    # if (i * 3 * 2**10)/ (9 * 24) == 128:
    if i * 2**10 > 128 * 72:
        print(2 ** (i - 1))  # 512
        break


# https://stepik.org/lesson/421031/step/8?auth=login&unit=410641
"""
I_300 = (300 * 300 * i) / 8 / 2**10 = 5 * 1024
I_150 = (150 * 150 * 4) / 8 / 2**10 = 512
300 * 300 * i == 150 * 150 * 4 * 10
"""
print((150**2 * 4 * 10) / 300**2) #  i = 10  --> N = 2**10 = 1024


# https://stepik.org/lesson/421031/step/9?auth=login&unit=410641
"""
I_400 = (400 * 400 * i) / 8 / 2**10 = 2 * 1024
I_100 = (100 * 100 * 6) / 8 / 2**10 = 96
100**2 * 6 * 2 * 1024 == i * 96 * 400**2
i = (100**2 * 6 * 2 * 1024) / (96 * 400**2)
"""
print((100**2 * 6 * 2 * 1024) / (96 * 400**2)) #  i = 8  --> N = 2**8 = 256


# https://stepik.org/lesson/421031/step/10?auth=login&unit=410641
N = 256  # i = 8
I = (512 * 192 * 8) / 8 / 2**20  # MB per 10 sec
res = I * 6 * 60 * 24
print(res) # 810 MB


# https://stepik.org/lesson/421031/step/11?auth=login&unit=410641
"""
I = 2 * 64*1000 * 32 * sec / 8 / 2**20 = 60
"""
sec = 60 / (2 * 64*1000 * 32 * 1 / 8/ 2**20)
print(sec // 60)  # min



""" 7.12 ЕГЭ Тренировка 7 """

# https://stepik.org/lesson/648369/step/1?auth=login&unit=645014
res = (55 * 2**10) / (12 * 300**2 * 16 / 8 / 2**10 + 4)
print(res) # 26.649316851008457
# 26

# https://stepik.org/lesson/648369/step/2?auth=login&unit=645014
res = (760 * 2**10) / (20 * 600**2 * 24 / 8 / 2**10 + 8)
print(res) # 36.88035352518156
# 36


# https://stepik.org/lesson/648369/step/3?auth=login&unit=645014
I = 4 * 7 * 300**2 * 24 / 8 / 1024 + 6  # KB
res = (640 * 1024) // I
print(res)  # 88

# https://stepik.org/lesson/648369/step/4?auth=login&unit=645014
I = 3 * 4 * 300**2 * 16 / 8 / 1024 + 4  # KB
print(I)  # 2113.375  --> 2114 (округление вверх)


# https://stepik.org/lesson/648369/step/5?auth=login&unit=645014
I = 4 * 5 * 600**2 * 24 / 8 / 1024 + 8  # KB
print(I)  # 21101.75  --> 21102 (округление вверх)




