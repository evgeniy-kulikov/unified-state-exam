""" https://kompege.ru/task """
"""
841 844 845 846 847 854 884 9788
1061 1136 1349 2364 2575 2865 3970
11669 1252
15336 17532 17560 19635 17638 17875 18958 19750
"""


# 841 (Уровень: Базовый)
# ✔️ 2 кучи
def f(a, b, m, w=0):
    if a+b >= 125:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, b, m-1), f(a*4, b, m-1), f(a, b+1, m-1), f(a, b*4, m-1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 118) if f(7, s, 2, 1)][0])
s20 = [s for s in range(1, 118) if f(7, s, 3) and not f(7, s, 1)]
print(s20[0], s20[-1])
print(*[s for s in range(1, 118) if f(7, s, 4) and not f(7, s, 2)])
"""
8
12 29
28
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


# № 845 (Уровень: Средний)  Случай перелета за верхнюю границу ✅
def f(a, m):
    if 36 <= a <= 60:
        return not m % 2
    if a > 60:
        return m % 2  # ✅
    if not m:
        return False
    g = [f(a+1,  m-1), f(a*2,  m-1), f(a*3,  m-1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print(*[a for a in range(1, 36) if f(a, 2)])  # 34
print(len([a for a in range(1, 36) if f(a, 3) and not f(a, 1)]))  # 1
print(*[a for a in range(1, 36) if f(a, 4) and not f(a, 2)])  # 11 32
"""
34
1
11 32
"""


# https://kompege.ru/task   № 846 (Уровень: Базовый)
def f(a, m):
    if a >= 65:
        return not m % 2
    if not m:
        return 0
    g = [f(a + 1, m - 1), f(a + 2, m - 1), f(a * 3, m - 1)]
    return any(g) if m % 2 else all(g)

print([a for a in range(1, 65) if f(a, 2)][-1])
s20 = [a for a in range(1, 65) if f(a, 3) and not f(a, 1)]
print(s20[0], s20[-1])
print(*[a for a in range(1, 65) if f(a, 4) and not f(a,2)])
"""
21
7 20
18
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


# 884 Джобс 25.12.2020 (Уровень: Средний)
# ✔️+👍  2 кучи + Интересное условие 1 ≤ K ≤ 29,  1 ≤ S ≤ 29
def f(a, b, m):
    if a+b >= 30:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
    return any(g) if m % 2 else all(g)

s19 = [(a, b) for a in range(1, 30) for b in range(1, 30) if a+b < 30]
print(len([i for i in s19 if f(i[0], i[1], 2)]))
s20 = [s for s in range(1, 30) if f(6, s, 3) and not f(6, s, 1)]
print(s20[0], s20[-1])
print(len([i for i in s19 if f(i[0], i[1], 4) and not f(i[0], i[1], 2)]))
"""
10
5 11
8
"""


# 9788 Основная волна 20.06.23 (Уровень: Базовый)
def f(a, m):
    if a >= 59:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, m-1), f(a+3, m-1), f(a*4, m-1)]
    return any(g) if m % 2 else all(g)

print(*[s for s in range(1, 59) if f(s,2)])
print(*[s for s in range(1, 59) if f(s,3) and not f(s, 1)][:2])
print([s for s in range(1, 59) if f(s,4) and not f(s, 2)][0])
"""
14
11 13
10
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


# 1136 (Уровень: Базовый)
# ✔️ 2 кучи
def f(a, b, m, w=0):
    if a+b >= 79:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, b, m-1), f(a+b, b, m-1), f(a, b+1, m-1), f(a, b+a, m-1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 70) if f(9, s, 2, 1)][0])
print(*[s for s in range(1, 70) if f(9, s, 3) and not f(9, s, 1)][:2])
print(*[s for s in range(1, 70) if f(9, s, 4) and not f(9, s, 2)])
"""
21
20 34
33
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


# 2364 (Уровень: Средний)
def f(s, m):
    if s > 20:
        return not m % 2
    if not mv:
        return 0
    g = [f(s + 1, m - 1), f(s + 2, m - 1), f(s + 3, m - 1)]
    return any(g) if m % 2 else all(g)

