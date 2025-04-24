""""""
"""
Task 01
ЕГЭ Питоныч
https://stepik.org/course/100138/syllabus
"""

# https://stepik.org/lesson/767811/step/15?unit=770173
from itertools import permutations
print(*'1234567')
g = {'a': 'cbe', 'b': 'daf', 'c': 'agd', 'd': 'cgb', 'e': 'af', 'f': 'be', 'g': 'cd'}
t = '0010010' + '0000111' + '1001000' + '0010011' + '0100001' + '1101000' + '0101100'
for p in permutations('abcdefg'):
    t_p = ''
    for key in p:
        for val in p:
            t_p += str(int(val in g[key]))
    if t_p == t:
        print(*p)
# 1 2 3 4 5 6 7
# e c f b g a d
# f d e a g b c
# 15


# https://stepik.org/lesson/767811/step/16?unit=770173
from itertools import permutations
print(*'12345678')
g = 'fbe aeh fgh gh ab ca cd cdb'
t = '248 157 456 136 23 34 28 17'
g = {frozenset(i) for i in g.split()}
for p in permutations('abcdefgh'):
    t_g = t
    for i in range(8):
        t_g = t_g.replace(str(i + 1), p[i])
    t_g = {frozenset(k) for k in t_g.split()}
    if t_g == g:
        print(*p)
# 1 2 3 4 5 6 7 8
# h c a b f e g d
# 23


# https://stepik.org/lesson/767811/step/13?unit=770173
from itertools import permutations
g = {'a': 'eh', 'b': 'deg', 'c': 'fh', 'd': 'eb', 'e': 'adb', 'f': 'cg', 'g': 'bhf', 'h': 'acg'}
t = '00100001' + '00001001' + '10010100' + '00100100' + '01000010' + '00110010' + '00001101' + '11000010'
print(*'12345678')
for p in permutations('abcdefgh'):
    t_p = ''
    for key in p:
        for val in p:
            t_p += str(int(val in g[key]))
    if t_p == t:
        print(*p)
# 1 2 3 4 5 6 7 8
# a c e d f b g h
# 37


# https://stepik.org/lesson/1400832/step/5?unit=1417788
from itertools import permutations
g = 'б авже бж жд ежг бжд гдебв'
t = '47 46 6 12567 467 2345 145'
g = {frozenset(i) for i in g.split()}
print(*'1234567')
for p in permutations('абвгдеж'):
    t_p = t
    for i in range(7):
        t_p = t_p.replace(str(i + 1), p[i])
    t_p = {frozenset(i) for i in t_p.split()}
    if t_p == g:
        print(*p)
# 1 2 3 4 5 6 7
# г в а ж е б д
# 17
