""""""
"""
Task 23
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 23.1 Задание 23 ЕГЭ | Урок 1 """
# https://stepik.org/lesson/1715370/step/3?unit=1738823
# https://kompege.ru/task   № 413 (Уровень: Базовый)
def f(st, en):
    if st == en:
        return 1
    if st > en:
        return 0
    return f(st + 1, en) + f(st+3, en) + f(st*2, en)
print(f(1, 15))  # 448


# https://stepik.org/lesson/1715370/step/4?unit=1738823
# https://kompege.ru/task   № 633 Джобс 02.11.2020 (Уровень: Базовый)
def f(st, en):
    if st == en:
        return 1
    if st > en:
        return 0
    return f(st + 1, en) + f(st*2, en) + f(st**2, en)
print(f(5, 154))  # 8966


# https://stepik.org/lesson/1715370/step/5?unit=1738823
# https://kompege.ru/task   № 2344 (Уровень: Базовый)
def f(st, en):
    if st > en:
        return 0
    if st == en:
        return 1
    return f(st + 1, en) + f(st + 2, en) + f(st * 4, en)
print(f(1, 13))  # 298


# https://stepik.org/lesson/1715370/step/6?unit=1738823
# https://kompege.ru/task   № 1301 Открытый вариант КЕГЭ (Уровень: Базовый)
def f(st, en):
    if st == en:
        return 1
    if st < en:
        return 0
    return f(st - 2, en) + f(st - 5, en)
print(f(23, 2))  # 29


