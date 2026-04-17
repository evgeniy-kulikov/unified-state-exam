""" https://kompege.ru/task """
"""
844 847 854 1061 1349 2575 2865 3970
11669
15336 17532 19635 19750
"""


# 844 (Уровень: Средний)
#  Случай перелета за верхнюю границу ✅
def f(a, m):
    if 43 <= a <= 72:
        return not m % 2
    if a > 72:
        return m % 2 # ✅
    if not m:
        return 0
    g = [f(a+1, m-1), f(a*2, m-1), f(a*3, m-1)]
    return any(g) if m % 2 else all(g)

print([s for s in range(1, 43) if f(s, 2)][0])
print(len([s for s in range(1, 43) if f(s, 3) and not f(s, 1)]))
s21 = [s for s in range(1, 43) if f(s, 4) and not f(s, 2)]
print(s21[0], s21[-1])
"""
14
3
12 39
"""


# 847 (Уровень: Базовый)
def f(a, m):
    if a > 33:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, m-1), f(a+2, m-1), f(a+3, m-1), f(a*2, m-1)]
    return any(g) if m % 2 else all(g)

print([s for s in range(1, 38) if f(s, 2)][0])
s20 = [s for s in range(1, 38) if f(s, 3) and not f(s, 1)]
print(s20[0], s20[-1])
print(*[s for s in range(1, 38) if f(s, 4) and not f(s, 2)])
"""
18
9 17
14
"""


#  854 (Уровень: Сложный)
def f(a, m):
    if a < 10:
        return not m % 2
    if not m:
        return 0
    g = [f(a-1, m-1), f(a-2, m-1), f(a-3, m-1), f(a-4, m-1), f(a-5, m-1)]
    if not a % 2:
        g += [f(a//2, m-1)]
    return any(g) if m % 2 else all(g)

print(*[s for s in range(10, 200) if f(s, 2)])
s20 = [s for s in range(10, 200) if f(s, 3) and not f(s, 1)]
print(s20[0], s20[-1])
print(*[s for s in range(10, 200) if f(s, 4) and not f(s, 2)])
"""
15
17 30
21
"""


# 1061 Джобс 15.03.2021 (Уровень: Средний)
def f(a, b, m, w=eval('all')):
    if a + b >= 45:
        return not m % 2
    if not m:
        return 0
    g = [f(a, b+a, m-1), f(a+b, b, m-1)]
    if m % 2:
    # if not (m-1) % 2:
        return any(g)
    return w(g)

print([s for s in range(45) if f(7, s, 2, eval('any'))][0])  # 11
res = [s for s in range(45) if f(6, s, 3) and not f(6, s, 1)]
print(min(res), max(res))  # 7 13
print([s for s in range(45) if f(s, s, 4) and not f(7, s, 2)][0])  # 4

# вариант без eval('all') ✔️✔️✔️
def f(a, b, m, w=0):
    if a+b >= 45:
        return not m % 2
    if not m:
        return 0
    g = [f(a+b, b, m-1), f(a, b+a, m-1), ]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 50) if f(7, s, 2, 1)][0])
s20 = [s for s in range(1, 50) if f(6, s, 3) and not f(6, s, 1)]
print(s20[0], s20[-1])
print([s for s in range(1, 50) if f(s, s, 4) and not f(s, s, 2)][0])
"""
11
7 13
4
"""


