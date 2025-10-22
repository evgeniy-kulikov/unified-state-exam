""""""
"""
Task 16
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""


""" 3.3 Домашка: 16 номер. """
# https://stepik.org/lesson/1038709/step/2?unit=1062775
def f(n):
    if n <= 3:
        return 3
    if n > 3 and not n % 2:
        return f(n // 2) + 5
    return f(n - 1) - (n - 2)
print(f(20))  # 15


# https://stepik.org/lesson/1038709/step/3?unit=1062775
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n >= 10_000:
        return 1
    if n < 10_000 and not n % 2:
        return f(n + 3) + 7
    return f(n + 1) - 3

[f(i) for i in range(10_000, 0, -1)]
print(f(50) - f(57))  # 11


# https://stepik.org/lesson/1038709/step/4?unit=1062775
def f(n):
    if n > 10**6:
        return n
    return n + f(2 * n)

def g(n):
    return f(n) / n

num = g(2000)
cnt = 0
for i in range(1, 10**6 + 1):
    cnt += g(i) == num
print(cnt)  # 1953


# https://stepik.org/lesson/1038709/step/5?unit=1062775
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return (n + 1) * f(n - 1)

d = [f(i) for i in range(1, 2025)]
print((f(2024) - 3 * f(2023)) // f(2022))  # 4092528

# Руками
print(2022 * 2024)  # 4092528

# используем setrecursionlimit()
import sys
sys.setrecursionlimit(2025)

def f(n):
    if n == 1:
        return 1
    return (n + 1) * f(n - 1)

print((f(2024) - 3 * f(2023)) // f(2022))  # 4092528
