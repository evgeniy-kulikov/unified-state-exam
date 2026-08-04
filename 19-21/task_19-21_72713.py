""""""
"""
task 19-21
https://stepik.org/course/72713/syllabus
Подготовка к ЕГЭ по информатике
"""



# https://stepik.org/lesson/727346/step/12?unit=729958
# https://stepik.org/lesson/727346/step/13?unit=729958
# https://stepik.org/lesson/727346/step/14?unit=729958
def f(a, b, mv, w=1):
    if a+b >= 77:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+1, b, mv-1), f(a + b*2, b, mv-1), f(a, b+1, mv-1), f(a, b + a*2, mv-1)]
    if mv % 2:
        return any(g)
    return all(g) if w else any(g)

print([s for s in range(1, 68) if f(9, s,2, 0)][0])
print(*[s for s in range(1, 68) if f(9, s,3) and not f(9, s, 1)][:2])
print([s for s in range(1, 68) if f(9, s,4) and not f(9, s, 2)][0])
"""
5
7 22
21
"""


# https://stepik.org/lesson/897802/step/8?unit=903508
# https://stepik.org/lesson/897802/step/9?unit=903508
# https://stepik.org/lesson/897802/step/10?unit=903508
def f(a, mv, w=1):
    if a >= 102:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+1, mv-1), f(a*2, mv-1)]
    if mv % 2:
        return any(g)
    return all(g) if w else any(g)

print([s for s in range(1, 102) if f(s,2, 0)][0])
print(*[s for s in range(1, 102) if f(s,3) and not f(s, 1)][:2])
print([s for s in range(1, 102) if f(s,4) and not f(s, 2)][0])
"""
26
25 49
48
"""



