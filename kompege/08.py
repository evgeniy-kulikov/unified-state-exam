""" https://kompege.ru/task """
"""
52 399 1241 1339 1363 1933 2928 3029 3729 4564 5553 6901 6985 8417 8553 9155
10090 11201 11291 11300 11827 12097 12240 12462 12917 13094 16319 16374 17521 17549 17627 19753
20069 20269 20270 20271 20833 20855 20857 20898 21894 21975 22419 23367 23746 23808 24455 24533 24614 24888 24984 25132 
26117 26349 26350 27281 27282 27620 27763 28694 28695 28696 28929 29340
31115 31146 31216 31354 31505
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



""" Взято на мой курс """
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



""" Взято на мой курс """
# 6985 (Уровень: Средний)
from itertools import product
cnt = res = 0
for p in product('123456', repeat=6):
    cnt += 1
    p = ''.join(p)
    if not any(['26' in p, '62' in p]) and sorted(p.count(i) for i in set(p)) == [1, 1, 1, 3]:
        res = cnt
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


""" Взято на мой курс """
# 11201 (Уровень: Средний)
from itertools import *
cnt = 0
for p in permutations('12****', 6):
    cnt += p.index('1') + p.index('2') + 2 == 6
print(cnt)  # 96


# 11300 (Уровень: Базовый)
from itertools import *
c = res = 0
for p in product(sorted('ГОНДУБШ'), repeat=6):
    c += 1
    if all([p[0]!='Б', c % 2, p.count('Н') >= 2, not p.count('У')]):
        res = c
print(res)  # 117625


""" Взято на мой курс """
# 11827 (Уровень: Средний)
from itertools import *
cnt = 0
for p in product('02221117', repeat=7):  # 4 чётных и 4 нечётных в восьмеричной СС
    if p[0] != '0':
        p = ''.join(p).replace('0', '2')
        if p.count('2') == 2:
            cnt += all(i not in p for i in ('71', '17', '77'))  # учитываем '77'❗
print(cnt)  # 95904



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


# 12240 ЕГКР 16.12.13_(23) (Уровень: Базовый)
from itertools import *
c = 0
for p in product('012345678', repeat=5):
    c += p[0] != '0' and p.count('5') == 1 and not sum(a == b for a, b in zip(p, p[1:]))
print(c)  # 13377


# 12462 PRO100 ЕГЭ 29.12.13_(23) (Уровень: Базовый) ✅
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


# 19753 (Уровень: Средний)
# Число делится на 4 тогда, когда число, образованное его двумя последними цифрами, делится на 4,
# или если оно оканчивается двумя нулями (но у нас "00" отсекается условием задачи)
from itertools import *
res = 0
for p in product(range(10), repeat=6):
    if p[0] and len(set(p)) == 6:
        if not any(not a % 2 and (not b % 2) for a, b in zip(p, p[1:])):
            res += not int(str(p[-2]) + str(p[-1])) % 4
print(res)  # 7440



# 20069 (Уровень: Средний)
from itertools import *
c = a = b = 0
for p in product(sorted('ЧМСЕИАК'), repeat=5):
    w = ''.join(p)
    c += 1
    if w == 'МАСИК':
        a = c
    if w == 'ЧЕЧИК':
        b = c
        break
print(b - a - 1)  # 5193


# 20269 (Уровень: Средний) 🌶️
from itertools import *
res = 0
for p in product(range(5), repeat=9):
    if p[0]:
        w = ''
        for i in p:
            w += '01'[i % 2]
        if w.count('00') == 2 and not '000' in w:
            res += 1
print(res)  # 151200



# 20270 (Уровень: Средний) 🌶️
from itertools import *
res = 0
for p in product(range(7), repeat=5):
    if p[0]:
        w = ''
        for i in p:
            w += '01'[i % 2]
        if w.count('00') >= 2 and not '000' in w:
            res += 1
print(res)  # 576


# 20271 (Уровень: Сложный) 🌶️😉
# good: 11100 11011 11000 10000 00000
#  bed: 11110 11111
# best variant 👍✔️
from itertools import *
res = 0
for p in product(range(12), repeat=5):
    if p[0]:
        w = ''
        for i in p:
            w += '01'[i % 2]
        res += '1111' not in w
print(res)  # 206064
# излишний код 👎
from itertools import *
res = 0
for p in product(range(12), repeat=5):
    if p[0]:
        w = ''
        for i in p:
            w += '01'[i % 2]
        k = 0
        for i in range(4):
            k += w[i:i+2] == '11'
        if k <= 2:
            res += 1
print(res)  # 206064



# 20833 (Уровень: Средний) 🌶️
from itertools import *
res = c = 0
for p in product(range(10), repeat=5):
    if p[0]:
        c += 1  # ✔️начинаем с 10_000
    if not c % 15:
        if all(a % 2 != b % 2 for a, b in zip(p, p[1:])):
            res = c
print(res)  # 88950


# 20855 (Уровень: Средний) 🌶️
from itertools import *
res = 0
c = -1  # нумерация начинается с '0' ❗❗❗
for p in product(range(13), repeat=3):
    if p[0]:
        c += 1  # ✔️начинаем с 100
    if c % 10 == 7:
        if not any(a % 2 and b % 2 for a, b in zip(p, p[1:])):
        # if all(not a % 2 or (not b % 2) for a, b in zip(p, p[1:])):
            res += 1
print(res)  # 110


# 20857 (Уровень: Средний) 🌶️
from itertools import *
res = c = 0
for p in product(range(9), repeat=6):
    if p[0]:
        c += 1  # ✔️начинаем с 100000
    if c % 10 == 5:
        if not any(a % 2 and b % 2 for a, b in zip(p, p[1:])):
        # if all(not a % 2 or (not b % 2) for a, b in zip(p, p[1:])):
            res = ''.join(map(str, p))
print(res)  # 888881


# 20898 Апробация 05.03.25(Уровень: Базовый)🌶️
from itertools import *
res = 0
for p in product(range(9), repeat=5):
    if p[0] and p.count(0) == 1:
        p = (*p, 2)
        i = p.index(0)
        if all([not p[i-1] % 2,not p[i+1] % 2]):
            res += 1
print(res)  # 5120


# 21894 Открытый вариант 2025(Уровень: Базовый)
from itertools import *
res = 0
for p in product(range(10), repeat=4):
    if p[0] and len(set(p)) == 4:
        w = ''
        for i in p:
            w += '*_'[i % 2]
        if all(i not in w for i in ['**', '__']):
            res += 1
print(res)  # 720


# 21975 (Уровень: Базовый) 🌶️🌶️🌶️👍👍👍
# ⌛ долго ~20sec ⌛
from itertools import *
res = 0
for p in product(range(17), repeat=6):
    if p[0] and len(set(p)) == 6:
        w = ''
        for i in p:
            w += '*_'[i % 2]
        if all(i not in w for i in ['***', '___']):
            res += 1
print(res)  # 3873408

# ✅variant: маска числа + комбинаторика = очень быстро✅
from itertools import *
# Цифры 17-ричной системы — значения 0..16: чётных 9 (0, 2, …, 16), нечётных 8 (1, 3, …, 15).
# Шестизначных чисел с разными цифрами почти 9 млн — перебирать долго. Условие касается только чётности,
# поэтому перебираем «маску» чётности (m[i] = 0 — чётная, 1 — нечётная; масок 2⁶ = 64), а цифры
# ставим по местам слева направо: на очередное чётное место — любая ещё не занятая чётная цифра,
# на нечётное — любая не занятая нечётная; варианты перемножаются.
res = 0
for m in product(range(2), repeat=6):
    three = False  # стоят ли три цифры одной чётности подряд
    for i in range(4):
        if m[i] == m[i + 1] and m[i + 1] == m[i + 2]:
            three = True
            break
    if not three:
        comb = 1  # кол-во вариантов для данного места
        ev = 9  # сколько чётных цифр ещё свободно
        od = 8  # сколько нечётных цифр ещё свободно
        for i in range(6):
            if m[i] == 0:
                if i == 0:  # первая цифра не должна быть нулем
                    comb *= ev - 1  # первая цифра — чётная, но не ноль
                else:
                    comb *= ev  # комбинаторика: кол-во вариантов из возможных чисел для данного места
                ev -= 1  # все цифры должны быть различные
            else:
                comb *= od
                od -= 1
        res += comb  # суммируем варианты для данной маски числа
print(res)  # 3873408



# 22419 (Уровень: Базовый) ️🌶️🌶️🌶️  long work
from itertools import *
res = 0
for p in product(range(13), repeat=7):
    if p[0] and len(set(p)) == 7:
        if 11 in p:
            p = [0] + [*p] + [0]
            i = p.index(11)
            if all([not p[i-1] % 2, not p[i+1] % 2]):
                res += 1
        else:
            res += 1
print(res) # 5372640


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


# 23808 (Уровень: Средний) 🌶️
from itertools import *
d = set(i for i in permutations('КОТЕНОК'))
c = res = 0
for p in product(sorted('КОТЕНА'), repeat=7):
    c += 1
    if c % 2 and p in d:
        res = c
print(res) # 270297


# 24455 (Уровень: Базовый)
from itertools import *
c = res = 0
for p in product(sorted('ТВОРИЛКА'), repeat=6):
    c += 1
    if ''.join(p) in ('ВИКТОР', 'КИРИЛЛ'):
        res += c
print(res) # 152724


# 24533 (Уровень: Средний) 🌶️
from itertools import *
d = set(i for i in permutations('ЕККНООТ'))
c = res = 0
for p in product(sorted('НЕАТОК'), repeat=7):
    c += 1
    if c % 2 and p in d:
        res = c
print(res) # 270297


# 24614 (Уровень: Средний) 🌶️ long work
from itertools import *
w = 'КОНФЕТЫ_ИЛИ_ЖИЗНЬ'
res = 0
for p in set(permutations(w, 7)):
    res += '__' in ''.join(p)
print(res)  # 697500


# 24888 (Уровень: Базовый)
from itertools import *
res = 0
for p in product(range(16), repeat=4):
    if p[0] and p.count(3) == 1:
        res += all(a != b for a, b in zip(p, p[1:]))
print(res)  # 11564


# 24984 (Уровень: Базовый)
from itertools import *
res = 0
for p in product(range(16), repeat=5):
    if p[0] and all(p.count(i) <= 2 for i in set(p)):
        if any(i in (1, 4, 9) for i in p):
            res += 1
print(res)  # 623430



# 25132 (Уровень: Средний)
from itertools import *
c = res = 0
for p in product(sorted('СДАЙЕГЭ'), repeat=6):
    c += 1
    if 'ЕГЭ' in ''.join(p):
        res += c
print(res)  # 79143659


# 26117 (Уровень: Базовый)
from itertools import *
c = res = 0
for p in product(sorted('МУЖЧИНА'), repeat=6):
    c += 1
    if not c % 2 and p[0]  != 'Ж':
        res += p.count('Ч') <= 1
print(res)  # 39528


# 26349 (Уровень: Средний) 🌶️
from itertools import *
for n in range(3, 10):
    c = 0
    for p in product(sorted('СУЛАК'), repeat=n):
        c += 1
        if not c % 2 and p[0] in 'СЛ':
            w = ''.join(p).replace('У', 'А')
            if w.count('А') <= 2 and 'АА' not in w:
                if c == 12368:
                    print(n)  # 6
                    break


# 26350 (Уровень: Средний) 🌶️
from itertools import *
for n in range(3, 10):
    c = 0
    for p in product(sorted('ТАРКИ'), repeat=n):
        c += 1
        if not c % 2 and p[0] in 'ТРК':
            w = ''.join(p).replace('И', 'А')
            if w.count('А') == 3 and 'ААА' in w:
                if c == 31314:
                    print(n)  # 7
                    break


# 27281 (Уровень: Базовый)
from itertools import *
res = 0
for p in product(range(13), repeat=5):
    if p[0] and p.count(0) == 1:
        if all(a != b for a, b in zip(p, p[1:])):
            res += 1
print(res)  # 68244


# 27282 (Уровень: Базовый) 🌶️
from itertools import *
res = 0
for p in product(range(13), repeat=6):
    if p[0] and p.count(0) >= 2:
        r = ''.join(('_*')[i > 9] for i in p)
        if r.count('*') == 2 and '**' in r:
            res += 1
print(res)  # 13779
# fast work variant ✔️
from itertools import *
small = '0123456789'
big = 'abc'
res = 0
for s in product(small, repeat=4):
    if s.count('0') >= 2:
        for b in product(big, repeat=2):
            for i in range(5):
                w = ''.join(s[:i]) + ''.join(b) + ''.join(s[i:])
                res += w[0] != '0'
print(res)  # 13779




# 27620 Апробация 04.03.26(Уровень: Базовый)
from itertools import *
res = c = 0
for p in product(sorted('ЦИТРУС'), repeat=5):
    c += 1
    if p.count('И') == 2 and 'ЦЦ' not in ''.join(p):
        res = c
print(res)  # 7525


# 27763 Апробация 04.03.26(Уровень: Базовый)
from itertools import *
res = 0
for p in product(range(7), repeat=5):
    if p[0] and p.count(0)==1 and p.count(1) <= 2:
        res += 1
print(res)  # 5100


# 28694 (Уровень: Средний)🌶️
from itertools import *
res = 0
for p in product(range(12), repeat=5):
        even = [i for i in p if not i % 2]
        if p[0] and len(even) == 2 and len(set(even)) == 1:
            w = even[0]
            for i in range(4):
                res += p[i:i+2] == (w,w)
print(res)  # 4968


# 28695 (Уровень: Базовый) 🌶️🌶️🌶️
from itertools import *
res = 0
for p in product([*range(13)], repeat=6):
    if p[0]:
        odd = [i for i in p if i % 2]
        if len(odd) == 3 and len(set(odd)) == 1:
            w = odd[0]
            for i in range(4):
                if p[i:i+3] == (w,w,w):
                    res += 1
                    break
print(res)  # 7350
# fast work variant ✔️
from itertools import *
odd = '13579b'
even = '02468ac'
res = 0
for d in odd:
    for p in product(even, repeat=3):
        for i in range(4):  # ниже формируется блок не более трёх цифр
            s = ''.join(p[:i]) + d * 3 + ''.join(p[i:])  # блок 'ddd' смещается с начала до конца строки 'p'
            res += s[0] != '0'
print(res)  # 7350



# 28696 (Уровень: Сложный) 🌶️🌶️
from itertools import *
res = 0
for p in product([*range(14)], repeat=5):
    w = [i for i in p if i % 2]
    if p[0] and len(w) == 2 and w[0] == w[1] and p.index(w[0]) <= 2:
        if p[p.index(w[0]) + 2] == w[0]:
            res += 1
print(res)  # 6517
# variant
from itertools import *
res = 0
for p in product([*range(14)], repeat=5):
    if  p[0] and sum(i % 2 for i in p) == 2:
        for i in range(3):
            if p[i] % 2 and p[i] == p[i + 2]:
                res += 1
print(res)  # 6517


# 28929 ЕГКР 18.04.26(Уровень: Базовый)
from itertools import *
c = res = 0
for p in product(sorted('СИМВОЛ'), repeat=5):
    c += 1
    if c % 2 and p[0] not in 'СО' and p.count('В') == 1 and p.count('С') <= 1:
        res = c
print(res)  # 5137


# 29340 Открытый вариант 2026(Уровень: Базовый)
from itertools import *
c = 0
for p in product(sorted('АПРЕЛЬ'), repeat=6):
    c += 1
    if c % 2 and p[0] not in 'АЛ' and p.count('П') >= 2:
        print(c)  # 7903
        break


# 31115 Основная волна 18.06.26(Уровень: Базовый)
from itertools import *
c = 0
for p in product(sorted('АКЦЕНТ'), repeat=5):
    c += 1
    if not c % 2 and p[0] not in 'АКЕ' and p.count('Ц') >= 2:
        print(c)  # 3924
        break


# 31146 Основная волна 19.06.26(Уровень: Базовый)
from itertools import *
c = res = 0
for p in product(sorted('ПЛАНЕР'), repeat=6):
    c += 1
    if c % 2 and all(not p.count(i) for i in 'ПР') and p.count('А') == 2 and p.count('Н') == 1:
        res = c
print(res)  # 26425


# 31216 Резерв 22.06.26(Уровень: Базовый)
from itertools import *
c = res = 0
for p in product(sorted('ЦВЕТОК'), repeat=6):
    c += 1
    if c % 2 and all(not p.count(i) for i in 'ВЕК') and p.count('Т') == 2 and p.count('Ц') == 1:
        res +=1
print(res)  # 20


# 31354 Пересдача 08.07.26(Уровень: Базовый)
from itertools import *
c = res = 0
for p in product('ЕЛНОСЦ', repeat=6):
    c += 1
    if c % 2 and p[0] not in 'НЦ' and all(p.count(i)==1 for i in 'НЦ'):
        res = c
print(res)  # 38619


# 31505 Демоверсия 2027(Уровень: Базовый)
from itertools import product
cnt = 0
for p in product(sorted('АКЦЕНТ'), repeat=5):
    cnt += 1
    if not cnt % 2 and p[0] not in 'АКЕ' and p.count('Т'):
        print(cnt)  # 3914
        break