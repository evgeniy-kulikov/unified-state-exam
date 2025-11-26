""""""
"""
Task 19-21
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""



""" https://stepik.org/lesson/1713458/step/2?unit=1736931 """
# https://stepik.org/lesson/1713458/step/2?unit=1736931
# https://kompege.ru/task   № 2364 (Уровень: Средний)
def f(s, mv):
    if s > 20:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s + 1, mv - 1), f(s + 2, mv - 1), f(s + 3, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print([s for s in range(1, 21) if f(s, 2)][0])  # 17
print(*[s for s in range(1, 21) if f(s, 5)][:3])  # 10 11 12
print(len([s for s in range(1, 21) if f(s, 10)]))  # 5
# print(len([s for s in range(1, 21) if f(s, 2) or f(s, 4) or f(s, 6) or f(s, 8) or f(s, 10)]))  # 5


# https://stepik.org/lesson/1713458/step/3?unit=1736931
# https://kompege.ru/task   № 2365 (Уровень: Сложный)
def f(s, mv, w=eval('all')):
    if not s:
        return not mv % 2
    if not mv:
        return 0
    if s == 1:
        g = [f(s - 1, mv - 1)]
    elif s in [2, 3]:
        g = [f(s - 1, mv - 1), f(s - 2, mv - 1)]
    else:
        g = [f(s - 1, mv - 1), f(s - 2, mv - 1), f(s - 4, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 16) if f(s, 2, eval('any'))][-1])  # 8
print(*[s for s in range(1, 16) if f(s, 5) and not f(s, 3)])  # 8 10
print([s for s in range(1, 16) if f(s, 10)][-1])  # 15


# https://stepik.org/lesson/1713458/step/4?unit=1736931
# https://kompege.ru/task   № 846 (Уровень: Базовый)
def f(s, mv, w=eval('all')):
    if s >= 65:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s + 1, mv - 1), f(s + 2, mv - 1), f(s * 3, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 65) if f(s, 2)][-1])  # 21
print(*[s for s in range(1, 65) if f(s, 3) and not f(s, 1)])  # 7 20
print(*[s for s in range(1, 65) if f(s, 4) and not f(s,2)])  # 18







