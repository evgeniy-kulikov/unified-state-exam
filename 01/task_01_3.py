# Подготовка к ЕГЭ информатика
# https://stepik.org/course/57248
""""""

# https://stepik.org/lesson/262332/step/1?unit=243224
from itertools import permutations
print(*'1234567')
t = '0000110' + '0011001' + '0100101' + '0100010' + '1010010' + '1001100' + '0110000'
g = {'A': 'BF', 'B': 'AFD', 'C': 'DGE', 'D': 'BC', 'E': 'GC', 'F': 'ABG', 'G': 'FCE'}
for p in permutations(g):
    t_p = ''
    for h in p:
        for rel in p:
            t_p += ['0' ,'1'][rel in g[h]]
    if t_p == t:
        print(*p)
# 1 2 3 4 5 6 7
# A C G D F B E
# E B F D G C A
# 26


# https://stepik.org/lesson/262332/step/2?unit=243224
from itertools import permutations
print(*'1234567')
g = {'А': 'БВ', 'Б': 'АВД', 'В': 'АБДЕГ', 'Г': 'ВЕК', 'Д': 'БВЕ', 'Е': 'КДВГ', 'К': 'ЕГ'}
t = '0101000' + '1001010' + '0000111' + '1100011' + '0010010' + '0111101' + '0011010'
for p in permutations(g):
    t_p = ''
    for h in p:
        for rel in p:
            t_p += ['0' ,'1'][rel in g[h]]
    if t_p == t:
        print(*p)
# 1 2 3 4 5 6 7
# К Г Б Е А В Д
# 8


# https://stepik.org/lesson/262340/step/1?unit=243232
#  Решение через dict()
from itertools import permutations
print(*'1234567')
g = {'A': 'BF', 'B': 'DAF', 'C': 'DEG', 'D': 'BC', 'E': 'CG', 'F': 'ABG', 'G': 'FCE'}
t = '0000110' + '0011001' + '0100101' + '0100010' + '1010010' + '1001100' + '0110000'
for p in permutations(g):
    tmp = ''
    for top in p:
        for rel in p:
            tmp += ['0' ,'1'][rel in g[top]]
    if tmp == t:
        print(*p)
# 1 2 3 4 5 6 7
# A C G D F B E
# E B F D G C A
# 26

#  Решение через frozenset
from itertools import permutations
g = 'BF DFA BC DGE CG FCE ABG'
g = {frozenset(i) for i in g.split()}
t = '56 347 257 26 136 145 23'
print(*'1234567')
for p in permutations('ABCDEFG'):
    tmp = t
    for i in range(7):
        tmp = tmp.replace(str(i + 1), p[i])
    g_tmp = {frozenset(i) for i in tmp.split()}
    if g_tmp == g:
        print(*p)
# 1 2 3 4 5 6 7
# A C G D F B E
# E B F D G C A


# https://stepik.org/lesson/262340/step/3?unit=243232
from itertools import permutations
print(*'1234567')
g = 'БВ АВД АБДЕГ ВЕК БВЕ ДВГК ГЕ'
t = '24 146 567 1267 36 23457 346'
g = {frozenset(i) for i in g.split()}
for p in permutations('АБВГДЕК'):
    tmp = t
    for i in range(7):
        tmp = tmp.replace(str(i + 1), p[i])
    tmp = {frozenset(i) for i in tmp.split()}
    if g == tmp:
        print(*p)
# 1 2 3 4 5 6 7
# К Г Б Е А В Д
# 11

# https://stepik.org/lesson/419936/step/1?unit=409514
from itertools import permutations
print(*'1234567')
t = '0011110' + '0010111' + '1100010' + '1000001' + '1100001' + '1110000' + '0101100'
g = {'А': 'БД', 'Б': 'АВГ', 'В': 'БГД', 'Г': 'БВЕК', 'Д': 'АВЕК', 'Е': 'ГДК', 'К': 'ГЕД'}
for p in permutations(g):
    t_ = ''
    for g_ in p:
        for rel in p:
            t_ += ['0', '1'][rel in g[g_]]
    if t == t_:
        print(*p)
