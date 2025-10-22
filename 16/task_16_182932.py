""""""
"""
# Рекурсия
# Информатика Подготовка к ЕГЭ 2025
# https://stepik.org/course/182932/syllabus
"""

# https://stepik.org/lesson/1112872/step/11?unit=1124255
from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(1000000)

@lru_cache(None)
def f(n):
    if n < 11:
        return n
    if n >= 11:
        return n + f(n - 1)
print(f(2024) - f(2021))  # Ошибка  Process finished with exit code -1073741571
"""
!!!  Яркий пример, что не все нужно решать через функцию  !!!
!!!  Решаем логически  !!!
Смотрим на последнее условие:
if n >= 11:
    return n + f(n-1)

f(2024) == 2024 + f(2023)
f(2023) == 2023 + f(2022)
f(2022) == 2022 + f(2021)
f(2021) == 2021 + f(2020)

f(2024) - f(2021) == 
2024 + f(2023) - f(2021) == 
2024 + 2023 + f(2022) - f(2021) == 
2024 + 2023 + 2022 + f(2021) - f(2021) ==
2024 + 2023 + 2022
"""
print(2024 + 2023 + 2022)  # 6069
