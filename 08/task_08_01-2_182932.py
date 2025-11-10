""""""
"""
Task 08
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
"""


""" 1.3 Повторение 3 часть """
# https://stepik.org/lesson/1342070/step/3?unit=1357751
from itertools import product
cnt = res = 0
for p in product('бгдноуш', repeat=6):
    cnt += 1
    if all([cnt % 2, p[0] != 'б', p.count('н') > 1, not p.count('у')]):
        res = cnt
print(res)  # 117625


# https://stepik.org/lesson/1342070/step/4?unit=1357751
from itertools import product
alf = '0123456789abcdef'
cnt = 0
for p in product(alf, repeat=4):
    if p[0] != '0' and p.count('9') == 1:
        p = [alf.index(i) for i in p]
        if all(p[i] % 2 != p[i+1] % 2 for i in range(3)):
            cnt += 1
print(cnt)  # 1680

# без алфавита
from itertools import product
alf = [*range(16)]
cnt = 0
for p in product(alf, repeat=4):
    if p[0] != 0 and p.count(9) == 1:
        if all(p[i] % 2 != p[i+1] % 2 for i in range(3)):
            cnt += 1
print(cnt)  # 1680


# https://stepik.org/lesson/1342070/step/5?unit=1357751
from itertools import product
cnt = 0
for p in product([*range(6)], repeat=6):
    if p[0] != 0 and p.count(2) == 1:
        p = (0,) + p + (0,)
        i = p.index(2)
        if not p[i-1] % 2 and not p[i+1] % 2:
            cnt += 1
print(cnt)  # 3700



""" 9.4 Задания на исключающие комбинации """
# https://stepik.org/lesson/1107347/step/1?unit=1118585
from re import findall
r = r'[1357]{2}|[02468]{2}'
cnt = 0
# for n in range(int('10000', 8), int('77777', 8) + 1):
for n in range(int('23054', 8), int('76544', 8)): # логически обрезаем интервал
    s = ''
    while n:
        s = str(n % 8) + s
        n //= 8
    d = s
    cnt += all([not s.count('1'), not findall(r, s), len(set(s)) == 5])
print(cnt)


# https://stepik.org/lesson/1107347/step/2?unit=1118585
from re import findall
reg = r'[02468ace]{2}|[13579bdf]{2}'
cnt = 0
for n in range(200, 4500):
    i = hex(n)[2:]
    cnt += all([len(i) == 3, len(set(i)) == 3, not findall(reg, i)])
print(cnt)


# https://stepik.org/lesson/1107347/step/3?unit=1118585
# ... в кодах не должно быть 3-х стоящих рядом гласных ИЛИ  3-х стоящих рядом согласных...
from itertools import permutations
w = {''.join(p) for p in permutations('АААИЯ', 3)}
s = {''.join(p) for p in permutations('НССТ', 3)}
res = set()
for p in permutations('АНАСТАСИЯ'):
    p = ''.join(p)
    if all([not (i in p) for i in w]) or all([not (i in p) for i in s]):
        res |= {p}
print(len(res))  # 23040


# https://stepik.org/lesson/1107347/step/4?unit=1118585
cnt = 0
even = '135'
for n in range(int('10000', 7), int('66666', 7) + 1):
    s = ''
    while n:
        s = str(n % 7) + s
        n //= 7
    if len(s) == 5 and s.count('5') == 1:
        i = s.index('5')
        s = '1' + s + '1'
        cnt += s[i] in even and s[i + 2] in even
print(cnt)