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


# https://stepik.org/lesson/1650995/step/8?unit=1673697
# https://kompege.ru/task   № 1984 (Уровень: Базовый)
from itertools import permutations
cnt = 0
for p in permutations('igrok'):
    s = ''.join(p)
    if s[0] != 'k' and 'rok' not in s:
        cnt += 1
print(cnt)  # 90


# https://stepik.org/lesson/1650995/step/9?unit=1673697
# https://kompege.ru/task   № 1985 (Уровень: Средний)
from itertools import permutations
cnt = 0
for p in permutations('----****'):
    s = ''.join(p)
    cnt += all(['**' not in s, '--' not in s])
print(cnt) # 1152


# https://stepik.org/lesson/1650995/step/10?unit=1673697
# https://kompege.ru/task   № 1415 (Уровень: Базовый)
from itertools import permutations, product
cnt = 0
for p in product('00123', repeat=8):
    cnt += p.count('0') == 2
print(cnt)  # 81648


# https://stepik.org/lesson/1650995/step/11?unit=1673697
# https://kompege.ru/task   № 1216 Апробация 27.04 (Уровень: Базовый)
from itertools import product, permutations
cnt = 0
for p in product('01234', repeat=6):
    cnt += p[-1] not in '34' and p[0] not in '10'
print(cnt)  # 5625


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
# https://stepik.org/lesson/1650996/step/1?unit=1673698
# https://kompege.ru/task   № 1288 Открытый вариант КЕГЭ (Уровень: Базовый)
from itertools import product
cnt = 0
for p in product('visna', repeat=6):
    cnt += all([p.count('v') <= 1, p[0] != 's', p[-1] not in 'ia'])
print(cnt)  # 4352


# https://stepik.org/lesson/1650996/step/2?unit=16736988
# https://kompege.ru/task   № 947 (Уровень: Базовый)
from itertools import product
cnt = 0
for p in product('abcd', repeat=4):
    cnt += p[0] <= p[1] <= p[2] <= p[3]
print(cnt)  # 35


# https://stepik.org/lesson/1650996/step/3?unit=1673698
# https://kompege.ru/task   № 1852 Основная волна 2021 (Уровень: Базовый)
from itertools import product, permutations
cnt = 0
for p in product('gepard', repeat=5):
    cnt += all([p.count('g')==1, p[0] != 'a', p[-1] != 'e'])
print(cnt)  # 2200


# https://stepik.org/lesson/1650996/step/4?unit=1673698
# https://kompege.ru/task   № 1921 (Уровень: Базовый)
from itertools import product, permutations
cnt = 0
for p in product('0123456789', repeat=3):
    cnt += all([p[0] != '0', sorted(p) == list(p)])
print(cnt)  # 165


# https://stepik.org/lesson/1650996/step/5?unit=1673698
# https://kompege.ru/task   № 1929 (Уровень: Базовый)
from itertools import permutations
cnt = 0
for p in permutations('deikstra', 6):
    if 'i' in p[:-1]:
        cnt += p[p.index('i') + 1] in 'dkstr'
print(cnt)  # 9000

# variant
from itertools import permutations
cnt = 0
for p in permutations('deikstra', 6):
    w = ''.join(p)
    cnt += any([s in w for s in ('id', 'ik', 'is', 'it', 'ir')])
print(cnt)  # 9000



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




""""""
""" Варианты """
# 29.1 Вариант 2 | Часть 1
# https://stepik.org/lesson/1729865/step/8?unit=1753692
# https://kompege.ru/task  № 19240 ЕГКР 21.12.24 (Уровень: Базовый)
from itertools import *
s = 'авнрья'
c = res = 0
for i in product(s, repeat=5):
    c += 1
    p = ''.join(i)
    if p[0] not in 'ая' and p.count('ь') <= 1 and 'яя' not in p:
        res = c
print(res)  # 6406


# 30.1 Вариант 3 | Часть 1
# https://stepik.org/lesson/1730526/step/9?unit=1754355
# https://kompege.ru/task  № 17549 Основная волна 08.06.24 (Уровень: Базовый)
from itertools import *
cnt = 0
res = 0
for p in product('kocyf', repeat=5):
    cnt += 1
    if p[0] != 'k' and p.count('f') == 0 and p.count('y') == 2:
        res = cnt
print(res)  # 2313


# 31.1 Вариант 4 | Часть 1
# https://stepik.org/lesson/1736669/step/9?unit=1760675
# https://kompege.ru/task  № 21407 Досрочная волна 2025 (Уровень: Базовый)
from itertools import *
s = 'dgiase'
c = 0
for p in product(s, repeat=5):
    if p[0] not in 'iae' and p[-1] not in 'dgs':
        c += 1
print(c)  # 1944


# 32.1 Вариант 5 | Часть 1
# https://stepik.org/lesson/1754188/step/9?unit=1778647
# https://kompege.ru/task  № 21703 ЕГКР 19.04.25 (Уровень: Базовый)
from itertools import *
s = sorted('ПОБЕДА')
c = 0
res = 0
for p in product(s, repeat=6):
    c += 1
    if len(set(p)) == 6 and p[0] == 'О' and not c % 2:
        res = c
print(res)  # 38306


# 33.1 Вариант 6 | Часть 1
# https://stepik.org/lesson/1943170/step/9?unit=1969924
# https://kompege.ru/task  № 23192 Основная волна 10.06.25 (Уровень: Базовый)
from itertools import *
s = sorted([*'теория'])
cnt = 0
res = 0
for p in product(s, repeat=6):
    cnt += 1
    if cnt % 2 and p[0] not in 'тря' and p.count('и') >= 2:
        res = cnt
print(res)  # 23159


# 34.1 Вариант 7 | Часть 1
# https://stepik.org/lesson/1943172/step/9?unit=1969926
# https://kompege.ru/task  № 23267 Основная волна 11.06.25 (Уровень: Базовый)
from itertools import *
c = res = 0
for p in product(sorted('строка'), repeat=5):
    c += 1
    if c % 2 and p[0] != 'а' and p.count('с') == 1:
        res = c
print(res)  # 7775


# 35.1 Вариант 8 | Часть 1
# https://stepik.org/lesson/1943178/step/8?unit=1969932
# https://kompege.ru/task  № 23554 Пересдача 03.07.25 (Уровень: Базовый)
from itertools import *
s = sorted('алгоритм')
c = 0
for p in product(s, repeat=5):
    c += 1
    if not c % 2 and p[0] not in 'аг' and p.count('р') >= 2:
        print(c)  # 8626
        break


