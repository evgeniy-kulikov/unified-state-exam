"""
Task 23
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 13.1 Количество путей в графе """

# https://stepik.org/lesson/608587/step/15?unit=603786
def fn(st, end):
    if st > end or st == 8:  return 0  # не содержит число 8
    if st == end: return 1
    return fn(st + 1, end) + fn(st * 2, end)
print(fn(2, 20) * fn(20, 40))  # содержит число 20
# 20

""" 13.2 Рекурсивные функции для задания 23 """

# https://stepik.org/lesson/559867/step/4?unit=553912
def fn(st, end):
    if st > end:  return 0
    if st == end: return 1
    return fn(st + 1, end) + fn(st * 2, end)
print(fn(1, 15))  # 26


# https://stepik.org/lesson/559867/step/5?unit=553912
def fn(st, end):
    if st > end:  return 0
    if st == end: return 1
    return fn(st + 1, end) + fn(st * 3, end)
print(fn(2, 18))  # 7


# https://stepik.org/lesson/559867/step/6?unit=553912
def fn(st, end):
    if st > end:  return 0
    if st == end: return 1
    return fn(st + 1, end) + fn(st * 3, end) + fn(st * 4, end)
print(fn(3, 24)) # 11


# https://stepik.org/lesson/559867/step/10?unit=553912
def fn(st, end):
    if st > end:  return 0
    if st == end: return 1
    return fn(st + 1, end) + fn(st * 2, end)  + fn(st ** 2, end)
print(fn(2, 27))  # 92



""" 13.3 Задание 23 КЕГЭ. Часть 1 """

# https://stepik.org/lesson/569846/step/5?unit=564380
def fn(cur, end):
    if cur > end: return 0
    if cur == end: return 1
    return fn(cur + 1, end) + fn(cur * 2, end)
print(fn(1, 10) * fn(10, 15)) # 14


# https://stepik.org/lesson/569846/step/8?unit=564380
def fn(cur, end):
    if cur > end or cur == 14: return 0
    if cur == end: return 1
    return fn(cur + 1, end) + fn(cur + 3, end) + fn(cur * 2, end)
print(fn(4, 28))


# https://stepik.org/lesson/569846/step/10?unit=564380
def fn(cur, end):
    if cur > end or cur == 40: return 0
    if cur == end: return 1
    return fn(cur + 2, end) + fn(cur * 2, end)
print(fn(2, 10) * fn(10, 48)) # 20


