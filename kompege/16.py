""" https://kompege.ru/task """
"""
699
1594 17557
23562 
"""


# 699 Джобс 16.11.2020 (Уровень: Базовый)
def f(n):
    if n <= 1:
        return 1
    if n:
        if not n % 2:
            return n * f(n-1)
        return n + f(n - 2)

print(f(84))  # 148176




# 1594 (Уровень: Средний)
def g(n):
    if n == 1:
        return 1
    return f(n-1) - 2*g(n-1)

def f(n):
    if n == 1:
        return 1
    return f(n-1) + 3*g(n-1)

print(sum(map(int, str(f(18)))))  # 46


# 17557 Основная волна 08.06.24 (Уровень: Базовый)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return 2 * n * f(n - 1)

[f(i) for i in range(1, 2025)]
print((f(2024) // 16 - f(2023)) // f(2022))  # 1019592





# 23562 Пересдача 03.07.25 (Уровень: Базовый)
from functools import lru_cache
@lru_cache
def g(n):
    if n <= 9:
        return 3 * n
    return g(n-2) + 1

# def f(n):  # лишняя функция
#     return g(n-1)

[g(n) for n in range(9, 47995)]
print(g(47994))  # 24017
