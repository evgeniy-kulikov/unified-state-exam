# Task 01
# ЕГЭ Информатика
# https://stepik.org/course/100056/syllabus

# https://stepik.org/lesson/760445/step/2?unit=1065191
from itertools import permutations
g = {'А': 'БВ', 'Б': 'АВД', 'В': 'АБЕ', 'Г': 'ДКЕ', 'Д': 'БГК', 'Е': 'КГВ', 'К': 'ДГЕ'}
t = '0000111' + '0010101' + '0101010' + '0010010' + '1100001' + '1011000' + '1100100'
# print(*range(1,8))
print(*'1234567')
for p in permutations(g):
    tn = ''
    for x in p:
        for y in p:
            if y in g[x]:
                tn += '1'
            else:
                tn += '0'
    if tn == t:
        print(*p)
# 1 2 3 4 5 6 7
# Д Е В А Г Б К
# Д Е В А К Б Г
# Е Д Б А Г В К
# Е Д Б А К В Г


"""         """
# https://stepik.org/lesson/760445/step/4?unit=1065191
from itertools import permutations
g = {'A': 'EFB', 'B': 'AG', 'C': 'FGD', 'D': 'CG', 'E': 'AF', 'F': 'EAC', 'G': 'BCD'}
t = '0001001' + '0010110' + '0100100' + '1000101' + '0111000' + '0100001' + '1001010'
# print(*range(1,8))
print(*'1234567')
for p in permutations(g):
    tn = ''
    for x in p:
        for y in p:
            if y in g[x]:
                tn += '1'
            else:
                tn += '0'
    if tn == t:
        print(*p)
# 1 2 3 4 5 6 7
# D A E C F B G
# E G D F C B A

from itertools import permutations
g = 'EFB AG BCD CG FGD EAC AF'
t = '47 356 25 157 234 27 146'
print(*'1234567')

g_set = {frozenset(i) for i in g.split()}
for p in permutations('ABCDEFG'):
    g_p = t
    for i in range(len(p)):
        g_p = g_p.replace(str(i + 1), p[i])
    g_p = {frozenset(i) for i in g_p.split()}
    if g_p == g_set:
        print(*p)
# 1 2 3 4 5 6 7
# D A E C F B G
# E G D F C B A


"""         """
# https://stepik.org/lesson/983014/step/2?unit=990285
from itertools import permutations
g = {'А': 'БВГ', 'Б': 'АВЕЖ', 'В': 'БАГ', 'Г': 'АВЕД', 'Д': 'ГЕ', 'Е': 'ЖБГД', 'Ж': 'БЕ'}
t = '0110100' + '1011001' + '1100100' + '0100001' + '1010011' + '0000101' + '0101110'
# print(*range(1,8))
print(*'1234567')
for p in permutations(g):
    tn = ''
    for x in p:
        for y in p:
            if y in g[x]:
                tn += '1'
            else:
                tn += '0'
    if tn == t:
        print(*p)
# 1 2 3 4 5 6 7
# А Б В Ж Г Д Е
# А Г В Д Б Ж Е
# В Б А Ж Г Д Е
# В Г А Д Б Ж Е
# 26

# https://stepik.org/lesson/983014/step/2?unit=990285
from itertools import permutations
g = 'БВГ АВЕЖ БАГ АВЕД ГЕ ЖБГД БЕ'
t = '235 1347 125 27 1367 57 2456'
num = '1234567'
head = 'АБВГДЕЖ'
print(*num)
g_main = {frozenset(i) for i in g.split()}
for p in permutations(head):
    g_repl = t
    for x, y in zip(num, p):
        g_repl = g_repl.replace(x, y)
    g_repl = {frozenset(k) for k in g_repl.split()}
    if g_main == g_repl:
        f = 1
        print(*p)


"""         """
# https://stepik.org/lesson/983017/step/2?unit=990288
from itertools import permutations
g = 'БД ГВА ГБД БВЕК АВЕК ГКД ГЕД'
t = '2457 136 2567 16 137 234 135'
head = 'АБВГДЕК'
num = '1234567'
print(*num)
g_set = {frozenset(i) for i in g.split()}

for p in permutations(head):
    g_per = t
    for x, y in zip(num, p):
        g_per = g_per.replace(x , y)
    g_per = {frozenset(i) for i in g_per.split()}
    if g_set == g_per:
        print(*p)


from itertools import permutations
g = {'А': 'БД', 'Б': 'ГВА', 'В': 'БГД', 'Г': 'БВЕК', 'Д': 'АВЕК', 'Е': 'ГДК', 'К': 'ГЕД'}
t = '0101101' + '1010010' + '0100111' + '1000010' + '1010001' + '0111000' + '1010100'
# print(*range(1,8))
print(*'1234567')
for p in permutations(g):
    tn = ''
    for x in p:
        for y in p:
            if y in g[x]:
                tn += '1'
            else:
                tn += '0'
    if tn == t:
        print(*p)
# 1 2 3 4 5 6 7
# Д В Г А Е Б К
# Д В Г А К Б Е
# 17 answer



# https://stepik.org/lesson/1339536/step/1?unit=1355230
from itertools import permutations

g = 'BF ECD FC AFD GBC BA GAE'
t = '246 16 57 15 347 127 356'
g_real = {frozenset(i) for i in g.split()}
head = 'ABCDEFG'
num = '1234567'
print(*num)

for p in permutations(head):
    g_per = t
    for x, y in zip(num, p):
        g_per = g_per.replace(x, y)
    g_per = {frozenset(i) for i in g_per.split()}
    if g_per == g_real:
        print(*p)
# 1 2 3 4 5 6 7
# B G D E F A C
# F D G E B C A
# 23 answer


# https://stepik.org/lesson/1339536/step/2?unit=1355230
from itertools import permutations

g = {'A': 'HG', 'B': 'FHC', 'C': 'BG', 'D': 'EG', 'E': 'FD', 'F': 'EBH', 'G': 'DCA', 'H': 'FBA'}
t = '00010011' + '00100001' + '01001100' + '10001000' + '00110000' + '00100010' + '10000101' + '11000010'
print(*'12345678')

for p in permutations(g):
    t_per = ''
    for x in p:
        for y in p:
            if y in g[x]:
                t_per += '1'
            else:
                t_per += '0'
    if t_per == t:
        print(*p)
# 1 2 3 4 5 6 7 8
# F A G E D C B H
# F C G E D A H B
# 110 answer