# https://stepik.org/lesson/569846/step/15?unit=564380
def fn(cur, end):
    if cur < end or cur in (9, 16): return 0
    if cur == end: return 1
    return fn(cur - 1, end) + fn(cur - 2, end) + fn(cur // 3, end)
print(fn(19, 3))  # 180



""" 13.4 Задание 23 КЕГЭ. Часть 2 """

# https://stepik.org/lesson/900196/step/3?unit=905265
def fn(cur, end):
    if cur > end: return 0
    if cur == end: return 1
    return fn(cur + 1, end) + fn(cur * 2, end)
print(fn(5, 10) + fn(5, 22))  # 12


# https://stepik.org/lesson/900196/step/4?unit=905265
def fn(cur, end):
    if cur > end: return 0
    if cur == end: return 1
    return fn(cur + 1, end) + fn(cur * 3, end)
print(fn(5, 15) + fn(5, 46))  # 15


# https://stepik.org/lesson/900196/step/6?unit=905265
# РЕШЕНИЕ НЕ НАЙДЕНО !!!!
def fn(cur, end):
    if cur > end: return 0
    if cur == end: return 1
    return fn(cur + 1, end) + fn(cur + 5, end)
print(fn(1, 29))  # 1326


# https://stepik.org/lesson/900196/step/8?unit=905265
def fn(cur, end):
    if cur < end: return 0
    if cur == end: return 1
    return fn(cur - 1, end) + fn(cur - 3, end) + fn(cur % 4, end)
print(fn(22, 3))  # 1113


# https://stepik.org/lesson/900196/step/9?unit=905265
def fn(cur, end):
    if cur < end: return 0
    if cur == end: return 1
    res = fn(cur - 1, end) + fn(cur - 3, end)
    if cur > 4:
        res += fn(cur % 4, end)
    return res
print(fn(22, 2))  # 1873


# https://stepik.org/lesson/900196/step/10?unit=905265
def fn(cur, end):
    if cur < end: return 0
    if cur == end: return 1
    res = fn(cur - 1, end) + fn(cur - 2, end)
    if not cur % 4:
        res += fn(cur // 4, end)
    return res
print(fn(22, 2))  # 11677

# Идем с обратной стороны (исключаем проверку на делимость)
def fn(cur, end):
    if cur > end: return 0
    if cur == end: return 1
    res = fn(cur + 1, end) + fn(cur + 2, end) + fn(cur * 4, end)
    return res
print(fn(2, 22))  # 11677


# https://stepik.org/lesson/900196/step/11?unit=905265
def fn(cur, end):
    if cur < end: return 0
    if cur == end: return 1
    return fn(cur - 1, end) + fn(cur // 2, end)
print(fn(30, 8) * fn(8, 1))  # 288


# https://stepik.org/lesson/900196/step/13?unit=905265
def fn(cur, end):
    if cur > end: return 0
    if cur == end: return 1
    return fn(cur + 1, end) + fn(cur * 2, end) + fn(cur * 2 + 1, end)
print(fn(int('10', 2), int('1110110', 2)))  # 91560


# https://stepik.org/lesson/900196/step/15?unit=905265
def fn(cur, end):
    if cur < end: return 0
    if cur == end: return 1
    return fn(cur - 1, end) + fn(cur // 2, end)
print(fn(int('100001', 2), int('100', 2)))  # 119


# https://stepik.org/lesson/900196/step/16?unit=905265
def fn(cur, end):
    if cur > end: return 0
    if cur == end: return 1
    return fn(cur + 2, end) + fn(cur + 3, end) + fn(cur * 4, end)
print(fn(int('1', 4), int('100', 4)))  # 43


""" 13.5 Задание 23 КЕГЭ. Часть 3 """

# https://stepik.org/lesson/902769/step/2?unit=907940
def fn(st, end):
    if st > end: return 0
    if st == end: return 1
    return fn(st + 2, end) + fn(st + 5, end)

for i in range(5 + 1, 100):
    if fn(5, i) == 34:
        print(i)  # 27
        break

# Вариант
a = [0] * 101
a[5] = 1
for i in range(6, 101):
    a[i] += a[i - 2] + a[i - 5]
print(a.index(34))


# https://stepik.org/lesson/902769/step/3?unit=907940
def fn(st, end):
    if st > end: return 0
    if st == end: return 1
    return fn(st + 2, end) + fn(st + 4, end) + fn(st + 5, end)

for i in range(32, 100):
    if fn(31, i) == 1001:
        print(i)  # 56
        break


# https://stepik.org/lesson/902769/step/4?unit=907940
from functools import lru_cache

@lru_cache(None)
def fn(st, end):
    if st > end: return 0
    if st == end: return 1
    return fn(st + 2, end) + fn(st * 2, end) + fn(st + 5, end)

ls = []
for i in range(13, 1000):
    if fn(12, i) == 60:
        ls.append(i)  # Избыточный подход
        # print(i)  # Достаточный подход
        # break

print(min(ls))  # 36


# https://stepik.org/lesson/902769/step/6?unit=907940
def fn(st, end, cnt):
    if st > end: return 0
    if st == end and cnt: return 0
    if st == end and not cnt: return 1
    return fn(st + 1, end, cnt - 1) + fn(st + 2, end, cnt - 1) + fn(st + 3, end, cnt - 1)

print(fn(3, 22, 7))  # 28


# https://stepik.org/lesson/902769/step/7?unit=907940
def fn(st, end, cnt):
    if st > end: return 0
    if st == end and cnt: return 0
    if st == end and not cnt: return 1
    return fn(st + 1, end, cnt - 1) + fn(st * 2, end, cnt - 1) + fn(st * 3, end, cnt - 1)

print(fn(1, 34, 8))  # 21


# https://stepik.org/lesson/902769/step/8?unit=907940
def fn(st, end, cnt):
    if st > end: return 0
    if st == end and cnt: return 0
    if st == end and not cnt: return 1
    return fn(st + 1, end, cnt - 1) + fn(st + 2, end, cnt - 1) + fn(st * 2, end, cnt - 1)

print(fn(1, 20, 6))  # 36


# https://stepik.org/lesson/902769/step/10?unit=907940
"""
В данном случае нельзя использовать функцию lru_cache, 
иначе многие промежуточные значения функции НЕ будут вычисляются внутри функции, 
а забираться из кэша lru_cache
"""
def fn(st, end, cnt):
    # 10 - ручное ограничение верхней границы значений списка (уменьшаем расчеты)
    if st > end or cnt > 10: return 0
    if st == end: ls.append(cnt)
    return fn(st + 1, end, cnt + 1) + fn(st + 5, end, cnt + 1) + fn(st * 3, end, cnt + 1)

ls = []
fn(1, 227, 0)
print(min(ls))  # 7


# https://stepik.org/lesson/902769/step/11?unit=907940
def fn(st, end, cnt):
    # 10 - ручное ограничение верхней границы значений списка (уменьшаем расчеты)
    if st > end or cnt > 10: return 0
    if st == end: ls.append(cnt)
    return fn(st + 1, end, cnt + 1) + fn(st + 3, end, cnt + 1) + fn(st * 2, end, cnt + 1)

ls = []
fn(1, 172, 0)
print(min(ls))  # 8


# https://stepik.org/lesson/902769/step/12?unit=907940
def fn(st, end, cnt):
    # 10 - ручное ограничение верхней границы значений списка (уменьшаем расчеты)
    if st > end or cnt > 10: return 0
    if st == end: ls.append(cnt)
    return fn(st + 1, end, cnt + 1) + fn(st + 2, end, cnt + 1) + fn(st * 2, end, cnt + 1)

ls = []
fn(1, 8, 0)
print(ls.count(min(ls)))  # 6


# https://stepik.org/lesson/902769/step/13?unit=907940
def fn(st, cnt):
    if not cnt: ls.add(st)
    else:
        fn(st + 1, cnt - 1)
        fn(st + 5, cnt - 1)
        fn(st * 3, cnt - 1)

ls = set()
fn(1, 4)
print(len(ls))  # 43


# https://stepik.org/lesson/902769/step/14?unit=907940
def fn(st, cnt):
    if not cnt:
        if 34 <= st <= 59:
            ls.add(st)
    else:
        fn(st + 1, cnt - 1)
        fn(st + 2, cnt - 1)
        fn(st * 2, cnt - 1)

ls = set()
fn(1, 6)
print(len(ls))  # 11


# https://stepik.org/lesson/902769/step/15?unit=907940
def fn(st, cnt):
    if not cnt:
        if 1000 <= st <= 1024:
            ls.add(st)
    else:
        fn(st + 1, cnt - 1)
        fn(st + 5, cnt - 1)
        fn(st * 3, cnt - 1)

ls = set()
fn(1, 8)
print(len(ls))  # 1




