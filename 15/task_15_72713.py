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


# https://stepik.org/lesson/371198/step/8?unit=358729
def f(x):
    p = 30 <= x <= 45
    q = 40 <= x <= 55
    a = a1 <= x <= a2
    return (a or (not p)) and (q <= a)

d = [y for x in (30, 45, 40, 55) for y in (x-0.1, x, x+0.1)]
res = 1000
for a1 in d:
    for a2 in d:
        if a2-a1 >= 0:
            if all(f(x) for x in range(100)):
                res = min(res, a2-a1)
print(round(res))  # 40


# https://stepik.org/lesson/371198/step/11?unit=358729
def f(x):
    p = 1 <= x <= 39
    q = 23 <= x <= 58
    a = a1 <= x <= a2
    return p and q or not a

d = [y for x in (1, 39, 23, 58) for y in (x-0.1, x, x+0.1)]
res = 0
for a1 in d:
    for a2 in d:
        if a2-a1 >= 0:
            if all(f(x) for x in range(1000)):
                res = max(res, a2-a1)
print(round(res))  # 16


# https://stepik.org/lesson/592529/step/4?unit=588579
def f(x):
    p = 0 <= x <= 10
    q = 25 <= x <= 50
    a = a1 <= x <= a2
    return a or not (p or q)

d = [y for x in (0, 10, 25, 50) for y in (x-0.1, x, x+0.1)]
res = 100
for a1 in d:
    for a2 in d:
        if a2-a1 >= 0 and all(f(x) for x in range(1000)):
            res = min(res, a2-a1)
print(round(res))  # 50


# https://stepik.org/lesson/592529/step/7?unit=588579
def f(x):
    p = 21 <= x <= 25
    q = 8 <= x <= 35
    a = a1 <= x <= a2
    return (p or not q) <= (not a)

d = [y for x in (21, 25, 8, 35) for y in (x-0.1, x, x+0.1)]
res = 0
for a1 in d:
    for a2 in d:
        if a2-a1 >= 0 and all(f(x) for x in range(1000)):
            res = max(sum(not i%2 for i in range(round(a1), round(a2)+1)), res)
print(res) # 7



# https://stepik.org/lesson/545274/step/3?unit=538821
def f(x, y):
    return ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))

for a in range(150, -1, -1):
    if all(f(x, y) for y in range(500) for x in range(500)):
        print(a)
        break


# https://stepik.org/lesson/545274/step/9?unit=538821
def f(x):
    # return ((x in a) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in a))
    return ((not x in a) or (x**2 <= 100)) and (x**2 > 64 or (x in a))

a = set(range(-500, 501))
for x in range(-500, 501):
    if not f(x):
        a.remove(x)
print(len(a) - 1)  # 20  (точек на одну больше, чеи длина отрезка с этими точками)


# https://stepik.org/lesson/545274/step/10?unit=538821
def f(x):
    return ((not x in a) or (x**2 <= 100)) and (x**2 > 64 or (x in a))

a = set()
for x in range(-500, 501):
    if not f(x):
        a |= {x}
print(len(a) - 1)  # 16  (точек на одну больше, чеи длина отрезка с этими точками)


# https://stepik.org/lesson/545355/step/3?unit=538898
def f(x):
    # return ((x&28 != 0) or (x&45 != 0)) <= ((x&48 == 0) <= (x&a != 0))
    return not x&28 and not x&45 or x&48 or x&a

for a in range(1000):
    if all(f(x) for x in range(1000)):
        print(a)
        break


# https://stepik.org/lesson/683089/step/3?unit=682018
def f(x, y):
    return (x <= 14 or x**2 > a) and ((y**2 <= a) or y >= 11)

c = 0
for a in range(100, 300):
    c += all(f(x, y) for x in range(100) for y in range(100))
print(c)  # 125



