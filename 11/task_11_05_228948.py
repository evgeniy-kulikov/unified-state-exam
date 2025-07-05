""""""
"""
Task 02
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""

""" 2.1 тест № 1 (егэ-2024, день 1) """
# https://stepik.org/lesson/1594698/step/12?unit=1616271
from math import ceil, log2
i = ceil(log2(10 + 52 + 458))
for x in range(10, 1000):
    I = ceil(x * i / 8) / 1024
    if I * 862 > 276:
        print(x - 1)
        break


""" 2.4 тест № 2 (пересдача ЕГЭ 2024) """
# https://stepik.org/lesson/1599363/step/12?unit=1621007
from  math import log2, ceil
i = ceil(log2(10 + 26 + 450))
for x in range(500):
    if ceil(x * i / 8) * 575 / 1024 > 100:
        print(x)  # можно больше !!!
        break