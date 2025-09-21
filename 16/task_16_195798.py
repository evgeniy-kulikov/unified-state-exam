""""""
"""
Task 16
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 21.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1227123/step/1?unit=1240641
def f(n):
    if n > 2024:
        return n
    return n * f(n+1)

print(f(2022) / f(2024))  # 4090506


# https://stepik.org/lesson/1227123/step/2?unit=1240641
import sys
sys.setrecursionlimit(3050)

def f(n):
    if n < 3:
        return 3
    return 2 * n + 5 + f(n-2)
print(f(3027) - f(3023))  # 12114


# Запоминаем cache
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 3:
        return 3
    return 2 * n + 5 + f(n-2)

for n in range(1, 3050):
    f(n)
print(f(3027) - f(3023))  # 12114


# https://stepik.org/lesson/1227123/step/3?unit=1240641
from functools import lru_cache
@lru_cache()
def f(n):
    if n >= 10_000:
        return 1
    if n < 10_000 and not n % 2:
        return f(n+3) + 7
    return f(n+1) - 3

for n in range(10_000, 50,-1):  # Начинаем с точки выхода из рекурсии
    f(n)
print(f(50) - f(57))  # 11


# https://stepik.org/lesson/1227123/step/4?unit=1240641
from functools import lru_cache
@lru_cache()
def f(n):
    if n <3:
        return 2
    return 2*f(n-2)

for n in range(2, 2223):
    f(n)
print(f(2222) / f(2182))  # 1048576


# https://stepik.org/lesson/1227123/step/5?unit=1240641
def f(n):
    if n <= 1:
        return n
    if n > 1 and not n % 3:
        return f(n-1) + f(n-2) + 1
    return g(n-3)

def g(n):
    if n > 100:
        return n
    return g(n+2) + 1

print(f(15) + f(12))  # 593


# https://stepik.org/lesson/1227123/step/6?unit=1240641
import sys
sys.setrecursionlimit(3000)
def f(n):
    if n>3456:
        return n+1
    if n <= 3456 and not n % 3:
        return f(n+1) + f(n+2)
    return f(n + n%3) + 2

print(f(12) - f(17))  # 8054


# https://stepik.org/lesson/1227123/step/8?unit=1240641
from functools import lru_cache, cache

# @lru_cache(None) == @cache
# @lru_cache(None)  # Включает вытеснение старых ключей
# @lru_cache(None)
@cache # Включает вытеснение старых ключей
def g(n):
    if n > 1500:
        return 5
    return g(n+1) + g(n+2) + 1

for i in range(1500, 0, -1):
    g(i)

# @lru_cache(None)
@cache
def f(n):
    if n<=4:
        return 1
    return f(n-1) + f(n-3) + g(n-2)

for i in range(1200):
    f(i)
print((f(1200) + g(100)) % 10_000)  # 7062



""" 21.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1227124/step/1?unit=1240642
from functools import lru_cache
@lru_cache()
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n + f(n-1)

for i in range(2025):
    f(i)

cnt = 0
for n in range(1, 101):
    cnt += not f(2023) // f(n) % 2
print(cnt)


# https://stepik.org/lesson/1227124/step/2?unit=1240642
from functools import cache
@ cache
def f(n):
    if n > 10**6:
        return n
    return n + f(2*n)

def g(n):
    return f(n) / n

cnt = 0
for n in range(1, 10**6):
    cnt += g(n) == g(2000)
print(cnt)  # 1953


# https://stepik.org/lesson/1227124/step/2?unit=1240642
from functools import cache








