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


# https://stepik.org/lesson/1697472/step/6?unit=1720848
# https://kompege.ru/task   № 608 (Уровень: Базовый)
def f(n):
    if n== 1:
        return 2
    return f(n-1) + 5*n**2
print(f(39))  # 102697


# https://stepik.org/lesson/1697472/step/7?unit=1720848
# https://kompege.ru/task   № 610 (Уровень: Базовый)
def f(n):
    if n < 5:
        return 1 + 2*n
    if n % 3:
        return 1 + 2*n + f(n-1) + 2*f(n-2)
    return 2 * (n + 1) * f(n-2)
print(f(15))  # 5158048


# https://stepik.org/lesson/1697472/step/8?unit=1720848
# https://kompege.ru/task   № 1199 Апробация 27.04 (Уровень: Базовый)
def f(n):
    if n <= 1:
        return 1
    if n % 2:
        return 2*f(n-2)
    return 3*n + f(n-1)
print(f(31))  # 32768


# https://stepik.org/lesson/1697472/step/9?unit=172084891
# https://kompege.ru/task  № 1020 100 базовых задач Е. Джобс (Уровень: Базовый)
def f(n):
    if n <= 3:
        return 3
    if n % 2:
        return f(n - 1) - f(n - 2)
    return f(n // 2) + 5
print(f(20))  # 15


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


# https://stepik.org/lesson/1697473/step/4?unit=1720849
# https://kompege.ru/task   № 673 Джобс 09.11.2020 (Уровень: Средний)
def f(n):
    if n > 30:
        return n**2 + 5*n + 4
    if n <= 30:
        if n % 2:
            return 2*f(n + 2) + f(n + 5)
        return f(n + 1) + 3*f(n + 4)

d = [f(n) for n in range(1, 1001)]
print(sum(sum(map(int, str(i))) == 27 for i in d))  # 137


# https://stepik.org/lesson/1697473/step/5?unit=1720849
# https://kompege.ru/task  № 2237 (Уровень: Средний)
def f(n):
    if not n:
        return 0
    if n % 2:
        return 1 + f(n - 1)
    return f(n / 2)

cnt = 0
for n in range(1, 501):
    cnt += f(n) == 8
print(cnt)  # 5


# https://stepik.org/lesson/1697473/step/6?unit=1720849
# https://kompege.ru/task  № 1131 (Уровень: Средний)
def f(n):
    if n == 1:
        return 1
    if n % 2:
        return f(n - 1) + n
    return f(n / 2) + 1

for n in range(1, 500):
    if f(n) == 19:
        print(n)  # 448
        break


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


# https://stepik.org/lesson/1697473/step/8?unit=1720849
# https://kompege.ru/task  № 605 (Уровень: Средний)  👍
def f(n):
    c = n * n
    if n > 1:
        # c += 2 * n + 1
        # c += f(n - 2)
        # c += f(n // 3)
        c += 2 * n + 1 + f(n - 2) + f(n // 3)
    return c

print(f(100))  # 296541


# https://stepik.org/lesson/1697473/step/9?unit=1720849
# https://kompege.ru/task  № 2248 (Уровень: Сложный)  👍
"""
lru_cache  и  sys.setrecursionlimit здесь не помогут.
строка  f(n + 3) уводит в бесконечность
"""
def f(n):
    if n <= 1:
        return n
    if n % 3:
        return n + f(n + 3)
    return n + f(n / 3)

for n in range(100):
    try:
        if f(n) > 100:
            print(n)  # 81
    except:  # уходим от бесконечной рекурсии 😉
        pass


# https://stepik.org/lesson/1697473/step/10?unit=1720849
# https://kompege.ru/task  № 2247 (Уровень: Сложный) 👍
def f(n):
    if n < 3:
        return n + 1
    if n % 2:
        return f(n + 2) + n + 2
    return f(n - 2) + n - 2

cnt = 0
for n in range(1, 1000):
    try:
        if 10000 <= f(n) < 100000:
            cnt += 1
    except:
        pass
print(cnt)  # 216





""" 16.3 Задание 16 | Задачи прошлых лет """
# https://stepik.org/lesson/1697474/step/1?unit=1720850
# https://kompege.ru/task  № 9747 Основная волна 19.06.23 (Уровень: Базовый)
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 11:
        return n
    return n + f(n - 1)
[f(n) for n in range(10, 2025)]
print(f(2024) - f(2021))  # 6069


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


# https://stepik.org/lesson/1697474/step/3?unit=1720850
# https://kompege.ru/task  № 9839 Основная волна 27.06.23 (Уровень: Базовый)
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 3:
        return 3
    return 2 * n + 5 + f(n - 2)

[f(n) for n in range(2, 3030)]
print(f(3027) - f(3023))  # 12114


# https://stepik.org/lesson/1697474/step/4?unit=1720850
# https://kompege.ru/task  № ***
from functools import lru_cache
@lru_cache()
def f(n):
    if n == 1:
        return 1
    return (n + 1) * f(n - 1)

[f(n) for n in range(1, 2025)]
print((f(2024) - 3 * f(2023)) // f(2022))  # 4092528


# https://stepik.org/lesson/1697474/step/5?unit=1720850
# https://kompege.ru/task  № ***
from functools import lru_cache
@lru_cache()
def f(n):
    if n == 1:
        return 1
    return 2 * n * f(n - 1)

[f(n) for n in range(1, 2026)]
print((f(2024) // 16 - f(2023)) // f(2022))  # 1019592


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


# https://stepik.org/lesson/1697474/step/7?unit=1720850
# https://kompege.ru/task  № ***
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 10:
        return n
    return 3 * n + f(n - 3)

[f(n) for n in range(9, 6251)]
print((f(6250) + 2 * f(6244)) // f(6238))  # 3


# https://stepik.org/lesson/1697474/step/8?unit=1720850
# https://kompege.ru/task  № 23756 Демоверсия 2026 (Уровень: Базовый)
from functools import lru_cache
@lru_cache(None)
def g(n):
    if n < 10:
        return 2 * n
    return g(n - 2) + 1

def f(n):
    return 2 * (g(n - 3) + 8)

[g(n) for n in range(9, 15549)]
print(f(15548))  # 15588


# https://stepik.org/lesson/1697474/step/9?unit=1720850
# https://kompege.ru/task  № 23375 Резервный день 19.06.25 (Уровень: Базовый)
from functools import lru_cache
@lru_cache(None)
def g(n):
    if n <= 9:
        return 3 * n
    return g(n - 4) + 2

def f(n):
    return g(n - 1) + g(n - 3)

[g(n) for n in range(9, 43000)]
print(f(42999))  # 43032


# https://stepik.org/lesson/1697474/step/10?unit=1720850
# https://kompege.ru/task  № 23275 Основная волна 11.06.25 (Уровень: Базовый)
from functools import lru_cache
@lru_cache(None)
def g(n):
    if n < 10:
        return 2 * n
    return g(n - 2) + 1

def f(n):
    return 2 * (g(n - 3) + 8)

[g(n) for n in range(9, 15549)]
print(f(15548))  # 15588



""""""
""" Варианты """
# 28.1 Вариант 1 | Часть 1
# https://stepik.org/lesson/1729565/step/4?unit=1753394
#  https://kompege.ru/task  № 17872 Демоверсия 2025 (Уровень: Базовый)
from functools import lru_cache
@lru_cache()
def f(n):
    if n == 1:
        return 1
    return (n - 1) * f(n - 1)

[f(i) for i in range(1, 2025)]
print((f(2024) + 2 * f(2023)) / f(2022))  # 4094550


# 29.1 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/4?unit=1753726
# https://kompege.ru/task  № 19248 ЕГКР 21.12.24 (Уровень: Базовый)
from functools import *
@lru_cache()
def f(n):
    if n < 5:
        return n
    return 2*n * f(n-4)

[f(i) for i in range(1, 13766)]
print((f(13766) - 9 * f(13762)) // f(13758))  # 757543052


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730528/step/4?unit=1754357
# https://kompege.ru/task  № 17872 Демоверсия 2025 (Уровень: Базовый)
from functools import lru_cache
@lru_cache()
def f(n):
    if n == 1:
        return 1
    return (n-1) * f(n-1)

[f(n) for n in range(1, 2025)]
print((f(2024) + 2 * f(2023)) // f(2022))  # 4094550


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/4?unit=1760676
# https://kompege.ru/task  № 21415 Досрочная волна 2025 (Уровень: Базовый)
from functools import *
@lru_cache()
def f(n):
    if n <= 5:
        return 1
    return n + f(n-2)

[f(i) for i in range(2127)]
print(f(2126) - f(2122))  # 4250


# 32.2 Вариант 5 | Часть 2
# https://stepik.org/lesson/1754189/step/4?unit=17786487
# https://kompege.ru/task  № 21711 ЕГКР 19.04.25 (Уровень: Базовый)
from functools import lru_cache
@lru_cache()
def f(n):
    if n < 20:
        return n
    return (n - 6) * f(n - 7)

[f(i) for i in range(20, 47873)]
print((f(47872) - 290 * f(47865)) / f(47858))  # 2276939784


# 33.2 Вариант 6 | Часть 2
# https://stepik.org/lesson/1943171/step/4?unit=1969925
# https://kompege.ru/task  № 23200 Основная волна 10.06.25 (Уровень: Базовый)
from functools import *
@lru_cache(None)
def f(n):
    if n < 10:
        return n
    return 3*n + f(n - 3)

[f(i) for i in range(6251)]
print( (f(6250) + 2*f(6244)) // f(6238) )  # 3


# 34.2 Вариант 7 | Часть 2
# https://stepik.org/lesson/1943174/step/4?unit=1969928
# https://kompege.ru/task  № 23275 Основная волна 11.06.25 (Уровень: Базовый)
from functools import *
@lru_cache()
def g(n):
    if n < 10:
        return 2 * n
    return g(n - 2) + 1

def f(n):
    return 2 * (g(n - 3) + 8)

[g(i) for i in range(15_600)]
print(f(15_548))  # 15588


# 35.2 Вариант 8 | Часть 2
# https://stepik.org/lesson/1943181/step/4?unit=1969936
# https://kompege.ru/task  № 23562 Пересдача 03.07.25 (Уровень: Базовый)
from functools import *
@lru_cache(None)
def g(n):
    if n <= 9:
        return 3 * n
    return g(n - 2) + 1

def f(n):
    return g(n-1)

[g(i) for i in range(1, 48000)]
print(f(47995))  # 24017


