"""
Task 19
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

# https://stepik.org/lesson/909256/step/3?unit=914858
def fn(n):
    if n > 16:
        return 'w'
    if fn(n + 1) == 'w' or fn(n * 2) == 'w':
        return 'p1'
cnt = 0
for n in range(1, 17):
    if fn(n) == 'p1':
        cnt += 1
print(cnt)  # 8

# вариант
def fn(n, mv):
    if n > 16:
        return mv == 1
    return any([n + 1 > 16, n * 2 > 16])
cnt = 0
for n in range(1, 17):
    if fn(n, 0):
        cnt += 1
print(cnt)  # 8


# https://stepik.org/lesson/909256/step/5?unit=914858
def fn(n):
    if n > 16:
        return 'w'  # Конец игры
    if fn(n + 1) == 'w' or fn(n * 2) == 'w':
        return 'p1'  # Выигрышная позиция для 1-го хода
    if fn(n + 1) == 'p1' and fn(n * 2) == 'p1':
        return 'v1'  # Выигрышная позиция для 2-го хода
    if fn(n + 1) == 'v1' or fn(n * 2) == 'v1':
        return 'p2'  # Выигрышная позиция для 3-го хода
for n in range(1, 17):
    if fn(n) == 'p2':
        print(n, end=' ')  # 4 7

# вариант
def fn(n, mv):
    if n > 16:
        return mv == 3
    if not mv % 2:
        return any([fn(n + 1, mv + 1), fn(n * 2, mv + 1)])
    return all([fn(n + 1, mv + 1), fn(n * 2, mv + 1)])
for n in range(1, 17):
    if fn(n, 0):
        print(n, end=' ')  # 4 7


# https://stepik.org/lesson/909256/step/6?unit=914858
def fn(n):
    if n > 16:
        return 'w'  # Конец игры
    if fn(n + 1) == 'w' or fn(n * 2) == 'w':
        return 'p1'  # Выигрышная позиция для 1-го хода
    if fn(n + 1) == 'p1' and fn(n * 2) == 'p1':
        return 'v1'  # Выигрышная позиция для 2-го хода
    if fn(n + 1) == 'v1' or fn(n * 2) == 'v1':
        return 'p2'  # Выигрышная позиция для 3-го хода
    if (fn(n + 1) == 'p1' or fn(n + 1) == 'p2') and (fn(n * 2) == 'p1' or fn(n * 2) == 'p2'):
        return 'v2'  # Выигрышная позиция для 4-го хода

for n in range(1, 17):
    if fn(n) == 'p2':
        print(n, end=' ')  # 6

# Вариант
# 19/course_100138/19_02.ods   Условие задачи 6


# https://stepik.org/lesson/909256/step/7?unit=914858
def kp(n):
    if n >= 27:
        return 'w' # достигнуто необходимое количество камней, победа
    if kp(n + 2) == 'w' or kp(n * 2) == 'w':
        return 'p1' # Петя побеждает первым ходом
    if kp(n + 2) == 'p1' and kp(n * 2) == 'p1':
        return 'v1' # Ваня побеждает первым ходом
    if kp(n + 2)== 'v1' or kp(n * 2) == 'v1':
        return 'p2' # Петя побеждает вторым ходом
    if (kp(n + 2) == 'p1' or kp(n + 2) == 'p2') and (kp(n * 2) == 'p1' or kp(n * 2) == 'p2'):
        return 'v2' # Ваня побеждает вторым ходом

for s in range(26, 0, -1):
    print(s, kp(s))



# https://stepik.org/lesson/909256/step/8?unit=914858
def fn(n):
    if n >= 27:
        return 'w' # достигнуто необходимое количество камней, победа
    if fn(n + 2) == 'w' or fn(n * 2) == 'w':
        return 'p1' # Петя побеждает первым ходом

cnt = 0
for n in range(26, 0, -1):
    cnt +=  fn(n) == 'p1'
print(cnt)  # 13


# https://stepik.org/lesson/909256/step/9?unit=914858
def fn(n):
    if n >= 27:
        return 'w' # достигнуто необходимое количество камней, победа
    if fn(n + 2) == 'w' or fn(n * 2) == 'w':
        return 'p1' # Петя побеждает первым ходом
    if fn(n + 2) == 'p1' and fn(n * 2) == 'p1':
        return 'v1' # Ваня побеждает первым ходом

cnt = 0
for n in range(1, 27):
    if fn(n) == 'v1':
        print(n, end=' ')  # 12 13
# Вариант таблицей
# 19/course_100138/19_02.ods   Условие задачи 9


# https://stepik.org/lesson/909256/step/10?unit=914858
def fn(n):
    if n >= 27:
        return 'w' # достигнуто необходимое количество камней, победа
    if fn(n + 2) == 'w' or fn(n * 2) == 'w':
        return 'p1' # Петя побеждает первым ходом
    if fn(n + 2) == 'p1' and fn(n * 2) == 'p1':
        return 'v1' # Ваня побеждает первым ходом
    if fn(n + 2)== 'v1' or fn(n * 2) == 'v1':
        return 'p2' # Петя побеждает вторым ходом

cnt = 0
for n in range(1, 27):
    if fn(n) == 'p2':
        print(n, end=' ')  # 6 10 11
# Вариант таблицей
# 19/course_100138/19_02.ods   Условие задачи 10


# https://stepik.org/lesson/909256/step/11?unit=914858
# Важное примечание: у Пети стратегии нет !!!
def fn(n):
    if n >= 27:
        return 'w' # достигнуто необходимое количество камней, победа
    if fn(n + 2) == 'w' or fn(n * 2) == 'w':
        return 'p1'
    if fn(n + 2) == 'p1' and fn(n * 2) == 'p1':
        return 'v1'
    if fn(n + 2)== 'v1' or fn(n * 2) == 'v1':
        return 'p2'
    if (fn(n + 2) == 'p1' or fn(n + 2) == 'p2') and (fn(n * 2) == 'p1' or fn(n * 2) == 'p2'):
        return 'v2' # Ваня побеждает вторым ходом (у Пети стратегии нет)

cnt = 0
for n in range(1, 27):
    if fn(n) == 'v2':
        print(n, end=' ')  # 8 9
# Вариант таблицей
# 19/course_100138/19_02.ods   Условие задачи 11


# https://stepik.org/lesson/909256/step/12?unit=914858
def kp(n):
    if n >= 50:
        return 'w' # достигнуто необходимое количество камней, победа
    if kp(n + 4)== 'w' or kp(n * 3) == 'w':
        return 'p1' # Петя побеждает первым ходом
    if kp(n + 4) == 'p1' and kp(n * 3) == 'p1':
        return 'v1' # Ваня побеждает первым ходом
    if kp(n + 4) == 'v1' or kp(n * 3) == 'v1':
        return 'p2' # Петя побеждает вторым ходом
    if (kp(n + 4) == 'p1' or kp(n + 4) == 'p2') and (kp(n * 4) == 'p1' or kp(n * 4) == 'p2'):
        return 'v2' # Ваня побеждает вторым ходом

for s in range(49, 0, -1):
    print(s, kp(s))


# https://stepik.org/lesson/909256/step/13?unit=914858
def fn(n):
    if n >= 50:
        return 'w' # победа
    if fn(n + 4) == 'w' or fn(n * 3) == 'w':
        return 'p1' # Петя побеждает первым ходом
cnt = 0
for s in range(49, 0, -1):
    cnt += fn(s) == 'p1'
print(cnt)  # 33


# https://stepik.org/lesson/909256/step/14?unit=914858
def fn(n):
    if n >= 50:
        return 'w' # победа
    if fn(n + 4) == 'w' or fn(n * 3) == 'w':
        return 'p1' # Петя побеждает первым ходом
    if fn(n + 4) == 'p1' and fn(n * 3) == 'p1':
        return 'v1' # Ваня побеждает первым ходом

cnt = 0
for s in range(49, 0, -1):
    cnt += fn(s) == 'v1'
print(cnt)  # 4


# https://stepik.org/lesson/909256/step/15?unit=914858
def fn(n):
    if n >= 50:
        return 'w' # победа
    if fn(n + 4) == 'w' or fn(n * 3) == 'w':
        return 'p1' # Петя побеждает первым ходом
    if fn(n + 4) == 'p1' and fn(n * 3) == 'p1':
        return 'v1' # Ваня побеждает первым ходом
    if fn(n + 4) == 'v1' or fn(n * 3) == 'v1':
        return 'p2' # Петя побеждает вторым ходом

cnt = 0
for s in range(1, 50):
    if fn(s) == 'p2':
        print(s)  # 5
        break

False
# https://stepik.org/lesson/909256/step/16?unit=914858
def fn(n):
    if n >= 50:
        return 'w' # победа
    if fn(n + 4) == 'w' or fn(n * 3) == 'w':
        return 'p1' # Петя побеждает первым ходом
    if fn(n + 4) == 'p1' and fn(n * 3) == 'p1':
        return 'v1' # Ваня побеждает первым ходом
    if fn(n + 4) == 'v1' or fn(n * 3) == 'v1':
        return 'p2' # Петя побеждает вторым ходом
    if (fn(n + 4) == 'p1' or fn(n + 4) == 'p2') and (fn(n * 4) == 'p1' or fn(n * 4) == 'p2'):
        return 'v2' # Ваня побеждает вторым ходом
cnt = 0
for s in range(1, 50):
    if fn(s) == 'v2':
        print(s)  # 6
        break


# https://stepik.org/lesson/909257/step/2?unit=914859
from functools import lru_cache
def hod(n):
    return n + 1, n + 2, n + 3, n * 2
@lru_cache(maxsize = 1000)
def kp(n):
    if n >= 38:
        return 'w'
    if any(kp(i) == 'w' for i in hod(n)):
        return 'p1'
    if all(kp(i) == 'p1' for i in hod(n)):
        return 'v1'
    if any(kp(i) == 'v1' for i in hod(n)):
        return 'p2'
    if all(kp(i) == 'p1' or kp(i) == 'p2' for i in hod(n)):
        return 'v2'

for s in range(40, 0, -1):
    print(s, kp(s))


# https://stepik.org/lesson/909257/step/3?unit=914859
from functools import lru_cache
def move(n):
    return n + 1, n + 2, n + 3, n * 2

@lru_cache(maxsize = 1000)
def fn(n):
    if n >= 38:
        return 'w'
    if any(fn(i) == 'w' for i in move(n)):
        return 'p1'
    if all(fn(i) == 'p1' for i in move(n)):
        return 'v1'

for n in range(1, 40):
    if fn(n) == 'v1':
        print(n)  # 18


# https://stepik.org/lesson/909257/step/3?unit=914859
from functools import lru_cache
def move(n):
    return n + 1, n + 2, n + 3, n * 2

@lru_cache(maxsize = 1000)
def fn(n):
    if n >= 38:
        return 'w'
    if any(fn(i) == 'w' for i in move(n)):
        return 'p1'
    if all(fn(i) == 'p1' for i in move(n)):
        return 'v1'
    if any(fn(i) == 'v1' for i in move(n)):
        return 'p2'

for n in range(1, 40):
    if fn(n) == 'p2':
        print(n)  # 9 17


# https://stepik.org/lesson/909257/step/5?unit=914859
from functools import lru_cache

""" Внимание! Новый вариант! ОЧЕНЬ ХОРОШИЙ !!! """
# Лучший вариант
# @lru_cache(None)  # Для этого случая не нужно
def fn(st, mv):
    if st >= 38: return mv % 2 == 0
    if mv == 0: return 0
    gm = [fn(st + 1, mv - 1), fn(st + 2, mv - 1), fn(st + 3, mv - 1), fn(st * 2, mv - 1)]
    if (mv - 1) % 2 == 0: return any(gm)
    return all(gm)

for n in range(1, 40):
    if fn(n, 4) and not fn(n, 2):  # Ищем победы В4 но исключаем вариант победы В2
        print(n)  # 14

# Вариант хуже (работает медленнее + кода больше)
def move(n):
    return n + 1, n + 2, n + 3, n * 2
@lru_cache(maxsize = 1000)

def fn(n):
    if n >= 38:
        return 'w'
    if any(fn(i) == 'w' for i in move(n)):
        return 'p1'
    if all(fn(i) == 'p1' for i in move(n)):
        return 'v1'
    if any(fn(i) == 'v1' for i in move(n)):
        return 'p2'
    if all(fn(i) == 'p1' or fn(i) == 'p2' for i in move(n)):
        return 'v2'

for n in range(1, 40):
    # Ищем победы v2 (В4) но исключаем вариант победы v1 (В2)
    if fn(n) == 'v2' and not fn(n) == 'v1':
        print(n)  # 14


# https://stepik.org/lesson/909257/step/6?unit=914859
from functools import lru_cache
def hod(n):
    return n+1, n+2, n*3
@lru_cache(maxsize = 1000)
def kp(n):
    if n >= 65:
        return 'w'
    if any(kp(i) == 'w' for i in hod(n)):
        return 'p1'
    if all(kp(i) == 'p1' for i in hod(n)):
        return 'v1'
    if any(kp(i) == 'v1' for i in hod(n)):
        return 'p2'
    if all(kp(i) == 'p2' or kp(i) == 'p1' for i in hod(n)):
        return 'v2'

for s in range(64, 0,-1):
    print(s, kp(s))


# https://stepik.org/lesson/909257/step/7?unit=914859
def fn(st, mv):
    if st > 64: return mv == 0
    # if st > 64: return mv % 2 == 0  # ловит ходы П1 дальше 64
    if mv == 0: return 0
    rules = [fn(st + 1, mv - 1), fn(st + 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0: return any(rules)
    return all(rules)

for s in range(1, 67):
    if fn(s, 2):
        print(s) # 21


# https://stepik.org/lesson/909257/step/7?unit=914859
def fn(st, mv):
    if st > 64: return mv == 0  # Если ищем П1 или В1 (иначе получаем камни st > 64)
    # if st > 64: return mv % 2 == 0  # ловит ходы П1 дальше 64
    if mv == 0: return 0
    rules = [fn(st + 1, mv - 1), fn(st + 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0: return any(rules)
    return all(rules)

for s in range(1, 67):
    if fn(s, 3) and not fn(s, 1):
        print(s) # 7 20


# https://stepik.org/lesson/909257/step/9?unit=914859
def fn(st, mv):
    # if st > 64: return mv == 0
    if st > 64: return mv % 2 == 0
    if mv == 0: return 0
    rules = [fn(st + 1, mv - 1), fn(st + 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0: return any(rules)
    return all(rules)

for s in range(1, 67):
    # if fn(s, 4):
    if fn(s, 4) and not fn(s, 2):
        print(s) # 18


# https://stepik.org/lesson/909257/step/11?unit=914859
def fn(st, mv):
    if st > 35:
        # return mv % 2 == 0
        return mv == 0  # Если ищем П1 или В1 (иначе получаем камни st > 35)
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st + 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 37):
    if fn(s, 2):
        print(s)  # 11


# https://stepik.org/lesson/909257/step/12?unit=914859
def fn(st, mv):
    if st > 35:
        return mv % 2 == 0
        # return mv == 0  # Если ищем П1 или В1 (иначе получаем камни st > 35)
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st + 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 37):
    if fn(s, 3) and not fn(s, 1):
        print(s) # 9 10  --> answer 2


# https://stepik.org/lesson/909257/step/13?unit=914859
def fn(st, mv):
    if st > 35:
        return mv % 2 == 0
        # return mv == 0  # Если ищем П1 или В1 (иначе получаем камни st > 35)
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st + 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 37):
    if fn(s, 4) and not fn(s, 2):
        print(s)  # 8


# https://stepik.org/lesson/912172/step/2?unit=917804
def fn(st, mv):
    if st > 29:
        # return mv % 2 == 0
        return mv == 0  #
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st * 2, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return any(rules)  # П1 сделал ошибочный ход (подиграл В1)

for s in range(1, 31):
    if fn(s, 2):
        print(s) # 8 ... 28  --> 8


# https://stepik.org/lesson/912172/step/3?unit=917804
def fn(st, mv):
    if st > 49:
        return mv % 2 == 0
        # return mv == 0
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st * 2, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 31):
    if fn(s, 3) and not fn(s, 1):
        print(s) # 12 23  --> 2


# https://stepik.org/lesson/912172/step/4?unit=917804
def fn(st, mv):
    if st > 55:
        return mv % 2 == 0
        # return mv == 0
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 31):
    if fn(s, 4) and not fn(s, 2):
        print(s) # 16


# https://stepik.org/lesson/912172/step/6?unit=917804
def fn(st, mv):
    if 36 <= st <= 60:
        return mv % 2 == 0
    if st > 60:
        return mv % 2 != 0
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st * 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 36):
    if fn(s, 2):
        print(s) # 34


# https://stepik.org/lesson/912172/step/7?unit=917804
def fn(st, mv):
    if 36 <= st <= 60:
        return mv % 2 == 0
        # return mv == 0
    if st > 60:
        return mv % 2 != 0
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st * 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 36):
    if fn(s, 3) and not fn(s, 1):
        print(s) # 33  --> 1


# https://stepik.org/lesson/912172/step/8?unit=917804
def fn(st, mv):
    if 36 <= st <= 60:
        return mv % 2 == 0
        # return mv == 0
    if st > 60:
        return mv % 2 != 0
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st * 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 36):
    if fn(s, 4) and not fn(s, 2):
        print(s) # 11 32


# https://stepik.org/lesson/912172/step/9?unit=917804
def fn(st, mv):
    if 43 <= st <= 72:
        return mv % 2 == 0
    if st > 72:
        return mv % 2 != 0
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st * 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 43):
    if fn(s, 2):
        print(s) # 14 41  --> 14


# https://stepik.org/lesson/912172/step/11?unit=917804
def fn(st, mv):
    if 43 <= st <= 72:
        return mv % 2 == 0
    if st > 72:
        return mv % 2 != 0
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st * 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return all(rules)

for s in range(1, 43):
    if fn(s, 3) and not fn(s, 1):
        print(s) # 7 13 40  --> 3


# https://stepik.org/lesson/912172/step/10?unit=917804
""" ! ! !  Новая фишка. Будет использоваться в других случаях ! !  """
# w=eval('all') - аргумент позволяющий менять поведение функции
def fn(st, mv, w=eval('all')):
    if 43 <= st <= 72:
        return mv % 2 == 0
    if st > 72:
        return mv % 2 != 0
    if mv == 0:
        return 0
    rules = [fn(st + 1, mv - 1), fn(st * 2, mv - 1), fn(st * 3, mv - 1)]
    if (mv - 1) % 2 == 0:
        return any(rules)
    return w(rules)  # Новая фишка. Будет использоваться в других случаях

for s in range(1, 43):
    if fn(s, 4) and not fn(s, 2):
        print(s) # 12 39


# https://stepik.org/lesson/597911/step/3?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 40: return mv % 2 == 0
    if mv == 0: return 0
    rules = ([fn(a + 2, b, mv - 1), fn(a * 2, b, mv - 1), fn(a, b + 2, mv - 1) , fn(a, b * 2, mv - 1)])
    if (mv - 1) % 2 == 0:
        return any(rules)
    return w(rules)

print([s for s in range(1, 33) if fn(7, s, 1)])  # 17 32
# [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]


# https://stepik.org/lesson/597911/step/4?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 40: return mv % 2 == 0
    if mv == 0: return 0
    rules = ([fn(a + 2, b, mv - 1), fn(a * 2, b, mv - 1), fn(a, b + 2, mv - 1) , fn(a, b * 2, mv - 1)])
    if (mv - 1) % 2 == 0:
        return any(rules)
    return w(rules)

print([s for s in range(1, 33) if fn(7, s, 2)])  # 16


# https://stepik.org/lesson/597911/step/5?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 40: return mv % 2 == 0
    if mv == 0: return 0
    rules = ([fn(a + 2, b, mv - 1), fn(a * 2, b, mv - 1), fn(a, b + 2, mv - 1) , fn(a, b * 2, mv - 1)])
    if (mv - 1) % 2 == 0:
        return any(rules)
    return w(rules)

print(*[s for s in range(1, 33) if fn(7, s, 3) and not fn(7, s, 1)])  # 8 10 11 14 15
# [8, 10, 11, 14, 15]


# https://stepik.org/lesson/597911/step/6?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 40: return mv % 2 == 0
    if mv == 0: return 0
    rules = ([fn(a + 2, b, mv - 1), fn(a * 2, b, mv - 1), fn(a, b + 2, mv - 1) , fn(a, b * 2, mv - 1)])
    if (mv - 1) % 2 == 0:
        return any(rules)
    return w(rules)

print(*[s for s in range(1, 33) if fn(7, s, 4) and not fn(7, s, 2)])  # 13


# https://stepik.org/lesson/597911/step/7?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 40: return mv % 2 == 0
    if mv == 0: return 0
    rules = ([fn(a + 2, b, mv - 1), fn(a * 2, b, mv - 1), fn(a, b + 2, mv - 1) , fn(a, b * 2, mv - 1)])
    if (mv - 1) % 2 == 0:
        return any(rules)
    return w(rules)

print(*[s for s in range(1, 33) if fn(7, s, 2, w=eval('any'))])  # 9
# [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


# https://stepik.org/lesson/597911/step/9?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 40: return not mv % 2
    if not mv: return 0
    rules = [fn(a + 1, b, mv - 1), fn(a * 2, b, mv - 1), fn(a, b + 1, mv - 1), fn(a, b * 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(rules)
    return w(rules)

print(len([s for s in range(1, 31) if fn(9, s, 1)]))  # 15
# [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print([s for s in range(1, 31) if fn(9, s, 2)])  # 15
print(len([s for s in range(1, 31) if fn(9, s, 3) and not fn(9, s, 1)])) # 2
# [3, 14]
# answer 15 15 2


# https://stepik.org/lesson/597911/step/10?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 40: return not mv % 2
    if not mv: return 0
    rules = [fn(a + 1, b, mv - 1), fn(a * 2, b, mv - 1), fn(a, b + 1, mv - 1), fn(a, b * 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(rules)
    return w(rules)

print([s for s in range(1, 31) if fn(9, s, 2, w=eval('any'))])  # 4
# [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]


# https://stepik.org/lesson/597911/step/12?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 49: return not mv % 2
    if not mv: return 0
    rules = [fn(a + 2, b, mv - 1), fn(a * 3, b, mv - 1), fn(a, b + 2, mv - 1), fn(a, b * 3, mv - 1)]
    if not (mv - 1) % 2:
        return any(rules)
    return w(rules)

print(len([s for s in range(1, 43) if fn(6, s, 1)])) # 28
# [15, 16, 17, ... 38, 39, 40, 41, 42]
print([s for s in range(1, 43) if fn(6, s, 2)]) # 14
print([s for s in range(1, 43) if fn(6, s, 3) and not fn(6, s, 1)]) # 2
# [12, 13]
print([s for s in range(1, 43) if fn(6, s, 4) and not fn(6, s, 2)]) # 11
# answer -->  28 14 2 11


# https://stepik.org/lesson/597911/step/13?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 49: return not mv % 2
    if not mv: return 0
    rules = [fn(a + 2, b, mv - 1), fn(a * 3, b, mv - 1), fn(a, b + 2, mv - 1), fn(a, b * 3, mv - 1)]
    if not (mv - 1) % 2:
        return any(rules)
    return w(rules)

print([s for s in range(1, 43) if fn(6, s, 2, w=eval('any'))]) # 1
# [1, 2, 3, ... 38, 39, 40]


# https://stepik.org/lesson/597911/step/15?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 42: return not mv % 2
    if not mv: return 0
    rules = [fn(a + 1, b, mv - 1), fn(a + b, b, mv - 1), fn(a, b + 1, mv - 1), fn(a, b + a, mv - 1)]
    if not (mv - 1) % 2:
        return any(rules)
    return w(rules)

print(*[s for s in range(1, 35) if fn(7, s, 3) and not fn(7, s, 1)])  # 9 10 16


# https://stepik.org/lesson/597911/step/16?unit=592978
def fn(a, b, mv, w=eval('all')):
    if a + b >= 42: return not mv % 2
    if not mv: return 0
    rules = [fn(a + 1, b, mv - 1), fn(a + b, b, mv - 1), fn(a, b + 1, mv - 1), fn(a, b + a, mv - 1)]
    if not (mv - 1) % 2:
        return any(rules)
    return w(rules)

print([s for s in range(1, 35) if fn(7, s, 4) and not fn(7, s, 2)])  # []  --> 0


# https://stepik.org/lesson/765361/step/4?unit=767587
def fn(stn, mv, w=eval('all')):
    if stn >= 22: return not mv % 2
    if not mv: return 0
    rules = [fn(stn + 1, mv - 1), fn(stn * 2, mv - 1)]
    if not (mv - 1) % 2: return any(rules)
    return w(rules)

print('1)', min([s for s in range(1, 22) if fn(s, 1)]))  # 11
print('2)', *[s for s in range(1, 22) if fn(s, 2)])  # 10
print('3)', min([s for s in range(1, 22) if fn(s, 3)]))  # 5
print('4)', max([s for s in range(1, 22) if fn(s, 3) and not fn(s, 1)]))  # 9
print('5)', *([s for s in range(1, 22) if fn(s, 4) and not fn(s, 2)]))  # 8
# 11 10 5 9 8


# https://stepik.org/lesson/765361/step/5?unit=767587
def fn(stn, mv, w=eval('all')):
    if stn >= 21: return not mv % 2
    if not mv: return 0
    rules = [fn(stn + 2, mv - 1), fn(stn * 2, mv - 1)]
    if not (mv - 1) % 2: return any(rules)
    return w(rules)

print(min([s for s in range(1, 21) if fn(s, 1)]), end=' ')  # 11
print(min(s for s in range(1, 21) if fn(s, 2)), end=' ')  # 9
print(max([s for s in range(1, 21) if fn(s, 2)]), end=' ')  # 10
print(min([s for s in range(1, 21) if fn(s, 3) and not fn(s, 1)]), end=' ')  # 5
print(max([s for s in range(1, 21) if fn(s, 3) and not fn(s, 1)]), end=' ')  # 8
print(*([s for s in range(1, 21) if fn(s, 4) and not fn(s, 2)]), end=' ')  # 6
# 11 9 10 5 8 6


# https://stepik.org/lesson/765361/step/6?unit=767587
def fn(stn, mv, w=eval('all')):
    if stn >= 29: return not mv % 2
    if not mv: return 0
    rules = [fn(stn + 1, mv - 1), fn(stn * 2, mv - 1)]
    if not (mv - 1) % 2: return any(rules)
    return w(rules)

print(min([s for s in range(1, 29) if fn(s, 1)]), end=' ')  # 15
print(min(s for s in range(1, 29) if fn(s, 2)), end=' ')  # 14
print(min([s for s in range(1, 29) if fn(s, 3) and not fn(s, 1)]), end=' ')  # 7
print(max([s for s in range(1, 29) if fn(s, 3) and not fn(s, 1)]), end=' ')  # 13
print(min([s for s in range(1, 29) if fn(s, 4)]))  # 12
# 15 14 7 13 12

