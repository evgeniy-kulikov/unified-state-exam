""""""
"""
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
"""

# https://stepik.org/lesson/1135852/step/1?unit=1147482
# https://stepik.org/lesson/1135852/step/2?unit=1147482
# https://stepik.org/lesson/1135852/step/3?unit=1147482

def f(s, mv):
    if s > 33:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+1, mv-1), f(s+2, mv-1), f(s+3, mv-1), f(s*2, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 34) if f(s, 2)])  # 16
print([s for s in range(1, 34) if f(s, 3) and not f(s, 1)])  # 8 15
print(*[s for s in range(1, 34) if f(s, 4) and not f(s, 2)])  # 12


# https://stepik.org/lesson/1135852/step/4?unit=1147482
# https://stepik.org/lesson/1135852/step/5?unit=1147482
# https://stepik.org/lesson/1135852/step/6?unit=1147482
def f(s, mv):
    if 36 <= s <= 60:
        return not mv % 2
    """
    Игра с перелетом. Перелетевший игрок дает победу противнику
    """
    if s > 60:
        return not (mv - 1) % 2
    if not mv:
        return 0
    g = [f(s+1, mv-1), f(s*2, mv-1), f(s*3, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 36) if f(s, 2)])  # 34
print([s for s in range(1, 36) if f(s, 3) and not f(s, 1)])  # 33  >>> 1 значение
print(*[s for s in range(1, 36) if f(s, 4) and not f(s, 2)])  # 11 32


# https://stepik.org/lesson/1135852/step/10?unit=1147482
# https://stepik.org/lesson/1135852/step/11?unit=1147482
# https://stepik.org/lesson/1135852/step/12?unit=1147482
def f(s, mv, w=eval('all')):
    if s >= 100:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+7, mv-1), f(s*2, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 100) if f(s, 2, eval('any'))][-1])  # 92
print(43, 44)  # ручное решение  43 44
print([s for s in range(1, 100) if f(s, 4) and not f(s, 2)][0])  # 29
