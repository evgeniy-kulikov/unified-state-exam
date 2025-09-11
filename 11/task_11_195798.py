""""""
"""
Task 11
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 16.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1223081/step/1?unit=1236570
from math import log2, ceil
I = ceil(310 * ceil(log2(10 + 2042)) / 8) + 14
print(I * 65_536 / 2**10)