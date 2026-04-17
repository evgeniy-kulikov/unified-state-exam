# https://stepik.org/lesson/564193/step/3?unit=558441
#  Случай перелета за верхнюю границу ✅
def f(a, m, w=0):
    if 65 <= a <= 100:
        return not m % 2
    if a > 100:
        return m % 2 # ✅
    if not m:
        return 0
    g = [f(a+1, m-1), f(a*3, m-1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 65) if f(s, 2, 1)][0])
print(*[s for s in range(1, 65) if f(s, 3) and not f(s, 1)])
print(*[s for s in range(1, 65) if f(s, 4) and not f(s, 2)])
"""
8
21 62
61
"""

# https://stepik.org/lesson/564193/step/3?unit=558441
# ❗ ❗ ❗ ❗ ❗
# 😉 Другой вариант кода ✔️
#  Случай перелета за верхнюю границу ✅
def f(a, m, c=0, w=0):  # параметр 'c' - текущий ход
    if 65 <= a <= 100:
        return c % 2 == m % 2
    if a > 100:
        return c % 2 != m % 2 # ✅
    if c == m:
        return 0
    g = [f(a+1, m, c+1), f(a*3, m, c+1)]
    if (c+1) % 2 == m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 65) if f(s, 2, 0, 1)][0])
print(*[s for s in range(1, 65) if f(s, 3) and not f(s, 1)])
print(*[s for s in range(1, 65) if f(s, 4) and not f(s, 2)])
"""
8
21 62
61
"""


# https://stepik.org/lesson/564193/step/5?unit=558441
# Вся трудность в Задании 21 🌶️🌶️🌶️
def f(a, m, w=0):
    if a >= 1000:
        return not m % 2
    if not m:
        return 0
    g = [f(a+100, m-1), f(a*2, m-1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print(len([s for s in range(1, 1000) if f(s, 2)]))
print(len([s for s in range(1, 1000) if f(s, 3) and not f(s, 1)]))
# случаи рассматриваются отдельно
s21_min = [s for s in range(1, 1000) if f(s, 2, 1)][0]
s21_max = [s for s in range(1, 1000) if f(s, 4) and not f(s, 2)][-1]  # 250 есть в этом списке
print(s21_min, s21_max)
"""
100
150
250 299
"""



# https://stepik.org/lesson/687434/step/2?unit=686599
# ✅ Простые 2 кучи
def f(a, b, m, w=0):
    if a+b >= 99:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, b, m-1), f(a*3, b, m-1), f(a, b+1, m-1), f(a, b*3, m-1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 91) if f(8, s, 2, 1)][0])
print(len([s for s in range(1, 91) if f(8, s, 3) and not f(8, s, 1)]))
print(*[s for s in range(1, 91) if f(8, s, 2)])
"""
11
3
30
"""

