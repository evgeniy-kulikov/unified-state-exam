""""""
"""
Task 23
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
"""


""" 1.2 Повторение 2 часть """
# https://stepik.org/lesson/1341300/step/12?unit=1356964
from functools import lru_cache
@lru_cache(None)
def f(st, end):
    if st == end:
        return 1
    if st == 100 or st > end:
        return 0
    cnt = 0
    if st % 10:
        cnt += f(st + st % 10, end)
    if st % 68:
        cnt += f(st + st % 68, end)
    cnt += f(st ** 2, end)
    return cnt

# [f(68, x) for x in range(68, 681)]
print(f(2, 68) * f(68, 680))  # 47997789947424


""" 13.1 Задачи на составление путей программ """
# https://stepik.org/lesson/1149683/step/1?unit=1161670
def f(st, end):
    if st == end:
        return 1
    if st < end:
        return 0
    return f(st - 2, end) + f(st - 5, end)

print(f(23, 2))  # 29


# https://stepik.org/lesson/1149683/step/2?unit=1161670
def f(st, end):
    if st == end:
        return 1
    if st < end:
        return 0
    return f(st - 1, end) + f(st - 3, end) + f(st // 3, end)

print(f(22, 2))  # 2196


# https://stepik.org/lesson/1149683/step/3?unit=1161670
def f(st, end):
    if st == end:
        return 1
    if st > end:
        return 0
    return f(st + 1, end) + f(st * 2, end)

print(f(1, 10) * f(10, 20))  # 28


# https://stepik.org/lesson/1149683/step/4?unit=1161670
def f(st, end):
    if st == end:
        return 1
    if st > end:
        return 0
    return f(st + 1, end) + f(st + 3, end) + f(st * 2, end)

print(f(3, 9) * f(9, 12) * f(12, 20))  # 234


# https://stepik.org/lesson/1149683/step/6?unit=1161670
def f(st, end):
    if st == end:
        return 1
    if st > end or st == 11 or st == 18:
        return 0
    return f(st + 1, end) + f(st + 2, end) + f(st * 3, end)

print(f(4, 8) * f(8, 23))  # 400


# https://stepik.org/lesson/1149683/step/8?unit=1161670
def f(st, end):
    if st == end:
        return 1
    if st > end:
        return 0
    if not st % 2:
        return f(int(st * 1.5), end) + f(st + 1, end)
    return f(st + 1, end)

print(f(1, 20))


# https://stepik.org/lesson/1149683/step/9?unit=1161670
# Определите число, для получения которого из числа 31 существует 1001 программа
def f(st, end):
    if st == end:
        return 1
    if st > end:
        return 0
    return f(st + 2, end) + f(st + 4, end) + f(st + 5, end)

for n in range(100):
    if f(31, n) == 1001:
        print(n)  # 56
        break


# https://stepik.org/lesson/1149683/step/10?unit=1161670
def f(st, end, cnt):
    if st > end:
        return 0
    if st == end and cnt:
        return 0
    if st == end and not cnt:
        return 1
    return f(st + 1, end, cnt - 1) + f(st + 4, end, cnt - 1) + f(st * 2, end, cnt - 1)

print(f(3, 27, 7))  # 37


# https://stepik.org/lesson/1149683/step/11?unit=1161670
# Т.к. нужно кол-во различных результатов (а не их значения), то в другую СС переводить не нужно
res = set()

def f(st, cnt):
    if cnt == 0:
        res.add(st)
        # return None
        return
    f(st * 2, cnt - 1)
    f(st * 2 + 1, cnt - 1)

f(1, 15)
print(len(res))  # 32768

# variant
res = set()
def f(st, cnt):
    if cnt == 0:
        res.add(st)
        return 0
    return f(st * 2, cnt - 1) + f(st * 2 + 1, cnt - 1)

f(1, 15)
print(len(res))  # 32768


# https://stepik.org/lesson/1149683/step/12?unit=1161670
def f(st, end, flag=False):
    if st > end:
        return 0
    if st == end:
        return 1
    if flag:
        return f(st + 1, end) + f(st + 2, end)
    return f(st + 1, end) + f(st + 2, end) + f(st * 2, end, True)

print(f(1, 15))  # 1545


# https://stepik.org/lesson/1149683/step/13?unit=1161670
def f(st, end, cnt):
    if st > end:
        return 0
    if st == end:
        return cnt == 1
    return f(st + 1, end, cnt) + f(st + 2, end, cnt) + f(st * 2, end, cnt + 1)

print(f(2, 12, 0))  # 68


# https://stepik.org/lesson/1149683/step/14?unit=1161670
def f(st, end, cnt):
    if st > end:
        return 0
    if st == end:
        return cnt <= 3
    return f(st + 2, end, cnt) + f(st * 3, end, cnt + 1) + f(st * 5, end, cnt + 1)

print(f(2, 200, 0))  # 793


# https://stepik.org/lesson/1149683/step/15?unit=1161670
def f(st, end, cnt):
    cnt += not st % 2
    if st > end:
        return 0
    if st == end:
        return cnt == 6
    return f(st + 1, end, cnt) + f(st + 3, end, cnt) + f(st + 5, end, cnt)

print(f(3, 25, 0))  # 3432

