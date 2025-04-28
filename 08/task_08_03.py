""""""
"""
Task 08
ЕГЭ Питоныч
https://stepik.org/course/100138
"""

""" 20.1 Решение задания 8 КЕГЭ """
# https://stepik.org/lesson/657154/step/4?unit=654239
from itertools import product
cnt = 0
for p in product('кегэ', repeat=5):
    cnt += p[0] in 'кг'
print(cnt)  # 512
# Математика:   2 * 4 * 4 * 4 * 4 = 512


# https://stepik.org/lesson/657154/step/5?unit=654239
from itertools import product
cnt = 0
for p in product('кегэ', repeat=5):
    cnt += p[0] in 'еэ' and p[-1] in 'еэ'
print(cnt)  # 256
# Математика:   2 * 4 * 4 * 4 * 2 = 256


from itertools import product
cnt = 0
for p in product('кегэ', repeat=5):
    cnt += p.count('к') == 2
print(cnt)  # 270


# https://stepik.org/lesson/657154/step/12?unit=654239
from itertools import permutations
cnt = 0
for p in permutations('мышь'):
    p = ''.join(p)
    cnt += p[0] != 'ь' and 'ыь' not in p
print(cnt)  # 12


from itertools import permutations
cnt = 0
for p in permutations('ручка'):
    p = ''.join(p)
    cnt += p[0] != 'ч' and 'ча' not in p and 'чу' not in p
print(cnt)  # 60


# https://stepik.org/lesson/657154/step/14?unit=654239
n = 240 - 1
tr = 'УОА'
s = ''
while n:
    s += tr[n % 3]
    n //= 3
print(s[::-1])


# https://stepik.org/lesson/657154/step/15?unit=654239
# 'ШКОЛА' --> 41320
print(int('41320', 5) + 1)


# https://stepik.org/lesson/657154/step/16?unit=654239
n = 67 - 1
ns = 'КЛРТ'
s = ''
while n:
    s += ns[n % 4]
    n //= 4
print(s[::-1])


""" 20.2 Функция product """
# https://stepik.org/lesson/861063/step/3?unit=865097
from itertools import product
cnt = 0
for p in product('мыло', repeat=5):
    cnt += p[0] in 'ыо' and p[-1] in 'ыо'
print(cnt)  # 256


# https://stepik.org/lesson/861063/step/11?unit=865097
from itertools import product
cnt = 0
for n in range(4, 6):
    for p in product('планшет', repeat=n):
        cnt += p[1] in 'ае' and p[-2] in 'плншт'
print(cnt)  # 3920


""" 20.3 Осортированная последовательность чисел """

# https://stepik.org/lesson/1401020/step/3?unit=1417982
from itertools import product

cnt = 0
for p in product('ЕГЭ', repeat=5):
    cnt += 1
    if ''.join(p) == 'ГЕГЭГ':
        print(cnt)  # 98
        break

# ГЕГЭГ --> 10121
print(int('10121', 3) + 1)  # 98


# https://stepik.org/lesson/1401020/step/4?unit=1417982
d = 'ЕЛМРУ'
s = ''
n = 126 - 1
while n:
    s += d[n % 5]
    n //= 5
print(s[::-1])  # ЛЕЕЕ

# вариант
from itertools import product
cnt = 0
for p in product('ЕЛМРУ', repeat=4):
    cnt += 1
    if cnt == 126:
        print(''.join(p))
        break

""" 20.4 Комбинации с числами """

# https://stepik.org/lesson/861771/step/2?unit=865794
from itertools import product
cnt = 0
for p in product('012345', repeat=5):
    n = ''.join(p)
    cnt += n[0] != '0' and not int(n, 6) % 2
print(cnt)  # 3240


# https://stepik.org/lesson/861771/step/4?unit=865794
from itertools import product
cnt = 0
for p in product('01234567', repeat=3):
    n = ''.join(p)
    cnt += n[0] != '0' and not int(n, 8) % 4 and n == ''.join(sorted(p))
print(cnt)  # 10


# https://stepik.org/lesson/861771/step/5?unit=865794
from itertools import product
cnt = 0
for p in product('0123456789', repeat=3):
    n = ''.join(p)
    cnt += n[0] != '0' and n[-1] in '13579' and n == ''.join(sorted(p, reverse=True))
print(cnt)  # 95


# https://stepik.org/lesson/861771/step/9?unit=865794
from itertools import product
cnt = 0
for p in product('0123456789', repeat=5):
    n = ''.join(p)
    cnt += len([i for i in n if i in '13579']) == 5 and n == n[::-1]
print(cnt)  # 125

# https://stepik.org/lesson/861771/step/11?unit=865794
from itertools import product
cnt = 0
bad = ['40', '42', '44', '46', '04', '24', '64']
for p in product('01234567', repeat=5):
    n = ''.join(p)
    cnt += n[0] != '0' and n.count('4') == 1 and all([i not in n for i in bad])
print(cnt)  # 4676

""" 20.5 Функция permutations """


# https://stepik.org/lesson/861303/step/4?unit=865334
from itertools import permutations
cnt = 0
for p in permutations('ДИВАН'):
    p = ''.join(p)
    cnt += p[0] != 'Д' and p[-1] != 'Д'
print(cnt)  # 72


# https://stepik.org/lesson/861303/step/8?unit=865334
from itertools import permutations, product
cnt = 0
bad = [''.join(i) for i in product('ДВН', repeat=2)]
for p in permutations('ДИВАН'):
    p = ''.join(p)
    cnt += p[0] != 'Й' and all([i not in p for i in bad])
print(cnt)  # 12


# https://stepik.org/lesson/861303/step/10?unit=865334
from itertools import permutations, product
d = set()
for p in permutations('КОЛОБОК'):
    d.add(''.join(p))
print(len(d))  # 420