"""
Task 19
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""


""" 24.1 Теория игр. Часть 1 """
# https://stepik.org/lesson/909258/step/3?unit=914860
def fn(stn, mv):
    if stn >= 15 or mv > 1:
        return mv == 1  # первый ход игры
    return fn(stn + 1, mv + 1) or fn(stn + 2, mv + 1)

res = [i for i in range(1, 15) if fn(i, 0)]
print(*sorted(res))  # 13 14


# https://stepik.org/lesson/909258/step/4?unit=914860
def fn(stn, mv):
    if stn >= 15 or mv > 2:
        return mv == 2  # второй ход игры
    if mv % 2:
        return fn(stn + 1, mv + 1) or fn(stn + 2, mv + 1)
    return fn(stn + 1, mv + 1) and fn(stn + 2, mv + 1)

res = [i for i in range(1, 15) if fn(i, 0)]
print(*sorted(res))  # 12


# https://stepik.org/lesson/909258/step/5?unit=914860
def fn(stn, mv):
    if stn >= 15 or mv > 3:
        return mv == 3  # ход игры
    if not mv % 2:
        return fn(stn + 1, mv + 1) or fn(stn + 2, mv + 1)
    return fn(stn + 1, mv + 1) and fn(stn + 2, mv + 1)

res = [i for i in range(1, 15) if fn(i, 0)]
print(*sorted(res))  # 10 11


# https://stepik.org/lesson/909258/step/6?unit=914860
def fn(stn, mv):
    # if stn >= 15:
    #     return mv == 4
    if stn >= 15 or mv > 4:
        return mv == 4  # ход игры
    if  mv % 2:
        return fn(stn + 1, mv + 1) or fn(stn + 2, mv + 1)
    return fn(stn + 1, mv + 1) and fn(stn + 2, mv + 1)

res = [i for i in range(1, 15) if fn(i, 0)]
print(*sorted(res))  # 9


# https://stepik.org/lesson/909258/step/7?unit=914860
def fn(stn, mv):
    # if  stn >= 10:
    #     return mv == 1
    if stn >= 10 or mv > 1:
        return mv == 1  # ход игры
    return fn(stn + 1, mv + 1) or fn(stn + 2, mv + 1) or fn(stn + 3, mv + 1)

res = [i for i in range(1, 10) if fn(i, 0)]
print(*sorted(res))  # 7 8 9


# https://stepik.org/lesson/909258/step/11?unit=914860
def fn(stn, mv):
    # if stn >= 10 or mv > 4:
    #     return mv == 4  # ход игры
    if stn >= 21:
        return mv == 1
    if not mv % 2:
        return any([fn(stn + 1, mv + 1), fn(stn * 2, mv + 1)])


res = [i for i in range(1, 100) if fn(i, 0)]
print(* sorted(res))  # 11 12 13 14 15 16 17 18 19 20
print(min(res), max(res))  # 11 20


# https://stepik.org/lesson/909258/step/8?unit=914860
def fn(stn, mv):
    # if  stn >= 10:
    #     return mv == 2
    if stn >= 10 or mv > 2:
        return mv == 2  # ход игры
    if mv % 2:
        return fn(stn + 1, mv + 1) or fn(stn + 2, mv + 1) or fn(stn + 3, mv + 1)
    return fn(stn + 1, mv + 1) and fn(stn + 2, mv + 1) and fn(stn + 3, mv + 1)

res = [i for i in range(1, 10) if fn(i, 0)]
print(*sorted(res))  # 6


# https://stepik.org/lesson/909258/step/9?unit=914860
def fn(stn, mv):
    if stn >= 10:
        return mv == 3
    if not mv % 2:
        return any([fn(stn + 1, mv + 1), fn(stn + 2, mv + 1), fn(stn + 3, mv + 1)])
    return all([fn(stn + 1, mv + 1), fn(stn + 2, mv + 1), fn(stn + 3, mv + 1)])

res = [i for i in range(1,100) if fn(i, 0)]
print(* sorted(res))  # 3 4 5


# https://stepik.org/lesson/909258/step/10?unit=914860
def fn(stn, mv):
    # if stn >= 10 or mv > 4:
    #     return mv == 4  # ход игры
    if stn >= 10:
        return mv == 4
    if mv % 2:
        return any([fn(stn + 1, mv + 1), fn(stn + 2, mv + 1), fn(stn + 3, mv + 1)])
    return all([fn(stn + 1, mv + 1), fn(stn + 2, mv + 1), fn(stn + 3, mv + 1)])

res = [i for i in range(1,100) if fn(i, 0)]
print(* sorted(res))  # 2


# https://stepik.org/lesson/909258/step/11?unit=914860
def fn(stn, mv):
    if stn >= 21:
        return mv == 1
    if not mv % 2:
        return any([fn(stn + 1, mv + 1), fn(stn * 2, mv + 1)])

res = [i for i in range(1, 100) if fn(i, 0)]
print(* sorted(res))  # 11 12 13 14 15 16 17 18 19 20
print(min(res), max(res))  # 11 20


# https://stepik.org/lesson/909258/step/12?unit=914860
def fn(stn, mv):
    if stn >= 21:
        return mv == 2
    if mv % 2:
        return any([fn(stn + 1, mv + 1), fn(stn * 2, mv + 1)])
    return all([fn(stn + 1, mv + 1), fn(stn * 2, mv + 1)])

res = [i for i in range(1, 100) if fn(i, 0)]
print(* sorted(res))  # 10


# https://stepik.org/lesson/909258/step/13?unit=914860
def fn(stn, mv):
    if stn >= 21:
        return mv == 3
    if mv % 2:
        return all([fn(stn + 1, mv + 1), fn(stn * 2, mv + 1)])
    return any([fn(stn + 1, mv + 1), fn(stn * 2, mv + 1)])

res = [i for i in range(1, 100) if fn(i, 0)]
print(* sorted(res))  # 5 9


# https://stepik.org/lesson/909258/step/14?unit=914860
# !!! Легче решать на бумаге !!!
# Позиция на которую должен прийти Ваня (2-й ход игры)
def fn(stn, mv):
    if stn >= 21:
        return mv == 2
    if not mv % 2:
        return all([fn(stn + 1, mv + 1), fn(stn * 2, mv + 1)])
    return any([fn(stn + 1, mv + 1), fn(stn * 2, mv + 1)])

res = [i for i in range(6, 44) if fn(i, 0)]
print(*res)  # 10  - Позиция на которую должен прийти Ваня
# Минус ход Вани, минус ход Пети  10 - 1 - 1 = 8
# Петя должен стартовать с позиции  8



""" 24.2 Задачи с одной кучей камней. Часть 1 """
# https://stepik.org/lesson/909256/step/2?unit=914858
def kp(n):
    if n >= 17:
        return 'w'  # достигнуто необходимое количество камней, победа
    if kp(n + 1) == 'w' or kp(n * 2) == 'w':
        return 'p1'  # Петя побеждает первым ходом
    if kp(n + 1) == 'p1' and kp(n * 2) == 'p1':
        return 'v1'  # Ваня побеждает первым ходом
    if kp(n + 1) == 'v1' or kp(n * 2) == 'v1':
        return 'p2'  # Петя побеждает вторым ходом
    if (kp(n + 1) == 'p1' or kp(n + 1) == 'p2') and (kp(n * 2) == 'p1' or kp(n * 2) == 'p2'):
        return 'v2'  # Ваня побеждает вторым ходом

for s in range(17, 0, -1):
    print(s, kp(s))


# https://stepik.org/lesson/909256/step/3?unit=914858
def fn(n):
    if n >= 17:
        return 'w'  # победа
    if fn(n + 1) == 'w' or fn(n * 2) == 'w':
        return 'p1'  # Петя побеждает первым ходом
print(*[i for i in range(17, 0, -1) if fn(i) == 'p1'])  # 16 15 14 13 12 11 10 9
print(len([i for i in range(17, 0, -1) if fn(i) == 'p1']))  # 8

# вариант
def fn(stn, mv):
    if stn >= 17:
        return mv == 1
    if mv == 0: return 0
    if not mv % 2:
        return any([fn(stn + 1, mv + 1), fn(stn * 2, mv + 1)])
print(*[i for i in range(17, 0, -1) if fn(i, 0)])  # 16 15 14 13 12 11 10 9
print(len([i for i in range(17, 0, -1) if fn(i, 0)]))  # 8



""" 7.32 ЕГЭ Тренировка 19 """
# https://stepik.org/lesson/484592/step/1?auth=login&unit=475907
def f(a, b, mv):
    if a + b >= 77: return not mv % 2
    if mv == 0: return 0
    g = [f(a + 1, b, mv - 1), f(a * 2, b, mv - 1), f(a, b + 1, mv - 1), f(a, b * 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return any(g)
print(min(s for s in range(1, 70) if f(7, s, 2)))  # 18



# https://stepik.org/lesson/484592/step/2?auth=login&unit=475907
# a - a // 2     - уменьшить количество камней в куче в два раза
# (если количество камней в куче нечётно, остаётся на 1 камень БОЛЬШЕ, чем убирается)
def f(a, b, mv):
    if a + b <= 20: return not mv % 2
    if mv == 0: return 0
    g = [f(a - 1, b, mv - 1), f(a - a // 2, b, mv - 1), f(a, b - 1, mv - 1), f(a, b - b // 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return any(g)
print(max(s for s in range(11, 100) if f(10, s, 2)))  # 40


# https://stepik.org/lesson/484592/step/5?auth=login&unit=475907
# a // 2     - уменьшить количество камней в куче в два раза
# (если количество камней в куче нечётно, остаётся на 1 камень МЕНЬШЕ, чем убирается)
def f(a, b, mv):
    if a + b <= 20: return not mv % 2
    if mv == 0: return 0
    g = [f(a - 1, b, mv - 1), f(a // 2, b, mv - 1), f(a, b - 1, mv - 1), f(a, b // 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return any(g)

print(max(s for s in range(11, 100) if f(10, s, 2)))  # 43



""" 7.33 ЕГЭ Тренировка 19-21 (по три номера подряд) """
# https://stepik.org/lesson/622571/step/1?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/2?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/3?auth=login&unit=619541
def fn(a, b, mv, w=eval('all')):
    if a + b <= 20: return not mv % 2
    if mv == 0: return 0
    game = [fn(a - 1, b, mv - 1), fn(a // 2, b, mv - 1),
            fn(a, b - 1, mv - 1), fn(a, b // 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(game)
    return w(game)

print(max(s for s in range(11, 100) if fn(10, s, 2, w=eval('any'))))  # 43  any-any
print(''.join([str(s) for s in range(11, 100) if fn(10, s, 3) and not fn(10, s, 1)]))  # 2324324445
print(max(s for s in range(11, 100) if fn(10, s, 4) and not fn(10, s, 2)))  # 25


# https://stepik.org/lesson/622571/step/4?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/5?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/6?auth=login&unit=619541
def fn(a, b, mv, w=eval('all')):
    if a + b >= 13: return not mv % 2
    if mv == 0: return 0
    game = [fn(a + 1, b, mv - 1), fn(a + 2, b, mv - 1),
            fn(a, b + 1, mv - 1), fn(a, b + 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(game)
    return w(game)

print(min(s for s in range(1, 10) if fn(3, s, 2, w=eval('any')) and fn(3, s, 1, w=eval('any'))))  # 8
print(''.join([str(s) for s in range(1, 10) if fn(3, s, 3) and not fn(3, s, 1)]))  # 56
print(*[s for s in range(1, 10) if fn(3, s, 4) and not fn(3, s, 2)])  # 4


# https://stepik.org/lesson/622571/step/7?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/8?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/9?auth=login&unit=619541
""" нестандартное условие """
def fn(a, b, mv, w=eval('all')):
    if a + b >= 47: return not mv % 2
    if not mv: return 0
    g = [fn(a + 3, b, mv - 1), fn(a * 2, b, mv - 1), fn(a, b + 3, mv - 1), fn(a, b * 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return w(g)
print(min(s for s in range(1, 37) if fn(10, s, 2, w=eval('any'))))  # 7
print(max(s for s in range(1, 37) if fn(10, s, 3) and not fn(10, s, 1)))  # 16
print(min(s for s in range(1, 37) if fn(10, s, 4)))  # 12


# https://stepik.org/lesson/622571/step/10?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/11?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/12?auth=login&unit=619541
""" нестандартное условие """
def fn(a, mv):
    if a < 10: return not mv % 2
    if not mv: return 0
    if a % 2:
        g = [fn(a-1, mv-1), fn(a-2, mv-1), fn(a-3, mv-1), fn(a-4, mv-1),fn(a-5, mv-1)]
    else:
        g = [fn(a-1, mv-1), fn(a-2, mv-1), fn(a-3, mv-1), fn(a-4, mv-1),fn(a-5, mv-1), fn(a//2, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)
print(*[s for s in range(50, 10, -1) if fn(s, 2)])  # 15
print(*[s for s in range(50, 10, -1) if fn(s, 3) and not fn(s, 1)][::-1])  # 1730
print(*[s for s in range(50, 10, -1) if fn(s, 4) and not fn(s, 2)])  # 21


# https://stepik.org/lesson/622571/step/13?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/14?auth=login&unit=619541
# https://stepik.org/lesson/622571/step/15?auth=login&unit=619541
""" нестандартное условие """
def fn(a,b, mv):
    if a + b <= 18: return not mv % 2
    if not mv: return 0
    g = [fn(a - 1, b, mv - 1), fn(a // 2, b, mv - 1), fn(a, b - 1, mv - 1), fn(a, b // 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)
print(*[s for s in range(10, 100) if fn(s, s, 2)])  # 13
print(*[s for s in range(6, 100) if fn(13, s, 3) and not fn(13, s, 1)])  # 1427
print(min(s for s in range(10, 100) if fn(s, s, 4) and not fn(s,s,2)))  # 14