# https://stepik.org/lesson/1715370/step/7?unit=1738823
# https://kompege.ru/task   № 313 Джобс 28.09.2020 (Уровень: Базовый)
def f(st, en):
    if st == en:
        return 1
    if st < en:
        return 0
    return f(st - 1, en) + f(st - 3, en) + f(st // 3, en)
print(f(22, 2))  # 2196


# https://stepik.org/lesson/1715370/step/8?unit=1738823
# https://kompege.ru/task   № 1974 Демоверсия 2022 (Уровень: Базовый)
def f(st, en):
    if st == en:
        return 1
    if st > en:
        return 0
    return f(st + 1, en) + f(st*2, en)

print(f(1, 10) * f(10, 20))  # 28


# https://stepik.org/lesson/1715370/step/9?unit=1738823
# https://kompege.ru/task   № 1037 100 базовых задач Е. Джобс (Уровень: Базовый)
def f(st, en):
    if st == en:
        return 1
    if st > en:
        return 0
    return f(st + 1, en) + f(st * 2, en)
print(f(1, 12) * f(12, 30))  # 100


# https://stepik.org/lesson/1715370/step/10?unit=1738823
# https://kompege.ru/task   № 65 Джобс 31.08.2020 (Уровень: Базовый)
def f(st,en):
    if st == en:
        return 1
    if st > en:
        return 0
    return f(st + 1, en) + f(st + 3, en) + f(st * 2, en)
print(f(3, 9) * f(9, 12) * f(12, 20)) # 234








""" 23.2 Задание 23 ЕГЭ | Урок 2 """
# https://stepik.org/lesson/1715371/step/1?unit=1738824
# https://kompege.ru/task   № 1076 (Уровень: Базовый)
def f(st, en):
    if st == en:
        return 1
    if st > en or st in (11, 18):
        return 0
    return f(st + 1, en) + f(st + 2, en) + f(st * 3, en)
print(f(4, 8) * f(8, 23))  # 400


# https://stepik.org/lesson/1715371/step/2?unit=1738824
# https://kompege.ru/task   № 104 Джобс 07.09.2020 (Уровень: Базовый)
def f(st, en):
    if st == en:
        return 1
    if st > en:
        return 0
    return f(st + 1, en) + f(st * 2, en) + f(st * 2 + 1, en) + f(st * 10, en)
print(f(1, 15))  # 84


# https://stepik.org/lesson/1715371/step/3?unit=1738824
# https://kompege.ru/task   № 473 Джобс 12.10.2020 (Уровень: Базовый)
def f(st, en):
    if st > en or st == 43:
        return 0
    if st == en:
        return 1
    if st < en:
        return f(st + 2, en) + f(st + st - 1, en) + f(st + st + 1, en)
print(f(7, 63))  # 116


# https://stepik.org/lesson/1715371/step/4?unit=1738824
# https://kompege.ru/task   № 1137 (Уровень: Сложный)
# Супер задача!!!
"""
Вспоминаем основы СС
n = 3   >>> int('11' , 2)
int(f'{n}' + '0', 2) == n * 2
int(f'{n}' + '1', 2) == n * 2 + 1
"""
def f(st, en):
    if st > en:
        return 0
    if st == en:
        return 1
    return f(st + 1, en) + f(st * 2, en) + f(st * 2 + 1, en)
print(f(int('100', 2), int('11101', 2)))  # 79


# https://stepik.org/lesson/1715371/step/5?unit=1738824
# https://kompege.ru/task   № 2342 (Уровень: Сложный)
# Супер задача!!!
def cnv(num):
    n = [*map(int, str(num))]
    for i in range(len(n)):
        if n[i] < 9:
            n[i] = str(n[i] + 1)
        else:
            n[i] = '9'
    return int(''.join(n))

def f(st, en):
    if st == en:
        return 1
    if st > en:
        return 0
    return f(st + 1, en) + f(cnv(st), en)
print(f(25, 51))  # 33


# https://stepik.org/lesson/1715371/step/6?unit=1738824
# https://kompege.ru/task   № 2343 (Уровень: Средний)
def f(st,en):
    if st == en:
        return 1
    if st > en:
        return 0
    if st % 2:
        return f(st + 1, en)
    return f(st + 1, en) + f(st * 1.5, en)

print(f(1, 20)) # 32


# https://stepik.org/lesson/1715371/step/7?unit=1738824
# https://kompege.ru/task   № 2340 (Уровень: Средний)
def f(st,en):
    if st == en:
        return 1
    if st > en:
        return 0
    return f(st + 2, en) + f(st + 4, en) + f(st + 5, en)

for i in range(32, 100):
    if f(31, i) == 1001:
        print(i)  # 56
        break






""" 23.3 Задание 23 ЕГЭ | Задачи прошлых лет """
# https://stepik.org/lesson/1715372/step/1?unit=1738825
# https://kompege.ru/task   № 9752 Основная волна 19.06.23 (Уровень: Базовый)
def f(st, en):
    if st > en or st == 17:
        return 0
    if st == en:
        return 1
    if st < en:
        return f(st + 2, en) + f(st + 3, en) + f(st * 2, en)
print(f(3, 10) * f(10, 25))  # 90


# https://stepik.org/lesson/1715372/step/2?unit=1738825
# https://kompege.ru/task   № 9790 Основная волна 20.06.23 (Уровень: Базовый)
def f(st, en):
    if st < en or st in (9, 16):
        return 0
    if st == en:
        return 1
    return f(st - 1, en) + f(st - 2, en) + f(st // 3, en)
print(f(19, 3))  # 180


# https://stepik.org/lesson/1715372/step/3?unit=1738825
# https://kompege.ru/task   № 17534 Основная волна 07.06.24 (Уровень: Базовый)
def f(st,en):
    if st == en:
        return 1
    if st < en:
        return 0
    return f(st - 1, en) + f(st // 2, en)
print(f(30, 8) * f(8, 1))  # 288


# https://stepik.org/lesson/1715372/step/4?unit=1738825
# https://kompege.ru/task   № 17562 Основная волна 08.06.24 (Уровень: Базовый)
def f(st,en):
    if st == en:
        return 1
    if st > en:
        return 0
    return f(st + 1, en) + f(st + 2, en) + f(st + 3, en)
print(f(5, 7) * f(7, 11))  # 14





""""""
""" Варианты """
# 29.1 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/9?unit=1753726
# https://kompege.ru/task  № 19253 ЕГКР 21.12.14 (Уровень: Базовый)
def f (st, en):
    if st < en or st == 24:
        return 0
    if st == en:
        return 1
    return f(st - 1, en) + f(st - 6, en) + f(st // 2, en)
print(f(34, 29) * f(29, 19) * f(19, 6))  # 115


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/9?unit=1760676
def f(st, en):
    if st == en:
        return 1
    if st > en or st == 35:
        return 0
    return f(st+1, en) + f(st+2, en) + f(st*2, en)
print(f(7, 13) * f(13, 15) * f(15, 51))  # 174034068


