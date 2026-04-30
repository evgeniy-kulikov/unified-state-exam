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




# https://stepik.org/lesson/564192/step/4?unit=558440
# ✔️+👍  2 кучи + Интересное условие S+K ≥ 19
def f(a, b, m):
    if a+b <= 18:
        return not m % 2
    if not m:
        return 0
    g = [f(a-1, b, m-1), f(a//2, b, m-1), f(a, b-1, m-1), f(a, b//2, m-1)]
    return any(g) if m % 2 else all(g)
    # if m % 2:
    #     return any(g)
    # return any(g) if w else all(g)

print(*[s for s in range(10, 100) if f(s, s, 2)])
s20 = [s for s in range(6, 100) if f(13, s, 3) and not f(13, s, 1)]
print(s20[0], s20[-1])
print([s for s in range(10, 100) if f(s, s, 4) and not f(s, s, 2)][0])
"""
13
14 27
14
"""


# https://stepik.org/lesson/564192/step/5?unit=558440
# ✔️+👍  2 кучи + Интересное условие K+S ≤ 43
def f(a, b, m):
    if a+b >= 45:
        return not m % 2
    if not m:
        return 0
    g = [f(a+2, b, m-1), f(a*3, b, m-1), f(a, b+2, m-1), f(a, b*3, m-1)]
    return any(g) if m % 2 else all(g)
    # if m % 2:
    #     return any(g)
    # return any(g) if w else all(g)
s19 = [(a, b) for a in range(1, 43) for b in range(1, 43) if a+b<=43]
print(len([i for i in s19 if f(i[0], i[1], 2)]))
s20 = [s for s in range(1, 40) if f(4, s, 3) and not f(4, s, 1)]
print(s20[0], s20[-1])
print(*[s for s in range(1, 31) if f(13, s, 4) and not f(13, s, 2)])
"""
16
7 11
1
"""



# https://stepik.org/lesson/564192/step/6?unit=558440
# ✔️+👍  2 кучи + Интересное условие K+S ≤ 29
def f(a, b, m):
    if a+b >= 30:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*3, m-1)]
    return any(g) if m % 2 else all(g)

s19 = [(a, b) for a in range(1, 30) for b in range(1, 30) if a+b < 30]
print(len([i for i in s19 if f(i[0], i[1], 2)]))
s20 = [s for s in range(1, 30) if f(s, 7, 3) and not f(s, 7, 1)]
print(s20[0], s20[-1])
print(*[s for s in range(1, 30) if f(1, s, 4) and not f(1, s, 2)])
"""
7
4 7
8
"""