# 1349 Danov2101 (Уровень: Сложный) 🌶️🌶️
def f(a, m, w=0):
    if a == 1:
        return not m % 2
    if not m:
        return 0
    g = []
    if a % 2:
        g += [f(a-2, m-1)]
    else:
        g += [f(a//2, m - 1)]
    if not a % 3:
        g += [f(a//3, m - 1)]
    else:
        g += [f(a-3, m - 1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

z19 = [s for s in range(2, 38) if f(s, 1)]  # ищем упущенные верные ходы Пети
print([s for s in z19 if f(s, 2, 1)][-1])  # и используем их для Вани которому случайно повезло
z20 = [s for s in range(2, 38) if f(s, 3) and not f(s, 1)]
print(z20[0], z20[-1])  # 7 18
print([s for s in range(2, 38) if f(s, 4) and not f(s, 2)][0])  # 9
"""
4
7 18
9
"""


# 2575 (Уровень: Средний)
# 🌶️ нельзя повторять ход, который только что сделал второй игрок
def f(a, m, c=''):
    if a >= 62:
        return not m % 2
    if not m:
        return 0
    g = []
    if c != '+1':
        g += [f(a+1, m-1, '+1')]
    if c != '+2':
        g += [f(a+2, m-1, '+2')]
    if c != '*3':
        g += [f(a*3, m-1, '*3')]
    return any(g) if m % 2 else all(g)

print(*[s for s in range(1, 62) if f(s, 2, 1)])
s20 = [s for s in range(1, 62) if f(s, 3) and not f(s, 1)]
print(s20[0], s20[-1])
print(*[s for s in range(1, 62) if f(s, 4) and not f(s, 2)])
"""
20
7 19
6
"""


# 2865 Статград 08.02.2022 (Уровень: Средний) 🌶️🌶️🌶️
def f(a, m, p1='', p2=''):  # 0(, , '', '') ->
    if a >= 21:
        return not m % 2
    if not m:
        return 0
    g = []
    if p2 != '+1':
        # -> 1(, , '+1', '') ->  2(, , '+1', '+1') -> 3(, , '???', '+1')❗запрет предыдущего своего одинакового хода
        g += [f(a+1, m-1, '+1', p1)]
    if p2 != '+2':
        g += [f(a+2, m-1, '+2', p1)]
    if p2 != '*2':
        g += [f(a*2, m-1, '*2', p1)]
    if m % 2:
        return any(g)
    return all(g)

print([s for s in range(1, 21) if f(s, 3) and not f(s, 1)][0])  # 8
print(*[s for s in range(1, 21) if f(s, 4) and not f(s, 2)])  # 6 7
print([s for s in range(1, 21) if f(s, 5) and not f(s, 3)][-1])  # 5
"""
8
6 7
5
"""


# 3970 (Уровень: Базовый)
# Шикарное условие ✅🍒🍓🌶️✅
# for n in range(1, 21):
#     print(f'{2**n + 1:b}')
#     print(f'{2**n + 1:b}'.count('1'))  # всегда 2
def f(a, m, w=0):
    if a >= 60:
        return not m % 2
    if not m:
        return 0
    g = [f(a+2, m-1), f(a*2, m-1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 58) if f(s, 2, 1)][0])
s20 = [s for s in range(1, 58) if f(s, 3) and not f(s, 1)]
print(s20[0], s20[-1])
print([s for s in range(1, 58) if f(s, 4) and not f(s, 2)][0])
"""
15
14 27
24
"""





# 11669 (Уровень: Базовый)  🌶️🌶️🌶️
def f(a, m, p=0):
    if a < 117:
        return not m % 2
    if not m:
        return 0
    g = [f(a-7, m-1, p), f(a//3, m-1, p)]
    if m % 2:
        return any(g)
    return any(g) if m==2 and p else all(g)  # ✅👍  выборочная подстановка 'any' дальше первых ходов

print([s for s in range(117, 10_001) if  f(s, 3) and not f(s, 1)][-1])  # 3158
d_20 = [s for s in range(117, 10_001) if f(s, 3) and not f(s, 1)]
print(min(d_20), max(d_20))  # 358 1073
print([s for s in range(117, 10_001) if f(s, 4) and not f(s, 2)][-1])  # 1080
"""
3158
358 1073
1080
"""





# 15336 Досрочная волна 2024 (Уровень: Базовый)
# ✅ Простые 2 кучи
def f(a, b, m, w=0):
    if a+b >= 123:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 109) if f(13, s, 2, 1)][0])
print(*[s for s in range(1, 109) if f(13, s, 3) and not f(13, s, 1)][:2])
print([s for s in range(1, 109) if f(13, s, 4) and not f(13, s, 2)][0])
"""
28
48 54
47
"""


# 17532 Основная волна 07.06.24 (Уровень: Базовый)
def f(a,b,m):
    if a+b >= 65:
        return not m % 2
    if not m:
        return False
    g = [f(a+1, b, m-1), f(a*3, b, m-1), f(a, b+1, m-1), f(a, b*3, m-1)]
    if not (m-1) % 2:
        return any(g)
    return all(g)
    # return any(g)

# print([s for s in range(1, 59) if f(6, s, 2)][0])  # 7
print(*[s for s in range(1, 59) if f(6, s, 3) and not f(6, s, 1)][:2])  # 10 19
print([s for s in range(1, 59) if f(6, s, 4) and not f(6, s, 2)][0])  # 18
"""
7
10 19
18
"""


# 19635 (Уровень: Базовый)
# ✅ 2 кучи
def f(a, b, m, w=0):
    if a+b <= 100:
        return not m % 2
    if not m:
        return 0
    g = [f(a-3, b-3, m-1), f(a//2, b, m-1), f(a, b//2, m-1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(53, 1000) if f(48, s, 2, 1)][0])
s20 = [s for s in range(53, 1000) if f(48, s, 3) and not f(48, s, 1)]
print(s20[0], s20[-1])
print([s for s in range(53, 1000) if f(48, s, 4) and not f(48, s, 2)][0])
"""
59
115 229
124
"""



# 19750 (Уровень: Средний)
# 1
def f(a, m):
    if a <= 19:
        return not m % 2
    if not m:
        return 0
    g = [f(a - 5, m - 1)]
    if not a % 2:
        g += [f(a//2, m - 1)]
    elif not a % 3:
        g += [f(a//3, m - 1)]
    if a % 2 and a % 3:
        g += [f(a+1, m - 1)]
    if m % 2:
        return any(g)
    return all(g)

print([s for s in range(20, 500) if f(s, 2)][0])  # 25
print(*[s for s in range(20, 500) if f(s, 3) and not f(s, 1)][:2])  # 40 43
print([s for s in range(20, 500) if f(s, 4) and not f(s, 2)][0])  # 60
"""
25
40 43
60
"""