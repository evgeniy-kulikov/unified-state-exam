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


# https://stepik.org/lesson/1713458/step/5?unit=1736931
# https://kompege.ru/task   № 844 (Уровень: Средний)
def f(s, mv):
    if 43 <= s <= 72:
        return not mv % 2
    elif s > 72:
        return mv % 2
    if not mv:
        return 0
    g = [f(s + 1, mv - 1), f(s * 2, mv - 1), f(s * 3, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print([s for s in range(1, 43) if f(s, 2)][0])  # 14
print(len([s for s in range(1, 43) if f(s, 3) and not f(s, 1)]))  # 3
print(*[s for s in range(1, 43) if f(s, 4) and not f(s,2)])  # 12 39


# https://stepik.org/lesson/1713458/step/6?unit=1736931
# https://kompege.ru/task   № 854 (Уровень: Сложный)
def f(a, m):
    if a < 10:
        return not m % 2
    if not m:
        return 0
    g = [f(a-1, m-1), f(a-2, m-1), f(a-3, m-1), f(a-4, m-1), f(a-5, m-1)]
    if not a % 2:
        g.append(f(a // 2, m-1))
    if not (m-1)% 2:
        return any(g)
    return all(g)

print(*[s for s in range(10, 100) if f(s, 2)])  # 15
print(*[s for s in range(10, 100) if f(s, 3) and not f(s, 1)])  # 17 30
print(*[s for s in range(10, 100) if f(s, 4) and not f(s, 2)])  # 21
"""
15
17 30
21
"""


# https://stepik.org/lesson/1713458/step/9?unit=1736931
# https://kompege.ru/task   № 847 (Уровень: Базовый)
def f(a, m):
    if a > 33:
        return not m % 2
    if not m:
        return False
    g = [f(a+1,  m-1), f(a+2,  m-1), f(a+3,  m-1), f(a*2,  m-1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print(*[a for a in range(1, 34) if f(a, 2)])  # 16
print(*[a for a in range(1, 34) if f(a, 3) and not f(a, 1)])  # 8 15
print(*[a for a in range(1, 34) if f(a, 4) and not f(a, 2)])  # 8 15
"""
16
8 15
12
"""


# https://stepik.org/lesson/1713458/step/10?unit=1736931
# https://kompege.ru/task   № 845 (Уровень: Средний)  Случай перелета за верхнюю границу ✅
def f(a, m):
    if 36 <= a <= 60:
        return not m % 2
    if a > 60:  # ✅
        return m % 2
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


# https://stepik.org/lesson/1713458/step/11?unit=1736931
# https://kompege.ru/task   № 1202 Апробация 27.04 (Уровень: Базовый)
def f(a, b, m):
    if a + b >= 59:
        return not m % 2
    if not m:
        return False
    g = [f(a+1, b, m-1), f(a*2, b, m-1), f(a, b+1, m-1), f(a, b*2, m-1)]
    return any(g) if  m % 2 else all(g)

print([a for a in range(1, 53) if f(a, 5, 1)][0])
print(*[a for a in range(1, 53) if f(a, 5, 3) and not f(a, 5, 1)])
print([a for a in range(1, 53) if f(a, 5, 4) and not f(a, 5, 2)][0])
"""
27
24 26
23
"""





""" 20.1 Задание 19 - 21 ЕГЭ | Урок 2 """
# https://stepik.org/lesson/1713459/step/2?unit=1736932
# https://kompege.ru/task   № 853 (Уровень: Базовый)
def f(a, b, mv, w=eval('all')):
    if a + b >= 77:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a + 1, b, mv - 1), f(a * 2, b, mv - 1), f(a, b + 1, mv - 1), f(a, b * 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 70) if f(7, s, 2, eval('any'))][0])  # 18
print(*[s for s in range(1, 70) if f(7, s, 3) and not f(7, s, 1)])  # 31 34
print([s for s in range(1, 70) if f(7, s, 4) and not f(7, s, 2)][0])  # 30


# https://stepik.org/lesson/1713459/step/3?unit=1736932
# https://kompege.ru/task   № 1135 (Уровень: Базовый)
def f(a, b, m, w=eval('all')):
    if a+b >= 68:
        return not m % 2
    if not m:
        return 0
    g = [f(a + 1, b, m-1), f(a + b, b, m-1), f(a, b + 1, m-1), f(a, b + a, m-1)]
    if not (m - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 60) if f(8, s, 2, w=eval('any'))][0])  # 18
print([s for s in range(1, 60) if f(8, s, 3) and not f(8, s, 1)][0], end=' ')
print([s for s in range(1, 60) if f(8, s, 3) and not f(8, s, 1)][-1])  # 17 29
print(*[s for s in range(1, 60) if f(8, s, 4) and not f(8, s, 2)])  # 17 29
"""
18
17 29
28
"""


# https://stepik.org/lesson/1713459/step/4?unit=1736932
# https://kompege.ru/task   № 1420 (Уровень: Базовый)
def f(a, b, m):
    if a * b >= 63:
        return not m % 2
    if not m:
        return 0
    g = [f(a + 1, b, m-1), f(a * 2, b, m-1), f(a, b + 1, m-1), f(a, b * 2, m-1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 32) if f(2, s, 2)])  # 15