# 1 2 3 4 5 6 7
# Д Г Е А В К Б
# Д Г К А В Е Б
# 18

## frozenset()
# https://stepik.org/lesson/419936/step/1?unit=409514
from itertools import permutations
print(*'1234567')
g = 'БД БГД ГКД АВГ БВЕК ГДЕ АВЕК'
g = {frozenset(i) for i in g.split()}
t = '3456 3567 126 17 127 123 245'
for p in permutations('АБВГДЕК'):
    t_ = t
    for i in range(7):
        t_ = t_.replace(str(i+1), p[i])
    t_ = {frozenset(i) for i in t_.split()}
    if t_ == g:
        print(*p)
# 1 2 3 4 5 6 7
# Д Г Е А В К Б
# Д Г К А В Е Б

# https://stepik.org/lesson/419936/step/2?unit=409514
# 01/pic/57248__01_001.gif
from itertools import permutations
print(*'1234567')
g = 'ВД БВ АВД БГЕК ДЕ ВДК АБГЕ'
g = {frozenset(i) for i in g.split()}
t = '3567 3467 12 26 17 124 125'
for p in permutations('АБВГДЕК'):
    t_ = t
    for i in range(7):
        t_ = t_.replace(str(i + 1), p[i])
    t_ = {frozenset(i) for i in t_.split()}
    if t_ == g:
        print(*p)
# 1 2 3 4 5 6 7
# В Д Г А К Е Б
# В Д Г К А Е Б
# Д В Г А К Б Е
# Д В Г К А Б Е
# 35


# https://stepik.org/lesson/419936/step/3?unit=409514
from itertools import permutations
print(*'1234567')
g = 'АВ БВГ АД ГЕЖ ДЕ ВДЖ БАЕ'
g = {frozenset(i) for i in g.split()}
t = '67 346 24 235 47 127 156'
for p in permutations('АБВГДЕЖ'):
    t_ = t
    for i in range(7):
        t_ = t_.replace(str(i + 1), p[i])
    t_ = {frozenset(i) for i in t_.split()}
    if t_ == g:
        print(*p)
# 1 2 3 4 5 6 7
# Б Е Ж Д Г В А
# Ж В Б А Г Е Д
# 26


# https://stepik.org/lesson/419936/step/4?unit=409514
from itertools import permutations
print(*'1234567')
g = {'А': 'БГВ', 'Б': 'АГЕ', 'В': 'АГ', 'Г': 'АБВДЕЖ', 'Д': 'ГЕЖ', 'Е': 'БГД', 'Ж': 'ГД'}
t = '0011001' + '0010110' + '1101111' + '1010000' + '0110000' + '0110001' + '1010010'
for p in permutations(g):
    t_ = ''
    for key in p:
        for val in p:
            t_ += ['0', '1'][val in g[key]]
    if t_ == t:
        print(*p)
# 1 2 3 4 5 6 7
# А Д Г В Ж Е Б
# Д А Г Ж В Б Е
# 67


# https://stepik.org/lesson/419936/step/5?unit=409514
# 01/pic/57248__01_002.gif
from itertools import permutations
print(*'1234567')
g = {'А': 'БВГ', 'Б': 'АВ', 'В': 'БАГД', 'Г': 'АВДЕ', 'Д': 'ВГЕ', 'Е': 'ДГЖ', 'Ж': 'Е'}
t = '0000011' + '0001101' + '0000100' + '0100111' + '0111000' + '1001001' + '1101010'
for p in permutations('АБВГДЕЖ'):
    t_ = ''
    for key in p:
        for val in p:
            t_ += ['0', '1'][val in g[key]]
    if t == t_:
        print(*p)
# 1 2 3 4 5 6 7
# Б Д Ж Г Е А В
# БАВДГЕЖ  (59)

