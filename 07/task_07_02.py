"""
Task 07
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248?auth=login
"""

"""  Измерение графической информации """

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
    # if (100**2 * i * 3 * 2**20 * 8)/ (300 ** 2 * 24) == 128 * 2**10 * 8:
    # if (i * 3 * 2**10)/ (9 * 24) == 128:
    if i * 2**10 > 128 * 72:
        print(2 ** (i - 1))  # 512
        break

# https://stepik.org/lesson/648369/step/1?auth=login&unit=645014
res = (55 * 2**10) / (12 * 300**2 * 16 / 8 / 2**10 + 4)
print(res) # 26.649316851008457
# 26

# https://stepik.org/lesson/648369/step/2?auth=login&unit=645014
res = (760 * 2**10) / (20 * 600**2 * 24 / 8 / 2**10 + 8)
print(res) # 36.88035352518156
# 36



