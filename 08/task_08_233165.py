""""""
"""
Task 08
ЕГЭ Информатика 2026 | Полный Курс
https://stepik.org/course/233165

all from https://kompege.ru/task
"""


""" 8.1 Задание 8 | Урок 1 """
# https://stepik.org/lesson/1650995/step/3?unit=1673697
from itertools import product
cnt = 0
for p in product('kpeslo', repeat=4):
    cnt += p[0] in 'kpsl' and p[-1] in 'eo'
print(cnt)  # 288


# https://stepik.org/lesson/1650995/step/3?unit=1673697
from itertools import product
cnt = 0
for p in product('abcwxyz', repeat=6):
    cnt += all(i in 'wxyz' for i in p[0] + p[-1]) and all(i in 'abc' for i in p[1:-1])
print(cnt)  # 1296

# прикол
cnt = 0
for a in '1234':
    for b in '123':
        for c in '123':
            for d in '123':
                for e in '123':
                    for f in '1234':
                        cnt += 1
print(cnt)


# https://stepik.org/lesson/1650995/step/4?unit=1673697
from itertools import product
cnt = 0
for p in product('pyla', repeat=6):
    cnt += p.count('y') == 2
print(cnt)  # 1215


# https://stepik.org/lesson/1650995/step/6?unit=1673697
from itertools import product
cnt = 0
for p in product('lodka', repeat=4):
    cnt += p.count('o') >= 2
print(cnt)  # 113


# https://stepik.org/lesson/1650995/step/7?unit=1673697
# https://kompege.ru/task   № 1983 (Уровень: Базовый)
from itertools import product
cnt = 0
for p in product('salo', repeat=6):
    cnt += 1 <= p.count('o') <= 3
print(cnt)  # 3213




# https://stepik.org/lesson/1650995/step/12?unit=1673697
from itertools import product
cnt = 0
for p in product(map(int, '0234567'), repeat=5):  # убираем '1'
    if p[0] and len(set(p)) == 5:
        cnt += all(p[i] % 2 != p[i+1] % 2 for i in range(4))
print(cnt)  # 180

# variant
from itertools import permutations
cnt = 0
for p in permutations('0234567', 5):  # убираем '1'
    s = ''.join(p)
    if s[0] != '0':
        s = s.replace('5', '3').replace('7', '3')
        s = s.replace('2', '0').replace('4', '0').replace('6', '0')
        cnt += '00' not in s and '33' not in s
print(cnt)  # 180



""" 8.2 Задание 8 | Урок 2 """
# https://stepik.org/lesson/1650996/step/8?unit=1673698
# ЛЕЕЕ  --> 1000
print(int('1000', 5) + 1)  # 126


# https://stepik.org/lesson/1650996/step/9?unit=1673698
# https://kompege.ru/task   № 265 Джобс 21.09.2020 (Уровень: Базовый)
from itertools import product
cnt = res = 0
for p in product('agilmopt', repeat=4):
    cnt += 1
    if p[-2:] == ('i', 'm'):
        res = cnt
print(res)  # 4053

# variant
from itertools import product
cnt = 0
for p in product('agilmopt', repeat=4):
    cnt += 1
    if ''.join(p) == 'ttim':
        print(cnt)  # 4053
        break


# https://stepik.org/lesson/1650996/step/10?unit=1673698
# https://kompege.ru/task   № 988 100 базовых задач Е.Джобс (Уровень: Базовый)
from itertools import product
cnt = 0
for p in product('aimpy', repeat=4):
    cnt += 1
    if ''.join(p) == 'apiy':
        print(cnt)  # 85
        break




""" 8.3 Задание 8 | Задачи прошлых лет """
# https://stepik.org/lesson/1650998/step/1?unit=1673700
from itertools import product, permutations
cnt = res = 0
for p in product('agmncty', repeat=6):
    cnt += 1
    if p.count('m') == 2 and p.count('g') <= 1:
        res = cnt
    if p[0] == 'y':
        break
print(res)  # 100810


# https://stepik.org/lesson/1650998/step/7?unit=1673700
# https://kompege.ru/task   № 23192 Основная волна 10.06.25 (Уровень: Базовый)
from itertools import product, permutations
cnt = res = 0
for p in product('еиортя', repeat=6):
    cnt += 1
    if p[0] not in 'ртя' and p.count('и') >= 2 and cnt % 2:
        res = cnt
print(res)  # 23159


# https://stepik.org/lesson/1650998/step/8?unit=1673700
# https://kompege.ru/task   № 23267 Основная волна 11.06.25 (Уровень: Базовый)
from itertools import product
cnt = res = 0
for p in product('akopct', repeat=5):
    cnt += 1
    if all([cnt % 2, p[0] != 'a', p.count('c') == 1]):
        res = cnt
print(res)  # 7775





