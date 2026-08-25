""""""
"""
task 15
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""


# https://stepik.org/lesson/371198/step/5?unit=358729
def f(x):
    p = 23 <= x <= 58
    q = 1 <= x <= 39
    a = a1 <= x <= a2
    return (p or a) <= (q or a)

d = [y for x in (23, 58, 1, 39) for y in (x-0.1, x, x+0.1)]
res = 1000
for a1 in d:
    for a2 in d:
        if a2-a1 >= 0:
            if all(f(x) for x in range(100)):
                res = min(res, a2-a1)
print(round(res))  # 19


# https://stepik.org/lesson/371198/step/6?unit=358729
def f(x):
    p = 12 <= x <= 62
    q = 52 <= x <= 92
    a = a1 <= x <= a2
    return not (not a and p) or q

d = [y for x in (12, 62, 52, 92) for y in (x-0.1, x, x+0.1)]
res = 1000
for a1 in d:
    for a2 in d:
        if a2-a1 >= 0:
            if all(f(x) for x in range(100)):
                res = min(res, a2-a1)
print(round(res))  # 40

