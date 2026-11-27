""" https://kompege.ru/task """
"""
593=724 596 605 628 699
1594 4739 4740 4741 6911 8426 8474 8561
10659 1199 17557 17679
21979 23562 24371 25355 25397 29082 29083 31224
"""


# 593 (Уровень: Средний)
# 724 Джобс 13_(23).11.2020 (Уровень: Средний)
from functools import lru_cache
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) - 2*g(n - 1)

@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + g(n - 1) + n

[g(n) for n in range(1, 37)]
# print(g(36))  # 378805153
print(sum(map(int, str(g(36)))))  # 40


""" Взято на мой курс """
# 596 (Уровень: Базовый)
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


""" Взято на мой курс """
# 605 (Уровень: Средний)
def f(n, c=0):
    c += n * n
    if n > 1:
        # c += 2 * n + 1
        # c += f(n - 2)
        # c += f(n // 3)
        c += 2 * n + 1 + f(n - 2) + f(n // 3)
    return c
print(f(100))  # 296541

# variant
def f(n):
    c = n * n
    if n > 1:
        c += 2 * n + 1
        c += f(n - 2)
        c += f(n // 3)
    return c
print(f(100))  # 296541


""" Взято на мой курс """
# 628 Джобс 02.11.2020 (Уровень: Средний)
def f(n):
    if n <= 18:
        return n + 3
    if n % 3:
        return f(n - 1) + n ** 2 + 5
    return (n // 3) * f(n // 3) + n - 12

cnt = 0
for n in range(1, 1001):
    cnt += all(i in '02468' for i in str(f(n)))
print(cnt)



# 699 Джобс 16.11.2020 (Уровень: Базовый)
def f(n):
    if n <= 1:
        return 1
    if n:
        if not n % 2:
            return n * f(n-1)
        return n + f(n - 2)
print(f(84))  # 148176


""" Взято на мой курс """
# 8561 (Уровень: Базовый)
def f(n):
    if n <= 1:
        return n
    if n % 3:
        return g(n - 3)
    return f(n - 1) + f(n  -2) + 1

def g(n):
    if n > 100:
        return n
    return g(n + 2) + 1
print(f(15) + f(12))  # 593



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


# 4739 (Уровень: Средний)
def f(n):
    if n > 10_000:
        return n - 10_000
    return f(n + 1) + f(n + 2)

# (f(10) - f(12)) // f(11) == 1
print(f(12_345) + f(10_101))  # 2446


# 4740 (Уровень: Средний)
from math import factorial
from functools import lru_cache
@lru_cache
def f(n):
    if n >= 5_000:
        return factorial(n)
    return 2*f(n+1)//(n+1)

[f(i) for i in range(5_000,0,-1)]
print(1000*f(7) // f(4))  # 26250


# 4741 (Уровень: Средний)
def f(n):
    if int(n**0.5) == n**0.5:
        return int(n**0.5)
    return f(n + 1) + 1

print(f(4850) + f(5000))  # 232


# 6911 (Уровень: Базовый)
def f(n):
    if not n:
        return 0
    if n % 2:
        return 1 + f(n - 1)
    return f(n // 2) - 1
print(sum(not f(n) for n in range(1000)))  # 41


# 8426 (Уровень: Средний)
def f(n):
    if n > 1_000_000:
        return n
    return n + f(2 * n)

c = 0
m = f(2_000) / 2_000
for i in range(1, 10_001):
    if f(i) / i == m:
        c += 1
print(c)  # 1953


# 8474 (Уровень: Базовый)
from functools import lru_cache
@ lru_cache
def f(n):
    if n > 3456:
        return n + 1
    if not n % 3:
        return f(n+1) + f(n+2)
    return f(n + n%3) + 2
[f(n) for n in range(3457, 10, -1)]
print(f(12) - f(17))  # 8054



# 10659 (Уровень: Средний)
from functools import lru_cache
@lru_cache
def f(n):
    if n == 1:
        return 1
    return n + f(n-1)

[f(i) for i in range(1, 2024)]
c = 0
for n in range(1, 101):
    c += not f(2023) // f(n) % 2
print(c)  # 50


""" Взято на мой курс """
# 1199 Апробация 27.04 (Уровень: Базовый)
def f(n):
    if n <= 1:
        return 1
    if n % 2:
        return 2 * f(n-2)
    return 3*n + f(n-1)
print(f(31))  # 32768


""" Взято на мой курс """
# 17557 Основная волна 08.06.24 (Уровень: Базовый)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return 2 * n * f(n - 1)
[f(i) for i in range(1, 2025)]
print((f(2024) // 16 - f(2023)) // f(2022))  # 1019592


# 17679 Пересдача 04.07.24(Уровень: Базовый)
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
from functools import lru_cache
@lru_cache()
def f(n):
    if n == 1:
        return 1
    return (n - 1) * f(n - 1)

[f(i) for i in range(1, 2025)]
print((f(2024) // 7 - f(2023)) // f(2022))
# Решение через списки (обход проблемы губины рекурсии)
d = [1] * 2040
for n in range(2, 2030):
    d[n] = (n - 1) * d[n - 1]  # наполняем список значениями
print((d[2024] // 7 - d[2023]) / d[2022])  # 582336



""" Взято на мой курс """
# 21979 (Уровень: Базовый)
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 110:
        return n
    return (n - 7) * f(n - 8)

[f(i) for i in range(109, 74915)]
print((f(74914) - f(74898)) // (16 * f(74890)))  # 26260807145392



""" Взято на мой курс """
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


""" Взято на мой курс """
# 24371 (Уровень: Базовый)
from functools import lru_cache
@lru_cache()
def g(n):
    if n < 100:
        return n
    return f(n - 3) + 1

def f(n):
    return g(n - 2)

[g(i) for i in range(99, 5001)]
print(f(5000))  # 1078




# 25355 ЕГКР 13.12.25 (Уровень: Базовый)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 19:
        return 6 * (g(n - 7) - 36)
    return f(n - 4) + 3580

@lru_cache(None)
def g(n):
    if n < 248045:
        return g(n + 9) - 4
    return n / 20 + 28  #  float

[g(n) for n in range(248045, 10, -1)]  # для каждой функции @lru_cache делает свою таблицу ✅
[f(n) for n in range(19, 674)]  # для каждой функции @lru_cache делает свою таблицу ✅
# print(f(673))  # 47.0
print(int(f(673)))  # 47  # f может быть float из-за деления в G


# 25397 (Уровень: Средний)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n <= 40:
        return 3 * (g(n - 2) - 15)
    return f(n - 4) + 3020

@lru_cache(None)
def g(n):
    if n < 301208:
        return g(n + 7) - 21
    return 10 * n + 50

[g(n) for n in range(301208, 0, -1)]  # для каждой функции @lru_cache делает свою таблицу ✅
[f(n) for n in range(2026)]  # для каждой функции @lru_cache делает свою таблицу ✅
print(f(2026))  # 7826800



""" Взято на мой курс """
# 29082 (Уровень: Средний)
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 19:
        return 5
    return (n + 4) * f(n - 7)

[f(i) for i in range(19, 157164)]
print((f(157163) // 234 + f(157149) // 533) // f(157142)) # 16588617837881

# Решается руками. Через рекурсию долго
"""
f(157163): (157163 + 4) * f(157156)  >>  (157163 + 4) * (157156 + 4) * f(157149)  >> (157163 + 4) * (157156 + 4) * (157149 + 4) * f(157142)
>>  157167 * 157160 * 157153 * f(157142)

f(157149): (157149 + 4) * f(157142)
>>  157153 * f(157142)

f(157142) * ((157167 * 157160 * 157153 / 234) + 157153 / 533) / f(157142)
>>  157167 * 157160 * 157153 / 234 + 157153 / 533
"""
print(157167 * 157160 * 157153 / 234 + 157153 / 533) # 16588617837881




""" Взято на мой курс """
# 29083 (Уровень: Средний)
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 17:
        return 6
    return (n + 5) * f(n - 9)

[f(i) for i in range(234535)]
print((f(234561) // 436 + f(234552) // 218) // f(234534)) # 29598002876968
# Решается руками. Через  списки долго


""" Взято на мой курс """
# 31224 Резерв 22.06.26(Уровень: Базовый)
from functools import lru_cache
@lru_cache()
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * f(n - 1)

[f(i) for i in range(1, 32029)]
print((3 * f(32028) - f(32027)) // f(32026)) # 3077058080


