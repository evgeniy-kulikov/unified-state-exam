""""""
"""
Task 08
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""

""" 12.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1221556/step/2?unit=1234966
from itertools import product
cnt = 0
for p in product('МАСЛО', repeat=6):
    if p.count('А') + p.count('О') == 1:
    # if len([i for i in p if i in 'АО']) == 1:
        cnt += 1
print(cnt)  # 2916


# https://stepik.org/lesson/1221556/step/4?unit=1234966
from itertools import product
cnt = 0
for p in product(sorted('ЦАПЛЯ'), repeat=5):
    cnt += 1
    if p.count('А') <=1 and p.count('Ц') == 2 and not p.count('Л'):
        print(cnt, p)
        break


# https://stepik.org/lesson/1221556/step/5?unit=1234966
from itertools import product
import re
a = r'\b2[04]\d*'
b = r'\d*[04]2[04]\d*'
c = r'\d*[04]2\b'
reg = f"{a}|{b}|{c}"
cnt = 0
for p in product('012345', repeat=6):
    if not p[0] == '0' and p.count('2') == 1:
        p = ''.join(p)
        if re.findall(reg, p):
            cnt += 1
print(cnt)  # 3700

# проще
from itertools import product
cnt = 0
for p in product('012345', repeat=6):
    if not p[0] == '0' and p.count('2') == 1:
        p = '*' + ''.join(p) + '*'
        i = p.index('2')
        if not p[i - 1] in '135' and not p[i + 1] in '135':
            cnt += 1
print(cnt)  # 3700


# https://stepik.org/lesson/1221556/step/6?unit=1234966
# повтор букв не ограничен !!!
from itertools import product
cnt = 0
for i in range(5, 8):
    for p in product('БЕРСК', repeat=i):
        cnt += 1
print((cnt))  # 96875


# https://stepik.org/lesson/1221556/step/7?unit=1234966
from itertools import permutations
cnt = 0
for p in permutations('КAРПЫ', 5):
    p = ''.join(p)
    if all([not 'Р' in p[0] + p[-1], not 'AЫ' in p, not 'ЫA' in p]):
        cnt += 1
print(cnt)  # 48


# https://stepik.org/lesson/1221556/step/8?unit=1234966
# not p[0] == 'Ь'  !!!
from itertools import product
cnt = 0
for p in product('МОЛЬ', repeat=5):
    p = ''.join(p)
    if all([not 'ЬЬ' in p, not 'ОЬ' in p, not p[0] == 'Ь']):
        cnt += 1
print(cnt)  # 495


# https://stepik.org/lesson/1221556/step/9?unit=1234966
from itertools import permutations
cnt = 0
for p in permutations('ЛЕВИОСА'):
    p = ''.join(p)
    if all([not p[0] in 'ЕИОА', not p[3] in 'ЛВС']):
        cnt += 1
print(cnt)  # 1440


# https://stepik.org/lesson/1221556/step/10?unit=1234966
from itertools import product
cnt = 0
for p in product('0123456', repeat=6):
    p = ''.join(p)
    if p.count('6') == 1 and not p[0] == '0':
        flag = 1
        for i in range(5):
            if int(p[i]) % 2 == int(p[i + 1]) % 2:
                flag = 0
                break
        cnt += flag
print(cnt)  # 1296


# https://stepik.org/lesson/1221556/step/12?unit=1234966
from itertools import product
cnt = 0
for p in product('АРБУЗ', repeat=6):
    p = ''.join(p)
    cnt += all([p.count('А') == 3, 'АА' in p, not 'ААА' in p])
print(cnt)  # 768


# https://stepik.org/lesson/1221556/step/13?unit=1234966
# Обязятелен set() для исключения одинаковых слов
from itertools import permutations
import re
cnt = 0
for p in set(permutations('АНАСТАСИЯ')):
    p = ''.join(p)
    a = not re.findall(r'[АИЯ]{3,}', p)
    b = not re.findall(r'[НСТ]{3,}', p)
    cnt += a or b
print(cnt)  #  23040


