""""""
"""
Task 16
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""


""" 2.5 тест № 2 (продолжение) """
# https://stepik.org/lesson/1599364/step/3?unit=1621008
# pic/001
from functools import lru_cache
import sys
sys.setrecursionlimit(9000)
@lru_cache(5000)
def F(n):
    if n == 1:
        return 1
    return (n - 1) * F(n - 1)
print((F(2024)/7 - F(2023))/F(2022))  # НЕ ПОЛУЧАЕТСЯ !!!

# А ТАК ПРОХОДИТ !!!
# Решение через списки (обход проблемы губины рекурсии)
d = [1] * 2040
for n in range(2, 2030):
    d[n] = (n - 1) * d[n - 1]  # наполняем список значениями
print((d[2024] // 7 - d[2023]) / d[2022])  # 582336
