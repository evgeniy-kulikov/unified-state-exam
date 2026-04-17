""" https://kompege.ru/task """
"""
5553 6901 8553 9155
10090 11201 11291 11827 12097 12240 12917 16319 16374 17521 17549 1933
23367 23746 
"""



# 5553 (Уровень: Базовый)
from itertools import *
s = 'СОТОЧКА'
c = 0
for p in set(permutations(s)):  # set() для исключения ✅ дубликатов 'ОО'
    p = ''.join(p)
    c += any(['ОО' in p, 'ОА' in p, 'АО' in p])
print(c) # 1800


# 6901 (Уровень: Средний)
from itertools import *
s = sorted(set('БАРАШ')) # set() для исключения ✅ дубликатов 'А'
c = res = 0
for p in product(s, repeat=5):
    c += 1
    if sum(i in 'БРШ' for i in p) <= 3 and len(set(p)) == 4:
            res = c
print(res) # 913


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




# 10090 Демоверсия 2024 (Уровень: Базовый)
from itertools import *
c = 0
for p in product('01234567', repeat=5):
    if p[0] != '0' and not '1' in p and len(set(p)) == 5:
        c += not sum(int(a) % 2 == int(b) % 2 for a, b in zip(p, p[1:]))
print(c)  # 180


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


# 12240 ЕГКР 16.12.23 (Уровень: Базовый)
from itertools import *
c = 0
for p in product('012345678', repeat=5):
    c += p[0] != '0' and p.count('5') == 1 and not sum(a == b for a, b in zip(p, p[1:]))
print(c)  # 13377


# 12917 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
from itertools import *
c = 0
for p in set(permutations('ПРОСТО')):
    c += not sum(a == b for a, b in zip(p, p[1:]))
print(c)  # 240
# ✅️Better
from itertools import *
c = 0
for p in set(permutations('ПРОСТО')):
    c += 'ОО' not in ''.join(p)
print(c)  # 240


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
# ✅️Better
c = 0
for p in product('0*_*_*_', repeat=7):
    if p[0] != '0':
        c += p.count('*') == 5
print(c)  # 75816


# 17521 Основная волна 07.06.24 (Уровень: Базовый)
from itertools import *
c = 0
for p in product('01234567', repeat=5):
    c += p[0] not in '01357' and p[-1] not in '26' and p.count('7') <= 2
print(c)  # 9135


# 17549 Основная волна 08.06.24 (Уровень: Базовый)
from itertools import *
s = sorted('ФОКУС')
c = res = 0
for p in product(s, repeat=5):
    c += 1
    if not p.count('Ф') and p.count('У') == 2:
            res = c
print(res) # 2313


# 1933 (Уровень: Базовый)
from itertools import *
res = []
for p in permutations('КЛАБХАУС'):
    if not sum(a == b for a, b in zip(p, p[1:])):
        res.append(p)
print(len(set(res)))  # 15120  # set() для исключения ✅ дубликатов

# ✅️Better
from itertools import *
c = 0
for p in set(permutations('КЛАБХАУС')):  # set() для исключения ✅ дубликатов
    c += not sum(a == b for a, b in zip(p, p[1:]))
print(c)  # 15120






# 23367 Резервный день 19.06.25 (Уровень: Базовый)
from itertools import *
c = 0
for p in product('0123456', repeat=5):
    if p[0] != '0' and p.count('6') == 1:
        c += all(a != b for a, b in zip(p, p[1:]))
print(c)  # 3625


# 23746 Демоверсия 2026 (Уровень: Базовый)
from itertools import *
c = res = 0
for p in product(sorted('СТРОКА'), repeat=5):
    c += 1
    if p[0] not in 'СТА' and p.count('О') == 2 and not c % 2:
        res = c
print(res)  # 5058