# https://stepik.org/lesson/1221556/step/14?unit=1234966
from itertools import product
cnt = res = 0
for p in product('ДЕЙНПТЬЯ', repeat=4):
    p = ''.join(p)
    cnt += 1
    # if len(set(p)) == 4 and len([i for i in p if i in 'ДЙНПТЬ']) == 4:
    if len(set(p)) == 4 and not [i for i in p if i in 'ЕЯ']:
        res = max(res, cnt)
print(res)  #  3428


# https://stepik.org/lesson/1221556/step/15?unit=1234966
from itertools import product
cnt = 0
for p in product('КАЛИЙ', repeat=6):
    p = ''.join(p)
    cnt += all([p.count('Й') <=1, 'Й' not in p[0]+p[-1], 'ИЙ' not in p, 'ЙИ' not in p])
print(cnt)  # 6400


# https://stepik.org/lesson/1221556/step/16?unit=1234966
from itertools import product
a, b = set(), set()
for p in product('КОНЕЦ', repeat=5):
    a.add(p)
for p in product('ДРАКОН', repeat=5):
    b.add(p)
print(len(a - b) + len(b - a))  # 10415



""" 12.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1221557/step/1?unit=1234967
from itertools import product
cnt = 0
for p in product('QWERTYNO', repeat=7):
    p = ''.join(p)
    flag = 1
    for i in p:
        if p.count(i) > 2:
            flag = 0
            break
    cnt += flag and not 'QWERTY' in p
print(cnt)  # 1345664


# https://stepik.org/lesson/1221557/step/2?unit=1234967
from itertools import product
cnt = res = 0
for p in product('AKLMPC', repeat=6):
    p = ''.join(p)
    cnt += 1
    if not sum(i in p for i in ('KC', 'CK')):
        ls = [p.count(i) for i in set(p)]
        if 3 in ls and len(ls) == 4:
            res = cnt
print(res)  # 46605


# https://stepik.org/lesson/1221557/step/3?unit=1234967
from itertools import product
cnt = res = 0
for p in product('abps', repeat=5):
    p = ''.join(p)
    cnt += 1
    if sum(i in 'bps' for i in p) <= 3:
        if len(set(p)) == 4:
            res = cnt
print(res)  # 913


# https://stepik.org/lesson/1221557/step/4?unit=1234967
from itertools import product
cnt = 0
for p in product('0123456', repeat=5):
    p = ''.join(p)
    if not p[0] == '0' and p.count('6') == 1:
        # a = sum(int(i) for i in p if i in '0246')
        a = sum(int(i) for i in p if not int(i) % 2)
        b = sum(int(i) for i in p if i in '135')
        cnt += a < b
print(cnt)  # 1390


# https://stepik.org/lesson/1221557/step/5?unit=1234967
from itertools import product
from string import hexdigits
cnt = 0
for p in product(hexdigits[:13], repeat=6):
    p = ''.join(p)
    if p[0] != '0' and p.count('a') <= 2 and len(set(p)) == 4:
       cnt += 1
print(cnt)  # 1004300


# https://stepik.org/lesson/1221557/step/6?unit=1234967
from itertools import product
cnt = 0
for p in product(range(10), repeat=6):
    a = p[:3]
    b = p[3:]
    cnt += all([sum(a) == sum(b),
            len(set(a)) == 3 and len(set(b)) == 3,
            len(set(a) & set(b)) > 0,
            a != b])  #  (2,1,0) (1,0,2)     (0,1,2) (1,0,2)   варианты счастливого билета
print(cnt)  # 25200


# https://stepik.org/lesson/1221557/step/7?unit=1234967
from itertools import product
cnt = 0
for p in product('abcde', repeat=4):
    cnt += all([p[-1] in 'bcd',
                p[1] in 'abc' and p[1] != p[0],
                (p[0] in 'ae' and p[2] in 'bcd') or (p[0] in 'bcd' and p[2] in 'ae')])
print(cnt)  # 87


# https://stepik.org/lesson/1221557/step/8?unit=1234967
# ерез set() удаляем похожие варианты (если в словах есть две и более одинаковых букв)
from itertools import permutations
cnt = 0
for p in set(permutations('АМФИБРАХИЙ')):
    p = ''.join(p)
    cnt +=  any(['ИИФАА' in p, 'ААФИИ' in p])
print(cnt)  # 1440

from itertools import permutations
cnt = set()
for p in permutations('АМФИБРАХИЙ'):
    p = ''.join(p)
    if any(['ИИФАА' in p, 'ААФИИ' in p]):
        cnt.add(p)
print(len(cnt))  # 1440


# https://stepik.org/lesson/1221557/step/9?unit=1234967
from itertools import product
cnt = 0
for p in product(range(10), repeat=5):
    if all([p[0], p[-1] not in (3,4,7)]):
        flag = 1
        for i in range(1, 4):
            if len(set(p[i-1: i+2])) == 1:
                flag = 0
        cnt += flag
print(cnt)  # 61236


# https://stepik.org/lesson/1221557/step/10?unit=1234967
from itertools import product
cnt = 0
for p in product(range(10), repeat=7):
    if all([p[0], p[-1] in (0, 5), len(set(p)) == 7]):
        cnt += all([p[i] % 2 != p[i+1] % 2 for i in range(6)])
print(cnt)  # 2880


# https://stepik.org/lesson/1221557/step/11?unit=1234967
from itertools import product
cnt = 0
for p in product(range(9), repeat=7):
    if all([p[0], 0 not in p]):
        if  all([p[i] % 2 != p[i+1] % 2 for i in range(6)]):
            cnt += not sum(p.count(i) > 3 for i in set(p))
print(cnt)  # 32256


# https://stepik.org/lesson/1221557/step/12?unit=1234967
from itertools import product
cnt = 0
for p in product(range(8), repeat=7):
    if p[0] and sum(not i % 2 for i in p) == 2:
        flag = 1
        p = (8,) + p + (8,)
        for i in range(1, 8):
            if p[i] == 7 and (p[i-1] % 2 or p[i+1] % 2):
                flag = 0
                break
        cnt += flag
print(cnt)  # 95904


# https://stepik.org/lesson/1221557/step/13?unit=1234967
from itertools import product
from string import hexdigits
cnt = 0
s = '13579b'
for p in product(hexdigits[:13], repeat=6):
    if p[0] != '0' and p.count('5') <= 1:
        cnt += not sum(p[i] in s and p[i+1] in s for i in range(5))
print(cnt)  # 1666784


# https://stepik.org/lesson/1221557/step/14?unit=1234967
from itertools import product
from string import hexdigits
cnt = 0
s = '02468ace'
for p in product(hexdigits[:16], repeat=5):
    if p[0] != '0' and p.count('6') == 2:
        p = ('1',) + p + ('1',)
        flag = 1
        for i in range(1, 7):
            if p[i] == '6' and (p[i-1] in s or p[i+1] in s):
                flag = 0
                break
        cnt += flag
print(cnt)  # 4352


# https://stepik.org/lesson/1221557/step/15?unit=1234967
from itertools import permutations
cnt = 0
for p in set(permutations('АССЕМБЛЕР')):
    sm = 0
    for i in range(9):
        if p[i] in 'АЕ':
            sm += i + 1
    cnt += sm == 9
print(cnt)  # 3240

# short
from itertools import permutations
cnt = 0
for p in set(permutations('АССЕМБЛЕР')):
    cnt += sum(i + 1 for i in range(9) if p[i] in 'АЕ') == 9
print(cnt)  # 3240


# https://stepik.org/lesson/1221557/step/16?unit=1234967
from itertools import permutations
cnt = 0
for p in permutations('ПАЙТОН'):
    cnt += sum(i + 1 for i in range(6) if p[i] in 'АО') == 6
print(cnt)  # 96




""" 15.3 Закрепление """
# https://stepik.org/lesson/1223041/step/8?unit=1236528
from itertools import product
c = 0
for p in product('god', repeat=6):
    c += p[0] in 'gd' and p[-1] in 'gd'
print(c)

""" 16.4 Закрепление """
# https://stepik.org/lesson/1223083/step/8?auth=login&unit=1236572
from itertools import product
c = 0
for p in product('abcx', repeat=5):
    c += (p[0] == 'x' and 'x' not in p[1:]) or 'x' not in p
print(c)  # 324

