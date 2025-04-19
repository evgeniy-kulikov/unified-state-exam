# Task 01
# Информатика Подготовка к ЕГЭ 2025
# https://stepik.org/course/182932/syllabus

# https://stepik.org/lesson/1095501/step/1?unit=1106259
from itertools import permutations
g = {'А': 'БГВ', 'Б': 'АГД', 'В': 'АГЕ', 'Г': 'ДБАВ', 'Д': 'БГЕК', 'Е': 'КДВ', 'К': 'ДЕ'}
t = '0101010' + '1011100' + '0100100' + '1100011' + '0110001' + '1001001' + '0001110'
print(*'1234567')
for p in permutations(g):
    tp = ''
    for x in p:
        for y in p:
            tp += ['0' , '1'][y in g[x]]
    if t == tp:
        print(*p)
# 1 2 3 4 5 6 7
# Б Д К Г Е А В
# 36


# https://stepik.org/lesson/1095501/step/2?unit=1106259
from itertools import permutations
g = 'БВ АВ АБДКГ ВК ВЕ ДК ЕВГ'
t = '56 47 46 236 16 13457 26'
g = {frozenset(i) for i in g.split()}
print(*'1234567')
for p in permutations('АБВГДЕК'):
    tp = t
    for i in range(7):
        tp = tp.replace(str(i + 1), p[i])
    tp = {frozenset(i) for i in tp.split()}
    if tp == g:
        print(*p)
# 1 2 3 4 5 6 7
# А Е Г К Б В Д
# Б Е Г К А В Д
# 25


