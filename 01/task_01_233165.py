""""""
"""
Task 01
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 1.7 Задание 1 | Задачи прошлых лет """
# https://stepik.org/lesson/1652707/step/10?unit=1675446
# https://kompege.ru/task   № 23738 Демоверсия 2026 (Уровень: Базовый)
# лучше делать через код
from itertools import permutations
print(*'12345678')
g = 'DA AC CB BH HD FH FE EG GC GA'.split()
t = '258 17 56 68 138 347 26 145'.split()
for p in permutations('ABCDEFGH'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(' '.join(p))
"""
1 2 3 4 5 6 7 8
G E B D C H F A
G E D B A H F C
15 + 37 = 52
"""