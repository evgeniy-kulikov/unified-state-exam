""""""
"""
Task 01
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 18.4 Закрепление """
# https://stepik.org/lesson/1224003/step/1?unit=1237500
from itertools import permutations
s='АБВГДЕЖК'
print(*'12345678')
g = 'АЖ ЖД ДК КЕ ЕБ БА ВЕ ВД ГБ ГА ГВ'.split()
t = '568 36 247 368 178 124 35 145'.split()
for p in permutations(s):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
# 1 2 3 4 5 6 7 8
# Б К Д В А Е Ж Г
