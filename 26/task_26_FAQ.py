""""""
""" Расчёт медианы списка """
# Для четного и нечетного кол-ва элементов списка
from statistics import median
num = [3, 1, 5, 2]
med = median(num)  # 2.5  - значение медианы

# Только для нечетного кол-ва элементов списка
ls = sorted([1, 3, 2, 5, 4])
med = ls[len(ls) // 2]  # 3


""" Перемножить элементы списка """
# Перемножить элементы списка - var 1
from math import prod  # С версии Python 3.8

res = prod([2, 3, 4])  # 24

# Перемножить элементы списка - var 2
from functools import reduce
from operator import mul

res = reduce(mul, [2, 3, 4])  # 24