print([s for s in range(1, 32) if f(2, s, 3) and not f(2, s, 1)][0], end=' ')
print([s for s in range(1, 32) if f(2, s, 3) and not f(2, s, 1)][-1])  # 7 14
print([s for s in range(1, 32) if f(2, s, 4) and not f(2, s, 2)][-1])  # 13
"""
15
7 14
13
"""


# https://stepik.org/lesson/1713459/step/5?unit=1736932
# https://kompege.ru/task   № 2369 (Уровень: Сложный)
def f(a,b,c, mv, w=eval('all')):
    if a+b+c >= 73:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+3,b,c, mv-1), f(a+13,b,c, mv-1), f(a+23,b,c, mv-1),
         f(a,b+3,c, mv-1), f(a,b+13,c, mv-1), f(a,b+23,c, mv-1),
         f(a,b,c+3, mv-1), f(a,b,c+13, mv-1), f(a,b,c+23, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)

print([s for s in range(1, 24) if f(2, s, 2*s, 2, eval('any'))][0])
print([s for s in range(1, 24) if f(2, s, 2*s, 3) and not f(2, s, 2*s, 1)][0], end=' ')
print([s for s in range(1, 24) if f(2, s, 2*s, 3) and not f(2, s, 2*s, 1)][-1])
print(*[s for s in range(1, 24) if f(2, s, 2*s, 4) and not f(2, s, 2*s, 2)][-2:])
"""
9
8 14
10 13
"""


