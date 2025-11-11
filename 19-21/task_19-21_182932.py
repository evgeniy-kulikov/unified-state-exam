""""""
"""
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
"""

""" 11.1 Задачи на теорию игр. Одна куча камней. """
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


# https://stepik.org/lesson/1135852/step/7?unit=1147482
# https://stepik.org/lesson/1135852/step/8?unit=1147482
# https://stepik.org/lesson/1135852/step/9?unit=1147482
def f(s, mv):
    if s >= 129:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+1,mv-1), f(s*2,mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 129) if f(s, 2)])  # 64
print(*[s for s in range(1, 129) if f(s, 3)][:2])  # 32 63
print([s for s in range(1, 129) if f(s, 4) and not f(s, 2)][0])  # 62


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


# https://stepik.org/lesson/1342070/step/10?unit=1357751
def f(a, b, mv, w=eval('all')):
    if a + b >= 123:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+1, b, mv-1), f(a*2, b, mv-1), f(a, b+1, mv-1), f(a, b*2, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return w(g)

print([i for i in range(1, 110) if f(13, i, 2, w=eval('any'))][0])  # 28
print(*[i for i in range(1, 110) if f(13, i, 3)][:2])  # 48 54
print([i for i in range(1, 110) if not f(13, i, 2) and f(13, i, 4)][0])  # 47


# https://stepik.org/lesson/1342070/step/11?unit=1357751
def f(a, b, mv, w=eval('all')):
    if a * b >= 385:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+5, b, mv-1), f(a*2, b, mv-1), f(a, b+5, mv-1), f(a, b*2, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return w(g)

print([i for i in range(1, 55) if f(8, i, 2, w=eval('any'))][0])  # 13
print(min(i for i in range(1, 55) if f(8, i, 3) and not f(8, i, 1)),
      max(i for i in range(1, 55) if f(8, i, 3) and not f(8, i, 1)))  # 10 19
print([i for i in range(1, 55) if not f(8, i, 2) and f(8, i, 4)][0])  # 6


# https://stepik.org/lesson/1342070/step/12?unit=1357751
def f(a, b, mv):
    if a + b >= 275:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+3, b, mv-1), f(a+7, b, mv-1), f(a*4, b, mv-1),
         f(a, b+3, mv-1), f(a, b+7, mv-1), f(a, b*4, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return all(g)

print([i for i in range(1, 216) if f(58, i, 2)][0])  # 40
print(min(i for i in range(1, 216) if f(58, i, 3) and not f(58, i, 1)),
      max(i for i in range(1, 216) if f(58, i, 3) and not f(58, i, 1)))  # 10 39
print([i for i in range(1, 216) if not f(58, i, 2) and f(58, i, 4)][0])  # 7



""" 11.2 Задачи на теорию игр. Две кучи камней. """
# https://stepik.org/lesson/1135853/step/1?unit=1147483
# https://stepik.org/lesson/1135853/step/2?unit=1147483
# https://stepik.org/lesson/1135853/step/3?unit=1147483
def f(a, b, mv, w=eval('all')):
    if a+b >= 77:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+1,b,mv-1), f(a*2,b,mv-1), f(a,b+1,mv-1), f(a,b*2,mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 70) if f(7, s, 2, eval('any'))][0])  # 18
print(*[s for s in range(1, 70) if f(7, s, 3)][:2])  # 31 34
print([s for s in range(1, 70) if f(7, s, 4)][0])  # 30


# https://stepik.org/lesson/1135853/step/4?unit=1147483
# https://stepik.org/lesson/1135853/step/5?unit=1147483
# https://stepik.org/lesson/1135853/step/6?unit=1147483
def f(a, b, mv, w=eval('all')):
    if a+b >= 342:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+2,b,mv-1), f(a*5,b,mv-1), f(a,b+2,mv-1), f(a,b*5,mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 326) if f(11, s, 2, eval('any'))][0])  # 14
print(*[s for s in range(1, 326) if f(11, s, 3)][:2])  # 57 64
print([s for s in range(1, 326) if f(11, s, 4)][0])  # 65


""" оригинальное условие """
# https://stepik.org/lesson/1135853/step/7?unit=1147483
# https://stepik.org/lesson/1135853/step/8?unit=1147483
# https://stepik.org/lesson/1135853/step/9?unit=1147483
def f(x, y, mv, w=eval('all')):
    if (x**2 + y**2)**0.5 >= 13:
        return not mv % 2
    if not mv:
        return 0
    g = [f(x+3, y, mv-1), f(x, y+3, mv-1), f(x, y+4, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 13) if f(s, 2, 2, eval('any'))][0])  # 7
print(*[s for s in range(1, 13) if f(s, 2, 3)][:2])  # 6 7
print([s for s in range(1, 13) if f(s, 2, 4)][0])  # 3


# https://stepik.org/lesson/1135853/step/10?unit=1147483
# https://stepik.org/lesson/1135853/step/11?unit=1147483
# https://stepik.org/lesson/1135853/step/12?unit=1147483
def f(a, b, mv, w=eval('all')):
    if a * b >= 455:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+1, b, mv-1), f(a*2, b, mv-1),
         f(a, b+1, mv-1), f(a, b*2, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 90) if f(s, 5, 2, eval('any'))][0])  # 23
print(*[s for s in range(1, 90) if f(s, 5, 3) and not f(s, 5, 1)][-2:])  # 37 44
print([s for s in range(1, 90) if f(s, 5, 4) and not f(s, 5, 2)][0])  # 36


