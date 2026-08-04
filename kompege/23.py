""" https://kompege.ru/task """
"""
1063 1351 2340 3032 3084 4488 4500 4502 5443 5494 5552 7011 7347 8585 9376
11953 12475 13099 14419 19253 19487 24804 27130 27311
"""


# 1063 Джобс 15.03.2021 (Уровень: Средний)
def f(a, b, c=0):
    c += a in (9, 17)
    if a == b and c==2:
        return 1
    if a > b:
        return 0
    return f(a+1, b, c) + f(a*2, b, c) + f(a+(2 if a % 2 else 1), b, c)  # 👍
print(f(3, 25))  # 229635


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


# 3084 (Уровень: Средний)
def f(a, b, c=0):
    c += a==29
    if a >= b:
        return a == b and c
    return f(a+2, b, c) + f(a + sum(map(int, str(a))), b, c)
print(f(3, 68))  # 9709


# 4488 (Уровень: Средний) 🌶️🌶️
def f(st, en):
    if st > en:
        return 0
    if st == en:
        return 1
    # суммируем все пути ✅ по допустимым командам с учётом условия про чётность
    return (f(st + 1, en) + f(st + 2, en) if not st % 2 else 0) + f(st*2, en)
print(f(1, 32))  # 101


# 4500 (Уровень: Сложный) 🌶️🌶️
# ❗❗❗ Важно (для решения f(3, 11) * f(11, 79)):
# при переходе через число 11 состояние «была ли последней команда +1» сохраняется для первой команды следующего участка.
# ✅ Для избежания этой сложной проверки, лучше проверим на финише каждой подходящей ветки:
# было ли у нее в пути число 11 (параметр 'num')

from functools import lru_cache
@lru_cache(None)
def f(a, b, c=0, num=0):
    if a == 11:
        num = 1  # путь проходит через число 11
    if a > b or a == 23:
        return 0
    if a == b and num:
        return 1
    if not c:
        return f(a + 1, b, 1, num) + f(a + 2, b, 0, num) + f(a * 2, b, 0, num)
    return f(a + 2, b, 0, num) + f(a * 2, b, 0, num)
print(f(3, 79))  # 812266767


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



# 5443 Джобс 21.12.22 (Уровень: Средний)
def f(st, en, w=''):
    if st > en:
        return 0
    if st == en and all(i in w for i in 'abc'):
        return 1
    return f(st+1, en, w+'a') + f(st+2, en, w+'b') + f(st*2, en, w+'c')
print(f(3, 25))  # 15092


# 5494 (Уровень: Средний) 🌶️🌶️
def f(st, en, w='--'):
    if st > en:
        return 0
    if st == en:
        return 1
    return ((f(st+1, en, w+'+') if w[-2:] != '++' else 0) +
            (f(st*2, en, w+'*') if w[-2:] != '**' else 0))
print(f(1, 16))  # 101

# variant
def f(st, en, prev='', c=0):
    if st > en:
        return 0
    if st == en:
        return 1
    res = 0  # ✅ переменная для хранения количества путей
    if prev != '1' or c < 2:  # если предыдущая команда не 1, или 1 не было уже дважды подряд
        res += f(st+1, en, '1', c+1 if prev=='1' else 1)  # выполняем команду 1
    if prev != '2' or c < 2:  # если предыдущая команда не 2, или 2 не было уже дважды подряд
        res += f(st*2, en, '2', c+1 if prev=='2' else 1)  # выполняем команду 2
    return res  # ✅ возвращаем общее количество путей
print(f(1, 16))  # 101



# 5552 (Уровень: Средний)
def f(a, b, c=0):
    c += a==55
    # if a > b:
    #     return 0
    # if a == b and c:
    #     return 1
    if a >= b:  # Сокращенный вариант ✅
        return  a == b and c
    return f(a+2, b, c) + f(a+int(max(str(a))), b, c)
print(f(32, 76))  # 476