print([s for s in range(1, 21) if f(s, 2)][0])
print(*[s for s in range(1, 21) if f(s, 5)][:3])
print(len([s for s in range(1, 21) if f(s, 10)]))  # 🌶️ 10 ходов хватит перебрать все камни
"""
17
10 11 12
5
"""


# 2575 (Уровень: Средний)
# 🌶️ нельзя повторять ход, который только что сделал второй игрок
def f(a, m, c=''):  # параметр 'c' запоминает текущий ход в игре
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


# 1252 Статград 26.04.2021 (Уровень: Базовый)
# ✔️ 2 кучи
def f(a, b, m, w=0):
    if a+b >= 88:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, b, m-1), f(a*3, b, m-1), f(a, b+1, m-1), f(a, b*3, m-1)]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 82) if f(6, s, 2, 1)][0])
print(*[s for s in range(1, 82) if f(6, s, 3) and not f(6, s, 1)])
print([s for s in range(1, 82) if f(6, s, 2)][-1])
"""
10
9 23 26
27
"""







# 15336 Досрочная волна 2024 (Уровень: Базовый)
# ✔️ 2 кучи
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
# ✔️ 2 кучи
def f(a,b,m, w=0):
    if a+b >= 65:
        return not m % 2
    if not m:
        return False
    g = [f(a+1, b, m-1), f(a*3, b, m-1), f(a, b+1, m-1), f(a, b*3, m-1)]
    if not (m-1) % 2:
        return any(g)
    return any(g) if w else all(g)


print([s for s in range(1, 59) if f(6, s, 2, 1)][0])  # 7
print(*[s for s in range(1, 59) if f(6, s, 3) and not f(6, s, 1)][:2])  # 10 19
print([s for s in range(1, 59) if f(6, s, 4) and not f(6, s, 2)][0])  # 18
"""
7
10 19
18
"""


# 17560 Основная волна 08.06.24 (Уровень: Базовый)
def f(a, m):
    if a >= 58:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, m-1), f(a+4, m-1), f(a*2, m-1),]
    return any(g) if m % 2 else all(g)

print([s for s in range(1, 58) if f(s, 2)][0])
print(*[s for s in range(1, 58) if f(s, 3) and not f(s, 1)][:2])
print([s for s in range(1, 58) if f(s, 4) and not f(s, 2)][0])
"""
28
14 24
23
"""


# 19635 (Уровень: Базовый)
# ✔️ 2 кучи
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


# 17638 Основная волна 19.06.24 (Уровень: Базовый)
def f(a, m):
    if a >= 39:
        return not m % 2
    if not m:
        return 0
    g = [f(a+1, m-1), f(a+3, m-1), f(a*2, m-1),]
    return any(g) if m % 2 else all(g)

print([s for s in range(1, 39) if f(s, 2)][0])
print(*[s for s in range(1, 39) if f(s, 3) and not f(s, 1)][:2])
print([s for s in range(1, 39) if f(s, 4) and not f(s, 2)][0])
"""
19
16 18
15
"""


#  17875 Демоверсия 2025 (Уровень: Базовый)
def f(a, m):
    if a <= 19:
        return not m % 2
    if not m:
        return 0
    g = [f(a-2, m-1), f(a-5, m-1), f(a//3, m-1)]
    return any(g) if m % 2 else all(g)

print([s for s in range(20, 200) if f(s, 2)][0])
print(*[s for s in range(20, 200) if f(s, 3) and not f(s, 1)][:2])
print([s for s in range(20, 200) if f(s, 4) and not f(s, 2)][0])
"""
60
62 63
64
"""


# 18958 (Уровень: Базовый)
def f(a, m, w=0):
    if a >= 665:
        return not m % 2
    if not m:
        return 0
    g = [f(a+3, m-1), f(a*3, m-1), f(a + a**2, m-1),]
    if m % 2:
        return any(g)
    return any(g) if w else all(g)

print([s for s in range(1, 666) if f(s, 2, 1)][0])
s20 = [s for s in range(1, 666) if f(s, 3) and not f(s, 1)]
print(s20[0], s20[-1])
print([s for s in range(1, 666) if f(s, 4) and not f(s, 2)][-1])
"""
5
8 22
19
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