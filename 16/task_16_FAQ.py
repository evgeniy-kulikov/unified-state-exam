""""""
"""
Task 16
"""

"""
Пути решения:

1. Простой рекурсией

2. Для ускорения расчета используется кеширование
from functools import lru_cache
@lru_cache(None)  # None - нет ограничения на кол-во ключей с данными
def fn(n):
    pass

3. Для увеличения глубины рекурсии меняем её дефолтное значение в системе.
Могут быть проблемы с одновременным использованием lru_cache
import sys
sys.setrecursionlimit(5000)

def fn(n):
    pass
    
4. Формализация
def fn(n):
    if n == 1:
        return 1
    return n * fn(n - 1)
    
Найти: (fn(2024) * fn(2023)) / fn(2022)

fn(2024) = 2024 * fn(2023)
fn(2023) = 2023 * fn(2022)

(2024 * 2023 * fn(2022)) / fn(2022)  =  2024 * 2023

"""

# Интересный вариант решения....
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
d = [1] * 2050
for n in range(2, 2040):
    d[n] = (n - 1) * d[n - 1]
print((d[2024] // 7 - d[2023]) / d[2022])