# 7011 (Уровень: Средний)
def f(a, b, s=''):
    if a > b or a == 28 or 'BACA' in s:
        return 0
    if a == b:
        return  1
    return f(a + 2, b, s + 'A') + f(a + 3, b, s + 'B') + f(a * 2, b, s + 'C')
print(f(2, 40))  # 27609


# 8585 (Уровень: Базовый)
def f(a, b, c=0):
    c += a==25
    if a < b:
        return 0
    if a == b and c:
        return 1
    return f(a-sum(map(int, str(a))), b, c) + f(a//2, b, c) + f(a-1, b, c)
print(f(40, 10))  # 247



# 9376 Джобс 10.06.23 (Уровень: Средний)
def f(a, b, c=0):
    c += a in (15, 21)
    if a == b and c == 1:
        return 1
    if a > b or c > 1:
        return 0
    return f(a + 1, b, c) + f(a + 2, b, c) + f(a * 3, b, c)
print(f(6, 25))  # 2700








# 11953 (Уровень: Средний)
from functools import lru_cache
@lru_cache(None)
def f(a, b):
    if a > b or a == 100:
        return 0
    if a == b:
        return  1
    res = f(a ** 2, b)
    if a % 10:
        res += f(a + a % 10, b)
    if a % 68:
        res += f(a + a % 68, b)
    return res
print(f(2, 68) * f(68, 680))  # 47997789947424


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


# 13099 (Уровень: Средний)
def f(a, b, w=0):
    if a == b:
        return 1
    if a > b+1:  #  b+1 >>  8 * 2 = 16 -> 16 - 1 = 15
        return 0
    return (f(a-1, b, 1) if not w else 0) + f(a*2, b, 0) + f(a*3, b, 0)
print(f(3, 15))  # 6

def f(a, b, w=''):
    if a == b:
        return 1
    if a > b+1 or '--' in w:  #  b+1 >>  8 * 2 = 16 -> 16 - 1 = 15
        return 0
    return f(a-1, b, w+'-') + f(a*2, b, w+'*') + f(a*3, b, w+'*')
print(f(3, 15))  # 6


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


# 19253 ЕГКР 21.12.14 (Уровень: Базовый)
def f(a, b, c=0):
    c += a in (19, 29)
    if a < b or a == 24:
        return 0
    if a == b and c == 2:
        return 1
    return f(a-1, b, c) + f(a-6, b, c) + f(a//2, b, c)
print(f(34, 6))  # 115


# 19487 (Уровень: Средний)
def f(st, en, w=0):
    w += st in (20, 30)
    if st > en:
        return 0
    if st == en and w != 2:
        return 1
    return f(st+2, en, w) + f(st+3, en, w) + f(st*2, en, w)

print(f(8, 35))  # 786


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
# 2340 (Уровень: Средний)
def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 2, b) + f(a + 4, b) + f(a + 5, b)

for n in range(100):
    if f(31, n) == 1001:
        print(n)  # 56
        break


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
# (программ одинаковой длины может быть несколько)
res = []
def f(a, b, k=0):  # k - кол-во программ ведущие к числу b
    if a == b:
        res.append(k)
    if a < b:
        # собираем все пути приводящие к числу b (все варианты, в т.ч. и с одинаковым кол-вом шагов)
        f(a + 1, b, k + 1)
        f(a + 2, b, k + 1)
        f(a * 2, b, k + 1)

f(1,28)
# print(min(res))  # 5
print(res.count(min(res)))  # 3


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


# 27130 (Уровень: Средний)
def f(a,b,c=0):
    c += a==959
    if a == b and c:
        return 1
    if a < b:
        return 0
    n = str(a)
    if n[-2] > n[-1]:
        return f(a-3, b, c) + f(int(n[:-2]+n[-1]+n[-2]), b, c)
    return f(a-3, b, c)

print(f(1001, 902))  # 50


# 27311 (Уровень: Средний)
def f(a, b, c=0):
    c += a in (25, 47)
    if a == b and c==1:
        return 1
    if a < b:
        return 0
    return f(a-2, b, c) + f(a-3, b, c) + f(a//5, b, c)

print(f(63, 3))  # 4715761  (подождать расчёт)


