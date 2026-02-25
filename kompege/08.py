""" https://kompege.ru/task """
"""
8553 9155
11201 11291 11827 12097 16319 16374
"""



# 8553 (Уровень: Средний)
from itertools import *
c = flag = 0
for p in product('aelmnor*', repeat=6):
    p = ''.join(p)
    if p == 'nenorm':
        flag = 1
    if flag:
        c += 1
    if p[:4] == 'norm':
        break
print(c - 2)  # 17228


# 9155 Джобс 06.06.2023 (Уровень: Базовый)
from itertools import *
c = res = 0
for p in product('*rplea', repeat=5):
    c += 1
    res += p[-1] == '*'
    if c == 387:
        break
print(res)  # 65




# 11201 (Уровень: Средний)
from itertools import *
c = 0
for p in permutations('*0**1*'):
    a = p.index('0')
    b = p.index('1')
    c += a + b == 4
print(c)  # 96


# 11827 (Уровень: Средний)
from itertools import *
c = 0
for p in product('01234567', repeat=7):
    if p[0] != '0':
        p = ''.join(p)
        for i in '246':
            p = p.replace(i, '0')
        for i in '135':
            p = p.replace(i, '*')
        if p.count('0') == 2:
            c += all(i not in p for i in ('7*', '*7', '77'))  # '77' not in p ❗❗❗
print(c)  # 95904


# 11291 (Уровень: Средний)
from itertools import *
c = 0
for p in product('012345', repeat=7):
    if p[0] != '0' and p.count('2') == 1:
        p = ''.join(p).replace('0', '4')
        c += '24' not in p and '42' not in p
print(c)  # 40500


# 12097 Новогодний вариант (Уровень: Базовый)
from itertools import *
c = res = 0
for p in product('agdilnrj', repeat=6):
    c += 1
    if not c % 2 and p.count('d') == 3 and p[0] != 'j':
        res = c
print(res)  # 226456


# 16319 Открытый вариант 2024 (Уровень: Базовый)
from itertools import *
c = res = 0
for p in product('aprcy', repeat=5):
    c += 1
    if p.count('y') == 1 and 'aa' not in ''.join(p):
        res = c
print(res)  # 2969


# 16374 ЕГКР 27.04.24 (Уровень: Базовый)
from itertools import *
c = 0
for p in product('0123456', repeat=7):
    if p[0] != '0':
        s = ''.join(p)
        for i in '246':
            s = s.replace(i, '0')
        c += s.count('0') == 2
print(c)  # 75816
#  ✅️Better
c = 0
for p in product('0*_*_*_', repeat=7):
    if p[0] != '0':
        c += p.count('*') == 5
print(c)  # 75816