""" https://kompege.ru/task """
"""
1351 2340 3032 4502 9376 12475 14419 24804
"""

# 1351 Danov2101 (Уровень: Средний)
# ✅ добавляем  аргумент со значением по умолчанию и меняем его только при наступлении события
def f(a, b, c=0):
    if a == b and c:
        return 1
    c += a in (17, 23)
    if a > b:
        return 0
    return f(a + 1, b, c) + f(a + 2, b, c)
print(f(11, 29))  # 3861


# 2340 (Уровень: Средний)
def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 2, b) + f(a + 4, b) + f(a + 5, b)

for n in range(32, 100):
    if f(31, n) == 1001:
        print(n)  # 56
        break


# 3032 (Уровень: Средний)
def f(a, b, c=0):
    if c <= 7 and a == b:
        return 1
    if a > b:
        return 0
    if c == 0:
        return f(a + 1, b, c + 1) +  f(a + 3, b) + f(a * 2, b)  #  первая программа a+1
    return f(a + 3, b, 0) + f(a * 2, b, 0)  # если ранее была программа a+1 (с=1), то мы ее не делаем, а параметр с делаем с=0

print(f(3, 30))  # 407


# 4502 (Уровень: Сложный)
def f(a=1, c=0):
    if c == 6:
        res.add(a)
        return  # получаем число на 6-м ходу и завершаем ветку дерева
    f(a + 1, c + 1)
    f(a + 2, c + 1)
    f(a * 2, c + 1)

res = set()
f()
res = sum(1 for i in res if i in [*range(34, 60)])
print(res)


# 9376 Джобс 10.06.23 (Уровень: Средний)
def f(a, b, c=0):
    c += a in (15, 21)
    if a == b and c == 1:
        return 1
    if a > b or c > 1:
        return 0
    return f(a + 1, b, c) + f(a + 2, b, c) + f(a * 3, b, c)
print(f(6, 25))  # 2700


# 12475 ФИПИ (Уровень: Средний)
from functools import *
@lru_cache(None)
def f(a, c=0):
    if c == 68:
        res.add(a)
        return  # получаем число на 68-м ходу и завершаем ветку дерева
    f(a + 3, c + 1)
    f(a - 2, c + 1)

res = set()
f(1)
print(len(res))


# 14419 (Уровень: Средний)
def f(a, b, d):
    if a == b:
        return 1
    if a > b or a == 30:
        return 0
    return f(a + d, b, d) + f(a * 2, b, d)

res = 0
for d in range(1, 10):  # дальше 9-ти нет смысла перебирать т.к. аргумент 'а' станет больше 10-ти
    res += f(1, 10, d) * f(10, 100, d)
print(res) # 3349


# 24804 (Уровень: Средний)
# ✅ добавляем  аргумент со значением по умолчанию и меняем его только при наступлении события
def f(a, b, c=0):
    if a == b and c < 2:
        return 1
    c += a in (4, 16)
    if a > b:
        return 0
    return f(a * 2, b, c) + f(a**2, b, c) + f(a**3, b, c)
print(f(2, 131072))  # 32







# 🍒 🍓 🌶️ задачи со стороны

""" 23.1 Количество программ с обязательным и избегаемым этапами """
# https://stepik.org/lesson/564194/step/11?unit=558442
# Сколько существует различных программ, которые преобразуют исходное число 1 в число 68
def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 1:  # ❗ исключаем ветку f(a ** 2, b) т.к. она зацикливается
        return f(a + 1, b) + f(a * 2, b)
    return f(a + 1, b) + f(a * 2, b) + f(a ** 2, b)
print(f(1, 68))  # 3628


# https://stepik.org/lesson/564227/step/9?unit=558475
def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 1, b) + f(int('1' + f'{a:b}', 2), b)

b = int('110001', 2)
print(f(4, b))  # 33


def f(a, b, c=0):
    if a == b and c % 2:
        return 1
    if a > b:
        return 0
    if a == 1:  # ❗ ветка f(a ** 2, b, c + 1) уведет в бесконечность
        return f(a + 2, b, c + 1) +  f(a * 2, b, c + 1)
    return f(a + 2, b, c + 1) +  f(a * 2, b, c + 1) + f(a ** 2, b, c + 1)
print(f(1, 100))  # 1025



""" 23.2 Число по количеству программ """
# https://stepik.org/lesson/644891/step/2?unit=641496
# Определите число, для получения которого из числа 1 существует 175 программ.
def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 1, b) + f(a + 5, b) + f(a * 3, b)

for n in range(100):
    if f(1, n) == 175:
        print(n)  # 19
        break


# https://stepik.org/lesson/564227/step/3?unit=558475
# Найдите длину самой короткой программы, в результате выполнения которой при исходном числе 1 результатом является число 227
def f(a, k, c=0):  # k - за сколько шагов должны придти к цели, c=0 - подсчет шагов
    if a == 227 and c==k:
        return 1
    if a > 227 or c > k:
        return 0
    return f(a + 1, k, c + 1) + f(a + 5, k, c + 1) +  f(a * 3, k, c + 1)

for i in range(1, 100):
    if f(1, i):
        print(i)  # 7
        break


# https://stepik.org/lesson/564227/step/4?unit=558475
# Сколько существует программ минимальной длины,
# в результате выполнения которых при исходном числе 1 результатом является число 28
def f(a, k, c=0):  # k - за сколько шагов должны придти к цели, c=0 - подсчет шагов
    if a == 28 and c==k:
        return 1
    if a > 28 or c > k:
        return 0
    return f(a + 1, k, c + 1) + f(a + 2, k, c + 1) + f(a * 2, k, c + 1)

for i in range(1, 100):
    if f(1, i):  # путь минимальной длины
        print(f(1, i))  # 3   кол-во программ для данного минимального пути
        break


# https://stepik.org/lesson/564227/step/10?unit=558475
# Укажите наименьшее натуральное число, которое нельзя получить из исходного числа 1,
# выполнив программу исполнителя, содержащую не более четырёх команд.
def f(a, b, c=0):
    if a == b and c <= 4:
        return 1
    if a > b or c > 4:
        return 0
    return f(a + 1, b, c + 1) + f(a * 2, b, c + 1)

for n in range(2, 100):
    if not f(1, n):
        print(n)
        break


# https://stepik.org/lesson/564227/step/11?unit=558475
def f(a, b, c=0):
    if c <= 7 and a == b:
        return 1
    if c > 7:  # ❗ завершаем только по превышению кол-ва программ
        return 0
    return f(a + 1, b, c + 1) +  f(a * 2, b, c + 1) + f(a - 3, b, c + 1)

print(f(1, 10))  # 38


""" 23.3 Количество чисел по заданному числу команд """
# https://stepik.org/lesson/564227/step/6?unit=558475
# Сколько разных чисел может быть получено из числа 1 с помощью программ, состоящих из 7 команд
def f(a=1, c=0):
    if c == 7:
        res.add(a)
        return  # получаем число на 7-м ходу и завершаем ветку дерева
    f(a + 1, c + 1)
    f(a + 5, c + 1)
    f(a * 3, c + 1)

res = set()
f()
print(len(res))