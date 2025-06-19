""""""
"""
Task 01
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""


""" 2.1 тест № 1 (егэ-2024, день 1) """
# https://stepik.org/lesson/1594698/step/2?unit=1616271
from itertools import permutations
print(*'12345678')
g = 'AH BAF HGD FC EGD AGC BHE EFC'
t = '247 148 578 126 38 47 136 235'
g = {frozenset(i) for i in g.split()}
for p in permutations('ABCDEFGH'):
    tp = t
    for i in range(len(p)):
        tp = tp.replace(str(i + 1), p[i])
    tp = {frozenset(i) for i in tp.split()}
    if tp == g:
        print(*p)
# 1 2 3 4 5 6 7 8
# G E H C B D F A
# 38

""" Новый вариант """
""" развернуто """
print(*'12345678')
g = 'GF EG CG AE AH BH CE CD DF AB HF'.split()
t = '247 148 578 126 38 47 136 235'.split()
for p in permutations('ABCDEFGH'):
    c = 0
    for x, y in g:
        c += str(p.index(x) + 1) in t[p.index(y)]
    if c == len(g):
        print(*p)
# 1 2 3 4 5 6 7 8
# G E H C B D F A

""" Новый вариант """
""" сжато """
print(*'12345678')
g = 'AB AE AH BH CE CG CD DF EG GF HF'.split()
t = '247 148 578 126 38 47 136 235'.split()
for p in permutations('ABCDEFGH'):
    if all(str(p.index(y) + 1) in t[p.index(x)] for x, y in g):
        print(*p)
# 1 2 3 4 5 6 7 8
# G E H C B D F A


""" 2.4 тест № 2 (пересдача ЕГЭ 2024) """
# https://stepik.org/lesson/1599363/step/2?unit=1621007
from itertools import permutations
g = 'CH HB BE EA AF FC AB CG GD DH'.split()
t = '248 157 456 136 23 34 28 17'.split()
print(*'12345678')
for p in permutations('ABCDEFGH'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
# 1 2 3 4 5 6 7 8
# H C A B F E G D
# C>G = 21  H>B=2   23

