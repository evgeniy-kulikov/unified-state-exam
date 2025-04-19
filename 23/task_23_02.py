"""
Task 23
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

# https://stepik.org/lesson/608587/step/15?unit=603786
def fn(st, end):
    if st > end or st == 8:  return 0  # не содержит число 8
    if st == end: return 1
    return fn(st + 1, end) + fn(st * 2, end)
print(fn(2, 20) * fn(20, 40))  # содержит число 20
# 20


# https://stepik.org/lesson/559867/step/4?unit=553912
def fn(st, end):
    if st > end:  return 0
    if st == end: return 1
    return fn(st + 1, end) + fn(st * 2, end)
print(fn(1, 15))  # 26


# https://stepik.org/lesson/559867/step/6?unit=553912
def fn(st, end):
    if st > end:  return 0
    if st == end: return 1
    return fn(st + 1, end) + fn(st * 3, end) + fn(st * 4, end)
print(fn(3, 24)) # 11


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



