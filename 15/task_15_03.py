""""""
"""
Task 15
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""

""" Задачи на отрезки """

""" 2.2 тест № 1 (продолжение) """
# https://stepik.org/lesson/1594773/step/2?thread=solutions&unit=1616347
# course_228948/pic_001
for x in [_ * 0.5 for _ in range(-100, 100)]:
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    f = (p <= ((q and 1) <= (not p)))
    if f == 0:
        print(x)  # 19



""" 2.5 тест № 2 (продолжение) """
# https://stepik.org/lesson/1599364/step/2?unit=1621008
def fn(a):
    # x  и  y   могут быть и дробными !!!
    for x in [_ * 0.5 for _ in range(1000)]:
        for y in [_ * 0.5 for _ in range(1000)]:
            if not (((x + y) <= 24) or (y <= (x - 2)) or (y >= a)):
                return 0
    return 1

for a in range(100, 0, -1):
    if fn(a):
        print(a)  # 11
        break


# https://stepik.org/lesson/1609596/step/2?unit=1631352
def fn(n):
    for x in range(1000):
        for y in range(1000):
            f = (x*y<a) or (x<y) or (9<x)
            if not f: return 0
    return 1

for a in range(100):
    if fn(a):
        print(a)  # 82
        break

