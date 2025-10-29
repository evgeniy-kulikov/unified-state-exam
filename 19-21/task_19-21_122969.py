""""""
"""
Task 19-21
Подборка задач для подготовки к ЕГЭ по информатике 2026 | itpy
https://stepik.org/course/122969
"""

""" 3.7 Домашка: 19-21 номер. """
# https://stepik.org/lesson/1038794/step/2?unit=1062789
def f(s, mv):
    if s >= 55:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+1, mv-1),f(s+4, mv-1),f(s*3, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(1, 55) if f(s, 2)][0])  # 18
print(*[s for s in range(1, 55) if f(s, 3) and not f(s,1)][:2])  # 6 14
print([s for s in range(1, 55) if f(s, 4) and not f(s,2)][0])  # 13


# https://stepik.org/lesson/1038794/step/3?unit=1062789
def f(s, mv):
    if s >= 39:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+1, mv-1),f(s+3, mv-1),f(s*2, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(1, 39) if f(s, 2)][0])  # 19
print(*[s for s in range(1, 39) if f(s, 3) and not f(s,1)][:2])  # 16 18
print([s for s in range(1, 39) if f(s, 4) and not f(s,2)][0])  # 15


# https://stepik.org/lesson/1038794/step/4?unit=1062789
def f(a, b, mv, w=eval('all')):
    if a * b >= 455:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+1, b, mv-1), f(a*2, b, mv-1), f(a, b+1, mv-1), f(a, b*2, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 91) if f(5, s, 2, eval('any'))][0])  # 23
print(*[s for s in range(1, 91) if f(5, s, 3) and not f(5,s,1)][-2:])  # 37 44
print([s for s in range(1, 91) if f(5, s, 4) and not f(5,s,2)][0])  # 36


# https://stepik.org/lesson/1038794/step/10?unit=1062789
def f(a, mv):
    if a <= 30:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a-3, mv-1), f(a-5, mv-1), f(a//4, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(31, 500) if f(s, 2)][0])  # 124
print(*[s for s in range(31, 500) if f(s, 3) and not f(s,1)][:2])  # 127 128
print([s for s in range(31, 500) if f(s, 4) and not f(s,2)][0])  # 132


# https://stepik.org/lesson/1038794/step/16?unit=1062789
def f(a,b, mv, w=eval('all')):
    if a + b >= 88:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a + 1, b, mv - 1), f(a * 3, b, mv - 1), f(a, b + 1, mv - 1), f(a, b * 3, mv - 1)]
    if not (mv-1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 82) if f(6, s, 2, eval('any'))][0])  # 10
print(*[s for s in range(1, 82) if f(6, s, 3) and not f(6, s, 1)])  # 9 23 26
print([s for s in range(1, 82) if f(6, s, 4) and not f(6, s, 2)][0])  # 22