# https://stepik.org/lesson/1713459/step/6?unit=1736932
# https://kompege.ru/task   № 843 (Уровень: Средний)
from math import ceil
def f(a, b, m):
    if a + b <= 20:
        return not m % 2
    if not m:
        return False
    # g = [f(a-1, b, m-1), f(ceil(a / 2), b, m-1), f(a, b-1, m-1), f(a, ceil(b / 2), m-1)]
    g = [f(a-1, b, m-1), f((a+1) // 2, b, m-1), f(a, b-1, m-1), f(a, (b+1) // 2, m-1)]  # ceil(5/2) == (5+1)//2 ✅
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print(*[a for a in range(11, 100) if f(10, a, 2)])  # 21
print(*[a for a in range(11, 100) if f(10, a, 3) and not f(a, 10, 1)])  # 22 42
print([a for a in range(11, 100) if f(10, a, 4) and not f(a, 10, 2)][0])  # 24
"""
11
22 42
24
"""


# https://stepik.org/lesson/1713459/step/7?unit=1736932
# https://kompege.ru/task   № 2370 (Уровень: Средний)
def f(a, m):
    if a >= 2163:
        return not m % 2
    if not m:
        return False
    g = [f(a+1, m-1), f(a*3, m-1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print(*[a for a in range(1, 2163) if f(a, 2)])  # 720
print(*[a for a in range(1, 2163) if f(a, 3) and not f(a, 1)][:2])  # 240 719
print(*[a for a in range(1, 2163) if f(a, 4) and not f(a, 2)])  # 718
"""
720
240 719
718
"""


# https://stepik.org/lesson/1713459/step/8?unit=1736932
# https://kompege.ru/task   № 9750 (Уровень: Средний)
def f(a, m):
    if a <= 19:
        return not m % 2
    if not m:
        return False
    g = [f(a-5, m-1)]
    if not a % 2:
        g += [f(a//2, m-1)]
    if not a % 3:
        g += [f(a // 3, m - 1)]
    if a % 2 and a % 3:
        g += [f(a + 1, m - 1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print([a for a in range(20, 100) if f(a, 2)][0])  # 25
print(*[a for a in range(20, 100) if f(a, 3) and not f(a, 1)][:2])  # 40 43
print([a for a in range(20, 100) if f(a, 4) and not f(a, 2)][0])  # 60
"""
25
40 43
60
"""








""" 21.1 Задание 19 - 21 ЕГЭ | Задачи прошлых лет """
# https://stepik.org/lesson/1713460/step/3?unit=1736933
# https://kompege.ru/task   № 9750 Основная волна 19.06.23 (Уровень: Базовый)
def f(a, mv):
    if a >= 88:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+1, mv-1), f(a+4, mv-1), f(a*3, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 88) if f(s, 2)])
print(*[s for s in range(1, 88) if f(s, 3) and not f(s, 1)][:2])
print([s for s in range(1, 88) if f(s, 4) and not f(s, 2)][0])
"""
29
25 28
24
"""




""""""
""" Варианты """
# 28.1 Вариант 1 | Часть 1
# https://stepik.org/lesson/1729565/step/7?unit=1753394
#  https://kompege.ru/task  № 17875 Демоверсия 2025 (Уровень: Базовый)
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


# 29.1 Вариант 2 | Часть 2
# https://stepik.org/lesson/1729899/step/7?unit=1753726
# https://kompege.ru/task  № 19251 ЕГКР 21.12.24 (Уровень: Базовый)
def f(a, m):
    if a >= 132:
        return not m % 2
    if not m:
        return 0
    g = [f(a + 3, m - 1), f(a + 6, m - 1), f(a * 3, m - 1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print([s for s in range(1, 132) if f(s, 2)][0])  # 41
print(*[s for s in range(1, 132) if f(s, 3) and not f(s, 1)][:2])  # 14 35
print([s for s in range(1, 132) if f(s, 4) and not f(s, 2)][0])  # 32
"""
41
14 35
32
"""


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730528/step/7?unit=1754357
# https://kompege.ru/task  № 20811 Апробация 05.03.25 (Уровень: Базовый)
def f(a, m):
    if a >= 51:
        return not m % 2
    if not m:
        return 0
    g = [f(a + 1, m - 1), f(a + 4, m - 1), f(a * 2, m - 1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 51) if f(s, 2)])  # 25
print(*[s for s in range(1, 51) if f(s, 3) and not f(s, 1)])  # 21 24
print([s for s in range(1, 51) if f(s, 4) and not f(s, 2)][0])  # 20
"""
25
21 24
20
"""


# 31.2 Вариант 4 | Часть 2
# https://stepik.org/lesson/1736670/step/7?unit=1760676
# https://kompege.ru/task  № 21418 Досрочная волна 2025 (Уровень: Базовый)
def f(a, m):
    if a <= 87:
        return not m % 2
    if not m:
        return 0
    g = [f(a-2, m-1), f(a//2, m-1)]
    if not (m-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(89, 500) if f(s, 2)][0])  # 176
print(*[s for s in range(89, 500) if f(s, 3) and not f(s, 1)][:2])  # 178 179
print([s for s in range(89, 500) if f(s, 4) and not f(s, 2)][0])  # 180
"""
176
178 179
180
"""


# 32.2 Вариант 5 | Часть 2
# https://stepik.org/lesson/1754189/step/7?unit=17786487
# https://kompege.ru/task  № 21714 ЕГКР 19.04.25 (Уровень: Базовый)
def f(a, m):
    if a >= 128:
        return not m % 2
    if not m:
        return 0
    g = [f(a+2, m-1), f(a+5, m-1), f(a*2, m-1)]
    if not (m-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(2, 127) if f(s, 2)][0])  # 62
print(*[s for s in range(2, 127) if f(s, 3) and not f(s, 1)][:2])  # 31 57
print([s for s in range(2, 127) if f(s, 4) and not f(s, 2)][0])  # 55
"""
62
31 57
55
"""


# 33.2 Вариант 6 | Часть 2
# https://stepik.org/lesson/1943171/step/7?unit=1969925
# https://kompege.ru/task  № 23203 Основная волна 10.06.25 (Уровень: Базовый)
def f(a, m):
    if a <= 11:
        return not m % 2
    if not m:
        return 0
    g = [f(a - 3, m-1), f(a - 7, m-1), f(a // 3, m-1)]
    # if not (m-1) % 2:
    if m % 2:
        return any(g)
    return all(g)

print([s for s in range(12, 500) if f(s, 2)][0])  # 36
print(*[s for s in range(12, 500) if f(s, 3) and not f(s, 1)][:2])  # 39 40
print([s for s in range(12, 500) if f(s, 4) and not f(s, 2)][0])  # 42
"""
36
39 40
42
"""


# 34.2 Вариант 7 | Часть 2
# https://stepik.org/lesson/1943174/step/7?unit=1969928
# https://kompege.ru/task  № 23278 Основная волна 11.06.25 (Уровень: Базовый)
def f(a, m):
    if a <= 16:
        return not m % 2
    if not m:
        return 0
    g = [f(a-3, m-1), f(a-8, m-1), f(a//3, m-1)]
    if not (m-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(17, 110) if f(s, 2)][0])  # 51
print(*[s for s in range(17, 110) if f(s, 3) and not f(s, 1)][:2])  # 54 55
print([s for s in range(17, 110) if f(s, 4) and not f(s, 2)][0])  # 57
"""
51
54 55
57
"""


# 35.2 Вариант 8 | Часть 2
# https://stepik.org/lesson/1943181/step/7?unit=1969936
# https://kompege.ru/task  № 23565 Пересдача 03.07.25 (Уровень: Базовый)
def f(a, m):
    if a <= 15:
        return not m % 2
    if not m:
        return 0
    g = [f(a-3, m-1), f(a-8, m-1), f(a//3, m-1)]
    if not (m-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(16, 200) if f(s, 2)][0])  # 48
print(*[s for s in range(16, 200) if f(s, 3) and not f(s, 1)][:2])  # 51 52
print([s for s in range(16, 200) if f(s, 4) and not f(s, 2)][0])  # 54
"""
48
51 52
54
"""


# 36.2 Вариант 9 | Часть 2
# https://stepik.org/lesson/1943186/step/7?unit=1969940
# https://kompege.ru/task  № 23759 Демоверсия 2026 (Уровень: Базовый)
def f(a, m):
    if a <= 30:
        return not m % 2
    if not m:
        return 0
    g = [f(a-3, m-1), f(a-5, m-1), f(a // 4, m-1)]
    if not (m - 1) % 2:
        return any(g)
    return all(g)

print([s for s in range(31, 500) if f(s, 2)][0])  # 124
print(*[s for s in range(31, 500) if f(s, 3) and not f(s, 1)][:2])  # 127 128
print([s for s in range(31, 500) if f(s, 4) and not f(s, 2)][0])  # 132
"""
124
127 128
132
"""

