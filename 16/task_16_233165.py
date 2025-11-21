""""""
"""
Task 16
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 16.1 Задание 16 | Урок 1 """
# https://stepik.org/lesson/1697472/step/3?unit=1720848
# https://kompege.ru/task   № 99 Джобс 07.09.2020 (Уровень: Базовый)
def f(n):
    if n <= 2:
        return (1, 3, 2)[n]
    return f(n - 1) * f(n - 3)
print(f(7))  # 144


# https://stepik.org/lesson/1697472/step/4?unit=1720848
# https://kompege.ru/task   № 596 (Уровень: Базовый)
def f(n):
    if n <= 3:
        return n
    elif n > 3:
        if not n % 3:
            return n**3 + f(n - 1)
        elif n % 3 == 1:
            return 4 + f(n // 3)
        else:
            return n**2 + f(n - 2)
print(f(100))  # 121757


# https://stepik.org/lesson/1697472/step/5?unit=1720848
# https://kompege.ru/task   № 597 (Уровень: Базовый)
def f(n):
    if n <= 10:
        return n
    if 10 < n <= 36:
        return n // 4 + f(n-10)
    return 2 * f(n-5)
print(f(100)) # 180224


# https://stepik.org/lesson/1697472/step/10?unit=1720848
# https://kompege.ru/task   № 1408 (Уровень: Базовый)
def f(n):
    if n <= 2:
        return n
    if not n % 2:
        return (n + f(n-2)) // 5
    return (2*n + f(n-1) + f(n-2)) // 4
print(f(50))  # 12


# https://stepik.org/lesson/1697472/step/11?unit=1720848
# https://kompege.ru/task   № 1860 Основная волна 2021 (Уровень: Базовый)
def f(n):
    if n <= 1:
        return 0
    if n > 1 and n % 2:
        return f(n-1) + 3*n**2
    return n//2 + f(n-1) + 2
print(f(49))  # 62820

# https://stepik.org/lesson/1697472/step/12?unit=1720848
# https://kompege.ru/task   № 592 (Уровень: Средний)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) + 2 * g(n-1)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) - n * g(n-1)
print(g(18))  # 87810480



""" 16.2 Задание 16 | Урок 2 """
# https://stepik.org/lesson/1697473/step/1?unit=1720849
# https://kompege.ru/task   № 724 Джобс 23.11.2020 (Уровень: Средний)
from functools import lru_cache
@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) + g(n-1) + n

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) - 2 * g(n-1)

# [g(i) for i in range(1, 37)]
print(sum(map(int, str(g(36)))))  # 40


# https://stepik.org/lesson/1697473/step/2?unit=1720849
# https://kompege.ru/task   № 1058 Джобс 15.03.2021 (Уровень: Средний)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if not n:
        return 1
    if n == 1:
        return 3
    return f(n-1) - f(n-2) + 3*n
print(f(40))  # 126


# https://stepik.org/lesson/1697473/step/3?unit=1720849
# https://kompege.ru/task   № 628 Джобс 02.11.2020 (Уровень: Средний)
def f(n):
    if n <= 18:
        return n + 3
    if n > 18:
        if not n % 3:
            return (n//3) * f(n//3) + n - 12
        return f(n-1) + n**2 + 5

cnt = 0
for n in range(1, 1001):
    cnt += all(i in '02468' for i in str(f(n)))
print(cnt)  # 16


# https://stepik.org/lesson/1697473/step/7?unit=1720849
# https://kompege.ru/task   № 601 (Уровень: Средний)
def f(n):
    cnt = 1
    if n >= 1:
        cnt += 2 + f(n-1) + f(n-3)
    return cnt
print(f(40))  # 22947841

# variant
def f(n):
    global cnt
    cnt += 1
    if n >= 1:
        cnt += 2
        f(n-1)
        f(n-3)

cnt = 0
f(40)
print(cnt)  # 22947841



""" 16.3 Задание 16 | Задачи прошлых лет """
# https://stepik.org/lesson/1697474/step/2?unit=1720850
# https://kompege.ru/task   № 9785 Основная волна 20.06.23 (Уровень: Базовый)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 7:
        return 7
    if n >= 7:
        return n + 1 + f(n-2)
[f(n) for n in range(7, 2025)]
print(f(2024) - f(2020))  # 4048


# https://stepik.org/lesson/1697474/step/6?unit=1720850
# https://kompege.ru/task   № 17529 Основная волна 07.06.24 (Уровень: Базовый)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

[f(n) for n in range(7, 2025)]
print((2 * f(2024) + f(2023)) // f(2022))  # 8191127
