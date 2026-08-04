""""""
"""
Task 11
Подготовка к ЕГЭ по информатике
https://stepik.org/course/72713/syllabus
"""


# https://stepik.org/lesson/373152/step/2?unit=584884
from math import ceil
psw = ceil(9 * 5 / 8)
add = 300 / 15 - psw
print(add)  # 14



# https://stepik.org/lesson/373152/step/3?unit=584884
from math import ceil, log2
code = 10 * 6  # 26+10 --> 2**6
year = 6  # 50 --> 2**6
monht = 4 # 12 --> 2**4
card = ceil((code + year + monht) / 8)
print(card)  # 9
