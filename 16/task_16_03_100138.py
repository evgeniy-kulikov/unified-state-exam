""""""
"""
Task 16
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 12.1 Решение задач задания 16 """

# https://stepik.org/lesson/569848/step/4?unit=564382
def fn(n):
    if n <= 5:
        return n
    if not n % 3:
        return n + fn(n - 1)
    return 2 * n + fn(n - 2)

cnt = 0
for n in range(1, 1001):
    cnt += not fn(n) % 5
print(cnt)  # 331


# https://stepik.org/lesson/569848/step/6?unit=564382
def fn(n):
    if n > 15:
        return n * n + 2 * n
    if not n % 2:
        return fn(n + 1) + 2 * fn(n + 2)
    return fn(n + 2) + 3 * fn(n + 3)

cnt = 0
for n in range(1, 101):
    cnt += fn(n) % 10 == 8
print(cnt)  # 17


# https://stepik.org/lesson/569848/step/7?unit=564382
def fn(n):
    if n <= 2:
        return 1
    return 2 * fn(n - 1) + 3 * fn(n - 2) + 3

print(sum(map(int, str(fn(25)))))  # 44


# https://stepik.org/lesson/569848/step/9?unit=564382
def fn(n):
    if n <= 1:
        return n
    if not n % 2:
        return 1 + fn(n // 2)
    return 1 + fn(n - 2)

for n in range(100):
    if fn(n) == 16:
        print(n)  # 31
        break


""" 12.2 Функция lru_cache """

# https://stepik.org/lesson/773346/step/3?unit=775815
from functools import lru_cache
@ lru_cache(None)
def fn(n):
    if n <= 1:
        return 2
    return 2 * fn(n - 1) + fn(n - 2) - 3

print(fn(270))
# 558952689134942049031089313476127272132069886522389714036525369410329526344404408674062077167075460125


# https://stepik.org/lesson/773346/step/7?unit=775815
from functools import lru_cache
@ lru_cache(None)
def fn(n):
    if n <= 5:
        return n
    if not n % 3:
        return n + fn(n - 1)
    return 2 * n + fn(n - 2)

cnt = 0
for n in range(1, 1001):
    cnt += not fn(n) % 5
print(cnt)


# https://stepik.org/lesson/773346/step/9?unit=775815
from functools import lru_cache
@ lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + 2 * g(n - 1) - n

@ lru_cache(None)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + 2 * g(n - 1) + 3

print(f(180) + g(180))
# 80409422937303414135916934816205315181003957035861596542001652730788089417645984576243


""" 12.3 Глубина рекурсии """

# https://stepik.org/lesson/862808/step/2?unit=866853
from functools import lru_cache
import sys
sys.setrecursionlimit(3500)
# @ lru_cache(None)  # начинает мешаться
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)

print(f(1970) / f(1968))  # 3878930
"""
f(1970) = 1970 * f(1969) = 1970 * 1969 * f(1968)
(1970 * 1969 * f(1968)) / f(1968) = 1970 * 1969 = 3878930
"""

# https://stepik.org/lesson/862808/step/4?unit=866853
res = (2*1812 + 1) * (2*1811 + 1)
print(res)

# https://stepik.org/lesson/862808/step/7?unit=866853
res = 3 ** 1234 / 3 ** 1230
print(res)  # 81


# https://stepik.org/lesson/862808/step/10?unit=866853
import sys
sys.setrecursionlimit(3000)
def fn(n):
    if n == 1:
        return 1
    return (2*n + 1) * fn(n - 1) - 1
print(fn(1812) / fn(1810))  # 13133375


""" 12.3 Глубина рекурсии """

# https://stepik.org/lesson/862808/step/12?unit=866853
from functools import lru_cache

@lru_cache(None)
def fn(n):
    if n == 1:
        return 1
    return n * fn(n - 1)

[fn(i) for i in range(1, 2025)]
print(int(fn(2024) / fn(2021)))  # 8279184144


""" 12.4 Формализация """

# https://stepik.org/lesson/1401502/step/2?unit=1418463
"""
F(n) = 1 при n = 1;
F(n) = 2 * n * F(n − 1), если n > 1
Найти:
(F(2024) / 16 -  F(2023)) / F(2022)

F(2024) / 16 = 2 * 2024 * F(2023) / 16 = 253 * F(2023)
253 * F(2023) - F(2023) = 252 * F(2023)

252 * F(2023) / F(2022) = 252 * 2 * 2023 * F(2022) / F(2022) = 252 * 2 * 2023

Ответ: 1019592
"""

