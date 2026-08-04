""" https://kompege.ru/task """
"""
52 399 1241 1339 1363 1933 2928 3029 3729 4564 5553 6901 6985 8417 8553 9155
10090 11201 11291 11300 11827 12097 12240 12462 12917 13094 16319 16374 17521 17549 17627 
23367 23746 
"""



# 52 Джобс 31.08.2020 (Уровень: Базовый)
from itertools import *
c = 0
for p in product('ГАФНИЙ', repeat=4):
    c += p[0] != 'Й' and sum(1 for i in p if i in 'АИ') > 0
print(c)  # 888


# 399 (Уровень: Базовый)
from itertools import *
c = 0
for p in set(permutations('011456')):
    s = ''.join(p).replace('0' , '1')
    c += '11' not in s
print(c)  # 72


# 1241 Статград 26.04.2021 (Уровень: Базовый)
from itertools import *
c = 0
for p in product('000012', repeat=5):
    c += p.count('1') <=1 and p.count('2') <= 1
print(c)  # 4864


# 1339 Danov2101 (Уровень: Сложный)
from itertools import product, permutations
res = []
ls = [''.join(p) for p in permutations('мари')]
for i in ls:
    for p in product('ина', repeat=4):
        res += [i + ''.join(p)]
res.sort()
print(res.index('марианна') + 1)  # 1078

# short code
from itertools import product, permutations
ls = [''.join(p) for p in permutations('мари')]
res = sorted(i + ''.join(p) for i in ls for p in product('ина', repeat=4))
print(res.index('марианна') + 1)  # 1078


# 1363 Джобс 16.05.2021 (Уровень: Сложный)
from itertools import *
c = 0
for p in product(range(5), repeat=6):
    if p[0] == 3:
        c += not sum(p) % 2  # для систем счисления с нечётным основанием: число чётно тогда, когда чётна сумма его цифр.
print(c)  # 1562


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


# 2928 Апробация 19.02.2022 (Уровень: Средний)
from itertools import *
c = 0
for p in product('0123456', repeat=7):
    if p[0] in '1246':
        p = ''.join(p)
        c += not ('22' in p and '44' in p)
print(c)  # 466456


# 3029 (Уровень: Средний)
from itertools import *
c = 0
bag = [i*3 for i in '012345678']
for p in product('012345678', repeat=7):
    if p[0] != '0' and p[-1] not in '347':
        c += all(i not in ''.join(p) for i in bag)
print(c)  # 2676053


# 3729 Джобс 05.05.2022 (Уровень: Средний)
from itertools import *
c = res = 0
for p in product('АЕЖЙМУ', repeat=5):
    c += 1
    if not c % 2:
        res += all(a != b for a, b in zip(p, p[1:]))
print(res)  # 1875


# 4564 (Уровень: Сложный) 🌶️🌶️🌶️  всего 281_474_976_710_656 комбинаций - МНОГО!!!
# Перебор за долю секунды
z = 0
for a in range(15, 10, -1):
    for b in range(a-1, 9, -2):
        for c in range(b-1, 8, -2):
            for d in range(c-1, 7, -2):
                for e in range(d-1, 6, -2):
                    for f in range(e-1, 5, -2):
                        for g in range(f-1, 4, -2):
                            for h in range(g-1, 3, -2):
                                for i in range(h-1, 2, -2):
                                    for j in range(i-1, 1, -2):
                                        for k in range(j-1, 0, -2):
                                            for l in range(k-1, -1, -2):
                                                # r = [a, b, c, d, e, f, g, h, i, j, k, l]  #  очень быстро
                                                z += 1
print(z)  # 104


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


# 6985 (Уровень: Средний)
from itertools import product
c = 0
res = None
for p in product('aklmpc', repeat=6):
    c += 1
    r = ''.join(p)
    if not any(['kc' in r, 'ck' in r]) and len(set(r)) == 4:
        res = c
print(res)  # 46605


# 8417 (Уровень: Базовый)
from itertools import permutations
c = 0
for p in permutations('aaassss', 5):
    c += p.count('s') > p.count('a') and 'aa' not in ''.join(p)
print(c)  # 1224


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


# 11300 (Уровень: Базовый)
from itertools import *
c = res = 0
for p in product(sorted('ГОНДУБШ'), repeat=6):
    c += 1
    if all([p[0]!='Б', c % 2, p.count('Н') >= 2, not p.count('У')]):
        res = c
print(res)  # 117625


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
from itertools import product
c = res = 0
for p in product('12345678', repeat=6):
    c += 1
    if p[0] != '8' and p.count('3') == 3 and not c % 2:
        res = c
print(res)  # 226456


# 12240 ЕГКР 16.12.23 (Уровень: Базовый)
from itertools import *
c = 0
for p in product('012345678', repeat=5):
    c += p[0] != '0' and p.count('5') == 1 and not sum(a == b for a, b in zip(p, p[1:]))
print(c)  # 13377


# 12462 PRO100 ЕГЭ 29.12.23 (Уровень: Базовый) ✅
from itertools import *
c = 0
for r in (3, 5):
    for p in product('0123456789abcdef', repeat=r):
        c += all(a > b for a , b in zip(p, p[1:]))
print(c)  # 4928


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


# 13094 (Уровень: Средний)  # ✅✅✅✅✅
from itertools import *
od = '1357'
ev = '2468'
c = 0
for p in product(od,ev,od,ev,od,ev,od,ev,od):  # ✅✅✅✅✅
    if all(p.count(i) <= 3 for i in p):
        c += 1
# умножили на 2 тк есть такое же кол-во чисел начинающихся с четного
print(c * 2)  # 483840

# Реализация того, что происходит в коде  product('1357', '2468', '1357', ... , '1357')
cnt = 0
s1 = '1357'
s2 = '2468'
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for f in s1:
                    for g in s2:
                        for h in s1:
                            for k in s2:
                                for l in s1:
                                    z = a + b + c + d + f + g + h + k + l
                                    if all(z.count(x) <= 3 for x in z):
                                        cnt += 1
print(cnt * 2)  # 483840
# умножили на 2 тк есть такое же кол-во чисел начинающихся с четного

from itertools import product
c = 0
for p in product(map(int, '12345678'), repeat=9):  # ⛔⛔⛔ ДОЛГО ❗❗❗
    if all(p.count(i) <= 3 for i in p):
        if all(a%2 != b%2 for a, b in zip(p, p[1:])):
            c += 1
print(c)  # 483840


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


# 17627 Основная волна 19.06.24 (Уровень: Базовый)
from itertools import product
c = 0
for p in product('0123456789aaaaa', repeat=5):
    c += p[0] != '0' and p.count('8') == 1 and p.count('a') >= 2
print(c)  # 83175





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